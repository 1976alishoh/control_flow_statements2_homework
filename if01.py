def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b > c :
        return a
    if b > c > a :
         return b
    if c > b > a :
         return c
print(main(1,4,2))
print(main(-5,-3,-1))
    