# Slide Content: Introduction to Web APIs

Copy each slide into Google Slides. Speaker notes are included below each slide.

---

## Slide 1: Title

**Using a Web API**

Post Central — Hands-on Session

> Speaker notes: Welcome slide. Keep displayed while trainees settle in.

---

## Slide 2: What you will do today

- Make real HTTP requests to a live API server
- Use three tools: **curl**, **Postman**, **Scalar API docs**
- Work in pairs — one laptop shows the live portal, the other is your workstation
- Register, log in, create posts, and watch them appear in real time

> Speaker notes: Set expectations. Emphasise this is hands-on — they will be typing, not just watching. The portal gives them instant visual feedback for every action they take.

---

## Slide 3: The tools

| Tool                | What it is                      | Best for                             |
| ------------------- | ------------------------------- | ------------------------------------ |
| **curl**            | Command-line tool               | Quick requests, scripting            |
| **Postman**         | Graphical HTTP client           | Building and saving complex requests |
| **Scalar API docs** | Interactive docs in the browser | Exploring and testing endpoints      |

> Speaker notes: All three do the same thing — send HTTP requests. The difference is the interface. Developers typically use all of them depending on the situation.

---

## Slide 4: Post Central — the API

A simple social posting API running on the local network:

- **Users** — register, log in, view users
- **Posts** — create, read, update, delete

Authentication: register or log in to get a **token**, include it in every request.

> Speaker notes: Briefly describe the API. They don't need to memorise this — they will look it up in the docs during exercises.

---

## Slide 5: Two ways to read the docs

1. **README** — written documentation
2. **Scalar API docs** (`/api-docs`) — interactive, generated from the OpenAPI spec

_Image suggestion: side-by-side screenshots of the README and the Scalar docs page_

> Speaker notes: Show each briefly on the projector. Point out that the Scalar docs let you send requests directly from the browser.

---

## Slide 6: The Portal — live feedback

The portal at the server's root URL shows all activity in real time.

When you create a post via the API, it appears on the portal instantly.

_Image suggestion: screenshot of the portal with a few posts visible_

> Speaker notes: Switch to the portal on the projector. Explain that one laptop in each pair will keep this open so they can see their API calls working.

---

## Slide 7: Pair setup

**Laptop A (portal)**

- Open `http://<instructor-ip>:3000`

**Laptop B (workstation)**

- Open a terminal
- Open Postman
- Open `http://<instructor-ip>:3000/api-docs`

_Write the server IP address on the board._

> Speaker notes: Give them a minute to set up. Write the IP clearly on the board. Check that pairs can load the portal before moving on.

---

## Slide 8: Exercise 1 — First request with curl

**Goal:** Make your first API request.

Find the `GET /posts/hello` endpoint in the docs and call it with curl.

Hints:

- `curl <url>`
- Add `-v` to see the full HTTP conversation

Check the portal — does anything change? Why not?

> Speaker notes: This is the easy warm-up. Walk around and make sure every pair gets a JSON response. The portal won't change because GET /posts/hello is read-only — use this to explain the difference between reading and writing data.

---

## Slide 9: Exercise 2 — Explore the Scalar API docs

**Goal:** Use the interactive docs to make the same request, then explore.

1. Open `/api-docs` in the browser
2. Find `GET /posts/hello` and use "Try it"
3. Browse the other endpoints — which ones need authentication?

> Speaker notes: Let them click around. The key discovery is that some endpoints show "Authentication Required" — they require a Bearer token. Ask: "What do you think a Bearer token is?"

---

## Slide 10: Exercise 3 — Register and log in with curl

**Goal:** Register a user and get a token.

1. Find `POST /users/register` in the docs — what fields does it need?
2. Use curl to register (you need to figure out the right flags)
3. Copy the **token** from the response
4. Check the portal — did your registration show up?

Bonus: Try logging in with a wrong password.

> Speaker notes: This is the hardest exercise because trainees need to construct a curl POST with headers and a JSON body. Circulate actively. Common issues: forgetting -X POST, missing Content-Type header, unquoted JSON. If a pair is stuck after 3 minutes, give them a nudge on the -H and -d flags.

---

## Slide 11: Exercise 4 — Create a post with Postman

**Goal:** Create a post using Postman with your token.

1. Check `POST /posts` in the docs
2. Set up the request in Postman: method, URL, Authorization header, JSON body
3. Send it and watch the portal

Bonus: Call `GET /posts/me` to see all your posts.

> Speaker notes: Postman should feel easier after the curl exercise. Make sure they select "raw" + "JSON" in the body tab. If they use the Auth tab instead of manually setting the header, that's fine — show both approaches.

---

## Slide 12: Exercise 5 — Update and delete via Scalar

**Goal:** Update and delete posts. Try modifying someone else's post.

1. Use the Scalar docs to `PUT /posts/:id` — update one of your posts
2. Try to `DELETE` a post that belongs to someone else
3. What status code do you get? What does it mean?

> Speaker notes: The 403 Forbidden response is the teaching moment. Authentication = who you are. Authorization = what you're allowed to do. You're authenticated, but not authorized to delete someone else's post.

---

## Slide 13: Wrap-up

- You used **three tools** to talk to the same API
- The tool doesn't matter — understanding the **docs** and the **HTTP protocol** does
- Every app you use works like this under the hood
- Next week: you build your own front end that talks to this API

> Speaker notes: Keep it short. Reinforce that the API didn't care which tool sent the request — it only cares about the HTTP method, URL, headers, and body.
