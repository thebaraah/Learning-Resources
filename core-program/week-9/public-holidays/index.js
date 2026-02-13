import { loadHolidays, loadCountries } from './services.js';
import { ui } from './ui.js';

window.addEventListener('load', () => ui.initialize(loadHolidays, loadCountries));
