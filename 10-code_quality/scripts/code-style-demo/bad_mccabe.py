def process(data):
    output = ""
    for i in range(1, 10):
        for j in range(1, 10):
            if i != j:
                for a in range(1, 10):
                    for b in range(1, 10):
                        if a == i and j == b:
                            output += data[i]

    return output

if __name__ == "__main__":
    print(process("abcdefghijklmno"))