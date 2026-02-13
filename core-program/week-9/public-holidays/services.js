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
  getRequest('https://date.nager.at/api/v3/AvailableCountries', (err, data) => {
    if (err) {
      console.error(err);
    }
    callback(err, data);
  });
}

export function loadHolidays(year, countryCode, callback) {
  getRequest(
    `https://date.nager.at/api/v3/PublicHolidays/${year}/${countryCode}`,
    (err, data) => {
      if (err) {
        console.error(err);
      }
      callback(err, data);
    }
  );
}
