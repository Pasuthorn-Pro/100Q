def find_non_multiples(start, end):
    if start >= end:
        return []

    result = [i for i in range(start, end + 1) if i % 3 != 0 and i % 4 != 0 and i % 5 != 0]
    return result

start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

print("Output:",find_non_multiples(start, end))