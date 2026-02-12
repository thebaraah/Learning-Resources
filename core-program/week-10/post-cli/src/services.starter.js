// Change base URL for API requests to the local IP of the Post Central API server
const BASE_URL = 'http://localhost:3000';

// ============================================================================
// AUTH TOKEN - Stored after login/register, sent with every request
// ============================================================================

/**
 * The JWT token received from login or register.
 * This token proves who you are to the server.
 */
let authToken = null;

/**
 * Save the token. Called by the UI after login/register and by unit tests.
 */
const setToken = (token) => {
  authToken = token;
};

/**
 * Get the current token. Use this to build the Authorization header
 * for authenticated requests: `Bearer ${getToken()}`
 */
const getToken = () => authToken;

// ============================================================================
// STAGE 1: GET REQUEST - Read data from the server
// ============================================================================

/**
 * Get current user information
 * Method: GET | Endpoint: /users/me | Auth: Yes
 * Response: { user: string }
 */
const getMe = async () => {
  // TODO
};

// ============================================================================
// STAGE 2: POST REQUEST - Send data to the server
// ============================================================================

/**
 * Register a new user
 * Method: POST | Endpoint: /users/register | Auth: No
 * Body: { name, password }
 * Response: { user: string, token: string }
 */
const createUser = async (name, password) => {
  // TODO
};

/**
 * Log in an existing user
 * Method: POST | Endpoint: /users/login | Auth: No
 * Body: { name, password }
 * Response: { user: string, token: string }
 */
const loginUser = async (name, password) => {
  // TODO
};

// ============================================================================
// STAGE 3: More CRUD Operations
// ============================================================================

/**
 * Create a new post
 * Method: POST | Endpoint: /posts | Auth: Yes
 * Body: { text }
 * Response: { id: number, text: string, user: string }
 */
const createPost = async (text) => {
  // TODO
};

/**
 * Get all posts for the current user
 * Method: GET | Endpoint: /posts/me | Auth: Yes
 * Response: Array of { id, text, user }
 */
const getPosts = async () => {
  // TODO
};

/**
 * Update an existing post
 * Method: PUT | Endpoint: /posts/:id | Auth: Yes
 * Body: { text }
 * Response: { id: number, text: string }
 */
const updatePost = async (id, text) => {
  // TODO
};

/**
 * Delete current user
 * Method: DELETE | Endpoint: /users/me | Auth: Yes
 * No response body
 */
const deleteUser = async () => {
  // TODO
};

/**
 * Delete a post
 * Method: DELETE | Endpoint: /posts/:id | Auth: Yes
 * No response body
 */
const deletePost = async (id) => {
  // TODO
};

// ============================================================================
// EXPORTS - Make functions available for testing and main.js
// ============================================================================

export {
  createPost,
  createUser,
  deletePost,
  deleteUser,
  getMe,
  getPosts,
  getToken,
  loginUser,
  setToken,
  updatePost,
};
