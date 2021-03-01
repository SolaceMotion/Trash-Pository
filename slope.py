import sys

def slope_intercept_points(y2, y1, x2, x1):
    print("On the form y=mx+b, where m represents the slope, and b represents the y-intercept, the linear equation is:")
    m = round((y2 - y1)/(x2 - x1), 3)
    b = round(y1 - (m*x1), 3)
    tuple_equation = "y=",str(m),"x+",str(b)
    joined_equation = "".join(tuple_equation)
    return joined_equation

try:
    print(slope_intercept_points(-4, 2, 1, 3))
except:
    print(sys.exc_info()[1])
