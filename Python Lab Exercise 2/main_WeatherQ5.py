from module_WeatherQ5 import find_highest_lowest_temps, days_above_30, average_humidity

weather_data = [
    {"date": "2024-08-01", "max_temp": 33, "min_temp": 18, "humidity": 70},
    {"date": "2024-08-02", "max_temp": 45, "min_temp": 22, "humidity": 60},
    # ... more data points
]
# Assuming weather_data is populated with actual data

highest, lowest = find_highest_lowest_temps(weather_data)
print("Highest temperature:", highest)
print("Lowest temperature:", lowest)

hot_days = days_above_30(weather_data)
print("Number of days above 30°C:", hot_days)

avg_humidity = average_humidity(weather_data)
print("Average humidity:", avg_humidity)
