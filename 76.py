def has_path(grid):
    rows, cols = len(grid), len(grid[0])
    stack = [(0, 0)]
    visited = set()

    while stack:
        x, y = stack.pop()
        if (x, y) == (rows - 1, cols - 1):
            return True
        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(1, 0), (0, 1)]:  # Move right or down
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                stack.append((nx, ny))

    return False

# Example Usage
grid = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0]
]
print(has_path(grid))