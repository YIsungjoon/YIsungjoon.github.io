def ceaser_cipher(text, n):
    result = ""
    for st in text:
        result += chr(ord(st)+n)
    return result

if __name__ == "__main__":
    print(ceaser_cipher("hello", 3))
