function getRequest(url, callback) {
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => callback(null, data))
    .catch((error) => callback(error));
}

export function loadCountries(callback) {
  // TODO: Replace the URL below with the correct API endpoint for loading
  // available countries.
  getRequest("TODO", (err, data) => {
    if (err) {
      console.error(err);
    }
    callback(err, data);
  });
}

export function loadHolidays(year, countryCode, callback) {
  // TODO: Replace the URL below with the correct API endpoint for loading
  // public holidays. Use a template literal to insert the `year` and
  // `countryCode` parameters into the URL.
  getRequest("TODO", (err, data) => {
    if (err) {
      console.error(err);
    }
    callback(err, data);
  });
}
