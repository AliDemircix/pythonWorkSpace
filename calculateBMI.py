height = input("Add your height as m")
weight = input("Add your weight as kg")

def calculate(height,weight):
        BMI=int(weight)/float(height)**2
        return '{0:.2f}'.format(BMI)

print(calculate(height,weight))
