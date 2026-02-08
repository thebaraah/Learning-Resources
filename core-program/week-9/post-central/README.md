# Post Central API

A simple REST API for managing users and posts, with real-time WebSocket updates. Users are identified by their IP address.

## Getting Started

Install dependencies and start the server:

```bash
npm install
npm start
```

The server runs on port **3000**.

## Authentication Model

There is no traditional authentication. The server identifies users by their **IP address** upon registration. When you register a user, your IP is recorded. You can only manage (edit/delete) users and posts associated with your IP.

## API Endpoints

### Users

#### `GET /users`

Returns a list of all registered users.

**Response:** `200 OK`

```json
[
  { "user": "admin", "ip": "192.168.1.10" }
]
```

---

#### `POST /users/register`

Register a new user. Your IP address is recorded automatically.

**Request body:**

| Field  | Type   | Required | Description          |
|--------|--------|----------|----------------------|
| `name` | string | Yes      | The username to register |

**Responses:**

| Status | Description |
|--------|-------------|
| `201 Created` | User registered successfully |
| `400 Bad Request` | `name` field is missing from the request body |
| `409 Conflict` | A user with that name already exists |

**Response body (success):**

```json
{ "user": "alice", "ip": "192.168.1.20" }
```

---

#### `DELETE /users/me`

Delete your own user account (identified by IP).

**Responses:**

| Status          | Description                      |
|-----------------|----------------------------------|
| `200 OK`        | User deleted successfully        |
| `404 Not Found` | No user registered with your IP  |

---

### Posts

All post endpoints require a registered user (matched by IP). Unregistered users receive a `403` error.

#### `POST /posts`

Create a new post.

**Request body:**

| Field  | Type   | Required | Description       |
|--------|--------|----------|-------------------|
| `text` | string | Yes      | The post content  |

**Responses:**

| Status | Description |
|--------|-------------|
| `200 OK` | Post created successfully |
| `400 Bad Request` | `text` field is missing from the request body |
| `403 Forbidden` | User not registered |

**Response body (success):**

```json
{ "id": 1, "user": "alice", "text": "Hello world!" }
```

---

#### `PUT /posts/:id`

Update an existing post. You can only edit your own posts.

**URL parameters:**

| Parameter | Description |
|-----------|-------------|
| `:id`     | The post ID to update |

**Request body:**

| Field  | Type   | Required | Description           |
|--------|--------|----------|-----------------------|
| `text` | string | Yes      | The new post content  |

**Responses:**

| Status | Description |
|--------|-------------|
| `200 OK` | Post updated successfully |
| `400 Bad Request` | `text` field is missing from the request body |
| `403 Forbidden` | User not registered, or post belongs to another user |
| `404 Not Found` | Post not found |

---

#### `DELETE /posts/:id`

Delete a post. You can only delete your own posts.

**URL parameters:**

| Parameter | Description |
|-----------|-------------|
| `:id`     | The post ID to delete |

**Responses:**

| Status | Description |
|--------|-------------|
| `200 OK` | Post deleted successfully |
| `403 Forbidden` | User not registered, or post belongs to another user |
| `404 Not Found` | Post not found |

---

## WebSocket

The server also runs a WebSocket server on the same port. Clients receive real-time broadcast messages when users or posts change.

**Message format:**

```json
{ "type": "<event>", "data": { ... } }
```

**Event types:**

| Event | Trigger |
|-------|---------|
| `user:register` | A new user registers |
| `user:delete` | A user is deleted |
| `post:create` | A new post is created |
| `post:update` | A post is updated |
| `post:delete` | A post is deleted |
