def greet(name):
    print(f"Hello, {name}! Welcome to the Func.py file!")
    print("This is a simple function that prints a personalized greeting message.")
    print("Welcome to the world of Python functions!")

if __name__ == "__main__":
    greet("User")
    print('Once Again Please!')
    greet("User")
    print('End of Func.py example. Import and use greet(name) from another script.')
# This code defines a simple function that greets the user and can be imported into other scripts.
# The function greet(name) takes a name as an argument and prints a personalized greeting message.
# The if __name__ == "__main__": block allows the function to be run directly when the script is executed, but also allows it to be imported without running the greeting code immediately.
