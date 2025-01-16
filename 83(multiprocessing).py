from multiprocessing import Pool

def square(n):
    return n * n

# Example Usage
if __name__ == "__main__":
    with Pool(4) as pool:
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)
        print(results)