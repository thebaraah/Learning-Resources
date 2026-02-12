# Post Central - Project Structure

```plaintext
post-central/
│
├── README.md                    # Main documentation, API reference, learning objectives
├── TEACHING_GUIDE.md            # For lecturers: session structure, tips, troubleshooting
├── QUICK_REFERENCE.md           # Student cheat sheet for fetch syntax
├── IMPLEMENTATION_SUMMARY.md    # Overview of the implementation
├── PROJECT_STRUCTURE.md         # This file
│
├── package.json                 # Dependencies and helpful npm scripts
├── package-lock.json            # Locked dependency versions
├── vitest.config.js             # Vitest test runner configuration
├── .gitignore                   # Git ignore rules
│
├── src/                         # Source code
│   ├── post-cli.js              # Interactive CLI application entry point
│   ├── services.js              # Student working file with API functions to implement
│   └── fetchers-solution.js     # Complete reference implementation
│
├── curl/                        # cURL examples for comparison
│   ├── README.md                # cURL documentation
│   ├── register.sh              # POST register user (name + password)
│   ├── login.sh                 # POST login user (name + password)
│   ├── get-user.sh              # GET user info (with token)
│   ├── get-posts.sh             # GET all posts (with token)
│   ├── post-message.sh          # POST new post (with token)
│   ├── update-message.sh        # PUT update post (with token)
│   └── post-cli.sh              # Interactive bash CLI with login
│
└── tests/                       # Vitest test files
    ├── test-get.test.js         # Test GET request functions
    ├── test-post.test.js        # Test POST request functions (+ loginUser)
    └── test-crud.test.js        # Test all CRUD operations
```

## File Purposes

### For Students

- **README.md** - Start here! Complete guide to the exercise
- **QUICK_REFERENCE.md** - Keep this open while coding
- **src/services.js** - Implement your fetch API functions here
- **src/post-cli.js** - Interactive CLI app that imports and runs your functions
- **tests/** - Vitest tests to verify your code

### For Lecturers

- **TEACHING_GUIDE.md** - Lesson plan and teaching tips
- **src/fetchers-solution.js** - Reference for live coding
- **curl/** - Demonstrate HTTP requests before fetch

### Key Files Explained

- **src/post-cli.js** - Interactive CLI entry point with register/login flow, imports student functions
- **src/services.js** - Students implement API functions here (token management provided, API functions are TODOs)
- **src/fetchers-solution.js** - Complete API function implementations with JWT auth

## Available Commands

```bash
# Main application
npm start              # Run the interactive CLI (src/post-cli.js)

# Testing
npm test               # Run all tests in watch mode
npm run test:run       # Run all tests once
npm run test:get       # Test GET request functions
npm run test:post      # Test POST request functions (+ loginUser)
npm run test:crud      # Test all CRUD operations

# cURL examples (pass token as argument)
./curl/register.sh
./curl/login.sh
./curl/get-user.sh <token>
./curl/get-posts.sh <token>
./curl/post-message.sh <token>
./curl/update-message.sh <token>
```

## CLI Commands (inside the app)

| Command        | Description          |
| -------------- | -------------------- |
| `/view`        | See all your posts   |
| `/update <id>` | Edit a post          |
| `/delete <id>` | Remove a post        |
| `/leave`       | Delete your account  |
| `/exit`        | Quit the application |
| _(any text)_   | Create a new post    |

## Suggested Learning Path

1. Read README.md
2. Look at curl examples to understand HTTP
3. Run tests to see expected behavior: `npm test`
4. Open src/services.js and start coding
5. Test frequently: `npm test` (watch mode) or `npm run test:get`, `npm run test:post`
6. Refer to QUICK_REFERENCE.md as needed
7. Run the app: `npm start` to see your functions in action
8. Compare with src/fetchers-solution.js when stuck

## Key Learning Concepts

- ✓ Making HTTP requests with fetch()
- ✓ Using async/await
- ✓ HTTP methods (GET, POST, PUT, DELETE)
- ✓ Request headers and body
- ✓ Authorization header and JWT tokens
- ✓ Public vs protected endpoints
- ✓ Response handling and error checking
- ✓ Working with JSON
- ✓ CRUD operations
