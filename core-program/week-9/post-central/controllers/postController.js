import {
  createPost as createPostService,
  deletePost as deletePostService,
  findPostById,
  updatePost as updatePostService,
} from '../services/postService.js';
import { findUserByIP } from '../services/userService.js';
import { getIP4Address } from '../utils/network.js';
import { broadcast } from '../utils/websocket.js';

export const createPost = (req, res) => {
  const ip = getIP4Address(req.ip);
  const user = findUserByIP(ip);
  if (!user) {
    return res.status(403).json({ error: 'User not registered' });
  }
  const { text } = req.body;
  if (!text) {
    return res.status(400).json({ error: 'Text is required' });
  }
  const post = createPostService(user.user, text);
  broadcast('post:create', { ...post, isNew: true });
  res.json(post);
};

export const updatePost = (req, res) => {
  const ip = getIP4Address(req.ip);
  const user = findUserByIP(ip);
  if (!user) {
    return res.status(403).json({ error: 'User not registered' });
  }
  const { id } = req.params;
  const { text } = req.body;
  if (!text) {
    return res.status(400).json({ error: 'Text is required' });
  }
  const post = findPostById(id);
  if (!post) {
    return res.status(404).json({ error: 'Post not found' });
  }
  if (post.user !== user.user) {
    return res.status(403).json({ error: 'You can only edit your own posts' });
  }
  const updatedPost = updatePostService(id, text);
  broadcast('post:update', updatedPost);
  res.json(updatedPost);
};

export const deletePost = (req, res) => {
  const ip = getIP4Address(req.ip);
  const user = findUserByIP(ip);
  if (!user) {
    return res.status(403).json({ error: 'User not registered' });
  }
  const { id } = req.params;
  const post = findPostById(id);
  if (!post) {
    return res.status(404).json({ error: 'Post not found' });
  }
  if (post.user !== user.user) {
    return res
      .status(403)
      .json({ error: 'You can only delete your own posts' });
  }
  const deletedPost = deletePostService(id);
  broadcast('post:delete', { ...deletedPost, message: 'Post deleted' });
  res.json({ ...deletedPost, message: 'Post deleted' });
};
