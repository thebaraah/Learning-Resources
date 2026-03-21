class UI {
  initialize(loaderFn, countriesLoaderFn) {
    this.loaderFn = loaderFn;
    this.dom = this.getElementsWithIds(document);

    this.populateYearSelect();

    // Set up change listeners on both dropdowns
    this.dom.yearSelect.addEventListener("change", () => this.loadHolidays());
    this.dom.countrySelect.addEventListener("change", () => {
      this.updateCountryName();
      this.loadHolidays();
    });

    // Load countries on startup
    this.showLoading();
    countriesLoaderFn((err, countries) => {
      this.hideLoading();
      if (err) {
        console.error(err);
        this.showError("Failed to load countries. Please try again later.");
        return;
      }
      this.populateCountrySelect(countries);
      this.updateCountryName();
      this.loadHolidays();
    });
  }

  loadHolidays() {
    const year = this.dom.yearSelect.value;
    const countryCode = this.dom.countrySelect.value;
    this.showLoading();
    this.loaderFn(year, countryCode, (err, data) => {
      this.hideLoading();
      if (err) {
        console.error(err);
        this.showError("Failed to load holidays. Please try again later.");
      } else {
        this.renderHolidays(data);
      }
    });
  }

  getDefaultCountryCode(countries) {
    const locale = navigator.language || "";
    const parts = locale.split("-");
    if (parts.length > 1) {
      const code = parts[1].toUpperCase();
      if (countries.some((c) => c.countryCode === code)) {
        return code;
      }
    }
    return "NL";
  }

  populateCountrySelect(countries) {
    const defaultCode = this.getDefaultCountryCode(countries);
    countries.forEach((country) => {
      const option = document.createElement("option");
      option.value = country.countryCode;
      option.textContent = country.name;
      if (country.countryCode === defaultCode) {
        option.selected = true;
      }
      this.dom.countrySelect.appendChild(option);
    });
  }

  updateCountryName() {
    const select = this.dom.countrySelect;
    const selectedOption = select.options[select.selectedIndex];
    this.dom.countryName.textContent = selectedOption
      ? selectedOption.textContent
      : "";
  }

  getElementsWithIds(root) {
    const elements = root.querySelectorAll("[id]");
    return Array.from(elements).reduce((obj, element) => {
      const name = element.id
        .split("-")
        .map((part, index) => {
          if (index === 0) return part;
          return part.charAt(0).toUpperCase() + part.slice(1);
        })
        .join("");
      obj[name] = element;
      return obj;
    }, {});
  }

  formatDate(dateString) {
    const date = new Date(dateString);
    const options = { year: "numeric", month: "long", day: "numeric" };
    return date.toLocaleDateString("en-US", options);
  }

  getTypeBadgeClass(type) {
    return type.toLowerCase();
  }

  createHolidayCard(holiday) {
    const card = document.createElement("div");
    card.className = "holiday-card";

    const date = document.createElement("div");
    date.className = "holiday-date";
    date.textContent = this.formatDate(holiday.date);

    const name = document.createElement("div");
    name.className = "holiday-name";
    name.textContent = holiday.name;

    const localName = document.createElement("div");
    localName.className = "holiday-local-name";
    localName.textContent = holiday.localName;

    const typesContainer = document.createElement("div");
    typesContainer.className = "holiday-types";

    holiday.types.forEach((type) => {
      const badge = document.createElement("span");
      badge.className = `holiday-type-badge ${this.getTypeBadgeClass(type)}`;
      badge.textContent = type;
      typesContainer.appendChild(badge);
    });

    card.appendChild(date);
    card.appendChild(name);
    card.appendChild(localName);
    card.appendChild(typesContainer);

    return card;
  }

  populateYearSelect() {
    const currentYear = new Date().getFullYear();
    const startYear = currentYear - 5;
    const endYear = currentYear + 1;

    for (let year = startYear; year <= endYear; year++) {
      const option = document.createElement("option");
      option.value = year;
      option.textContent = year;
      if (year === currentYear) {
        option.selected = true;
      }
      this.dom.yearSelect.appendChild(option);
    }
  }

  renderHolidays(holidays) {
    const container = this.dom.holidaysContainer;
    container.innerHTML = "";

    if (holidays.length === 0) {
      container.innerHTML = '<div class="empty-state">No holidays found</div>';
      return;
    }

    holidays.forEach((holiday) => {
      const card = this.createHolidayCard(holiday);
      container.appendChild(card);
    });
  }

  showError(message) {
    const errorElement = this.dom.errorMessage;
    errorElement.textContent = message;
    errorElement.classList.add("active");
  }

  showLoading() {
    this.dom.loading.classList.add("active");
    this.dom.errorMessage.classList.remove("active");
  }

  hideLoading() {
    this.dom.loading.classList.remove("active");
  }
}

export const ui = new UI();
