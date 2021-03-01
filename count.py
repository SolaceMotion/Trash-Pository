import math

def count(end, stop, iteration):
    isCounting = True
    i = 0
    if end > stop and iteration > 0 and stop > iteration:
        while i < end and isCounting == True:
            print(i)
            i = i + iteration
            if i == stop:
                isCounting = False
                print("The square root of", str(end - stop), "is" , str(round(math.sqrt(end - stop), 2)))
    else:
        print("stop can't be less than iterator")

        if iteration <= 0 and end <= stop:
            print("iterator variable can't be less than or equal to 0")
            print("end can't be less than or equal to stop")
        elif iteration <= 0:
            print("iterator variable can't be less than or equal to 0")
        elif end <= stop:
            print("end can't be less than or equal to stop")

try:
    count(arg1, arg2, arg3)
except ValueError:
    print(ValueError)
    
