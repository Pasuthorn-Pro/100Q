def find_divisors(input_number):
    if input_number <= 0:
        return ""
    else:
        divisors = [i for i in range(1, input_number + 1) if input_number % i == 0]
        return divisors

input_number = int(input("Enter number: "))
print(find_divisors(input_number))