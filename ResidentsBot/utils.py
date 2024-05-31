def is_valid_integer(s):
    try:
        number = int(s)
        if number <= 3000:
            return True
        else:
            return False
    except ValueError:
        return False
