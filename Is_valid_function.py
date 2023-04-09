from has_valid_character import has_invalid_characters


def is_valid(Email):
    if Email.count("@") != 1:
        return False

    prefix, domain = Email.split("@")

    if len(prefix) == 0:
        return False

    if domain.count(".") != 1:
        return False

    domain_name, extension = domain.split(".")

    if len(domain_name) == 0 or len(extension) == 0:
        return False
    if has_invalid_characters(prefix):
        return False

    if has_invalid_characters(domain):
        return False

    return True