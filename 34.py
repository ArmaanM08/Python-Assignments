# Display all primes in a range
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
primes = [num for num in range(start, end + 1) if is_prime(num)]
print(f"Prime numbers between {start} and {end}: {primes}")