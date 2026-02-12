async function fetchData(url, options = {}) {
  const response = await fetch(url, {
    ...options,
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
  });
  const data = await response.json();
  return { ok: response.ok, status: response.status, data, message: data.error || '' };
}

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
  return fetchData('/users/login', {
    method: 'POST',
    body: { name, password },
  });
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
  return fetchData('/users/register', {
    method: 'POST',
    body: { name, password },
  });
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
  return fetchData('/users/me', {
    method: 'GET',
    headers: { Authorization: `Bearer ${token}` },
  });
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
  return fetchData('/posts/me', {
    method: 'GET',
    headers: { Authorization: `Bearer ${token}` },
  });
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
  return fetchData('/posts', {
    method: 'POST',
    headers: { Authorization: `Bearer ${token}` },
    body: { text },
  });
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
  return fetchData(`/posts/${id}`, {
    method: 'PUT',
    headers: { Authorization: `Bearer ${token}` },
    body: { text },
  });
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
  return fetchData(`/posts/${id}`, {
    method: 'DELETE',
    headers: { Authorization: `Bearer ${token}` },
  });
}
