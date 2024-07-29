def find_highest_lowest_temps(data):
  """Finds the highest and lowest temperatures in the given data."""
  max_temp = max(data, key=lambda x: x['max_temp'])['max_temp']
  min_temp = min(data, key=lambda x: x['min_temp'])['min_temp']
  return max_temp, min_temp

def days_above_30(data):
  """Counts the number of days with temperatures above 30°C."""
  count = 0
  for day in data:
    if day['max_temp'] > 30:
      count += 1
  return count

def average_humidity(data):
  """Calculates the average humidity over the given period."""
  total_humidity = sum(day['humidity'] for day in data)
  return total_humidity / len(data)
