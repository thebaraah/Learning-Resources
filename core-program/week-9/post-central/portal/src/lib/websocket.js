export default class WebSocketClient {
  #ws = null;
  #url;
  #state;
  #reconnectAttempts = 0;
  #maxReconnectAttempts = 5;
  #reconnectDelay = 3000;

  constructor(url, state) {
    this.#url = url;
    this.#state = state;
  }

  connect() {
    try {
      this.#ws = new WebSocket(this.#url);

      this.#ws.onopen = () => {
        console.log('WebSocket connected');
        this.#reconnectAttempts = 0;
        this.#updateConnectionStatus('connected');
      };

      this.#ws.onmessage = (event) => {
        try {
          const message = JSON.parse(event.data);
          console.log('WebSocket message received:', message);
          this.#handleMessage(message);
        } catch (error) {
          console.error('Error parsing WebSocket message:', error);
        }
      };

      this.#ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        this.#updateConnectionStatus('disconnected');
      };

      this.#ws.onclose = () => {
        console.log('WebSocket disconnected');
        this.#updateConnectionStatus('disconnected');
        this.#attemptReconnect();
      };
    } catch (error) {
      console.error('Error creating WebSocket:', error);
      this.#updateConnectionStatus('disconnected');
    }
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
    const currentState = this.#state.get();
    const posts = currentState.posts || [];

    // Preserve timestamp and isNew flag from server
    const postWithTimestamp = {
      ...post,
      timestamp: post.timestamp || new Date().toISOString(),
      isNew: post.isNew !== false, // Default to true if not specified
    };

    this.#state.update({
      posts: [postWithTimestamp, ...posts],
      lastAction: { type: 'post:create', post: postWithTimestamp },
    });
  }

  #handlePostUpdate(updatedPost) {
    const currentState = this.#state.get();
    const posts = currentState.posts || [];

    const updatedPosts = posts.map((post) =>
      post.id === updatedPost.id
        ? { ...updatedPost, timestamp: updatedPost.timestamp, isEdited: true }
        : post
    );

    this.#state.update({
      posts: updatedPosts,
      lastAction: { type: 'post:update', post: updatedPost },
    });
  }

  #handlePostDelete(deletedPost) {
    const currentState = this.#state.get();
    const posts = currentState.posts || [];

    // Mark post as deleted and keep it in the list
    const updatedPosts = posts.map((post) =>
      post.id === deletedPost.id ? { ...post, isDeleted: true } : post
    );

    this.#state.update({
      posts: updatedPosts,
      lastAction: { type: 'post:delete', post: deletedPost },
    });
  }

  #handleUserRegister(user) {
    const currentState = this.#state.get();
    const users = currentState.users || [];

    this.#state.update({
      users: [...users, user],
      lastAction: { type: 'user:register', user },
    });
  }

  #handleUserLogin(user) {
    const currentState = this.#state.get();
    const users = currentState.users || [];

    // Add user to the list if not already present
    const userExists = users.some((u) => u.user === user.user);
    const updatedUsers = userExists ? users : [...users, user];

    this.#state.update({
      users: updatedUsers,
      lastAction: { type: 'user:login', user },
    });
  }

  #handleUserDelete(deletedUser) {
    const currentState = this.#state.get();
    const users = currentState.users || [];
    const posts = currentState.posts || [];

    const updatedUsers = users.filter((user) => user.user !== deletedUser.user);

    // Remove all posts from the deleted user
    const updatedPosts = posts.filter((post) => post.user !== deletedUser.user);

    this.#state.update({
      users: updatedUsers,
      posts: updatedPosts,
      lastAction: { type: 'user:delete', user: deletedUser },
    });
  }

  #updateConnectionStatus(status) {
    this.#state.update({ connectionStatus: status });
  }

  #attemptReconnect() {
    if (this.#reconnectAttempts < this.#maxReconnectAttempts) {
      this.#reconnectAttempts++;
      console.log(
        `Attempting to reconnect (${this.#reconnectAttempts}/${this.#maxReconnectAttempts})...`
      );
      setTimeout(() => this.connect(), this.#reconnectDelay);
    } else {
      console.error('Max reconnection attempts reached');
    }
  }

  disconnect() {
    if (this.#ws) {
      this.#ws.close();
      this.#ws = null;
    }
  }
}
