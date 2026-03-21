# Auth API

## Endpoints

### Register user

- **POST** `/user/register`
- **Body**: `{ "username": <username>, "password": <password> }`
- **Responses**:
  - `201 Created`: `{ "id": "<uuid>", "username": <username> }`
  - `400 Bad Request`: missing fields or username already exists

### Login

- **POST** `/user/login`
- **Body**: `{ "username": <username>, "password": <password> }`
- **Responses**:
  - `200 OK`: `{ "token": "<jwt>" }`
  - `400 Bad Request`: missing fields
  - `401 Unauthorized`: invalid username or password

### Logout

- **POST** `/user/logout`
- **Responses**:
  - `200 OK`: `{ "message": "Logged out successfully" }`

### Get profile

- **GET** `/user/me`
- **Headers**: `Authorization: Bearer <jwt>`
- **Responses**:
  - `200 OK`: `{ "message": "You are currently logged in as <username>" }`
  - `401 Unauthorized`: missing/invalid/expired token
  - `404 Not Found`: user id in token not found

## Notes

- For simplicity, this demo API comes with a hardcoded secret in `auth-service.js` for signing and verifying JSON web tokens.
- Passwords are hashed with bcrypt (10 salt rounds) before storage.
- Requests and JSON responses are logged to the console.
- Users are kept in-memory for this demo; restart clears registrations.
