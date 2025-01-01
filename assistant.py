def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact does not exist."
        except ValueError as e:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


def parse_input(user_input):
    if not user_input.strip():
        return None, []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    name, phone = args

    if name in contacts:
        return "Contact already exists."

    contacts[name] = phone

    return "Contact added."


@input_error
def change_contact(args, contacts):
    name, new_phone_number = args

    if name not in contacts:
        return "Contact does not exist."

    contacts[name] = new_phone_number
    return "Contact updated."


@input_error
def delete_contact(args, contacts):
    name = args[0]

    if name not in contacts:
        return "Contact does not exist."

    del contacts[name]
    return "Contact deleted."


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


@input_error
def show_phone(args, contacts):
    name = args[0]

    if name not in contacts:
        return "Contact does not exist."

    return f"{name}: {contacts[name]}"


def main():
    contacts = {}

    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        match command:
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, contacts))
            case "change":
                print(change_contact(args, contacts))
            case "delete":
                print(delete_contact(args, contacts))
            case "phone":
                print(show_phone(args, contacts))
            case "all":
                print(show_all(contacts))
            case "exit" | "close":
                print("Good bye!")
                break
            case _:
                print("Invalid command")


if __name__ == "__main__":
    main()
