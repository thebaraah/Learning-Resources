import chalk from 'chalk';
import cors from 'cors';
import express from 'express';
import { createServer } from 'http';
import morgan from 'morgan';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { WebSocketServer } from 'ws';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const app = express();
const server = createServer(app);
const wss = new WebSocketServer({ server });

const broadcast = (type, data) => {
  const message = JSON.stringify({ type, data });
  for (const client of wss.clients) {
    if (client.readyState === 1) {
      client.send(message);
    }
  }
};
const PORT = 3000;

const getLocalIP = () => {
  const interfaces = os.networkInterfaces();

  for (const name of Object.keys(interfaces)) {
    for (const iface of interfaces[name]) {
      // Skip internal (loopback) and non-IPv4 addresses
      if (iface.family === 'IPv4' && !iface.internal) {
        return iface.address;
      }
    }
  }
  return 'localhost';
};

const users = [{ user: 'admin', ip: getLocalIP() }];

const posts = [];

const generatePostId = () =>
  posts.length > 0 ? posts[posts.length - 1].id + 1 : 1;

app.use(cors());
app.use(morgan('dev'));
app.use(express.json());
app.use(express.static(path.join(__dirname, 'client')));

// Set global JSON indentation to 2 spaces
app.set('json spaces', 2);

const findUserByIP = (ip) => users.find((u) => u.ip === ip);

const findPostById = (id) => posts.find((p) => p.id === parseInt(id));

const getIP4Address = (ip) => {
  if (ip.startsWith('::ffff:')) {
    return ip.substring(7);
  }
  return ip;
};

// GET all users
app.get('/users', (req, res) => {
  res.json(users);
});

// POST a new user
app.post('/users/register', async (req, res) => {
  const { name } = req.body;
  if (!name) {
    return res.status(400).json({ error: 'Name is required' });
  }
  if (users.some((u) => u.user === name)) {
    return res
      .status(409)
      .json({ error: 'User with this name already exists' });
  }
  const ip = getIP4Address(req.ip);
  const newUser = {
    user: name,
    ip,
  };
  users.push(newUser);
  broadcast('user:register', newUser);
  res.status(201).json(newUser);
});

// DELETE a user
app.delete('/users/me', (req, res) => {
  const ip = getIP4Address(req.ip);

  const userIndex = users.findIndex((u) => u.ip === ip);
  if (userIndex === -1) {
    return res.status(404).json({ error: 'User not found' });
  }

  const user = users[userIndex];
  users.splice(userIndex, 1);
  broadcast('user:delete', { ...user, message: 'User deleted' });
  res.json({ ...user, message: 'User deleted' });
});

app.post('/posts', (req, res) => {
  const ip = getIP4Address(req.ip);
  const user = findUserByIP(ip);
  if (!user) {
    return res.status(403).json({ error: 'User not registered' });
  }
  const { text } = req.body;
  if (!text) {
    return res.status(400).json({ error: 'Text is required' });
  }
  const post = { id: generatePostId(), user: user.user, text };
  posts.push(post);
  broadcast('post:create', post);
  res.json(post);
});

app.put('/posts/:id', (req, res) => {
  const ip = getIP4Address(req.ip);
  const user = findUserByIP(ip);
  if (!user) {
    return res.status(403).json({ error: 'User not registered' });
  }
  const { id } = req.params;
  const { text } = req.body;
  if (!text) {
    return res.status(400).json({ error: 'Text is required' });
  }
  const post = findPostById(id);
  if (!post) {
    return res.status(404).json({ error: 'Post not found' });
  }
  if (post.user !== user.user) {
    return res.status(403).json({ error: 'You can only edit your own posts' });
  }
  post.text = text;
  broadcast('post:update', post);
  res.json(post);
});

app.delete('/posts/:id', (req, res) => {
  const ip = getIP4Address(req.ip);
  const user = findUserByIP(ip);
  if (!user) {
    return res.status(403).json({ error: 'User not registered' });
  }
  const { id } = req.params;
  const postIndex = posts.findIndex((p) => p.id === parseInt(id));
  if (postIndex === -1) {
    return res.status(404).json({ error: 'Post not found' });
  }
  const post = posts[postIndex];
  if (post.user !== user.user) {
    return res
      .status(403)
      .json({ error: 'You can only delete your own posts' });
  }
  posts.splice(postIndex, 1);
  broadcast('post:delete', { ...post, message: 'Post deleted' });
  res.json({ ...post, message: 'Post deleted' });
});

server.listen(PORT, () => {
  console.log(chalk.green(`Server is running on http://localhost:${PORT}`));
  console.log(
    chalk.green(`Accessible on local network at http://${getLocalIP()}:${PORT}`)
  );
  console.log(chalk.yellow('Press Ctrl+C to stop the server'));
});
