#What is the largest prime factor of the number 600,851,475,143 ?
def largest_prime_factor():
    target_num = 600851475143
    prime_list = [2]
    prime_factors = []
    working_ = target_num
    
    ##################################################
    # Create a list of prime factors possibilities
    ##################################################
    working_ = int(target_num/2)
    print ('Determining Primes')   
    x = 3
    while x <= working_:
        IS_PRIME = True
        for y in prime_list:
            if x % y == 0:
                IS_PRIME = False
                x += 2
                break
        if (IS_PRIME):
            prime_list.append(x)    
            x += 2

    ##################################################
    # Find the prime factors for the target number
    ##################################################

    working_ = target_num
    print ('Finding factors')
    for p in prime_list:
        is_factor = False
        while (working_ > 1 and ((working_ / p) % int(working_ / p) == 0)):
            working_ = int(working_ / p)
            is_factor = True
        
        if (is_factor):
            prime_factors.append(p)

    return max(prime_factors)
