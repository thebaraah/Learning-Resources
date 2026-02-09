export default class PostsView {
  #container;
  #state;
  #timestampUpdateInterval;

  constructor(container, state) {
    this.#container = container;
    this.#state = state;
    this.#state.subscribe(this);

    // Update timestamps every minute
    this.#timestampUpdateInterval = setInterval(() => {
      this.render(this.#state.get());
    }, 60000);
  }

  update(state) {
    this.render(state);
  }

  render(state) {
    const posts = state.posts || [];
    const lastAction = state.lastAction;

    // Show notification for user registration
    if (lastAction && lastAction.type === 'user:register') {
      this.#showNotification(
        `${lastAction.user.user} joined Post Central`,
        'user-joined'
      );
    }

    // Show notification for user deletion
    if (lastAction && lastAction.type === 'user:delete') {
      this.#showNotification(
        `${lastAction.user.user} left Post Central`,
        'user-left'
      );
    }

    if (posts.length === 0) {
      this.#container.innerHTML = `
        <div class="posts-empty">
          No posts yet. Waiting for new posts...
        </div>
      `;
      return;
    }

    this.#container.innerHTML = posts
      .map((post) => this.#renderPost(post))
      .join('');

    // Clear isNew flags after animation completes
    const newPosts = posts.filter((post) => post.isNew);
    if (newPosts.length > 0) {
      setTimeout(() => {
        const currentState = this.#state.get();
        const updatedPosts = currentState.posts.map((post) =>
          post.isNew ? { ...post, isNew: false } : post
        );
        this.#state.update({ posts: updatedPosts });
      }, 2000);
    }
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

    this.#container.insertAdjacentElement('beforebegin', notification);

    // Auto-remove notification after 5 seconds
    setTimeout(() => {
      notification.classList.add('fade-out');
      // Remove from DOM after fade-out animation completes
      setTimeout(() => {
        notification.remove();
      }, 500);
    }, 5000);
  }

  destroy() {
    this.#state.unsubscribe(this);
    if (this.#timestampUpdateInterval) {
      clearInterval(this.#timestampUpdateInterval);
    }
  }
}
