import { getAllPosts } from '../services/postService.js';
import chalk from 'chalk';

let websocketServer;

export const initializeWebSocket = (wss) => {
  websocketServer = wss;

  // Handle new client connections
  wss.on('connection', (ws) => {
    console.log(chalk.green('New WebSocket client connected'));

    // Send all existing posts to the newly connected client
    const posts = getAllPosts();
    posts.forEach((post) => {
      const message = JSON.stringify({
        type: 'post:create',
        data: { ...post, isNew: false },
      });
      ws.send(message);
    });

    ws.on('close', () => {
      console.log(chalk.green('WebSocket client disconnected'));
    });
  });
};

export const broadcast = (type, data) => {
  if (!websocketServer) {
    console.error(chalk.red('WebSocket server not initialized'));
    return;
  }

  const message = JSON.stringify({ type, data });
  for (const client of websocketServer.clients) {
    if (client.readyState === 1) {
      client.send(message);
    }
  }
};
