def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = str(n)
    return a.index(max(a))
print(main(76514))
print(main(54694))