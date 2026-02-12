# Fetch API Quick Reference

Quick reference guide for students during the exercise.

## Basic Fetch Structure

### GET Request (with Authorization)

```javascript
const response = await fetch(url, {
  headers: authHeaders(),
});
const data = await response.json();
```

### POST/PUT Request (with Authorization)

```javascript
const response = await fetch(url, {
  method: 'POST', // or 'PUT', 'DELETE'
  headers: authHeaders(),
  body: JSON.stringify({ key: 'value' }),
});
const data = await response.json();
```

### Public Request (no Authorization needed)

```javascript
const response = await fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ key: 'value' }),
});
const data = await response.json();
```

## Authentication

### The Authorization Header

Protected endpoints require a JWT token in the `Authorization` header:

```javascript
headers: {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer <your-token>'
}
```

The `authHeaders()` helper builds this for you automatically!

### Public vs Protected Endpoints

| Endpoint          | Needs Token? |
| ----------------- | ------------ |
| `/users/register` | No           |
| `/users/login`    | No           |
| Everything else   | Yes          |

## Common Patterns

### Check Response Status

```javascript
if (!response.ok) {
  throw new Error(`HTTP ${response.status} ${response.statusText}`);
}
```

### Complete Request Pattern

```javascript
const functionName = async () => {
  const response = await fetch(url, {
    headers: authHeaders(),
  });
  if (!response.ok) {
    throw new Error(`Failed: ${response.status} ${response.statusText}`);
  }
  return await response.json();
};
```

## HTTP Methods

| Method | Purpose                  |
| ------ | ------------------------ |
| GET    | Retrieve data            |
| POST   | Create new resource      |
| PUT    | Update existing resource |
| DELETE | Remove resource          |

## Required Headers

For JSON requests with authentication:

```javascript
headers: authHeaders()
// This produces:
// {
//   'Content-Type': 'application/json',
//   'Authorization': 'Bearer <your-token>'
// }
```

For public endpoints (register, login):

```javascript
headers: {
  'Content-Type': 'application/json'
}
```

## Request Body

Convert JavaScript object to JSON string:

```javascript
body: JSON.stringify({ name: 'value' });
```

❌ **Don't do this:**

```javascript
body: {
  name: 'value';
} // Won't work!
```

## Response Handling

### Parse JSON

```javascript
const data = await response.json();
```

### Access Response Properties

```javascript
response.status; // 200, 404, 500, etc.
response.ok; // true if status 200-299
response.statusText; // "OK", "Not Found", etc.
```

## Common Mistakes

### 1. Missing await

```javascript
// ❌ Wrong
const data = fetch(url).json();

// ✅ Correct
const response = await fetch(url, { headers: authHeaders() });
const data = await response.json();
```

### 2. Missing Content-Type

```javascript
// ❌ Wrong
fetch(url, {
  method: 'POST',
  body: JSON.stringify(data),
});

// ✅ Correct
fetch(url, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify(data),
});
```

### 3. Not checking response.ok

```javascript
// ❌ Wrong
const data = await fetch(url).then((response) => response.json());

// ✅ Correct
const response = await fetch(url, { headers: authHeaders() });
if (!response.ok) {
  throw new Error(`HTTP ${response.status} ${response.statusText}`);
}
const data = await response.json();
```

### 4. Using JSON.parse on response

```javascript
// ❌ Wrong
const data = JSON.parse(response);

// ✅ Correct
const data = await response.json();
```

### 5. Forgetting Authorization header

```javascript
// ❌ Wrong - will get 401 Unauthorized
const response = await fetch(`${BASE_URL}/posts/me`);

// ✅ Correct - include auth token
const response = await fetch(`${BASE_URL}/posts/me`, {
  headers: authHeaders(),
});
```

### 6. Adding Authorization to public endpoints

```javascript
// ❌ Unnecessary (but won't break)
const response = await fetch(`${BASE_URL}/users/register`, {
  method: 'POST',
  headers: authHeaders(), // Not needed for register!
  body: JSON.stringify({ name, password }),
});

// ✅ Correct - register and login are public
const response = await fetch(`${BASE_URL}/users/register`, {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name, password }),
});
```

## Template for API Functions

### Protected Endpoint (most functions)

```javascript
const functionName = async (parameter) => {
  const response = await fetch(`${BASE_URL}/endpoint`, {
    method: 'METHOD',
    headers: authHeaders(),
    body: JSON.stringify({ key: parameter }),
  });

  if (!response.ok) {
    throw new Error(`Error message: HTTP ${response.status}`);
  }

  return await response.json();
};
```

### Public Endpoint (register, login)

```javascript
const functionName = async (name, password) => {
  const response = await fetch(`${BASE_URL}/endpoint`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name, password }),
  });

  if (!response.ok) {
    throw new Error(`Error message: HTTP ${response.status}`);
  }

  return await response.json();
};
```

## Testing Your Functions

Use `console.log()` to debug:

```javascript
console.log('Response:', response);
console.log('Status:', response.status);
console.log('Data:', data);
```

## Need Help?

1. Check the error message - it usually tells you what's wrong
2. Got a 401? Make sure you're using `authHeaders()` for protected endpoints
3. Verify the API endpoint in README.md
4. Look at the test files for examples
5. Compare with curl examples
6. Ask your lecturer!

## Next Steps After Exercise

- Try other public APIs (GitHub, weather, etc.)
- Explore different authentication methods (API keys, OAuth)
- Explore async/await patterns
- Understand CORS
