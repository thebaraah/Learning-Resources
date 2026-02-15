import WebSocketClient from '../lib/websocket.js';
import DashboardView from '../views/dashboardView.js';

export default class DashboardPage {
  #state;
  #view;
  #wsClient;

  constructor({ state, container }) {
    this.#state = state;

    state.set({
      posts: [],
      users: [],
      connectionStatus: 'connecting',
      lastAction: null,
    });

    this.#view = new DashboardView(container);

    const hostname = window.location.hostname || 'localhost';
    const port = window.location.port || '3000';

    this.#wsClient = new WebSocketClient(`ws://${hostname}:${port}`, {
      onMessage: (message) => this.#handleMessage(message),
      onStatusChange: (status) => state.update({ connectionStatus: status }),
    });
  }

  mount() {
    this.#state.subscribe(this.#view);
    this.#view.update(this.#state.get());
    this.#wsClient.connect();
  }

  destroy() {
    this.#state.unsubscribe(this.#view);
    this.#wsClient.disconnect();
    this.#view.destroy();
  }

  #handleMessage(message) {
    const { type, data } = message;

    switch (type) {
      case 'post:create':
        this.#handlePostCreate(data);
        break;
      case 'post:update':
        this.#handlePostUpdate(data);
        break;
      case 'post:delete':
        this.#handlePostDelete(data);
        break;
      case 'user:register':
        this.#handleUserRegister(data);
        break;
      case 'user:login':
        this.#handleUserLogin(data);
        break;
      case 'user:delete':
        this.#handleUserDelete(data);
        break;
      default:
        console.warn('Unknown message type:', type);
    }
  }

  #handlePostCreate(post) {
    const { posts } = this.#state.get();

    const postWithTimestamp = {
      ...post,
      timestamp: post.timestamp || new Date().toISOString(),
      isNew: post.isNew !== false,
    };

    this.#state.update({
      posts: [postWithTimestamp, ...posts],
      lastAction: { type: 'post:create', post: postWithTimestamp },
    });
    queueMicrotask(() => this.#state.update({ lastAction: null }));
  }

  #handlePostUpdate(updatedPost) {
    const { posts } = this.#state.get();

    const updatedPosts = posts.map((post) =>
      post.id === updatedPost.id
        ? { ...updatedPost, timestamp: updatedPost.timestamp, isEdited: true }
        : post
    );

    this.#state.update({
      posts: updatedPosts,
      lastAction: { type: 'post:update', post: updatedPost },
    });
    queueMicrotask(() => this.#state.update({ lastAction: null }));
  }

  #handlePostDelete(deletedPost) {
    const { posts } = this.#state.get();

    const updatedPosts = posts.map((post) =>
      post.id === deletedPost.id ? { ...post, isDeleted: true } : post
    );

    this.#state.update({
      posts: updatedPosts,
      lastAction: { type: 'post:delete', post: deletedPost },
    });
    queueMicrotask(() => this.#state.update({ lastAction: null }));
  }

  #handleUserRegister(user) {
    const { users } = this.#state.get();

    this.#state.update({
      users: [...users, user],
      lastAction: { type: 'user:register', user },
    });
    queueMicrotask(() => this.#state.update({ lastAction: null }));
  }

  #handleUserLogin(user) {
    const { users } = this.#state.get();

    const userExists = users.some((u) => u.user === user.user);
    const updatedUsers = userExists ? users : [...users, user];

    this.#state.update({
      users: updatedUsers,
      lastAction: { type: 'user:login', user },
    });
    queueMicrotask(() => this.#state.update({ lastAction: null }));
  }

  #handleUserDelete(deletedUser) {
    const { users, posts } = this.#state.get();

    const updatedUsers = users.filter((user) => user.user !== deletedUser.user);
    const updatedPosts = posts.filter((post) => post.user !== deletedUser.user);

    this.#state.update({
      users: updatedUsers,
      posts: updatedPosts,
      lastAction: { type: 'user:delete', user: deletedUser },
    });
    queueMicrotask(() => this.#state.update({ lastAction: null }));
  }
}
