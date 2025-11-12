for i in range(5):
    print(f"The current number is: {i}")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like to eat a {fruit}")

count = 0

while count < 3:
    print(f"Count is currently: {count}")
    count += 1 

print("The loop has finished because count is no longer less than 3.")

user_input = "" 

while user_input != "stop":
    user_input = input("Type a word (type 'stop' to exit): ")
    if user_input != "stop":
        print(f"You typed: {user_input}")

print("Exiting the program.")

