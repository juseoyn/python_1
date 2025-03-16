#반지름
def get_radius(prompt):
    r = int(input(prompt))
    return r
#넓이공식
def circle_area(radius):
    return 3.14 * radius * radius
radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
# 원의 넓이 계산
area = circle_area(radius)

print(f"반지름 {radius}인 원의 넓이 = 3.14 x {radius} x {radius} = {3.14 * radius * radius}")
