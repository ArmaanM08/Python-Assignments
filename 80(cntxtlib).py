from contextlib import contextmanager

@contextmanager
def log_block():
    print("Code block started.")
    yield
    print("Code block ended.")

# Example Usage
with log_block():
    print("Inside the block.")