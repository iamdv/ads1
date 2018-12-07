def process(data):
    output = ""
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                output += _sub_process(data, i, j)
    return output


def _sub_process(data, i, j):
    sub_output = ""
    for a in range(1, 10):
        for b in range(1, 10):
            if a == i and j == b:
                sub_output += data[i]
    return sub_output


if __name__ == "__main__":
    print(process("abcdefghijklmno"))