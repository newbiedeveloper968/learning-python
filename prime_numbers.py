"""integers > 1 with exactly two factors, 1 and the number itself. Some of the prime numbers include 2, 3, 5, 7, 11, 13"""


def main():

    while True:
        try:
            user_input = int(input("Print Prime Numbers upto: "))
            prime(user_input)
            break
        except:
            print("Not an integer!")
    print(prime_numbers)


""" Checks if a single digit is a prime number or not """


def check_prime(number) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


prime_numbers = []

""" Appends each prime numbers to the list -> prime_numbers """


def prime(lim):
    for each_number in range(2, lim + 1):
        if check_prime(each_number):
            prime_numbers.append(each_number)


if __name__ == "__main__":
    main()
