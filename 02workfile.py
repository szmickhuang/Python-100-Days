import math

f = float(input('Please input a Fahrenheit degree: '))
c = (f-32)/1.8
print('%.1f Fahrenheit degree = %.1f degree Centigrade' % (f,c))


radius = float(input('Please input a radius value: '))
perimeter = 3.14 * 2 * radius
circle_area = 3.14 * math.pow(radius,2)
print('This circle\'s perimeter is %.2f, area is %.2f .' % (perimeter, circle_area))