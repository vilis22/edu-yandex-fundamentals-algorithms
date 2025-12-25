def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    all_or_results = set()
    prev_ending = set()
    
    for num in numbers:
        curr_ending = {val | num for val in prev_ending}
        curr_ending.add(num)
        all_or_results.update(curr_ending)
        prev_ending = curr_ending
    
    print(len(all_or_results))


if __name__ == "__main__":
    main()
