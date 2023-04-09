def has_invalid_characters(string):
    valid = "abcdefghijklmnopqrstuvwxyz0123456789."

    for ch in string:
        if ch not in valid:
            return True
    return False
