def ceaser_cipher(text, n):
    result = ""
    for st in text:
        result += chr(ord(st)+n)
    return result

if __name__ == "__main__":
    text = input("문자입력")
    num = int(input("문자의 거리입력:"))
    print(ceaser_cipher(text, num))
