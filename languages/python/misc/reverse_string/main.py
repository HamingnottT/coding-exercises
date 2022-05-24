# Recursive way to reverse a string

def reverse_string(n, string, accumulator):
    if n == 0: return accumulator
    else:
        return reverse_string(n - 1, string, string[-n] + accumulator)


def main():
    string = "Hello"
    print(f"Original string: {string}")
    print(f"Reversed string: {reverse_string(len(string), string, '')}")


if __name__ == '__main__':
    main()