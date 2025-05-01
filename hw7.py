shopping_bag = {}

print('[구입]')
while True:
    item = input('상품명? ')
    num = input('수량은? ')
    if item == '':
        break
    if num == '':
        break
    shopping_bag[item] = num
    print(f'장바구니에 {item} {shopping_bag[item]}개가 담겼습니다.')

print('>>>장바구니 보기: ')
for item, num in shopping_bag.items():
    print(f'{item} {num}개')

print("[검색]")
sh = input('장바구니에서 확인하고자 하는 상품은? ')
if sh in shopping_bag:
    print(f'{sh}는 장바구니에 {shopping_bag[sh]}개가 담겨 있습니다.')
else:
    print(f'{sh}는 장바구니에 없습니다.')