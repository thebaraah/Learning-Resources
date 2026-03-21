import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const DATA_FILE = path.join(__dirname, "..", "data", "posts.json");

const loadPosts = () => {
  try {
    const data = fs.readFileSync(DATA_FILE, "utf-8");
    return JSON.parse(data);
  } catch {
    return [];
  }
};

const savePosts = () => {
  const dir = path.dirname(DATA_FILE);
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
  fs.writeFileSync(DATA_FILE, JSON.stringify(posts, null, 2));
};

const posts = loadPosts();

const generatePostId = () =>
  posts.length > 0 ? posts[posts.length - 1].id + 1 : 1;

export const getAllPosts = () => posts;

export const findPostById = (id) => posts.find((p) => p.id === parseInt(id));

export const getPostsByUser = (username) =>
  posts.filter((p) => p.user === username);

export const deletePostsByUser = (username) => {
  for (let i = posts.length - 1; i >= 0; i--) {
    if (posts[i].user === username) {
      posts.splice(i, 1);
    }
  }
  savePosts();
};

export const createPost = (username, text) => {
  const post = {
    id: generatePostId(),
    user: username,
    text,
    timestamp: new Date().toISOString(),
  };
  posts.push(post);
  savePosts();
  return post;
};

export const updatePost = (id, text) => {
  const post = findPostById(id);
  if (!post) {
    return null;
  }
  post.text = text;
  post.timestamp = new Date().toISOString();
  post.isEdited = true;
  savePosts();
  return post;
};

export const deletePost = (id) => {
  const postIndex = posts.findIndex((p) => p.id === parseInt(id));
  if (postIndex === -1) {
    return null;
  }
  const post = posts[postIndex];
  posts.splice(postIndex, 1);
  savePosts();
  return post;
};
