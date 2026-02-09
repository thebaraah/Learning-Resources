import {
  createUser,
  deleteUserByIP,
  findUserByIP,
  findUserByName,
  getAllUsers,
} from '../services/userService.js';
import { getIP4Address } from '../utils/network.js';
import { broadcast } from '../utils/websocket.js';

export const getUsers = (req, res) => {
  res.json(getAllUsers());
};

export const getMe = (req, res) => {
  const ip = getIP4Address(req.ip);
  const user = findUserByIP(ip);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }
  res.json(user);
};

export const registerUser = async (req, res) => {
  const { name } = req.body;
  if (!name) {
    return res.status(400).json({ error: 'Name is required' });
  }
  if (findUserByName(name)) {
    return res
      .status(409)
      .json({ error: 'User with this name already exists' });
  }
  const ip = getIP4Address(req.ip);
  const newUser = createUser(name, ip);
  broadcast('user:register', newUser);
  res.status(201).json(newUser);
};

export const deleteUser = (req, res) => {
  const ip = getIP4Address(req.ip);

  const user = deleteUserByIP(ip);
  if (!user) {
    return res.status(404).json({ error: 'User not found' });
  }

  broadcast('user:delete', { ...user, message: 'User deleted' });
  res.json({ ...user, message: 'User deleted' });
};
