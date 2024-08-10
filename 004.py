num_inputs = 5

def calculate_sum_and_average():
    Sum = 0

    for i in range(num_inputs):
        user_input = input(f"Enter numbers {i + 1}: ")
        number = float(user_input)
        Sum += number

    Average = Sum / num_inputs

    print(f"Sum: {Sum}")
    print(f"Average: {Average}")

calculate_sum_and_average()