path = input("File path: ")

if path[0].isupper() and path[1] == ":" and path[2] == "\\" and path.find("."):
    depth = path.count("\\")
    filename = path.split("\\")[-1]
    filename_n = filename.split(".")[-1]
    print(f"Facts about your Windows path:\n"
          f"File depth: {depth}\n"
          f"Filename: {filename}\n"
          f"Extension: {filename_n}")
elif path[0] == '/' and path.find(".") and path[1].isupper():
    depth = path.count("/")
    filename = path.split("/")[-1]
    filename_n = filename.split(".")[-1]
    print(f"Facts about your Linux path:\n"
          f"File depth: {depth}\n"
          f"Filename: {filename}\n"
          f"Extension: {filename_n}")
else:
    print("Invalid path!")
