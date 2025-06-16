def main():
    userInput = input("File name: ")
    extensions(userInput)

def extensions(file):
    file = file.strip().lower()
    if file.endswith("gif"):
        return print("image/gif")
    elif file.endswith("jpg"):
        return print("image/jpeg")
    elif file.endswith("jpeg"):
        return print("image/jpeg")
    elif file.endswith("png"):
        return print("image/png")
    elif file.endswith("pdf"):
        return print("application/pdf")
    elif file.endswith("txt"):
        return print("text/plain")
    elif file.endswith("zip"):
        return print("application/zip")
    else:
        return print("application/octet-stream")

main()
