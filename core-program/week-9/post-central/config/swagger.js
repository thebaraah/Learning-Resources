import path from 'path';
import swaggerJsdoc from 'swagger-jsdoc';
import { fileURLToPath } from 'url';
import { PORT } from './constants.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export const swaggerOptions = {
  definition: {
    openapi: '3.0.0',
    info: {
      title: 'Post Central API',
      version: '1.0.0',
      description:
        'A real-time messaging API with WebSocket support for live updates',
      contact: {
        name: 'API Support',
      },
    },
    servers: [
      {
        url: `http://localhost:${PORT}`,
        description: 'Local server',
      },
    ],
    components: {
      schemas: {
        User: {
          type: 'object',
          properties: {
            user: {
              type: 'string',
              description: 'Username',
            },
            ip: {
              type: 'string',
              description: 'User IP address',
            },
          },
        },
        Post: {
          type: 'object',
          properties: {
            id: {
              type: 'integer',
              description: 'Post ID',
            },
            user: {
              type: 'string',
              description: 'Username who created the post',
            },
            text: {
              type: 'string',
              description: 'Post content',
            },
          },
        },
        Error: {
          type: 'object',
          properties: {
            error: {
              type: 'string',
              description: 'Error message',
            },
          },
        },
      },
    },
  },
  apis: [path.join(__dirname, '../routes/*.js')],
};

export const swaggerSpec = swaggerJsdoc(swaggerOptions);
