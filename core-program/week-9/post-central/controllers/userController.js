import bcrypt from 'bcrypt';
import jwt from 'jsonwebtoken';
import { JWT_EXPIRES_IN, JWT_SECRET } from '../config/constants.js';
import {
  createUser,
  deleteUserByName,
  findUserByName,
  getAllUsers,
  updateLastLogin,
} from '../services/userService.js';
import { deletePostsByUser } from '../services/postService.js';
import { broadcast } from '../utils/websocket.js';

const generateToken = (username, role) =>
  jwt.sign({ user: username, role }, JWT_SECRET, { expiresIn: JWT_EXPIRES_IN });

export const getUsers = (req, res) => {
  res.json(getAllUsers().filter((u) => u.role !== 'admin'));
};

export const getMe = (req, res) => {
  const user = findUserByName(req.user.user);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }
  res.json({
    user: user.user,
    role: user.role,
    createdAt: user.createdAt,
    lastLogin: user.lastLogin,
  });
};

export const registerUser = async (req, res) => {
  const { name, password } = req.body;
  if (!name || !password) {
    return res.status(400).json({ error: 'Name and password are required' });
  }
  if (findUserByName(name)) {
    return res
      .status(409)
      .json({ error: 'User with this name already exists' });
  }
  const hashedPassword = await bcrypt.hash(password, 10);
  const newUser = createUser(name, hashedPassword);
  const token = generateToken(name, newUser.role);
  broadcast('user:register', newUser);
  res.status(201).json({ ...newUser, token });
};

export const loginUser = async (req, res) => {
  const { name, password } = req.body;
  if (!name || !password) {
    return res.status(400).json({ error: 'Name and password are required' });
  }
  const user = findUserByName(name);
  if (!user) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) {
    return res.status(401).json({ error: 'Invalid credentials' });
  }
  updateLastLogin(name);
  const token = generateToken(name, user.role);
  broadcast('user:login', { user: user.user });
  res.json({ user: user.user, token });
};

export const deleteUser = (req, res) => {
  if (req.user.role === 'admin') {
    return res
      .status(403)
      .json({ error: 'Admin users cannot delete themselves' });
  }

  const user = deleteUserByName(req.user.user);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  deletePostsByUser(req.user.user);
  broadcast('user:delete', { ...user, message: 'User deleted' });
  res.json({ ...user, message: 'User deleted' });
};

export const deleteUserByAdmin = (req, res) => {
  if (req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Admin access required' });
  }

  const { name } = req.params;
  const target = findUserByName(name);
  if (!target) {
    return res.status(404).json({ error: 'User not found' });
  }
  if (target.role === 'admin') {
    return res.status(403).json({ error: 'Cannot delete an admin user' });
  }

  const user = deleteUserByName(name);
  deletePostsByUser(name);
  broadcast('user:delete', { ...user, message: 'User deleted by admin' });
  res.json({ ...user, message: 'User deleted by admin' });
};
