import { login } from '../services.js';
import { putToken } from '../lib/tokenUtils.js';
import LoginView from '../views/loginView.js';
import BasePage from './basePage.js';

export default class LoginPage extends BasePage {
  constructor(props) {
    super(props);
    this.view = new LoginView({
      onSubmit: this.#onSubmit,
      onRegister: this.#onRegister,
    });
  }

  #onSubmit = async (name, password) => {
    try {
      const result = await login(name, password);

      if (!result.ok) {
        throw new Error(result.message || 'Login failed');
      }

      const token = result.data?.token;
      putToken(token);
      this.state.update({ token, user: result.data?.user, error: null });

      this.router.navigateTo('home');
    } catch (error) {
      this.state.update({ error: error.message });
    }
  };

  #onRegister = () => {
    this.router.navigateTo('register');
  };
}
