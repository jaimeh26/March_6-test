# This is the code for the fibonacci_series cloud function.
def fibonacci_sum(request):
    fibonacci_numbers = [0, 1]
    while True:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_number >= 100:
            break
        fibonacci_numbers.append(next_number)
    return {"sum": sum(fibonacci_numbers)}


#This is the URL for the fibonacci_series cloud function
# https://northamerica-northeast1-certain-beach-391616.cloudfunctions.net/fibonacci_series


