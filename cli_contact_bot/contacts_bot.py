import handlers


def main():
    """Handle contacts through CLI"""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = handlers.parse_input(user_input)
        match command:
            case command if command in ["close", "exit"]:
                print("Good bye!")
                break
            case "hello":
                print("How can I help you?")
            case "add":
                handlers.add_contact(args, contacts)
            case "change":
                handlers.change_contact(args, contacts)
            case "phone":
                handlers.show_phone(args, contacts)
            case "all":
                handlers.show_all(contacts)
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
