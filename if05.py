def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = str(n)
    
    if max(a)==a[0]:    
         return a[0]
    elif max(a)==a[1]:    
         return a[1]
    elif max(a)==a[2]:    
         return a[2]
    elif max(a)==a[3]:    
         return a[3]
    elif max(a)==a[4]:    
         return a[4]

print(main(23546))