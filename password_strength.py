import sys
import getpass


def load_blacklist(filepath):
    with open(filepath) as blacklist:
        return blacklist.read()


def password_not_in_blacklist(password, blacklist):
    return bool(password not in blacklist.split())


def get_password_length(password):
    recommended_length = 8
    return bool(len(password) >= recommended_length)


def password_contains_numbers(password):
    return bool(any(char.isdigit() for char in password))


def case_sensitivity_check(password):
    if not password.isdigit():
        return bool(not(password.isupper() or password.islower()))
    else:
        return False


def password_contains_special(password):
    return bool(not password.isalnum())


def get_password_strength(password, blacklist):
    if not password_not_in_blacklist(password, blacklist):
        strength = 1
    else:
        strength = sum([
            get_password_length(password) * 2,
            password_contains_numbers(password) * 2,
            case_sensitivity_check(password) * 2,
            password_contains_special(password) * 2,
            password_not_in_blacklist(password, blacklist) * 2
        ])
    return strength


if __name__ == '__main__':
    try:
        blacklist = load_blacklist(sys.argv[1])
        password = getpass.getpass('Please enter your password: ')
        password_strength = get_password_strength(password, blacklist)
        print("Your password's strength is {}".format(password_strength))

    except (IndexError, FileNotFoundError):
        print('Input file is not specified or missed')
    except UnicodeDecodeError:
        print('Incorrect file')
    except SystemExit:
        print('Your password in blacklist! Strength = 1 Please try again')
