import re

def message(S):
    points = 0
    lower_case = re.findall("[a-z]", S)
    upper_case = re.findall("[A-Z]", S)

    for i in lower_case: points += 1

    for i in upper_case: points += 2

    return points


def main():
    S = 'Abfd@3#c'
    print(message(S))

if __name__ == '__main__':
    main()