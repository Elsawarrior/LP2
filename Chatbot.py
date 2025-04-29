print("Hello, I m your chatbot assistant!")
print("Welcome to Library!")
print("Type 'help' to see options and 'exit' to leave ")

books = {
    "maths": "available",
    "science" : "out of stock",
    "english" : "available"
}
while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Thank you!")
        break
    elif user_input == "help":
        print("Chatbot: I can help you with:\n")
        print("1. Store timings. \n")
        print("2. Book Availability.\n")
        print("3. Payment methods\n")
        print("Enter exit to leave chatbot\n")

    elif user_input == 'time':
        print("We are available from 9 am to 9 pm from Monday to Saturday\n Thank you!!")

    elif user_input == 'book':
        print(books)

    elif user_input == "payment":
        print("We accept cash, card and upi.\n Thank you!")

    else:
        print("Incorrect input!")
