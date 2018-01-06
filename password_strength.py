import sys


def load_blacklist(filepath):
    with open(filepath) as blacklist:
        return blacklist.read()


def password_in_blacklist(password, blacklist):
    for word in blacklist.split():
        if password == word:
            raise SystemExit
    return 2


def password_length(password):
    recommended_lenght = 8
    if len(password) < recommended_lenght:
        return 0
    else:
        return 2


def password_contains_numbers(password):
    if password.isdigit():
        return 0
    elif any(char.isdigit() for char in password):
        return 2
    else:
        return 1


def password_contains_register(password):
    if not password.isdigit():
        if (password.isupper() or password.islower()):
            return 0
        else:
            return 2
    else:
        return 0


def password_contains_special(password):
    if not password.isalnum():
        return 2
    else:
        return 0


def get_password_strength(password, blacklist):
    password_strength = (
            password_length(password) +
            password_contains_numbers(password) +
            password_contains_register(password) +
            password_contains_special(password) +
            password_in_blacklist(password, blacklist)
    )
    return password_strength


if __name__ == '__main__':
    try:
        blacklist = load_blacklist(sys.argv[1])
        password = input('Please enter your password: ')
        password_strength = get_password_strength(password, blacklist)
        print("Your password's strength is {}".format(password_strength))

    except (IndexError, FileNotFoundError):
        print('Input file is not specified or missed')
    except UnicodeDecodeError:
        print('Incorrect file')
    except SystemExit:
        print('Your password in blacklist! Strength = 1 Please try again')
