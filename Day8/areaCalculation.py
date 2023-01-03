import math
test_h=int(input("Height of wall \n"))
test_w=int(input("Width of wall \n"))
coverage=5

def calculateArea(h,w,cover):
    number_of_cans=math.ceil((h*w)/cover)
    print(f"You will need {number_of_cans} cans to paint")

calculateArea(test_h,test_w,coverage)
    