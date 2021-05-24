user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"



def make_function(func):
    def secure_function():

        if user["access_level"] == "admin":
            return func()

    return secure_function()
# print(get_admin_password())

get_admin_password = secure_function(get_admin_password)

print(get_admin_password)
