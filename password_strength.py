import sys


def load_blacklist(filepath):
    with open(filepath) as blacklist:
        return blacklist.read()


def password_in_blacklist(password, blacklist):
    word_in_list = False
    for word in blacklist.split():
        if password == word:
            word_in_list = True
    return word_in_list


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


def get_password_strength(password):
    password_not_in_blacklist = 2
    password_strength = (
            password_length(password) +
            password_contains_numbers(password) +
            password_contains_register(password) +
            password_contains_special(password) +
            password_not_in_blacklist
    )
    return password_strength


if __name__ == '__main__':
    try:
        blacklist_file = sys.argv[1]

        blacklist = load_blacklist(blacklist_file)
        password = input('Please enter your password: ')
        if password_in_blacklist(password, blacklist):
            raise SystemExit
        else:
            password_strenght = get_password_strength(password)
            print("Your password's strenght is {}".format(password_strenght))

    except (IndexError, FileNotFoundError):
        print('Input file is not specified or missed')
    except UnicodeDecodeError:
        print('Incorrect file')
    except SystemExit:
        print('Your password in blacklist! Strenght = 1 Please try again')
