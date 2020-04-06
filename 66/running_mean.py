def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    total, running_mean = 0, []
    for n, x in enumerate(sequence):
        total += x
        running_mean.append(round(total/(n+1), 2))
    return running_mean


if __name__ == '__main__':
    a = [1, 2, 3]   # [1, 1.5, 2]
    b = [2, 6, 10, 8, 11, 10]   # [2, 4, 6, 6.5, 7.4, 7.8]
    running_mean(a)
    running_mean(b)
    