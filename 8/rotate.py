def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    rotated = []
    for _ in string:
        rotated.append(string[n % len(string)])
        n += 1
    return ''.join(rotated)
