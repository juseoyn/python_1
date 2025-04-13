n = int(input('세 자리 정수 입력: '))
def read_single_digit(n):
    if n == 0:
        return '영'
    elif n == 1:
        return '일'
    elif n == 2:
        return '이'
    elif n == 3:
        return '삼'
    elif n == 4:
        return '사'
    elif n == 5:
        return '오'
    elif n == 6:
        return '육'
    elif n == 7:
        return '칠'
    elif n == 8:
        return '팔'
    else:
        return '구'

def read_number(n):
    if 99 < n < 1000:
        hundreds = read_single_digit(n // 100)  
        tens = read_single_digit((n % 100) // 10) 
        units = read_single_digit(n % 10)  
        return f"{hundreds} {tens} {units}" 
    else:
        return '잘못된 입력입니다.'
    
print(read_number(n))
   
    