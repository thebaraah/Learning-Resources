# Learning Guide for Lecturers

## Introduction

In last week's session, trainees made HTTP requests to the Post Central API using `curl` in the terminal and Postman. This week, we will use the same API server, but trainees will now complete JavaScript starter code and use the `fetch()` function to interact with it. The focus is on making HTTP requests with `fetch()`, handling responses, and managing authentication with JWT tokens. Another learning goal is to practice working with promises and async/await in JavaScript.

The session is structured around a simple Node.js command-line interface (CLI) application that lets users register, log in, and perform CRUD operations on posts. The application is mostly complete, except for the file that trainees are expected to complete. This file is the `srv/service.js` module, which exports functions that handle the network requests for CRUD operations as well as for user registration and login. The CLI application imports these functions and uses them to implement the user interface.

## Setting Up the API Server

As teacher, you should run the Post Central API server on your local machine during the session. If not already done so last week, please clone the following repository and navigate to the `week-9/post-central` folder and install the dependencies.

```bash
git clone https://github.com/HackYourFuture/Learning-Resources
cd Learning-Resources/week-9/post-central
npm install
```

Start the server with:

```bash
npm start
```

You will see output in the terminal similar to this:

```text
Server is running on http://localhost:3000
Accessible on local network at http://192.168.178.88:3000
API Documentation available at http://192.168.178.88:3000/api-docs
Press Ctrl+C to stop the server
```

Also available is a companion client application, statically served by the backend. This client subscribes to notifications from the API using websockets. Access it on your computer at <http://localhost:3000> and keep it open during the session as it shows in real-time, for all to see, postings being created, updated and deleted in a WhatsApp-like fashion.

Although not required, trainees can run the client too, at the local IP address of your computer (e.g. `http://192.168.178.88:3000/`).

Since the `localhost` address will not work from their machines, your trainees will need to make their requests against the local IP address (e.g. `http://192.168.178.88:3000`).

## Session Structure (60 minutes)

### Before the Session

- [ ] Ensure Post Central API server is running on the teacher's computer.
- [ ] Copy the `services-solution.js` file from the TBC to the `src` folder. This will be used for demonstration purposes. Trainees will complete the `services.js` file on their own.
- [ ] Ensure trainees have the Learning Resources repository available on their machines. This should have already have cloned it last week.
- [ ] Verify npm packages are installed (`npm install`)

### Introduction (5 min)

- Explain what APIs are and why they're important
- Show the curl examples to demonstrate raw HTTP
- Explain we'll build the same functionality with JavaScript fetch in a Node.js CLI application
- Briefly explain JWT authentication: "A token is like a wristband at a concert - you get it at the door (login), and show it to access different areas (endpoints)"
- Demonstrate running the solution with `npm start` with the `fetchers-solution.js` file copied to the `src` folder.

### Stage 1: GET Request (15 min)

**Learning Goal:** Basic fetch, response handling, JSON parsing, Authorization header

1. Open `services.js`
2. Show the provided `authHeaders()` helper and explain what it does
3. Live code the `getMe()` function together:
   - Show `fetch()` syntax (works in Node.js 18+ without additional packages)
   - Explain `await` and why it's needed
   - Show how to pass `{ headers: authHeaders() }` as the second argument
   - Check `response.ok`
   - Call `response.json()`
4. Students implement in pairs (5 min)
5. Test together using `npm run test:get`
   - Show Vitest output in the terminal
   - Explain the test assertions (including Authorization header checks)

**Common Issues:**

- Forgetting `await` → undefined promise
- Not checking `response.ok` → parsing error responses
- Using `JSON.parse()` instead of `response.json()`
- Forgetting to include the Authorization header → 401 Unauthorized

### Stage 2: POST Request (15 min)

**Learning Goal:** Request methods, headers, body, public vs protected endpoints

1. Live code `createUser()` together:
   - Show the options object
   - Explain `method: 'POST'`
   - Emphasize `Content-Type` header importance
   - Show `JSON.stringify()` for body (now includes `{ name, password }`)
   - Highlight that register and login are **public endpoints** (no Authorization header needed)
2. Live code `loginUser()` (similar pattern, different endpoint)
3. Students implement in pairs (7 min)
4. Test together using `npm run test:post`
   - Show how tests verify the response includes a `token`
   - Explain the token flow: register/login → get token → use token

**Common Issues:**

- Missing `Content-Type` header
- Forgetting `JSON.stringify()`
- Not understanding headers object
- Accidentally adding Authorization header to register/login (not needed)

### Stage 3: Complete CRUD (20 min)

**Learning Goal:** Putting it all together with authenticated requests

1. Quick demo of solution app (3 min)
   - Run `npm start` to show the interactive CLI
   - Show the register → login → create/view/update/delete flow
2. Students implement remaining functions:
   - `getPosts()` (GET with auth header)
   - `createPost()` (POST with auth header)
   - `updatePost()` (new: PUT method with auth header)
   - `deletePost()` (DELETE with auth header)
   - `deleteUser()` (DELETE with auth header)
3. Test with `npm run test:crud`
4. Show Vitest watch mode: `npm test`

**Extension Tasks for Fast Students:**

- Display posts with formatting
- Add error handling for network failures
- Handle token expiration gracefully

### Wrap Up (5 min)

- Review key concepts:
  - HTTP methods (GET, POST, PUT, DELETE)
  - Request structure (method, headers, body)
  - Response handling (status, ok, json())
  - Authentication: public vs protected endpoints
  - The Authorization header pattern
- Introduce Vitest for testing their code
- Preview next session topics
- Share resources for further learning

## Teaching Tips

### Explaining JWT Authentication

Keep it simple for trainees:

- **What is a token?** A string that proves who you are, like a wristband at a concert
- **How do you get one?** Register or login with your name and password
- **How do you use it?** Send it in the `Authorization` header with every request
- **The `authHeaders()` helper** does the work of building the correct headers for you
- **Public endpoints** (register, login) don't need a token - you haven't logged in yet!

### Demonstrations

- Run the CLI application to show the interactive interface
- Compare curl vs fetch side-by-side (both running in terminal)
- Show what happens when headers are missing
- Show what happens when the Authorization header is missing (401 error)
- Demonstrate the prompt-sync library for user input in Node.js
- Use `node --inspect` with Chrome DevTools for debugging if needed

### Common Questions

**Q: Why `await` twice?**

```javascript
const response = await fetch(url); // Wait for HTTP response
const data = await response.json(); // Wait for body parsing
```

**Q: What's the difference between `JSON.stringify()` and `JSON.parse()`?**

- `stringify()`: JavaScript object → JSON string (for sending)
- `parse()`: JSON string → JavaScript object (for receiving)
- `response.json()`: Does parsing automatically

**Q: Why do we need `Content-Type: application/json`?**

- Server needs to know what format the data is in
- Without it, server might interpret as plain text
- Think of it like file extensions

**Q: What is the Authorization header?**

- It tells the server who you are
- Format: `Authorization: Bearer <token>`
- The token comes from register or login
- Without it, protected endpoints return 401 Unauthorized

**Q: Why don't register and login need a token?**

- You need to be able to create an account and log in without already being logged in
- These are "public" endpoints - anyone can access them
- All other endpoints are "protected" and require a valid token

### Debugging Together

When trainees get stuck:

1. Check the console output - did the request actually send?
2. Look at status code in the error message - what does it mean?
3. Is it a 401? Check if the Authorization header is included
4. Add console.log statements to check request payload - is it formatted correctly?
5. Look at error message - it usually tells you what's wrong
6. Run with `node --inspect` and use the VS Code Debugger for advanced debugging

### Differentiation

**For Struggling Students:**

- Pair with stronger trainees
- Focus on GET and POST only
- Provide more scaffolding (fill-in-the-blanks)
- Use test files to verify each step

**For Advanced Students:**

- Implement all CRUD operations
- Add query parameters for filtering
- Handle pagination
- Add request timeout handling
- Implement retry logic

## Troubleshooting

### API Server Not Running

```bash
# Students will see fetch errors
Error: fetch failed
  cause: Error: connect ECONNREFUSED 127.0.0.1:3000
```

**Fix:** Start the API server first

### 401 Unauthorized Errors

```bash
Failed to get user info: HTTP 401 Unauthorized
```

**Fix:** Make sure `authHeaders()` is used instead of just `{ 'Content-Type': 'application/json' }`. Check that `setToken()` was called after login/register.

### Module Import Errors

```bash
Error [ERR_REQUIRE_ESM]: require() of ES Module
```

**Fix:** Check `package.json` has `"type": "module"`

### JSON Parse Errors

```bash
SyntaxError: Unexpected token < in JSON
```

**Fix:** Probably getting HTML error page, check `response.ok`

## Assessment Ideas

### Quick Checks

- Can student explain what `fetch()` does?
- Can they identify the HTTP method from code?
- Can they spot missing headers?
- Can they explain the difference between public and protected endpoints?
- Can they read and understand Vitest test output?

### Practical Tasks

- "Add a function to get a specific post by ID"
- "Make the update post command work"
- "Add error messages for each failure type"
- "Write a new Vitest test for a feature"

### Code Review

- Have trainees review each other's code
- Look for proper error handling
- Check for code duplication
- Verify Authorization headers are included where needed

## Resources for Students

- MDN fetch API: <https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API>
- HTTP status codes: <https://httpstatuses.com/>
- JSON.org: <https://www.json.org/>
- REST API tutorial: <https://restfulapi.net/>
- JWT Introduction: <https://jwt.io/introduction>

## Next Steps

After this session, trainees should:

1. Practice with public APIs (GitHub, OpenWeather, etc.)
2. Explore different authentication methods (API keys, OAuth)
3. Understand CORS and why it matters
4. Explore async/await patterns more deeply
