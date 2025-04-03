# 5-Day Weather Forecast Dashboard for Kirkland, US

This project is a Python-based web application that provides a 5-day weather forecast for Kirkland, US, using the OpenWeatherMap API. The application is built with Streamlit, making it easy to deploy and share as a web-based dashboard.

## Features

* **Real-time Weather Data:** Fetches 5-day weather forecast data from the OpenWeatherMap API.
* **Current Weather Display:** Shows current temperature, humidity, wind speed, and weather description.
* **Next 3 Hours Forecast:** Provides a brief forecast for the next 3 hours.
* **5-Day Average Temperature:** Calculates and displays the average temperature over the 5-day period.
* **Daily Temperature and Wind Speed Ranges:** Visualizes the daily minimum, maximum, and average temperatures and wind speeds using bar and line charts.
* **Temperature vs. Humidity Correlation:** Presents a scatter plot showing the correlation between temperature and humidity.
* **Temperature Trend Over 5 Days:** Displays the temperature trend over the 5-day forecast period using a line plot.
* **Statistical Summary:** Provides a statistical summary of temperature, humidity, and wind speed.
* **Timezone Handling:** Converts timestamps to the local "US/Pacific" timezone.
* **Error Handling:** Implements robust error handling for API requests and JSON parsing.

## Technologies Used

* Python
* Streamlit
* Pandas
* Requests
* Matplotlib
* Seaborn
* Datetime
* Pytz

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Cath-L/weather-dashboard.git](https://github.com/Cath-L/weather-dashboard.git)
    cd weather-dashboard
    ```
2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    (You'll need to create a `requirements.txt` file listing your dependencies. Run `pip freeze > requirements.txt` in your terminal)
3.  **Run the Streamlit app:**
    ```bash
    streamlit run weather_dashboard.py
    ```
4.  **Obtain an API Key:**
    * You'll need an API key from OpenWeatherMap (https://openweathermap.org/).
    * Replace `"113a2cce25ed392d8486b8deb259925b"` with your own API key in the `weather_dashboard.py` file.

## Usage

* Open the Streamlit app in your web browser.
* The dashboard will display the 5-day weather forecast for Kirkland, US.
* Observe the various charts, metrics, and textual descriptions to understand the weather forecast.

## Data Source

* OpenWeatherMap API: [https://openweathermap.org/forecast5](https://openweathermap.org/forecast5)

## Author

* Cathy Leung

## Considerations and Potential Improvements

* **City Selection:** The application currently only displays weather for Kirkland, US. Consider adding an input field to allow users to select different cities.
* **More Detailed Forecast:** Include additional weather details, such as precipitation probability, UV index, etc.
* **Interactive Charts:** Add interactive elements to the charts, such as tooltips or zoom functionality.
* **Error Handling:** Implement more specific error messages for various scenarios.
* **Unit Selection:** Allow users to choose between metric and imperial units.
* **Add outlier detection:** Add a function to detect and handle outliers.
* **Add forecasting:** Add a section that forecast future weather.
