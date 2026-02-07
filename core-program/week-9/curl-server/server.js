import chalk from 'chalk';
import cors from 'cors';
import express from 'express';

const app = express();
const PORT = 3000;

const users = [];
const methodChalks = {
  GET: chalk.green,
  POST: chalk.blue,
  PATCH: chalk.yellow,
  DELETE: chalk.red,
};

app.use(cors());
app.use(express.json());

// Set global JSON indentation to 2 spaces
app.set('json spaces', 2);

const generateId = () =>
  users.length > 0 ? users[users.length - 1].id + 1 : 1;
const findUserById = (id) => users.find((u) => u.id === parseInt(id));
const findIndexById = (id) => users.findIndex((u) => u.id === parseInt(id));
const findUserByIP = (ip) => users.find((u) => u.ip === ip);
const getIP4Address = (ip) => {
  if (ip.startsWith('::ffff:')) {
    return ip.substring(7);
  }
  return ip;
};

const printGreeting = (user, req) => {
  const { method, ip: rawIp } = req;
  const ip = getIP4Address(rawIp);
  const methodColor = methodChalks[method] || chalk.white;
  if (user.ip === ip) {
    console.log(
      methodColor(method.padEnd(6)) +
        ` User ${user.name} says: ${user.greeting}`
    );
    return;
  }
  const requestingUser = findUserByIP(ip);
  if (requestingUser) {
    console.log(
      methodColor(method.padEnd(6)) +
        ` User ${user.name} says: ${user.greeting}, as requested by user ${requestingUser.name}`
    );
  } else {
    console.log(
      methodColor(method.padEnd(6)) +
        ` Unknown user (IP: ${ip}) says: ${user.greeting}`
    );
  }
};

const printInvalidRequest = (user, req) => {
  const { method, ip: rawIp } = req;
  const ip = getIP4Address(rawIp);
  const requestingUser = findUserByIP(ip);
  const methodColor = methodChalks[method] || chalk.white;
  console.log(
    methodColor(method.padEnd(6)) +
      ` User ${requestingUser.name} is not authorized to act on behalf of user ${user.name}`
  );
};

app.get('/users', (req, res) => {
  res.json(users);
});

// CREATE a new user
app.post('/users', async (req, res) => {
  const { name, greeting } = req.body;
  if (!name) {
    return res.status(400).json({ error: 'Name is required' });
  }
  if (!greeting) {
    return res.status(400).json({ error: 'Greeting is required' });
  }
  if (users.some((u) => u.name === name)) {
    return res
      .status(409)
      .json({ error: 'User with this name already exists' });
  }
  const ip = getIP4Address(req.ip);
  const newUser = {
    id: generateId(),
    ip,
    name,
    greeting,
  };
  users.push(newUser);
  printGreeting(newUser, req);
  res.status(201).json(newUser);
});

// GET a user by ID
app.get('/users/:id', (req, res) => {
  const user = findUserById(req.params.id);
  if (!user) {
    res.status(404).json({ error: 'User not found' });
    return;
  }
  printGreeting(user, req);
  res.json(user);
});

// PATCH a user by ID (partial update)
app.patch('/users/:id', async (req, res) => {
  const userIndex = findIndexById(req.params.id);
  if (userIndex === -1) {
    return res.status(404).json({ error: 'User not found' });
  }
  const ip = getIP4Address(req.ip);
  if (users[userIndex].ip !== ip) {
    printInvalidRequest(users[userIndex], req);
    return res.status(403).json({ error: 'Forbidden' });
  }
  const { name, greeting } = req.body;
  if (name) {
    users[userIndex].name = name;
  }
  if (greeting) {
    users[userIndex].greeting = greeting;
  }
  printGreeting(users[userIndex], req);
  res.json(users[userIndex]);
});

// DELETE a user by ID
app.delete('/users/:id', (req, res) => {
  const userIndex = findIndexById(req.params.id);
  if (userIndex === -1) {
    return res.status(404).json({ error: 'User not found' });
  }
  const ip = getIP4Address(req.ip);
  if (users[userIndex].ip !== ip) {
    printInvalidRequest(users[userIndex], req);
    return res.status(403).json({ error: 'Forbidden' });
  }
  users[userIndex].greeting = 'Goodbye world!';
  printGreeting(users[userIndex], req);
  users.splice(userIndex, 1);
  res.status(204).end();
});

app.listen(PORT, () => {
  console.log(chalk.green(`Server is running on http://localhost:${PORT}`));
  console.log(chalk.yellow('Press Ctrl+C to stop the server'));
});
