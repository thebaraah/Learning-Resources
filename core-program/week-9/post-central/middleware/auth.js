import jwt from 'jsonwebtoken';
import { JWT_SECRET } from '../config/constants.js';

export const authenticate = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader || !authHeader.startsWith('Bearer ')) {
    return res.status(401).json({ error: 'Authorization token required' });
  }

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.verify(token, JWT_SECRET);
    req.user = { user: decoded.user, role: decoded.role };
    next();
  } catch {
    return res.status(401).json({ error: 'Invalid or expired token' });
  }
};
