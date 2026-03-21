import { register } from "../services/services.js";
import { putToken } from "../lib/tokenUtils.js";
import RegisterView from "../views/registerView.js";
import BasePage from "./basePage.js";

export default class RegisterPage extends BasePage {
  constructor(props) {
    super(props);
    this.view = new RegisterView({
      onSubmit: this.#onSubmit,
      onLogin: this.#onLogin,
    });
  }

  #onSubmit = async (name, password) => {
    try {
      const data = await register(name, password);

      putToken(data.token);
      this.state.update({ token: data.token, user: data.user, error: null });

      this.router.navigateTo("home");
    } catch (error) {
      this.state.update({ error: error.message });
    }
  };

  #onLogin = () => {
    this.router.navigateTo("login");
  };
}
