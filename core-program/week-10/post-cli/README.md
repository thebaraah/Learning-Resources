# Post Central - Fetch & APIs Learning Exercise

A hands-on exercise for learning to use `fetch()` and work with REST APIs in Node.js.

## Learning Objectives

By the end of this exercise, you will be able to:

- ✓ Make HTTP requests using the `fetch()` API
- ✓ Understand and use different HTTP methods (GET, POST, PUT, DELETE)
- ✓ Work with JSON request and response bodies
- ✓ Handle HTTP headers (especially `Content-Type` and `Authorization`)
- ✓ Implement proper error handling for API calls
- ✓ Use async/await with asynchronous operations
- ✓ Understand token-based authentication (JWT)

## Prerequisites

- Node.js installed (v18 or higher)
- Basic JavaScript knowledge (functions, promises)
- A running Post Central API server on the teacher's machine (students will connect to this).

## Setup

```bash
npm install
npm start     # Runs the application with your code
```

The `npm start` command runs `post-cli.js`, which imports and uses your functions from `services.js`. The main application logic is provided ready-made so you can focus on implementing the API functions.

## API Documentation

### Base URL

The `BASE_URL` in your `services.js` file needs to be set to the local IP address of the teacher's machine, which is where the Post Central API server is running. It should look something like this:

```plaintext
http://192.168.xxx.xxx:3000
```

### Authentication

The API uses **JWT (JSON Web Token)** authentication:

1. **Register** or **Login** to receive a token
2. Include the token in the `Authorization` header for all protected endpoints
3. Header format: `Authorization: Bearer <your-token>`

The `authHeaders()` helper function in `services.js` builds the correct headers for you.

### Endpoints

| Method | Endpoint          | Auth Required | Request Body                          | Response                                     |
| ------ | ----------------- | ------------- | ------------------------------------- | -------------------------------------------- |
| POST   | `/users/register` | No            | `{ name: string, password: string }`  | `{ user: string, token: string }`            |
| POST   | `/users/login`    | No            | `{ name: string, password: string }`  | `{ user: string, token: string }`            |
| GET    | `/posts/hello`    | No            | -                                     | `{ id: number, user: string, text: string, timestamp: string }` |
| GET    | `/users/me`       | Yes           | -                                     | `{ user: string, createdAt: string, lastLogin: string }` |
| DELETE | `/users/me`       | Yes           | -                                     | No content                                   |
| GET    | `/posts/me`       | Yes           | -                                     | `Array of posts`                             |
| POST   | `/posts`          | Yes           | `{ text: string }`                    | `{ id: number, text: string, user: string }` |
| PUT    | `/posts/:id`      | Yes           | `{ text: string }`                    | `{ id: number, text: string }`               |
| DELETE | `/posts/:id`      | Yes           | -                                     | No content                                   |

### Common HTTP Status Codes

- **200 OK** - Request succeeded
- **201 Created** - Resource created successfully
- **204 No Content** - Request succeeded, no response body
- **400 Bad Request** - Invalid request data
- **401 Unauthorized** - Missing or invalid token
- **403 Forbidden** - You can only modify your own posts
- **404 Not Found** - Resource not found
- **409 Conflict** - Username already exists
- **500 Internal Server Error** - Server error

## Exercise Structure

### Stage 0: Hello Endpoint - Verify Setup (5 min)

- Implement `getHello()` function
- Verify your `BASE_URL` is correct and the server is reachable
- Learn the basic structure of a `fetch()` call with no headers needed
- See what a post object looks like before touching authentication

### Stage 1: Simple GET Request (15 min)

- Implement `getMe()` function
- Learn about `fetch()`, `response.ok`, and `response.json()`
- Understand HTTP status codes
- Learn about the `Authorization` header

### Stage 2: POST with Body (15 min)

- Implement `createUser()` and `loginUser()` functions
- Learn about request methods, headers, and body
- Understand `Content-Type: application/json`
- Learn the difference between public and protected endpoints

### Stage 3: Complete CRUD (20 min)

- Implement `createPost()`, `updatePost()`, `getPosts()`, `deletePost()`
- Build the main application flow
- Handle different user scenarios

### Stage 4: Error Handling (10 min)

- Refine error messages
- Handle edge cases
- Test various failure scenarios

## Files in This Project

- **src/services.js** - Your working file - implement the API functions here
- **src/post-cli.js** - Application entry point (provided ready-made)
- **tests/** - Vitest tests to verify your functions work correctly

## Testing Your Functions

We use **Vitest** for testing. The tests verify that **your functions** work correctly by:

- **Mocking fetch** to avoid needing a running API server
- Verifying you call fetch with the correct URL, method, headers, and body
- Checking you parse and return responses correctly
- Testing error handling

```bash
# Run all tests in watch mode (recommended)
npm test

# Run specific test suites
npm run test:get      # Test your GET functions (getMe, getPosts)
npm run test:post     # Test your POST functions (createUser, loginUser, createPost)
npm run test:crud     # Test complete workflow (all functions together)

# Run tests once (no watch mode)
npm run test:run
```

## Tips for Success

1. Update the `services.js` file and implement one function at a time
2. Test each function before moving to the next
3. Read error messages carefully - they tell you what's wrong
4. Use `console.log()` to inspect responses during development
5. Check the API documentation when unsure about request format
6. `getHello()` needs no Authorization header — start there to verify your BASE_URL!
7. Remember: `register` and `login` don't need an Authorization header, but everything else does!
8. Don't hesitate to ask your lecturer for help

Good luck!
