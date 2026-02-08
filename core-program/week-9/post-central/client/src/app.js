// This app was created with Claude Code as assistant. It is a simple client-side application that connects to a WebSocket server to display posts and user activity in real-time. The app uses an observable state pattern to manage the application state and update the UI accordingly.

import ObservableState from './lib/observableState.js';
import WebSocketClient from './lib/websocket.js';
import PostsView from './views/postsView.js';

class App {
  #state;
  #wsClient;
  // eslint-disable-next-line no-unused-private-class-members
  #postsView;
  #connectionStatusElement;

  constructor() {
    this.#state = new ObservableState();
    this.#initialize();
  }

  #initialize() {
    // Initialize UI elements
    const postsContainer = document.getElementById('posts-container');
    this.#connectionStatusElement =
      document.getElementById('connection-status');

    // Initialize state with empty posts
    this.#state.set({
      posts: [],
      users: [],
      connectionStatus: 'connecting',
    });

    // Subscribe to state changes for connection status
    this.#state.subscribe({
      update: (state) => this.#updateConnectionStatus(state.connectionStatus),
    });

    // Initialize posts view
    this.#postsView = new PostsView(postsContainer, this.#state);

    // Connect to WebSocket using current hostname (supports localhost and local IP)
    const hostname = window.location.hostname || 'localhost';
    const port = window.location.port || '3000';
    const wsUrl = `ws://${hostname}:${port}`;
    this.#wsClient = new WebSocketClient(wsUrl, this.#state);
    this.#wsClient.connect();
  }

  #updateConnectionStatus(status) {
    const indicator =
      this.#connectionStatusElement.querySelector('.status-indicator');
    const text = this.#connectionStatusElement.querySelector('.status-text');

    indicator.className = 'status-indicator';

    if (status === 'connected') {
      indicator.classList.add('connected');
      text.textContent = 'Connected';
    } else if (status === 'disconnected') {
      indicator.classList.add('disconnected');
      text.textContent = 'Disconnected';
    } else {
      text.textContent = 'Connecting...';
    }
  }
}

// Start the app when DOM is ready
window.addEventListener('DOMContentLoaded', () => {
  new App();
});
