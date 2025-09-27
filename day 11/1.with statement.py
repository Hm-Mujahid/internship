# Without with
try:
    f = open("sample.txt", "r")
    data = f.read()
    1 / 0   # Force an error
finally:
    f.close()   # We must close manually

# With with
with open("sample.txt", "r") as f:
    data = f.read()
    1 / 0   # Force an error (file will still be closed automatically!)
