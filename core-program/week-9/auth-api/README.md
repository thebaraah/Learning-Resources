# Exercise: Authentication

In this exercise, you will walk through a simple authentication flow using a pre-made backend and Postman.

You will:

- Register a user
- Log in and get an authentication token
- Use the token to access a protected endpoint
- Log out
- Try some requests that should fail

---

## 1. Start the backend

Go to the `auth-api/server` folder and run:

```bash
npm install
```

Start the server:

```bash
npm start
```

The server listens on `http://localhost:3000`. Continue once the server is running.

> [!TIP]
> Keep the terminal visible while you work. The server logs every request and response with color coding, so you can see exactly what is happening as you send requests from Postman.

---

## 2. Register a user

1. In Postman, create a **POST** request to the **Register user** endpoint.
2. Set the request body to **raw JSON**, for example:

   ```json
   {
     "username": "alice",
     "password": "secret123"
   }
   ```

3. Send the request and check that the status and JSON response match `README_API.md`.

---

## 3. Log in and get a token

1. Create a **POST** request to the **Login** endpoint.
2. Use the same username and password in the JSON body.
3. Send the request. The response should contain a `token` field.
4. Copy the token value (without quotes).

   The token is valid for a limited time (1 hour in this example).

---

## 4. Call a protected endpoint without a token

1. Create a **GET** request to the **Get profile** endpoint.
2. Do **not** add any Authorization header.
3. Send the request.
4. You should get a `401 Unauthorized` response and a message like “Authorization header missing”.

---

## 5. Call the same endpoint with a token

1. On the same **Get profile** request, open the **Authorization** tab.
2. Choose **Bearer Token** and paste the token from Step 3 (without quotes).
3. Send the request again.
4. You should now get a `200 OK` response and a message like “You are currently logged in as <username>”.

---

## 6. Log out

1. Create a **POST** request to the **Logout** endpoint.
2. Use the **Bearer Token** authorization with the same token.
3. Send the request and check the logout response.

---

## 7. Try error scenarios

Optionally, try requests that should fail with 4xx errors:

- Registering a username that already exists
- Registering without a username or password
- Logging in with a non-existing user
- Logging in with a wrong password

Pay attention to the status codes and error messages to understand how the API reports problems.

---

## Keep secrets out of source control

For production APIs, you should never expose your secrets in code that is pushed to a remote repository. Instead, load secrets from environment variables. The [`dotenv`](https://github.com/motdotla/dotenv) NPM package is often used for this. Here is how you would use that:

1. Install dotenv (optional helper for local dev): `npm install dotenv`.
2. Create a `.env` file (not checked in) in the `server` folder:

   ```bash
   JWT_SECRET="<your-long-random-secret>"
   ```

3. Add `.env` to `.gitignore` so it never gets committed:

   ```bash
   echo ".env" >> .gitignore
   ```

4. In your server code, load the secret with `import 'dotenv/config';` before using `process.env.JWT_SECRET`.

---

## Client (optional)

While you can test the endpoints of your API with Postman and/or `curl`, we have also provided a fully functional demo front-end application that demonstrates how a web token based authentication system might be used from the front-end side. The demo front-end resides in the `client` folder and is statically served by the backend. When the backend is running you can access the client at <http://localhost:3000>.

The client allows you to register, login and logout. After logging in, it uses the received JWT token to fetch the profile of the logged-in user and shows it on its home page. If this fetch fails, e.g. due to an expired token, the user is redirected to the login page.

Upon logging in, the client stores the JWT token in `localStorage`. When the client starts it tries to load this token from `localStorage`. If a token was found it tries to load the client's home page directly. This may fail if the token is expired as mentioned earlier in which case the login page is loaded. If no token was found in `localStorage` at client startup the login page is loaded directly.

When logging out, the token is removed from `localStorage` and the user is redirected to the login page.

The process is illustrated in the diagram below.

![client-state-diagram](../.assets/client-state-diagram.png)

The client code logs debug information in the browser's console. This may help you to follow the application flow as you navigate through its pages.
