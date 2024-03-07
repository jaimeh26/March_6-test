# Code for the prime_numbers cloud function.
def prime_numbers(request):
    primes = []
    for num in range(1, 101):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return {"primes": primes}

# This is the trigger URL for the prime_numbers cloud function
# https://northamerica-northeast1-certain-beach-391616.cloudfunctions.net/prime_numbers
