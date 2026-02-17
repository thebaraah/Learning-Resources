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

> [!TIP]
> If you haven't already done so, install the VS Code [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) extension before continuing.
>
> 1. Right-click `index.html` in the VS Code Explorer and select **Open with Live Server**.
> 2. The application should open in your browser with a country dropdown, a year dropdown, and a list of holidays.

## Exercise

Open `services.js` — it contains two functions that each need to make an HTTP request to a different endpoint of the **Nager.Date** API. The URLs are currently set to `'TODO'` and need to be replaced with the correct ones.

Use the API documentation to find the right endpoints:

- [Nager.Date API explorer](https://date.nager.at/scalar/#api-version-3) (interactive documentation)
- [Nager.Date API documentation](https://date.nager.at/swagger/v3/swagger.json) (OpenAPI spec)

The base URL for the API is: `https://date.nager.at`

**What to do:**

1. `loadCountries()` — Find the endpoint that returns a list of available countries. This is a fixed URL (no parameters needed).
2. `loadHolidays(year, countryCode)` — Find the endpoint that returns public holidays for a specific year and country. You'll need to use a template literal to insert the function parameters into the URL.

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
