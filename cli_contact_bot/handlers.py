from decorators import input_error


def parse_input(user_input: str) -> tuple[str]:
    """Get command from user input and parse it"""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list[str], contacts: dict[str, str]):
    """Add contact to the list"""
    valid_args = validate_args(args)
    if not valid_args:
        raise ValueError()
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        print("Contact added.")
    else:
        raise KeyError(f"Contact with name {name} already exists!")


@input_error
def change_contact(args: list[str], contacts: dict[str, str]):
    """Update phone number of the exist contact"""
    valid_args = validate_args(args)
    if not valid_args:
        raise ValueError()
    name, phone = args
    if name not in contacts:
        raise KeyError(f"Contact with name {name} does not exist!")
    contacts[name] = phone
    print("Contact updated.")


@input_error
def show_phone(args: list[str], contacts: dict[str, str]):
    """Show contact's phone based on contact's name"""
    name = args[0]
    if not (name.isalnum() or len(name) >= 3):
        raise ValueError()
    if name not in contacts:
        print(f"Contact with name {name} does not exists.")
    else:
        print(f"{name}\'s phone number is: {contacts[name]}")


@input_error
def show_all(contacts: dict[str, str]):
    """Show all contacts"""
    if contacts:
        print(f"Here are all your contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        raise KeyError("You don't have any contact yet.")


def validate_args(args: list[str]) -> bool:
    """Basic validation of input data for 'add' and 'change' commands"""
    is_name = args[0].isalnum() and len(args[0]) >= 3
    is_phone = args[1].isdigit() and len(args[1]) >= 10
    if is_name and is_phone:
        return True
    return False
