import express from 'express';
import { compliments } from './compliments.js';

const app = express();

app.get("/", (req, res) => {
  res.send("Welcome to the Compliments API! Use /compliment/:name to get a personalized compliment.");
});

app.get("/compliment/:name", (req, res) => {
  const name = req.params.name;
  const randomIndex = Math.floor(Math.random() * compliments.length);
  const compliment = compliments[randomIndex].replace("{name}", name)

  res.json({
    number: randomIndex + 1,
    compliment: compliment,
  });
});


const port = process.env.PORT || 3000;

app.listen(port, () => {
  console.log(`Compliments server running on http://localhost:${port}`);
});