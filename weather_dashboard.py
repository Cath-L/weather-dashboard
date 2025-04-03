import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import pytz

API_KEY = "113a2cce25ed392d8486b8deb259925b"
CITY = "Kirkland,US"

url = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    weather_data = []
    for forecast in data["list"]:
        rain = forecast.get("rain", {}).get("3h", 0)
        snow = forecast.get("snow", {}).get("3h", 0)
        weather_data.append({
            "timestamp": forecast["dt"],
            "temperature": forecast["main"]["temp"],
            "humidity": forecast["main"]["humidity"],
            "wind_speed": forecast["wind"]["speed"],
            "description": forecast["weather"][0]["description"],
            "rain": rain,
            "snow": snow
        })

    df = pd.DataFrame(weather_data)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s").dt.tz_localize('UTC')
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    df["month"] = df["timestamp"].dt.month

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data: {e}")
    st.stop()
except KeyError as e:
    st.error(f"Error parsing JSON: Missing key {e}")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
    st.stop()

st.title(f"5-Day Weather Forecast for {CITY}")
st.write(
    """
    This dashboard displays a 5-day weather forecast obtained from the OpenWeatherMap API. 
    The data is updated every 3 hours and includes temperature, humidity, wind speed, and weather descriptions.
    **Data Source:** [OpenWeatherMap API](https://openweathermap.org/forecast5)
    """
)

local_timezone = pytz.timezone("US/Pacific")
local_time = df['timestamp'][0].astimezone(local_timezone).strftime("%Y-%m-%d %H:%M:%S")
next_3_hours_time = (df['timestamp'][0] + timedelta(hours=3)).astimezone(local_timezone).strftime("%H:%M:%S")

st.write(f"Updated at: {local_time}")

df['temperature_f'] = (df['temperature'] * 9/5) + 32
df['temperature_f'] = df['temperature_f'].round(0)

st.subheader(f"Current Weather: {df['description'][0].title()}")

daily_temp_range = df.groupby("date")["temperature_f"].agg(['min', 'max']).iloc[0]

st.metric(label="Temperature", value=f"{df['temperature_f'][0]}°F")
st.metric(label="Lowest/Highest Temp", value=f"{daily_temp_range['min']}°F/{daily_temp_range['max']}°F")
st.metric(label="Humidity", value=f"{df['humidity'][0]}%")
st.metric(label="Wind Speed", value=f"{df['wind_speed'][0]} m/s")

st.markdown(f"**Next 3 Hours ({next_3_hours_time}):** {df['temperature_f'][1]}°F, {df['description'][1].title()}")

st.write(f"Temperature Over 5 Days: {df['temperature_f'].mean():.0f}°F (average)")

st.subheader("Daily Temperature Range")
daily_avg_temp = df.groupby("date")["temperature_f"].agg(['mean', 'min', 'max'])
plt.figure(figsize=(10, 5))
plt.bar(daily_avg_temp.index, daily_avg_temp["mean"], label="Average", color='#a6d8f7')
plt.plot(daily_avg_temp.index, daily_avg_temp["min"], label="Lowest", marker='o', color='#272727')
plt.plot(daily_avg_temp.index, daily_avg_temp["max"], label="Highest", marker='o', color='#E07A5F')
plt.xticks(rotation=45)
plt.legend()
plt.ylabel("Temperature (°F)")
st.pyplot(plt)

st.subheader("Daily Wind Speed Range")
daily_avg_wind = df.groupby("date")["wind_speed"].agg(['mean', 'min', 'max'])
plt.figure(figsize=(10, 5))
plt.bar(daily_avg_wind.index, daily_avg_wind["mean"], label="Average", color='#a6d8f7')
plt.plot(daily_avg_wind.index, daily_avg_wind["min"], label="Lowest", marker='o', color='#272727')
plt.plot(daily_avg_wind.index, daily_avg_wind["max"], label="Highest", marker='o', color='#E07A5F')
plt.xticks(rotation=45)
plt.legend()
plt.ylabel("Wind Speed (mph)")
st.pyplot(plt)

st.subheader("Temperature vs. Humidity Correlation")
plt.figure(figsize=(8, 6))
sns.scatterplot(x="temperature_f", y="humidity", data=df, color = '#a6d8f7') 
plt.xlabel("Temperature (°F)")
plt.ylabel("Humidity (%)")
st.pyplot(plt)

st.subheader("Correlation Analysis")
correlation = df["temperature_f"].corr(df["humidity"])
st.write(f"Correlation: {correlation:.2f}. A strong negative correlation indicates that as temperature increases, humidity tends to decrease.")

st.subheader("Temperature Trend Over 5 Days (Average)")
plt.figure(figsize=(10, 5))
sns.lineplot(x="timestamp", y="temperature_f", data=df, color = '#a6d8f7') 
plt.ylabel("Temperature (°F)")
plt.xlabel(None)
st.pyplot(plt)

st.subheader("Statistical Summary")
summary_stats = df[["temperature_f", "humidity", "wind_speed"]].describe().round(2)
summary_stats = summary_stats.rename(columns={
    "temperature_f": "Temperature (F°)",
    "humidity": "Humidity (%)",
    "wind_speed": "Wind Speed (mph)"
})
summary_stats = summary_stats.drop(["count", "25%", "50%", "75%"])
summary_stats = summary_stats.rename(index={
    "mean": "Average",
    "std": "Standard Deviation",
    "min": "Lowest",
    "max": "Highest"
})
st.write(summary_stats)
