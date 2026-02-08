import { getLocalIP } from '../utils/network.js';

const users = [{ user: 'admin', ip: getLocalIP() }];

export const getAllUsers = () => users;

export const findUserByIP = (ip) => users.find((u) => u.ip === ip);

export const findUserByName = (name) => users.find((u) => u.user === name);

export const createUser = (name, ip) => {
  const newUser = { user: name, ip };
  users.push(newUser);
  return newUser;
};

export const deleteUserByIP = (ip) => {
  const userIndex = users.findIndex((u) => u.ip === ip);
  if (userIndex === -1) {
    return null;
  }
  const user = users[userIndex];
  users.splice(userIndex, 1);
  return user;
};
