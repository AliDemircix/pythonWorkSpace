height = input("Add your height as m")
weight = input("Add your weight as kg")

def calculate(height,weight):
        BMI=int(weight)/float(height)**2
        return round(BMI,2) # 2 makes decimal number
        #return '{0:.2f}'.format(BMI)  we can use this also for decimals

print(calculate(height,weight))
