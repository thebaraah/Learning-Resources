import { describe, it, expect, vi, beforeEach } from 'vitest';
import {
  login,
  register,
  getProfile,
  getMyPosts,
  createPost,
  editPost,
  deletePost,
} from '../web/src/services.js';

function mockFetchResponse(data, { ok = true, status = 200 } = {}) {
  globalThis.fetch = vi.fn(() =>
    Promise.resolve({
      ok,
      status,
      json: () => Promise.resolve(data),
    })
  );
}

function getFetchCallArgs() {
  const [url, options] = globalThis.fetch.mock.calls[0];
  return { url, ...options };
}

function getParsedBody() {
  const { body } = getFetchCallArgs();
  return JSON.parse(body);
}

function getHeader(name) {
  const { headers } = getFetchCallArgs();
  // Support both plain objects and Headers instances
  if (typeof headers.get === 'function') {
    return headers.get(name);
  }
  // Case-insensitive lookup for plain objects
  const key = Object.keys(headers).find(
    (k) => k.toLowerCase() === name.toLowerCase()
  );
  return key ? headers[key] : undefined;
}

beforeEach(() => {
  vi.restoreAllMocks();
});

describe('login', () => {
  it('should call POST /users/login with name and password', async () => {
    mockFetchResponse({ user: 'alice', token: 'jwt123' });

    const result = await login('alice', 'secret');

    expect(globalThis.fetch).toHaveBeenCalledOnce();

    const call = getFetchCallArgs();
    expect(call.url).toBe('/users/login');
    expect(call.method).toBe('POST');
    expect(getHeader('Content-Type')).toBe('application/json');

    const body = getParsedBody();
    expect(body.name).toBe('alice');
    expect(body.password).toBe('secret');

    expect(result.ok).toBe(true);
    expect(result.data.user).toBe('alice');
    expect(result.data.token).toBe('jwt123');
  });

  it('should return error info on failed login', async () => {
    mockFetchResponse(
      { error: 'Invalid credentials' },
      { ok: false, status: 401 }
    );

    const result = await login('alice', 'wrong');

    expect(result.ok).toBe(false);
    expect(result.status).toBe(401);
  });
});

describe('register', () => {
  it('should call POST /users/register with name and password', async () => {
    mockFetchResponse({ user: 'bob', token: 'jwt456' });

    const result = await register('bob', 'pass123');

    expect(globalThis.fetch).toHaveBeenCalledOnce();

    const call = getFetchCallArgs();
    expect(call.url).toBe('/users/register');
    expect(call.method).toBe('POST');
    expect(getHeader('Content-Type')).toBe('application/json');

    const body = getParsedBody();
    expect(body.name).toBe('bob');
    expect(body.password).toBe('pass123');

    expect(result.ok).toBe(true);
    expect(result.data.user).toBe('bob');
    expect(result.data.token).toBe('jwt456');
  });

  it('should return error info when user already exists', async () => {
    mockFetchResponse(
      { error: 'User already exists' },
      { ok: false, status: 409 }
    );

    const result = await register('bob', 'pass123');

    expect(result.ok).toBe(false);
    expect(result.status).toBe(409);
  });
});

describe('getProfile', () => {
  it('should call GET /users/me with Bearer token', async () => {
    mockFetchResponse({ user: 'alice' });

    const result = await getProfile('mytoken');

    expect(globalThis.fetch).toHaveBeenCalledOnce();

    const call = getFetchCallArgs();
    expect(call.url).toBe('/users/me');
    expect(call.method).toBe('GET');
    expect(getHeader('Authorization')).toBe('Bearer mytoken');

    expect(result.ok).toBe(true);
    expect(result.data.user).toBe('alice');
  });

  it('should return 401 for invalid token', async () => {
    mockFetchResponse(
      { error: 'Invalid token' },
      { ok: false, status: 401 }
    );

    const result = await getProfile('badtoken');

    expect(result.ok).toBe(false);
    expect(result.status).toBe(401);
  });
});

describe('getMyPosts', () => {
  it('should call GET /posts/me with Bearer token', async () => {
    const posts = [
      { id: 1, user: 'alice', text: 'Hello', timestamp: '2026-01-01T00:00:00Z' },
    ];
    mockFetchResponse(posts);

    const result = await getMyPosts('mytoken');

    expect(globalThis.fetch).toHaveBeenCalledOnce();

    const call = getFetchCallArgs();
    expect(call.url).toBe('/posts/me');
    expect(call.method).toBe('GET');
    expect(getHeader('Authorization')).toBe('Bearer mytoken');

    expect(result.ok).toBe(true);
    expect(result.data).toEqual(posts);
  });
});

describe('createPost', () => {
  it('should call POST /posts with Bearer token and text body', async () => {
    const post = {
      id: 1,
      user: 'alice',
      text: 'New post',
      timestamp: '2026-01-01T00:00:00Z',
    };
    mockFetchResponse(post);

    const result = await createPost('mytoken', 'New post');

    expect(globalThis.fetch).toHaveBeenCalledOnce();

    const call = getFetchCallArgs();
    expect(call.url).toBe('/posts');
    expect(call.method).toBe('POST');
    expect(getHeader('Authorization')).toBe('Bearer mytoken');
    expect(getHeader('Content-Type')).toBe('application/json');

    const body = getParsedBody();
    expect(body.text).toBe('New post');

    expect(result.ok).toBe(true);
    expect(result.data.text).toBe('New post');
  });
});

describe('editPost', () => {
  it('should call PUT /posts/:id with Bearer token and text body', async () => {
    const post = {
      id: 5,
      user: 'alice',
      text: 'Updated',
      timestamp: '2026-01-01T01:00:00Z',
      isEdited: true,
    };
    mockFetchResponse(post);

    const result = await editPost('mytoken', 5, 'Updated');

    expect(globalThis.fetch).toHaveBeenCalledOnce();

    const call = getFetchCallArgs();
    expect(call.url).toBe('/posts/5');
    expect(call.method).toBe('PUT');
    expect(getHeader('Authorization')).toBe('Bearer mytoken');
    expect(getHeader('Content-Type')).toBe('application/json');

    const body = getParsedBody();
    expect(body.text).toBe('Updated');

    expect(result.ok).toBe(true);
    expect(result.data.isEdited).toBe(true);
  });

  it('should return 403 when editing another user\'s post', async () => {
    mockFetchResponse(
      { error: 'Forbidden' },
      { ok: false, status: 403 }
    );

    const result = await editPost('mytoken', 99, 'Hacked');

    expect(result.ok).toBe(false);
    expect(result.status).toBe(403);
  });
});

describe('deletePost', () => {
  it('should call DELETE /posts/:id with Bearer token', async () => {
    const post = {
      id: 3,
      user: 'alice',
      text: 'Goodbye',
      timestamp: '2026-01-01T00:00:00Z',
      message: 'Post deleted',
    };
    mockFetchResponse(post);

    const result = await deletePost('mytoken', 3);

    expect(globalThis.fetch).toHaveBeenCalledOnce();

    const call = getFetchCallArgs();
    expect(call.url).toBe('/posts/3');
    expect(call.method).toBe('DELETE');
    expect(getHeader('Authorization')).toBe('Bearer mytoken');

    expect(result.ok).toBe(true);
    expect(result.data.message).toBe('Post deleted');
  });

  it('should not send a request body', async () => {
    mockFetchResponse({ id: 3, message: 'Post deleted' });

    await deletePost('mytoken', 3);

    const call = getFetchCallArgs();
    expect(call.body).toBeUndefined();
  });
});
