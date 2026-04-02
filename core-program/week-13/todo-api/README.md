# Todo API

A simple in-memory REST API for managing todos, built with Node.js and Express.

## Setup

```bash
npm install
npm start
```

Server runs at `http://localhost:3000`.

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/todos` | Get all todos |
| GET | `/todos/:id` | Get a todo by ID |
| POST | `/todos` | Create a todo `{ "text": "..." }` |
| PUT | `/todos/:id` | Update a todo `{ "text": "..." }` |
| DELETE | `/todos/:id` | Delete a todo |

> Data is stored in memory and resets on server restart.
