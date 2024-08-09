def find_multiples_of_three_and_four(start, end):
    if start >= end:
        return []
    
    multiple_3 = [i for i in range(start, end + 1) if i % 3 == 0]
    multiple_4 = [i for i in range(start, end + 1) if i % 4 == 0]
    multiple_12 = [i for i in range(start, end + 1) if i % 12 == 0]
    result = sorted(set(multiple_3 + multiple_4 + multiple_12))
    return result

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

print("Output:",find_multiples_of_three_and_four(start, end))