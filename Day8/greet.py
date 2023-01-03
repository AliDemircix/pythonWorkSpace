def greet(name):
    print(f"Hello {name}")

greet("Ali")

def multiParamFunc(name,age,job):
    print(f"Hello {name} you are now {age} years old. Good luck to you your job {job}")
# You can define any order if you use keyword arguments

multiParamFunc("Ali",35,"Python Developer")
multiParamFunc(age=34,job="Full Stack",name="Ali")