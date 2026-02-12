# Post Central Client

A web client for the Post Central API where users can register, log in, and
manage posts. The API server lives in `week-9/post-central`.

## Getting Started

1. From the `week-9/post-central` folder, install dependencies and start the
   server:

   ```bash
   npm install
   npm start
   ```

2. Open http://localhost:3000/ in your browser.

## Your Task

All the UI code is already in place. Your job is to implement the API service
functions that connect the UI to the server.

### Setup

1. Rename `src/services.starter.js` to `src/services.js` (replacing the
   existing file).
2. Open `src/services.js` — you'll see seven functions that all return a
   `NOT_IMPLEMENTED` error.
3. Implement each function so it calls the correct API endpoint using `fetch`.

### What Each Function Should Do

Every function must return an object with this shape:

```js
{
  ok: true/false,     // was the request successful?
  status: 200,        // the HTTP status code
  data: { ... },      // the parsed JSON response body
  message: ''         // error message (if any)
}
```

Use the JSDoc comments above each function for the exact endpoint, HTTP method,
headers, and request body.

Here is a summary:

| Function       | Method   | URL              | Auth   | Request Body       |
| -------------- | -------- | ---------------- | ------ | ------------------ |
| `login`        | `POST`   | `/users/login`   | No     | `{ name, password }` |
| `register`     | `POST`   | `/users/register`| No     | `{ name, password }` |
| `getProfile`   | `GET`    | `/users/me`      | Bearer | —                  |
| `getMyPosts`   | `GET`    | `/posts/me`      | Bearer | —                  |
| `createPost`   | `POST`   | `/posts`         | Bearer | `{ text }`         |
| `editPost`     | `PUT`    | `/posts/:id`     | Bearer | `{ text }`         |
| `deletePost`   | `DELETE` | `/posts/:id`     | Bearer | —                  |

**"Bearer"** means the request needs an `Authorization` header with the value
`Bearer <token>`.

**Request bodies** must be sent as JSON (`Content-Type: application/json`).

### Running Tests

There are unit tests that verify your implementation by checking that each
function calls the right URL with the right method, headers, and body. Run them
from the `post-client` folder:

```bash
npm install
npm test
```

When you first rename the starter file, all tests will fail. As you implement
each function, the corresponding tests will start passing.

### Tips

- Start with `login` — it's the simplest endpoint to test manually.
- Use the [API docs](http://localhost:3000/api-docs) (available while the
  server is running) for details on each endpoint.
- After implementing a couple of functions, look at your code. Do you see
  repeated patterns? Think about how you could reduce that repetition.
