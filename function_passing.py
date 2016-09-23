def num_digits(x):
    return len(str(x))

def most_digits(L):
    L = sorted(L, key=num_digits)
    return L[-1]

def largest_two_digit_even(L):
    two_digit_numbers = [i for i in L if num_digits(i)==2]
    evens = [i for i in two_digit_numbers if i%2==0]
    evens.sort()
    return evens[-1]

def num_ones_in_binary(num):
    return bin(num)[2:].count("1")

def most_ones_in_binary(nums):
    ones=0
    max=0
    res=0
    for num in nums:
        ones=num_ones_in_binary(num)
        if max < ones:
            max=ones
            res=num
    return res

def best(L, criteria):
    return criteria(L)



L = [1, 76, 84, 95, 214, 1023, 511, 32]
print(best(L, min)) # Prints 1
print(best(L, largest_two_digit_even)) # Prints 84
print(best(L, most_digits)) # Prints 1023
print(best(L,most_ones_in_binary))