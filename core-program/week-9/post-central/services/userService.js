import bcrypt from 'bcrypt';
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DATA_FILE = path.join(__dirname, '..', 'data', 'users.json');

const loadUsers = () => {
  try {
    const data = fs.readFileSync(DATA_FILE, 'utf-8');
    return JSON.parse(data);
  } catch {
    return null;
  }
};

const saveUsers = () => {
  const dir = path.dirname(DATA_FILE);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  fs.writeFileSync(DATA_FILE, JSON.stringify(users, null, 2));
};

// Load from file, or seed with default admin
let users = loadUsers();
if (!users) {
  const adminPassword = await bcrypt.hash('admin', 10);
  users = [{ user: 'admin', password: adminPassword }];
  saveUsers();
}

export const getAllUsers = () =>
  users.map(({ user }) => ({ user }));

export const findUserByName = (name) => users.find((u) => u.user === name);

export const createUser = (name, hashedPassword) => {
  const newUser = { user: name, password: hashedPassword };
  users.push(newUser);
  saveUsers();
  return { user: name };
};

export const deleteUserByName = (name) => {
  const userIndex = users.findIndex((u) => u.user === name);
  if (userIndex === -1) {
    return null;
  }
  users.splice(userIndex, 1);
  saveUsers();
  return { user: name };
};
