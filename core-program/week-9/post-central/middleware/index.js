import cors from 'cors';
import express from 'express';
import morgan from 'morgan';
import path from 'path';

export const setupMiddleware = (app, __dirname) => {
  app.use(cors());
  app.use(morgan('dev'));
  app.use(express.json());
  app.use(express.static(path.join(__dirname, 'client')));
  app.use('/web', express.static(path.join(__dirname, 'web')));

  // Set global JSON indentation to 2 spaces
  app.set('json spaces', 2);
};
