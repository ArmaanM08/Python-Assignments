# Invert a dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {v: k for k, v in original_dict.items()}
print(f"Inverted Dictionary: {inverted_dict}")