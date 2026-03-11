# Week 10 – Asynchronous Programming

## HackYourFuture Core Program

---

# Today's Agenda

1. Synchronous vs Asynchronous Code
2. Callbacks & Callback Hell
3. Promises (.then / .catch / .finally)
4. Asynchronous File I/O
5. The Event Loop
6. The Fetch API
7. Async/Await & Promise.all()

---

# Why Asynchronous Code?

Real applications need to:

- Talk to servers
- Read and write files
- Wait for timers
- React to user input

**…all without freezing the interface.**

JavaScript is **single-threaded** — it can only run one thing at a time.

---

# Synchronous = Blocking

Think of it as **standing at the door** waiting for a pizza delivery, doing nothing else.

```js
function wait(delay) {
  const endTime = Date.now() + delay;
  while (Date.now() < endTime) {
    // blocks everything!
  }
}

wait(1000);
console.log("This waits until the loop is done");
```

The page freezes. The user can't click, scroll, or type.

---

# Asynchronous = Non-blocking

Think of it as **ordering the pizza**, then watching TV while you wait.

```js
console.log("Before timer");

setTimeout(() => {
  console.log("Timer done!");
}, 1000);

console.log("After timer");
```

**Output:**
```
Before timer
After timer
Timer done!       ← appears after ~1 second
```

JavaScript moves on immediately — the callback runs *later*.

---

# Callback Functions

A **callback** is a function you pass as an argument to another function.

The receiving function decides **when** to call it.

```js
function greetLater(callback) {
  console.log("Preparing to greet...");
  callback();
}

greetLater(() => {
  console.log("Hello from the callback!");
});
```

You already know callbacks from `.forEach()`, `.map()`, `.filter()`.

---

# Timers: setTimeout & setInterval

**setTimeout** — runs the callback **once** after a delay:

```js
setTimeout(() => {
  console.log("Runs once after 1 second");
}, 1000);
```

**setInterval** — runs the callback **repeatedly** at an interval:

```js
const id = setInterval(() => {
  console.log("Every second");
}, 1000);

// Stop it later:
clearInterval(id);
```

---

# Callback Hell (Pyramid of Doom)

When async operations depend on each other, callbacks get deeply nested:

```js
fs.readFile(path1, (err, result1) => {
  if (err) { /* handle */ return; }
  fs.readFile(path2, (err, result2) => {
    if (err) { /* handle */ return; }
    fs.writeFile(path3, result2, (err) => {
      if (err) { /* handle */ return; }
      // done
    });
  });
});
```

**Problems:** hard to read, hard to maintain, error handling everywhere.

---

# Promises to the Rescue

A **Promise** is an object representing the eventual completion (or failure) of an async operation.

Three states:

- **pending** — not yet settled
- **fulfilled** — completed successfully
- **rejected** — something went wrong

Once settled, a promise is **immutable** — it cannot change again.

---

# Creating a Promise

```js
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Done!");
    // or: reject(new Error("Failed"));
  }, 1000);
});
```

- Call `resolve(value)` for success
- Call `reject(error)` for failure
- The first call wins — later calls are ignored

---

# Using Promises: .then() and .catch()

```js
promise
  .then((value) => {
    console.log("Fulfilled with:", value);
  })
  .catch((error) => {
    console.error("Rejected with:", error);
  });
```

- `.then()` runs when the promise **fulfills**
- `.catch()` runs when the promise **rejects**
- Both are scheduled as **microtasks** (more on this later)

---

# Promise Chains

When one async step depends on another, **chain** your `.then()` calls:

```js
getUser(1)
  .then((user) => {
    console.log("User:", user.name);
    return getPosts(user.name);  // ← must return!
  })
  .then((posts) => {
    console.log("Posts:", posts);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
```

**Key rule:** always `return` inside `.then()` when chaining.

A single `.catch()` at the end handles errors from the entire chain.

---

# .finally() — Cleanup

Runs regardless of success or failure. Does not receive the value or error.

```js
fetchData()
  .then((data) => { /* use data */ })
  .catch((err) => { /* handle error */ })
  .finally(() => {
    // cleanup: close connections, stop spinners, etc.
  });
```

---

# Async File I/O in Node.js

**Synchronous (blocking):**

```js
import fs from "node:fs";
const content = fs.readFileSync("file.txt", "utf8");
```

**Asynchronous with promises (non-blocking):**

```js
import fsPromises from "node:fs/promises";

fsPromises.readFile("file.txt", "utf8")
  .then((content) => { /* use content */ })
  .catch((err) => { /* handle error */ });
```

Use `fs/promises` for async file operations in Node.js.

---

# The Event Loop — Big Picture

JavaScript has **one thread** but uses **queues** to handle async work:

1. Run current code on the **Call Stack**
2. When the stack is empty → drain the **Microtask Queue** (Promise callbacks)
3. Then take the next item from the **Task Queue** (setTimeout, I/O)
4. Repeat

**Key takeaway:** Promise callbacks (microtasks) always run **before** timer callbacks (tasks).

---

# Event Loop — Predict the Output

```js
console.log("Hello!");

Promise.resolve().then(() => {
  console.log("promise then");
});

setTimeout(() => {
  console.log("timeout");
}, 0);

console.log("Goodbye!");
```

**Output:**
```
Hello!
Goodbye!
promise then     ← microtask runs first
timeout          ← task runs after
```

---

# The Fetch API

`fetch()` makes HTTP requests from JavaScript and returns a **promise**.

```js
fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => {
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    return response.json();
  })
  .then((data) => console.log(data))
  .catch((error) => console.error(error));
```

**Important:** `fetch` only rejects on **network errors**, not on 404/500!

Always check `response.ok`.

---

# Fetch — Common Pitfalls

**Forgetting to return `response.json()`:**

```js
// ❌ Wrong — next .then() gets undefined
.then((response) => {
  response.json();  // missing return!
})

// ✅ Correct
.then((response) => {
  return response.json();
})
```

**Ignoring `response.ok`:**

```js
// ❌ A 404 still resolves the promise
// ✅ Always check response.ok and throw if false
```

---

# POST Requests with Fetch

```js
fetch("https://jsonplaceholder.typicode.com/posts", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    title: "Hello",
    body: "World",
    userId: 1,
  }),
})
  .then((response) => response.json())
  .then((data) => console.log(data));
```

Same HTTP concepts as curl and Postman, now in JavaScript.

---

# From Promises to async/await

**Promise chain version:**

```js
function ask() {
  return whatIsTheMeaningOfLife()
    .then((result) => { /* handle */ })
    .catch((err) => { /* handle */ });
}
```

**async/await version:**

```js
async function ask() {
  try {
    const result = await whatIsTheMeaningOfLife();
    // handle result
  } catch (err) {
    // handle error
  }
}
```

`await` pauses the async function until the promise settles.

---

# async/await Rules

- `async` functions **always return a promise**
- `await` can only be used **inside** an `async` function
- `await` on a fulfilled promise → gives the value
- `await` on a rejected promise → throws (catch with `try/catch`)
- Under the hood, it's still promises and microtasks

```js
async function add(a, b) {
  return a + b;
}

add(2, 3).then((val) => console.log(val)); // 5
```

---

# Fetch with async/await

```js
async function fetchPost() {
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}`);
    }
    const data = await response.json();
    console.log("Data:", data);
  } catch (error) {
    console.error("Error:", error.message);
  }
}
```

Reads like synchronous code, but is fully non-blocking.

---

# Sequential vs Parallel

**Sequential (slow)** — each request waits for the previous one:

```js
const post1 = await fetch(url1).then((r) => r.json());
const post2 = await fetch(url2).then((r) => r.json());
// Total time ≈ time1 + time2
```

**Parallel (fast)** — all requests start at once:

```js
const [post1, post2] = await Promise.all([
  fetch(url1).then((r) => r.json()),
  fetch(url2).then((r) => r.json()),
]);
// Total time ≈ max(time1, time2)
```

---

# Promise.all()

Takes an **array of promises**, returns a single promise that:

- **Fulfills** with an array of all values (same order as input)
- **Rejects** as soon as **any** promise rejects

```js
const responses = await Promise.all(
  urls.map((url) => fetch(url))
);

const data = await Promise.all(
  responses.map((r) => r.json())
);
```

Pattern: "start everything, then `await Promise.all()`"

---

# When to Use What?

| Situation | Approach |
|---|---|
| Operations depend on each other | **Sequential** (`await` one by one) |
| Operations are independent | **Parallel** (`Promise.all()`) |
| Need the first result only | `Promise.race()` |
| Simple one-off async call | `.then()` chain or `async/await` |

---

# Key Takeaways

1. **Blocking = bad** — always write non-blocking async code
2. **Callbacks** work but lead to "callback hell" when nested
3. **Promises** flatten the chain — `.then()` / `.catch()` / `.finally()`
4. **Event Loop**: microtasks (promises) run before tasks (timers)
5. **Fetch API** returns promises — always check `response.ok`
6. **async/await** is syntactic sugar over promises — cleaner to read
7. **Promise.all()** runs independent operations in parallel

---

# Questions?

Week 10 — Asynchronous Programming

**Resources:**

- Notion: hub.hackyourfuture.nl/core-program-week-10
- GitHub: HackYourFuture/Learning-Resources (week-10)
- MDN: Promises, async/await, Fetch API
