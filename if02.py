def main(a,b,c):
    """
    Find the smallest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b > c :
        return c
    elif a > c > b :
        return b
    
    elif b > c > a :
         return a
    elif b > a >c:
         return c
    
    elif c > b > a :
         return a
    elif c > a > b:
         return b
print(main(1,4,2))
print(main(-5,-3,-1))
    