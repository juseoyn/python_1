def get_integer():
    amount = int(input("얼마 교환할거야?"))
    
    if amount < 0:
        print("양수로 입력해야 합니다.")
        return get_integer()     
    return amount

def exchange(amount):
    coins = [500, 100, 50, 10] 
    counts = {}  
    for coin in coins:
        counts[coin] = amount // coin  
        amount %= coin  
    for coin, count in counts.items():
        print(f"{coin}원 동전의 개수: {count}")  

total_amount = get_integer()
exchange(total_amount)