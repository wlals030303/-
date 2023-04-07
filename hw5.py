def read_single_digit(int):
    if int == 0:
        return '영'
    elif int == 1:
        return '일'
    elif int == 2:
        return '이'
    elif int == 3:
        return '삼'
    elif int == 4:
        return '사'
    elif int == 5:
        return '오'
    elif int == 6:
        return '육'
    elif int == 7:
        return '칠'
    elif int == 8:
        return '팔'
    elif int == 9:
        return '구'

def read_number(n):
    n = str(n)
    res = ""
    res += f"{read_single_digit(int(n[0]))} "

    if len(n) == 2:
        res += f"{read_single_digit(int(n[1]))}"
    
    elif len(n) == 3:
        res += f"{read_single_digit(int(n[1]))} "
        res += f"{read_single_digit(int(n[2]))}"
    
    return res

num = int(input("세 자리 정수 입력: "))
result = read_number(num)
print(result)