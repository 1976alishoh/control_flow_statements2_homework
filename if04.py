def main(a,b):
    """
    Return zero if the numbers are equal, return the larger one if they are not equal.
    Args:
        a: First number.
        b: Second number.
    Returns:
        int: return answer.
    """
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return 0
print(main(3,7))
print(main(5,5))