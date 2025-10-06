import datetime

current_timestamp = datetime.datetime.now()

# Print the timestamp in a readable format
print("Current Timestamp:", current_timestamp)
formatted_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
print("Formatted Timestamp:", formatted_timestamp)
