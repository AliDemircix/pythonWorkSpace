class User:
    def __init__(self,name):
        self.name=name
        self.is_logged_in=False
def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if args[0].is_logged_in==True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"Hello {user.name}")
my_user=User("Ali")
my_user.is_logged_in=True

create_blog_post(my_user)