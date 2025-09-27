import os

file_name = "example.txt"

# Check if file exists
if os.path.exists(file_name):
    print(f"{file_name} exists, now deleting it...")
    os.remove(file_name)
else:
    print("File not found.")
