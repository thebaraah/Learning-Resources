import chalk from 'chalk';
import express from 'express';
import { createServer } from 'http';
import path from 'path';
import { fileURLToPath } from 'url';
import { WebSocketServer } from 'ws';
import { setupApiDocs } from './config/apiDocs.js';
import { PORT } from './config/constants.js';
import { setupMiddleware } from './middleware/index.js';
import postRoutes from './routes/postRoutes.js';
import userRoutes from './routes/userRoutes.js';
import { getLocalIP } from './utils/network.js';
import { initializeWebSocket } from './utils/websocket.js';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

const app = express();
const server = createServer(app);
const wss = new WebSocketServer({ server });

// Initialize WebSocket
initializeWebSocket(wss);

// Setup middleware
setupMiddleware(app, __dirname);

// Setup API documentation
setupApiDocs(app);

// Setup routes
app.use('/users', userRoutes);
app.use('/posts', postRoutes);

// 404 handler for unknown endpoints
app.use((req, res) => {
  res.status(404).json({ error: `Cannot ${req.method} ${req.originalUrl}` });
});

// Start server
server.listen(PORT, () => {
  console.log(chalk.green(`Server is running on http://localhost:${PORT}`));
  console.log(chalk.cyan(`\nAPI accessible at http://${getLocalIP()}:${PORT}`));
  console.log(
    chalk.magenta(`\nClient app at http://${getLocalIP()}:${PORT}/client`)
  );
  console.log(
    chalk.magenta(`Portal app at http://${getLocalIP()}:${PORT}/portal`)
  );
  console.log(
    chalk.blue(`\nAPI Documentation at http://${getLocalIP()}:${PORT}/api-docs`)
  );
  console.log(chalk.yellow('\nPress Ctrl+C to stop the server'));
});

// Disable keep-alive to prevent hanging connections and ensure immediate response delivery
server.keepAliveTimeout = 0;
