import express from 'express';

const app = express();
const port = 3000;

// Parse incoming JSON request bodies
app.use(express.json());

// Store todos in memory (resets when the server restarts)
let todos = [];

// GET /todos — return all todos
app.get('/todos', (req, res) => {
  res.json(todos);
});

// GET /todos/:id — return a single todo by its ID
app.get('/todos/:id', (req, res) => {
  const id = Number(req.params.id);
  const todo = todos.find(todo => todo.id === id);

  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  res.json(todo);
});

// POST /todos — create a new todo
// Request body: { "text": "Buy groceries" }
app.post('/todos', (req, res) => {
  const text = req.body.text;

  if (!text) {
    return res.status(400).json({ error: 'text is required' });
  }

  const todo = {
    id: Math.floor(Math.random() * 999999) + 1,
    text: text
  };

  todos.push(todo);
  res.status(201).json(todo);
});

// PUT /todos/:id — update an existing todo's text
// Request body: { "text": "Updated text" }
app.put('/todos/:id', (req, res) => {
  const id = Number(req.params.id);
  const todo = todos.find(todo => todo.id === id);

  if (!todo) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  todo.text = req.body.text;
  res.json(todo);
});

// DELETE /todos/:id — delete a todo by its ID
app.delete('/todos/:id', (req, res) => {
  const id = Number(req.params.id);
  const index = todos.findIndex(todo => todo.id === id);

  if (index === -1) {
    return res.status(404).json({ error: 'Todo not found' });
  }

  todos.splice(index, 1);
  res.status(204).send();
});

app.listen(port, () => {
  console.log(`TODO server running on http://localhost:${port}`);
});

