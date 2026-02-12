import express from 'express';
import {
  createPost,
  deletePost,
  getMyPosts,
  updatePost,
} from '../controllers/postController.js';
import { authenticate } from '../middleware/auth.js';

const router = express.Router();

router.get('/me', authenticate, getMyPosts);
router.post('/', authenticate, createPost);
router.put('/:id', authenticate, updatePost);
router.delete('/:id', authenticate, deletePost);

export default router;
