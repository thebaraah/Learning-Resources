const NOT_IMPLEMENTED = {
  ok: false,
  status: 501,
  data: null,
  message: 'Not implemented',
};

/**
 * Log in a user.
 * @param {string} name - The username
 * @param {string} password - The password
 * @returns {Promise<object>} Result object: { ok, status, data, message }
 *
 * API endpoint: POST /users/login
 * Request body: { name, password }
 * Response data: { user: string, token: string }
 */
export async function login(name, password) {
  return NOT_IMPLEMENTED;
}

/**
 * Register a new user.
 * @param {string} name - The desired username
 * @param {string} password - The desired password
 * @returns {Promise<object>} Result object: { ok, status, data, message }
 *
 * API endpoint: POST /users/register
 * Request body: { name, password }
 * Response data: { user: string, token: string }
 */
export async function register(name, password) {
  return NOT_IMPLEMENTED;
}

/**
 * Get the current user's profile.
 * @param {string} token - The JWT token
 * @returns {Promise<object>} Result object: { ok, status, data, message }
 *
 * API endpoint: GET /users/me
 * Headers: Authorization: Bearer <token>
 * Response data: { user: string }
 */
export async function getProfile(token) {
  return NOT_IMPLEMENTED;
}

/**
 * Get the current user's posts.
 * @param {string} token - The JWT token
 * @returns {Promise<object>} Result object: { ok, status, data, message }
 *
 * API endpoint: GET /posts/me
 * Headers: Authorization: Bearer <token>
 * Response data: [{ id, user, text, timestamp, isEdited? }, ...]
 */
export async function getMyPosts(token) {
  return NOT_IMPLEMENTED;
}

/**
 * Create a new post.
 * @param {string} token - The JWT token
 * @param {string} text - The post content
 * @returns {Promise<object>} Result object: { ok, status, data, message }
 *
 * API endpoint: POST /posts
 * Headers: Authorization: Bearer <token>
 * Request body: { text }
 * Response data: { id, user, text, timestamp }
 */
export async function createPost(token, text) {
  return NOT_IMPLEMENTED;
}

/**
 * Edit an existing post.
 * @param {string} token - The JWT token
 * @param {number} id - The post ID to edit
 * @param {string} text - The updated post content
 * @returns {Promise<object>} Result object: { ok, status, data, message }
 *
 * API endpoint: PUT /posts/:id
 * Headers: Authorization: Bearer <token>
 * Request body: { text }
 * Response data: { id, user, text, timestamp, isEdited: true }
 */
export async function editPost(token, id, text) {
  return NOT_IMPLEMENTED;
}

/**
 * Delete a post.
 * @param {string} token - The JWT token
 * @param {number} id - The post ID to delete
 * @returns {Promise<object>} Result object: { ok, status, data, message }
 *
 * API endpoint: DELETE /posts/:id
 * Headers: Authorization: Bearer <token>
 * Response data: { id, user, text, timestamp, message: "Post deleted" }
 */
export async function deletePost(token, id) {
  return NOT_IMPLEMENTED;
}
