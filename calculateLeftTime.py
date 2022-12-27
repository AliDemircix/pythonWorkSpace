age=input('Write your currently age \n')

def calculateLeftTime(age):
    leftYears= 90-int(age)
    leftmonths= leftYears*12
    leftWeeks=leftYears*52
    leftDays= leftYears*365
    resultText= f" You have {leftYears} years, {leftmonths} months ,{leftWeeks} weeks, {leftDays} days to die...!!!"
    return resultText

print(calculateLeftTime(age))