import express from 'express';
import {
  deleteUser,
  getUsers,
  registerUser,
} from '../controllers/userController.js';

const router = express.Router();

/**
 * @openapi
 * /users:
 *   get:
 *     summary: Get all registered users
 *     description: Returns a list of all users currently registered in the system
 *     tags:
 *       - Users
 *     responses:
 *       200:
 *         description: List of users
 *         content:
 *           application/json:
 *             schema:
 *               type: array
 *               items:
 *                 $ref: '#/components/schemas/User'
 */
router.get('/', getUsers);

/**
 * @openapi
 * /users/register:
 *   post:
 *     summary: Register a new user
 *     description: Register a new user with a unique username. The user's IP address is automatically captured.
 *     tags:
 *       - Users
 *     requestBody:
 *       required: true
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             required:
 *               - name
 *             properties:
 *               name:
 *                 type: string
 *                 description: Username to register
 *                 example: johndoe
 *     responses:
 *       201:
 *         description: User successfully created
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/User'
 *       400:
 *         description: Name is required
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/Error'
 *       409:
 *         description: User with this name already exists
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/Error'
 */
router.post('/register', registerUser);

/**
 * @openapi
 * /users/me:
 *   delete:
 *     summary: Delete current user
 *     description: Delete the user account associated with the current IP address. This also triggers a WebSocket broadcast to notify all clients.
 *     tags:
 *       - Users
 *     responses:
 *       200:
 *         description: User successfully deleted
 *         content:
 *           application/json:
 *             schema:
 *               allOf:
 *                 - $ref: '#/components/schemas/User'
 *                 - type: object
 *                   properties:
 *                     message:
 *                       type: string
 *                       example: User deleted
 *       404:
 *         description: User not found
 *         content:
 *           application/json:
 *             schema:
 *               $ref: '#/components/schemas/Error'
 */
router.delete('/me', deleteUser);

export default router;
