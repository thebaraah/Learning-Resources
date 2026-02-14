# Post Central API

A simple REST API for managing users and posts, with real-time WebSocket updates. Users authenticate with a username and password, and receive a JWT token for subsequent requests.

## Getting Started

Install dependencies and start the server:

```bash
npm install
npm start
```

The server runs on port **3000**.

## Authentication Model

Users register with a **username** and **password**. Passwords are hashed using **bcrypt** before storage. On successful registration or login, the server returns a **JSON Web Token (JWT)**.

All endpoints except `/users/register`, `/users/login`, and `GET /posts/hello` require the JWT token in the `Authorization` header:

```http
Authorization: Bearer <token>
```

## API Endpoints

### Users

#### `POST /users/register`

Register a new user. Returns a JWT token.

**Request body:**

| Field      | Type   | Required | Description              |
|------------|--------|----------|--------------------------|
| `name`     | string | Yes      | The username to register |
| `password` | string | Yes      | The account password     |

**Responses:**

| Status            | Description                            |
|-------------------|----------------------------------------|
| `201 Created`     | User registered successfully           |
| `400 Bad Request` | `name` or `password` field is missing  |
| `409 Conflict`    | A user with that name already exists   |

**Response body (success):**

```json
{
  "user": "alice",
  "role": "user",
  "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

#### `POST /users/login`

Log in with an existing account. Returns a JWT token.

**Request body:**

| Field      | Type   | Required | Description  |
|------------|--------|----------|--------------|
| `name`     | string | Yes      | Username     |
| `password` | string | Yes      | Password     |

**Responses:**

| Status             | Description                           |
|--------------------|---------------------------------------|
| `200 OK`           | Login successful                      |
| `400 Bad Request`  | `name` or `password` field is missing |
| `401 Unauthorized` | Invalid credentials                   |

**Response body (success):**

```json
{
  "user": "alice",
  "token": "eyJhbGciOiJIUzI1NiIs..."
}
```

---

#### `GET /users`

Returns a list of all registered users. **Requires authentication.**

**Headers:**

| Header          | Value              |
|-----------------|--------------------|
| `Authorization` | `Bearer <token>`   |

**Responses:**

| Status             | Description                          |
|--------------------|--------------------------------------|
| `200 OK`           | List of users                        |
| `401 Unauthorized` | Authorization token required/invalid |

**Response body (success):**

```json
[
  {
    "user": "alice",
    "role": "user",
    "createdAt": "2025-06-15T10:30:00.000Z",
    "lastUsedAt": "2025-06-15T12:00:00.000Z"
  }
]
```

---

#### `GET /users/me`

Get the authenticated user's information. **Requires authentication.**

**Headers:**

| Header          | Value              |
|-----------------|--------------------|
| `Authorization` | `Bearer <token>`   |

**Responses:**

| Status             | Description                          |
|--------------------|--------------------------------------|
| `200 OK`           | The current user                     |
| `401 Unauthorized` | Authorization token required/invalid |
| `404 Not Found`    | User not found                       |

**Response body (success):**

```json
{
  "user": "alice",
  "role": "user",
  "createdAt": "2025-06-15T10:30:00.000Z",
  "lastUsedAt": "2025-06-15T12:00:00.000Z"
}
```

---

#### `DELETE /users/me`

Delete the authenticated user's account. **Requires authentication.**

**Headers:**

| Header          | Value              |
|-----------------|--------------------|
| `Authorization` | `Bearer <token>`   |

**Responses:**

| Status             | Description                          |
|--------------------|--------------------------------------|
| `200 OK`           | User deleted successfully            |
| `401 Unauthorized` | Authorization token required/invalid |
| `404 Not Found`    | User not found                       |

---

### Posts

Most post endpoints **require authentication**. The exception is `GET /posts/hello`, which is public and a good starting point. Include the `Authorization: Bearer <token>` header with all other requests.

#### `GET /posts/hello`

Returns a sample post with a greeting message. **No authentication required.** This is a good first endpoint to try.

**Responses:**

| Status   | Description         |
|----------|---------------------|
| `200 OK` | A sample hello post |

**Response body:**

```json
{
  "id": 0,
  "user": "post-central",
  "text": "Hello from Post Central",
  "timestamp": "2024-01-01T00:00:00.000Z"
}
```

---

#### `GET /posts/me`

Get all posts created by the authenticated user.

**Responses:**

| Status             | Description                          |
|--------------------|--------------------------------------|
| `200 OK`           | List of the user's posts             |
| `401 Unauthorized` | Authorization token required/invalid |

**Response body (success):**

```json
[
  {
    "id": 1,
    "user": "alice",
    "text": "Hello world!",
    "timestamp": "2024-01-01T00:00:00.000Z"
  }
]
```

---

#### `POST /posts`

Create a new post.

**Request body:**

| Field  | Type   | Required | Description       |
|--------|--------|----------|-------------------|
| `text` | string | Yes      | The post content  |

**Responses:**

| Status             | Description                          |
|--------------------|--------------------------------------|
| `200 OK`           | Post created successfully            |
| `400 Bad Request`  | `text` field is missing              |
| `401 Unauthorized` | Authorization token required/invalid |

**Response body (success):**

```json
{
  "id": 1,
  "user": "alice",
  "text": "Hello world!"
}
```

---

#### `PUT /posts/:id`

Update an existing post. You can only edit your own posts.

**URL parameters:**

| Parameter | Description           |
|-----------|-----------------------|
| `:id`     | The post ID to update |

**Request body:**

| Field  | Type   | Required | Description           |
|--------|--------|----------|-----------------------|
| `text` | string | Yes      | The new post content  |

**Responses:**

| Status             | Description                                     |
|--------------------|-------------------------------------------------|
| `200 OK`           | Post updated successfully                       |
| `400 Bad Request`  | `text` field is missing                         |
| `401 Unauthorized` | Authorization token required/invalid            |
| `403 Forbidden`    | Post belongs to another user                    |
| `404 Not Found`    | Post not found                                  |

---

#### `DELETE /posts/:id`

Delete a post. You can only delete your own posts.

**URL parameters:**

| Parameter | Description           |
|-----------|-----------------------|
| `:id`     | The post ID to delete |

**Responses:**

| Status             | Description                                     |
|--------------------|-------------------------------------------------|
| `200 OK`           | Post deleted successfully                       |
| `401 Unauthorized` | Authorization token required/invalid            |
| `403 Forbidden`    | Post belongs to another user                    |
| `404 Not Found`    | Post not found                                  |

---

## WebSocket

The server also runs a WebSocket server on the same port. Clients receive real-time broadcast messages when users or posts change.

**Message format:**

```json
{
  "type": "<event>",
  "data": { ... }
}
```

**Event types:**

| Event | Trigger |
|-------|---------|
| `user:register` | A new user registers |
| `user:delete` | A user is deleted |
| `post:create` | A new post is created |
| `post:update` | A post is updated |
| `post:delete` | A post is deleted |
