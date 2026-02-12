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

/** Save the token (called after login/register) */
const setToken = (token) => {
  authToken = token;
};

/** Get the current token */
const getToken = () => authToken;

/**
 * Build headers object with Content-Type and Authorization.
 * Learn: The Authorization header sends your JWT token to the server.
 * Format: "Bearer <token>"
 */
const authHeaders = () => {
  const headers = { 'Content-Type': 'application/json' };
  if (authToken) {
    headers['Authorization'] = `Bearer ${authToken}`;
  }
  return headers;
};

// ============================================================================
// HELPER FUNCTION - Reusable error handler
// ============================================================================

/**
 * Handles fetch response and extracts JSON data
 * @param {Response} response - The fetch response object
 * @param {string} errorMsg - Error message to show if request fails
 * @returns {Promise<any>} The parsed JSON data
 */
const handleResponse = async (response, errorMsg) => {
  // TODO: Check if response is ok, throw error if not
  // TODO: Return parsed JSON data
};

// ============================================================================
// STAGE 1: GET REQUEST - Read data from the server
// ============================================================================

/**
 * Get current user information
 * Learn: Basic GET request with Authorization header
 */
const getMe = async () => {
  // TODO: Make a GET request to /users/me
  // Hint: const response = await fetch(`${BASE_URL}/users/me`, { headers: authHeaders() });
  // Hint: Use authHeaders() to include your JWT token
  // Hint: Return the parsed JSON: await response.json()
};

// ============================================================================
// STAGE 2: POST REQUEST - Send data to the server
// ============================================================================

/**
 * Register a new user
 * Learn: POST method, headers, request body, JSON.stringify
 * @param {string} name - The user's name
 * @param {string} password - The user's password
 */
const createUser = async (name, password) => {
  // TODO: Make a POST request to /users/register
  // Hint: Set method to 'POST'
  // Hint: Add headers: { 'Content-Type': 'application/json' }
  // Hint: Add body: JSON.stringify({ name, password })
  // Hint: No Authorization header needed (this is a public endpoint!)
  // Hint: Check response and return JSON data (contains { user, token })
};

/**
 * Log in an existing user
 * Learn: POST with credentials, receive a JWT token
 * @param {string} name - The user's name
 * @param {string} password - The user's password
 */
const loginUser = async (name, password) => {
  // TODO: Make a POST request to /users/login
  // Hint: Similar to createUser - POST with { name, password }
  // Hint: No Authorization header needed (this is a public endpoint!)
  // Hint: Returns { user, token }
};

// ============================================================================
// STAGE 3: More CRUD Operations
// ============================================================================

/**
 * Create a new post
 * Learn: POST request with Authorization header
 * @param {string} text - The post content
 */
const createPost = async (text) => {
  // TODO: Make a POST request to /posts
  // Hint: Use authHeaders() to include your JWT token
  // Hint: body: JSON.stringify({ text })
};

/**
 * Get all posts
 * Learn: GET request with Authorization header
 */
const getPosts = async () => {
  // TODO: Make a GET request to /posts/me
  // Hint: Use authHeaders() to include your JWT token
};

/**
 * Update an existing post
 * Learn: PUT method for updates, with Authorization header
 * @param {number} id - The post ID to update
 * @param {string} text - The new post content
 */
const updatePost = async (id, text) => {
  // TODO: Make a PUT request to /posts/:id
  // Hint: Use template literal for URL: `${BASE_URL}/posts/${id}`
  // Hint: Use authHeaders() for headers
  // Hint: body: JSON.stringify({ text })
};

/**
 * Delete current user
 * Learn: DELETE method with Authorization header
 */
const deleteUser = async () => {
  // TODO: Make a DELETE request to /users/me
  // Hint: Use authHeaders() for headers
  // Hint: Only need to check response.ok, no JSON to return
};

/**
 * Delete a post
 * Learn: DELETE method with Authorization header
 * @param {number} id - The post ID to delete
 */
const deletePost = async (id) => {
  // TODO: Make a DELETE request to /posts/:id
  // Hint: Use template literal: `${BASE_URL}/posts/${id}`
  // Hint: Use authHeaders() for headers
  // Hint: Only need to check response.ok, no JSON to return
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
  handleResponse,
  loginUser,
  setToken,
  updatePost,
};
