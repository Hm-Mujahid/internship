# Open a file in write mode (creates if not exists)
with open("example.txt", "w") as f:
    f.write("Hello, this is the first line.\n")
    f.write("Python makes file handling easy.\n")

# Append more text
with open("example.txt", "a") as f:
    f.write("This line is appended at the end.\n")

# Read the whole file
with open("example.txt", "r") as f:
    content = f.read()
    print("Reading whole file:\n", content)

# Read line by line
with open("example.txt", "r") as f:
    for line in f:
        print("Line:", line.strip())
