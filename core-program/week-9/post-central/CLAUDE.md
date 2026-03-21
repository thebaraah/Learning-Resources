# CLAUDE.md

## Project overview

Post Central is an educational REST API app used during HackYourFuture classroom sessions. Trainees are the API consumers — they are learning how to read API documentation and send requests with curl and Postman. At this stage, trainees have not yet learned `fetch()`, promises, or async/await (that comes in week-10).

## Tech stack

- **Express v5** (ESM, `"type": "module"`)
- **Auth:** jsonwebtoken + bcrypt
- **WebSocket:** ws
- **Persistence:** file-based JSON (`data/users.json`, `data/posts.json`)
- **Portal frontend:** vanilla JS (served at `/`)
- **API docs:** OpenAPI 3.0 spec + Scalar UI
- **Dev tooling:** eslint, prettier, vitest

## Running the app

```bash
npm install
npm start        # starts on port 3000
npm run kill     # kills process on port 3000
```

## Architecture

```
server.js            → entry point, starts Express + WebSocket
routes/              → route definitions (userRoutes.js, postRoutes.js)
controllers/         → request handlers
services/            → business logic + JSON file persistence
middleware/          → setupMiddleware (cors, morgan, body parser, static files), auth
config/              → constants.js (PORT, JWT_SECRET, JWT_EXPIRES_IN), openapi.yaml
utils/               → websocket.js (broadcast helper)
data/                → users.json, posts.json (auto-created on first run)
portal/              → real-time dashboard frontend (vanilla JS, WebSocket client)
```

Routes → controllers → services pattern. Services read/write JSON files directly with `fs`.

## Auth and roles

- JWT Bearer tokens (`Authorization: Bearer <token>`)
- Two roles: `user` and `admin`
- Admin account (username: `admin`, password: `admin`) is auto-seeded on first run when `data/users.json` doesn't exist
- `req.user` is set by the `authenticate` middleware with `{ user, role }` from the JWT payload

**Public endpoints:**

- `POST /users/register`
- `POST /users/login`
- `GET /posts/hello`

**Protected endpoints (require Bearer token):**

- `GET /users` — returns all non-admin users
- `GET /users/me`, `DELETE /users/me`
- `DELETE /users/:name` — admin only
- `GET /posts/me`, `POST /posts`, `PUT /posts/:id`, `DELETE /posts/:id`

## Code conventions

- ES modules (`import`/`export`), no CommonJS
- Semicolons required
- Arrow functions for all function definitions (`export const fn = (args) => { ... }`)
- Error responses use `{ error: '...' }` pattern
- Consistent HTTP status codes: 200 success, 201 created, 400 bad request, 401 unauthorized, 403 forbidden, 404 not found
- JSON files saved with 2-space indentation

## Key guardrails

- **README.md is trainee-facing** — never expose admin credentials or internal details there
- **Config values are intentionally hardcoded** in `config/constants.js` (JWT secret, port, expiry) — this is fine for an educational app. **Exception:** the admin seed password is read from `process.env.ADMIN_PASSWORD` (loaded via dotenv) with fallback to `'admin'`
- **Admin is hidden from `GET /users`** — the controller filters out admin users; preserve this behavior
- **No database** — persistence is JSON files in `data/`; don't introduce a database
- **Keep it simple and beginner-friendly** — avoid over-engineering, complex abstractions, or advanced patterns that would confuse trainees reading the code

## WebSocket events

Six event types are broadcast to all connected portal clients:

| Event           | Trigger                                  |
| --------------- | ---------------------------------------- |
| `user:register` | New user registers                       |
| `user:login`    | User logs in                             |
| `user:delete`   | User is deleted                          |
| `post:create`   | Post is created (includes `isNew: true`) |
| `post:update`   | Post is updated                          |
| `post:delete`   | Post is deleted                          |

Message format: `{ type, data }`. On initial connection, all existing posts are sent with `isNew: false`.

## API docs

- OpenAPI 3.0 spec at `config/openapi.yaml`
- Scalar UI served at `/api-docs`
- Raw spec available as JSON at `/openapi.json`
- **Keep the spec in sync** when modifying endpoints

## Testing

Vitest is installed as a dev dependency but no tests exist yet.
