bot_name='Bob'
print ("Hello!' I am , bot_name! How can I assist you today?")

while True:
    user_input=input("you:").lower()

    if user_input in ["Hi","Hello"]:
        print("Bob: Hi there! How can I help you?")
    elif user_input in ["Bye","See you"]:
        print("Bob: Goodbye! have a great day!")
    elif user-input in ["+","add"]:
        print("Bob: Sure! Let's do some addition! please enter two numbers.")
        try:
            num1=float(input("First number:"))
            num2=float(input("Second number:"))
            print("Bob: The sum is num1+num2")
        except ValueError:
            print("Bob: Oops! That doesn't seem like a valid number.Try again!")
    else:
        print("Bob: I am sorry, I don't understant that.Please try again.")

