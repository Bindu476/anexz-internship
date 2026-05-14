rows = 4
i = 1

while i <= rows:
    spaces = rows - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)
    i = i + 1
