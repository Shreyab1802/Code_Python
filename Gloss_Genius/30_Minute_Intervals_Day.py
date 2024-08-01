from datetime import datetime, timedelta

# Initialize start time at midnight
start_time = datetime.strptime("00:00", "%H:%M")
end_time = datetime.strptime("23:30", "%H:%M")
interval = timedelta(minutes=30)

# Generate 30-minute intervals
time_intervals = {}
current_time = start_time

while current_time <= end_time:
    end_interval = current_time + interval
    time_intervals[current_time.strftime("%H:%M")] = end_interval.strftime("%H:%M")
    current_time = end_interval

# Print the dictionary of time intervals
for start, end in time_intervals.items():
    print(f"{start} - {end}")