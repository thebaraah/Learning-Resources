# Implementation Summary

## What's New

### Documentation Files

1. **README.md** - Comprehensive guide including:
   - Learning objectives
   - Exercise structure (4 stages, 60 minutes)
   - Complete API documentation table with authentication info
   - HTTP status codes reference
   - Fetch patterns and examples
   - Common mistakes to avoid
   - Setup instructions

2. **TEACHING_GUIDE.md** - For lecturers:
   - Detailed 60-minute session plan
   - JWT authentication teaching tips
   - Teaching tips and demonstrations
   - Common student questions with answers
   - Troubleshooting solutions
   - Assessment ideas
   - Differentiation strategies

3. **QUICK_REFERENCE.md** - Student cheat sheet:
   - Fetch syntax templates (with and without auth)
   - Common patterns
   - Error examples
   - Quick debugging tips

4. **PROJECT_STRUCTURE.md** - File organization guide:
   - Directory structure
   - File purposes
   - Available commands
   - Learning path

### Code Files

1. **src/services.js** - Student template with:
   - Token management code (provided ready-made)
   - `authHeaders()` helper function
   - TODO comments with hints
   - Empty function stubs for students to implement
   - Learning comments explaining concepts

2. **src/post-cli.js** - Command-line application (provided ready-made):
   - Register/Login authentication flow
   - Password input with masking
   - Interactive prompts for user input
   - Color-coded output with chalk
   - Error handling with try/catch
   - Commands: /view, /update, /delete, /leave, /exit
   - Uses student functions from src/services.js

### Test Files

1. **tests/test-get.test.js** - Vitest tests for GET requests:
   - Token setup/teardown in beforeEach/afterEach
   - Authorization header verification
   - Response validation

2. **tests/test-post.test.js** - Vitest tests for POST requests:
   - createUser with password
   - loginUser tests
   - Authorization header verification for createPost
   - Public vs protected endpoint distinction

3. **tests/test-crud.test.js** - Complete CRUD flow tests:
   - Full token-based authentication flow
   - All operations tested with Authorization headers
   - deletePost tests
   - Multiple test scenarios

### cURL Examples

All curl scripts with:

- Parameterized token (pass as argument or replace placeholder)
- Educational comments
- Visual feedback
- Usage instructions
- **register.sh** - Register with name + password
- **login.sh** - Login with name + password
- **get-user.sh** - GET with Authorization header
- **get-posts.sh** - GET with Authorization header
- **post-message.sh** - POST with Authorization header
- **update-message.sh** - PUT with Authorization header
- **post-cli.sh** - Interactive CLI with login

## Authentication Model

### JWT Token Flow

1. User registers or logs in with `{ name, password }`
2. Server returns `{ user, token }`
3. Token is stored via `setToken(token)` in the fetchers module
4. All subsequent requests include `Authorization: Bearer <token>` via `authHeaders()`

### Token Management

```javascript
let authToken = null;
const setToken = (token) => { authToken = token; };
const getToken = () => authToken;
const authHeaders = () => {
  const headers = { 'Content-Type': 'application/json' };
  if (authToken) headers['Authorization'] = `Bearer ${authToken}`;
  return headers;
};
```

### Public vs Protected Endpoints

| Endpoint             | Auth Required |
| -------------------- | ------------- |
| POST /users/register | No            |
| POST /users/login    | No            |
| All other endpoints  | Yes           |

## Complete CRUD Operations

- ✓ POST register user (`createUser`) - public
- ✓ POST login user (`loginUser`) - public
- ✓ GET user info (`getMe`) - protected
- ✓ DELETE user (`deleteUser`) - protected
- ✓ GET all posts (`getPosts`) - protected
- ✓ POST create post (`createPost`) - protected
- ✓ PUT update post (`updatePost`) - protected
- ✓ DELETE post (`deletePost`) - protected

## Reusable Helper Functions

```javascript
const handleResponse = async (response, errorMsg) => {
  if (!response.ok) {
    throw new Error(`${errorMsg}: HTTP ${response.status}`);
  }
  return await response.json();
};

const authHeaders = () => {
  const headers = { 'Content-Type': 'application/json' };
  if (authToken) headers['Authorization'] = `Bearer ${authToken}`;
  return headers;
};
```

## Learning Outcomes

After completing this exercise, students will:

- ✓ Understand HTTP request/response cycle
- ✓ Use fetch() API confidently
- ✓ Handle async operations with async/await
- ✓ Work with JSON data
- ✓ Implement proper error handling
- ✓ Understand REST API patterns
- ✓ Know all CRUD operations
- ✓ Understand token-based authentication (JWT)
- ✓ Use the Authorization header for protected endpoints
- ✓ Debug API issues effectively
