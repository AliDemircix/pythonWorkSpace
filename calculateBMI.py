height = input("Add your height as m")
weight = input("Add your weight as kg")

def calculate(height,weight):
        BMI=int(weight)/float(height)**2
        convertedBMI=round(BMI,2) # 2 makes decimal number
        if convertedBMI<18.5:
            return f"{convertedBMI} You are underweight"
        elif convertedBMI<25:
            return f"{convertedBMI} You have a normal weight"
        elif convertedBMI<30:
            return f"{convertedBMI} You are overweight"
        elif convertedBMI<35:
            return f"{convertedBMI} You are obese"
        else:
            return f"{convertedBMI} You are clinically obese"
        
        #return '{0:.2f}'.format(BMI)  we can use this also for decimals

print(calculate(height,weight))
