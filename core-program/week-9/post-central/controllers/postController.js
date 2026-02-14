import {
  createPost as createPostService,
  deletePost as deletePostService,
  findPostById,
  getAllPosts as getAllPostsService,
  getPostsByUser,
  updatePost as updatePostService,
} from '../services/postService.js';
import { broadcast } from '../utils/websocket.js';

export const getPosts = (req, res) => {
  if (req.user.role !== 'admin') {
    return res.status(403).json({ error: 'Admin access required' });
  }
  res.json(getAllPostsService());
};

export const getHello = (_req, res) => {
  res.json({
    id: 0,
    user: 'post-central',
    text: 'Welcome to Post Central!',
    timestamp: '2024-01-01T00:00:00.000Z',
  });
};

export const getMyPosts = (req, res) => {
  const posts = getPostsByUser(req.user.user);
  res.json(posts);
};

export const createPost = (req, res) => {
  const { text } = req.body;
  if (!text) {
    return res.status(400).json({ error: 'Text is required' });
  }
  const post = createPostService(req.user.user, text);
  broadcast('post:create', { ...post, isNew: true });
  res.json(post);
};

export const updatePost = (req, res) => {
  const { id } = req.params;
  const { text } = req.body;
  if (!text) {
    return res.status(400).json({ error: 'Text is required' });
  }
  const post = findPostById(id);
  if (!post) {
    return res.status(404).json({ error: 'Post not found' });
  }
  if (post.user !== req.user.user) {
    return res.status(403).json({ error: 'You can only edit your own posts' });
  }
  const updatedPost = updatePostService(id, text);
  broadcast('post:update', updatedPost);
  res.json(updatedPost);
};

export const deletePost = (req, res) => {
  const { id } = req.params;
  const post = findPostById(id);
  if (!post) {
    return res.status(404).json({ error: 'Post not found' });
  }
  if (post.user !== req.user.user && req.user.role !== 'admin') {
    return res
      .status(403)
      .json({ error: 'You can only delete your own posts' });
  }
  const deletedPost = deletePostService(id);
  broadcast('post:delete', { ...deletedPost, message: 'Post deleted' });
  res.json({ ...deletedPost, message: 'Post deleted' });
};
