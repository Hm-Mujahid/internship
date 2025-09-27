with open("sample.txt", "r") as f:
    content = f.read()
    line_count = content.count("\n") + 1
    word_count = len(content.split())
    char_count = len(content)

    print("Lines:", line_count)
    print("Words:", word_count)
    print("Characters:", char_count)
