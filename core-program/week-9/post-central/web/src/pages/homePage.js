import {
  getProfile,
  getMyPosts,
  createPost,
  editPost,
  deletePost,
} from '../services.js';
import { removeToken } from '../lib/tokenUtils.js';
import HomeView from '../views/homeView.js';
import BasePage from './basePage.js';

export default class HomePage extends BasePage {
  constructor(props) {
    super(props);
    this.view = new HomeView({
      onLogout: this.#onLogout,
      onCreatePost: this.#onCreatePost,
      onEditPost: this.#onEditPost,
      onDeletePost: this.#onDeletePost,
    });
    this.#loadData();
  }

  #handleAuthError(result) {
    if (result.status === 401) {
      removeToken();
      this.state.clear();
      this.router.navigateTo('login');
      return true;
    }
    return false;
  }

  async #loadData() {
    const { token } = this.state.get();
    if (!token) {
      this.router.navigateTo('login');
      return;
    }

    try {
      const profileResult = await getProfile(token);

      if (!profileResult.ok) {
        if (this.#handleAuthError(profileResult)) return;
        throw new Error(profileResult.message);
      }

      const postsResult = await getMyPosts(token);

      if (!postsResult.ok) {
        if (this.#handleAuthError(postsResult)) return;
        throw new Error(postsResult.message);
      }

      this.state.update({
        user: profileResult.data.user,
        posts: postsResult.data,
        error: null,
      });
    } catch (error) {
      this.state.update({ error: error.message });
    }
  }

  #onLogout = () => {
    removeToken();
    this.state.clear();
    this.router.navigateTo('login');
  };

  #onCreatePost = async (text) => {
    const { token } = this.state.get();
    try {
      const result = await createPost(token, text);
      if (!result.ok) {
        if (this.#handleAuthError(result)) return;
        throw new Error(result.message);
      }
      await this.#refreshPosts();
    } catch (error) {
      this.state.update({ error: error.message });
    }
  };

  #onEditPost = async (id, text) => {
    const { token } = this.state.get();
    try {
      const result = await editPost(token, id, text);
      if (!result.ok) {
        if (this.#handleAuthError(result)) return;
        throw new Error(result.message);
      }
      await this.#refreshPosts();
    } catch (error) {
      this.state.update({ error: error.message });
    }
  };

  #onDeletePost = async (id) => {
    const { token } = this.state.get();
    try {
      const result = await deletePost(token, id);
      if (!result.ok) {
        if (this.#handleAuthError(result)) return;
        throw new Error(result.message);
      }
      await this.#refreshPosts();
    } catch (error) {
      this.state.update({ error: error.message });
    }
  };

  async #refreshPosts() {
    const { token } = this.state.get();
    const result = await getMyPosts(token);
    if (result.ok) {
      this.state.update({ posts: result.data, error: null });
    }
  }
}
