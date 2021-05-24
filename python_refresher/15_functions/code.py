def hello():
    print("Hello!")


def user_age_in_seconds():
    user_age = int(input('Enter you age: '))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age {user_age} in seconds is {age_seconds}.")
    
print("Welcome to user age in seconds program!!")

user_age_in_seconds()


friends = ["Rolf" , "Bob"]

def add_friends():
    friend_name = input("Enter your frined name: ")
    friends = friends + [friend_name] #can't do this because friends is declared already, similar to x = x + 5 when x is first being declared




# can't call functions before they are created