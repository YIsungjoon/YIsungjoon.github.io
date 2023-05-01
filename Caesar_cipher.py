def ceaser_cipher(text, n):
    result = ""
    for st in text:
        if ord(st)+n > 122:
            n =  (ord(st)+n)%97
            result += chr(97+n)
        else:
            result += chr(ord(st)+n)
    return result

if __name__ == "__main__":
    text = input("문자입력")
    num = int(input("문자의 거리입력:"))
    print(ceaser_cipher(text, num))
