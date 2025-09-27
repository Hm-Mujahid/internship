with open("sample.txt", "w+") as f:
    f.write("Hello Python")
    f.seek(0)   # Move cursor to start of file
    print(f.read())   # ✅ Works now
