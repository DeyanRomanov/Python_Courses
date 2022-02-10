def get_primes(nums):
    for n in nums:
        if n > 1:
            r = 0
            for i in range(2, n + 1):
                if n % i == 0:
                    r += 1
            if r > 1:
                continue
            yield n
        else:
            continue


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print(list(get_primes([-2, 0, 0, 1, 1, 0])))