def main(a,b,c):
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a > b > c :
        return b
    elif a > c > b :
        return c
    
    elif b > c > a :
         return c
    elif b > a >c:
         return a
    
    elif c > b > a :
         return b
    elif c > a > b:
         return a
    
    elif a >= b > c:
        return b
    elif a >= c > b:
        return a
    
    elif b >= a > c:
        return a
    elif b >= c > a:
        return c
    
    elif c >= a > a:
        return a
    elif c >= b > a:
        return b
    
print(main(3,7,1))
print(main(5,5,-1))