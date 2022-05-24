def medicineOfPatients(N, med):
    countOfOperations = ""
    type1Ops = []
    type2Ops = []

    for i in med:
        type1Ops.append(i - 1)


def main():
    N = 3
    med = [2, 1, 2]
    medicineOfPatients(N, med)

if __name__ == '__main__':
    main()