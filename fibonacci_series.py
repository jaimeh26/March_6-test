# This is the code for the fibonacci_series cloud function.
def fibonacci_sum(request):
    fibonacci_sequence = [1, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number >= 100:
            break
        fibonacci_sequence.append(next_number)
    return {"sum": sum(fibonacci_sequence)}


