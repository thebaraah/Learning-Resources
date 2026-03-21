import ObservableState from "./lib/observableState.js";
import DashboardPage from "./pages/dashboardPage.js";

window.addEventListener("DOMContentLoaded", () => {
  const state = new ObservableState();
  const container = document.getElementById("app-root");
  const page = new DashboardPage({ state, container });
  page.mount();
});
