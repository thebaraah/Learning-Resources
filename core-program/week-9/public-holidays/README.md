# Public Holidays

This application displays public holidays for any supported country and year, using the **Nager.Date** public web API. It serves as a demo to illustrate how web applications interact with APIs using HTTP requests.

When you open the application, it loads a list of countries from the API and populates a dropdown. It then automatically loads the holidays for the selected country and year. Changing either dropdown triggers a new request.

## Application files

| File        | Description                                          |
| ----------- | ---------------------------------------------------- |
| index.html  | The HTML structure for the application.              |
| styles.css  | All styling for the application.                     |
| ui.js       | Handles all UI-related functionality.                |
| index.js    | The main entry point that wires everything together. |
| services.js | Where the HTTP requests are made.                    |

## Running the application

> If you haven't already done so, install the VS Code [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension before continuing.

1. Right-click `index.html` in the VS Code Explorer and select **Open with Live Server**.
2. The application should open in your browser with a country dropdown, a year dropdown, and a list of holidays.

## Understanding the API URLs

The key file to look at is `services.js`. It contains two functions that each make an HTTP request to a different API endpoint. The API documentation can be found here:

- [Nager.Date API explorer](https://date.nager.at/scalar/#api-version-3) (interactive documentation)
- [Nager.Date API documentation](https://date.nager.at/swagger/v3/swagger.json) (OpenAPI spec)

The base URL for the API is: `https://date.nager.at`

### `loadCountries`

This function loads the list of available countries. The full URL is:

```text
https://date.nager.at/api/v3/AvailableCountries
```

This is a fixed URL — it always returns the same type of data (a list of all supported countries).

### `loadHolidays`

This function loads the public holidays for a given year and country. The URL uses **path parameters** — values that are embedded directly in the URL path:

```text
https://date.nager.at/api/v3/PublicHolidays/{year}/{countryCode}
```

For example, to get the holidays for the Netherlands in 2026, the URL would be:

```text
https://date.nager.at/api/v3/PublicHolidays/2026/NL
```

In the code, the `year` and `countryCode` function parameters are inserted into the URL using a template literal:

```js
`https://date.nager.at/api/v3/PublicHolidays/${year}/${countryCode}`
```

### URL structure

Both URLs follow the same pattern:

```text
https://date.nager.at  /api/v3/  PublicHolidays/2026/NL
\_____________________/ \______/ \____________________/
       base URL          API       endpoint path
                        version    (with parameters)
```

## Inspecting network requests

Open the browser's Developer Tools by pressing <kbd>F12</kbd> on Windows/Linux or <kbd>Fn</kbd>+<kbd>F12</kbd> on a Mac. Select the **Network** tab and activate the **Fetch/XHR** filter.

Now change a dropdown. You should see a network request appear. Click on it to inspect the details:

- **Headers** — the request URL, method, and status code
- **Preview** — the parsed JSON response
- **Response** — the raw response text

Notice how the URL in the request corresponds to what is constructed in the code.

## Testing error handling

To see how the application handles errors:

1. In the Network tab, check the **Disable cache** checkbox.
2. From the throttling dropdown (shows **No throttling**), select **Offline**.
3. Change a dropdown. You should see a failed request and an error message in the UI.

Don't forget to set the throttling back to **No throttling** when you're done.
