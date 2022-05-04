from multiprocessing import Value


def arrange_string(s):

    def get_sorted_s(s):
        frequency = {}
        for i in s:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1

        sorted_freq = dict(sorted(frequency.items()))
        return sorted_freq

    sorted_output = get_sorted_s(s)
    
    s_list = ''.join([str(i) for i in sorted_output])

    print(s_list)
        

    


def main():
    s = 'llljkgghi'
    arrange_string(s)


if __name__ == '__main__':
    main()