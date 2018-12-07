def make_heading(title):
    """
    Takes a title and returns a formatted version in uppercase with a border.
    E.g. make_heading("Cambridge Spark") should return:
     CAMBRIDGE SPARK
    =================
    :param title: the title to format in upper case and with a border
    :return: a formatted string
    :raise: a ValueError if the title is longer than 60 characters
    """
    upper_title = title.upper()
    border_length = len(title) + 2
    border = "=" * border_length
    return " " + upper_title + " \n" + border

if __name__ == "__main__":
    print(make_heading("Cambridge Spark"))
