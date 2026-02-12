import cors from 'cors';
import express from 'express';
import morgan from 'morgan';
import path from 'path';

export const setupMiddleware = (app, __dirname) => {
  app.use(cors());
  app.use(morgan('dev'));
  app.use(express.json());
  app.use(express.static(path.join(__dirname, '../../week-10/post-client')));
  app.use('/portal', express.static(path.join(__dirname, 'portal')));

  // Set global JSON indentation to 2 spaces
  app.set('json spaces', 2);
};
