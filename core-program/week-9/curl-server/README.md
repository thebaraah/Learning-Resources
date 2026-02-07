# Curl Server

A simple Express.js REST API for managing users and their greetings. Designed for practicing `curl` commands and Postman.

The server runs on **port 3000**.

## Setup

```bash
npm install
node server.js
```

## API Endpoints

### List all users

```plaintext
GET /users
```

Returns an array of all users.

### Get a user by ID

```plaintext
GET /users/:id
```

Returns a single user object.

**Responses:**

| Status | Description    |
| ------ | -------------- |
| 200    | User found     |
| 404    | User not found |

### Create a user

```plaintext
POST /users
```

Creates a new user. The user's IP address is recorded and used for authorization on subsequent requests.

**Body (JSON):**

| Field      | Type   | Required | Description              |
| ---------- | ------ | -------- | ------------------------ |
| `name`     | string | Yes      | Unique name for the user |
| `greeting` | string | Yes      | The user's greeting      |

**Responses:**

| Status | Description                          |
| ------ | ------------------------------------ |
| 201    | User created                         |
| 400    | Missing `name` or `greeting`         |
| 409    | A user with that name already exists |

### Update a user

```plaintext
PATCH /users/:id
```

Partially updates a user. Only the user who created the resource (matched by IP address) can update it.

**Body (JSON):**

| Field      | Type   | Required | Description  |
| ---------- | ------ | -------- | ------------ |
| `name`     | string | No       | New name     |
| `greeting` | string | No       | New greeting |

**Responses:**

| Status | Description                              |
| ------ | ---------------------------------------- |
| 200    | User updated                             |
| 403    | Requester IP doesn't match the user's IP |
| 404    | User not found                           |

### Delete a user

```plaintext
DELETE /users/:id
```

Deletes a user. Only the user who created the resource (matched by IP address) can delete it.

**Responses:**

| Status | Description                              |
| ------ | ---------------------------------------- |
| 204    | User deleted (no content)                |
| 403    | Requester IP doesn't match the user's IP |
| 404    | User not found                           |

## User Object

```json
{
  "id": 1,
  "ip": "127.0.0.1",
  "name": "Alice",
  "greeting": "Hello world!"
}
```

## Notes

- User data is stored in memory and resets when the server restarts.
- PATCH and DELETE operations are restricted to the IP address that created the user.
