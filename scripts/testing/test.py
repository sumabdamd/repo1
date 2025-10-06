# import datetime

# current_timestamp = datetime.datetime.now()

# # Print the timestamp in a readable format
# print("Current Timestamp:", current_timestamp)
# formatted_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
# print("Formatted Timestamp:", formatted_timestamp)

import datetime
import json
import os

# Step 1: Get the current timestamp
current_timestamp = datetime.datetime.now()

# Format the timestamp (e.g., Year-Month-Day Hour:Minute:Second)
formatted_timestamp = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')

# Step 2: Store the timestamp in a JSON file
timestamp_data = {
    "timestamp": formatted_timestamp
}

# File path for storing the timestamp
file_path = "timestamp.json"

# Write the timestamp to the JSON file
with open(file_path, 'w') as json_file:
    json.dump(timestamp_data, json_file, indent=4)

print(f"Timestamp stored in {file_path}: {formatted_timestamp}")

