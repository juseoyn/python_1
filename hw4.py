def welcome_message():
    name = input("Input his/her name: ")
    
    msg1 = f"Hello {name},"
    msg2 = "Welcome to Seoul."

    box_length = max(len(msg1), len(msg2))

    print("-" * box_length)
    print(msg1)
    print(msg2)
    print("-" * box_length)

welcome_message()