def is_valid_identifier(identifier):
    """
    :param identifier: a string representing a course identifier. e.g. C103
    :return: whether the string follows the right format of alpha character + 3 digits
    """

    #length = len(identifier)
    #
    # the code needs to check for empty string otherwise exception is thrown (show that during demo)
    # if length < 4:
    #     return False
    letter = identifier[0]
    number = identifier[1:]
    return letter.isalpha() and number.isnumeric() and len(number) == 3

