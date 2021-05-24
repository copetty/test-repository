number = 7


# while True:
#     user_input = input("Enter 'y' if you would like to play? (Y/n)").lower()

#     if user_input == "n":
#         break


#     user_number = int(input("Guess our number: "))
#     if user_number == number:
#         print("You guessed correctly!")
#     elif abs(number - user_number) == 1:
#         print("you were off by one.")
#     else:
#         print("Sorry, its wrong!")









# friends = ["Rolf", "Jen", "Bob", "Anne"]

# for friend in friends: # can also use " for friend in range(4) "
#     print(f"{friend} is my friend.")


grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)
