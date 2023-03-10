def get_radius(prompt):
    r = int(input(prompt))
    return r

def get_circle_area(radius):
    s = radius * radius * 3.14
    return s

radius = get_radius("넓이를 구하고자 하는 원의 반지름은? ")
size = get_circle_area(radius)
print("반지름 " + str(radius) + "인 원의 넓이 = " + "3.14 x " + str(radius) + " x " + str(radius) + " = " + str(size))