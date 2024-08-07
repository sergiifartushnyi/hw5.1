import keyword
import string


def is_valid_variable_name(var_name):
    if var_name == "_":
        return True
    if all(char == "_" for char in var_name):
        return False
    if var_name in keyword.kwlist:
        return False

    if var_name[0].isdigit():
        return False

    allowed_characters = set(string.ascii_lowercase + string.digits + '_')
    if not set(var_name).issubset(allowed_characters):
        return False


    return True


if __name__ == "__main__":
    test_var_name = input("Введіть рядок для перевірки: ")
    print(is_valid_variable_name(test_var_name))
