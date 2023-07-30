#10038 jolly jumper


def is_jolly(seq):
    n = len(seq)
    diffs = [abs(seq[i] - seq[i+1]) for i in range(n-1)]
    return set(diffs) == set(range(1, n))

def main():
    try:
        while True:
            input_line = input().strip()
            if not input_line:
                break

            elements = list(map(int, input_line.split()))
            n, sequence = elements[0], elements[1:]

            result = is_jolly(sequence)
            if result:
                print("Jolly")
            else:
                print("Not jolly")
    except :
        print("some error occured")

if __name__ == "__main__":
    main()
