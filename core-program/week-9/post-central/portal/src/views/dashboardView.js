export default class DashboardView {
  #container;
  #postsContainer;
  #connectionStatusElement;
  #timestampUpdateInterval;
  #lastState;

  constructor(container) {
    this.#container = container;
    this.#postsContainer = container.querySelector('#posts-container');
    this.#connectionStatusElement = container.querySelector(
      '#connection-status'
    );

    this.#timestampUpdateInterval = setInterval(() => {
      if (this.#lastState) {
        this.#render(this.#lastState);
      }
    }, 60000);
  }

  update(state) {
    this.#lastState = state;
    this.#render(state);
  }

  #render(state) {
    this.#renderConnectionStatus(state.connectionStatus);
    this.#renderPosts(state);
  }

  #renderConnectionStatus(status) {
    const indicator = this.#connectionStatusElement.querySelector(
      '.status-indicator'
    );
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

  #renderPosts(state) {
    const posts = state.posts || [];
    const lastAction = state.lastAction;

    if (
      lastAction &&
      ['user:register', 'user:login'].includes(lastAction.type)
    ) {
      this.#showNotification(
        `${lastAction.user.user} joined Post Central`,
        'user-joined'
      );
    }

    if (lastAction && lastAction.type === 'user:delete') {
      this.#showNotification(
        `${lastAction.user.user} left Post Central`,
        'user-left'
      );
    }

    if (posts.length === 0) {
      this.#postsContainer.innerHTML = `
        <div class="posts-empty">
          No posts yet. Waiting for new posts...
        </div>
      `;
      return;
    }

    this.#postsContainer.innerHTML = posts
      .map((post) => this.#renderPost(post))
      .join('');
  }

  #renderPost(post) {
    const postClasses = ['post-item'];
    if (post.isNew) {
      postClasses.push('new-post');
    }
    if (post.isDeleted) {
      postClasses.push('deleted-post');
    }

    const timestamp = post.timestamp
      ? this.#formatTimestamp(post.timestamp)
      : 'Just now';

    const postContent = post.isDeleted
      ? '[This post has been deleted]'
      : this.#escapeHtml(post.text);

    return `
      <article class="${postClasses.join(' ')}" data-post-id="${post.id}">
        <div class="post-header">
          <div>
            <span class="post-author">${this.#escapeHtml(post.user)}</span>
            <span class="post-id">#${post.id}</span>
          </div>
          <time class="post-timestamp">${timestamp}</time>
        </div>
        <div class="post-content ${post.isDeleted ? 'post-deleted-content' : ''}">${postContent}</div>
        ${post.isEdited && !post.isDeleted ? '<div class="post-meta post-edited">Edited</div>' : ''}
      </article>
    `;
  }

  #formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    const now = new Date();
    const diffInSeconds = Math.floor((now - date) / 1000);

    if (diffInSeconds < 60) {
      return 'Just now';
    } else if (diffInSeconds < 3600) {
      const minutes = Math.floor(diffInSeconds / 60);
      return `${minutes}m ago`;
    } else if (diffInSeconds < 86400) {
      const hours = Math.floor(diffInSeconds / 3600);
      return `${hours}h ago`;
    } else {
      return date.toLocaleDateString('en-US', {
        month: 'short',
        day: 'numeric',
        year: date.getFullYear() !== now.getFullYear() ? 'numeric' : undefined,
      });
    }
  }

  #escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  #showNotification(message, notificationType = 'user-joined') {
    const notification = document.createElement('div');
    notification.className = `notification ${notificationType}`;
    notification.textContent = message;

    this.#postsContainer.insertAdjacentElement('beforebegin', notification);

    setTimeout(() => {
      notification.classList.add('fade-out');
      setTimeout(() => {
        notification.remove();
      }, 500);
    }, 5000);
  }

  destroy() {
    if (this.#timestampUpdateInterval) {
      clearInterval(this.#timestampUpdateInterval);
    }
  }
}
