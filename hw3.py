def get_fixed_price(b,c):
    return int(c / (1 - b / 100))

a = int(input("할인율은?"))
b = int(input(" A 상품의 할인된 가격은? "))
c = int(input(" B 상품의 할인된 가격은? "))

bb = get_fixed_price(a,b)
cc = get_fixed_price(a,c)

print("A 상품의 정가는", bb)
print("B 상품의 정가는", cc)