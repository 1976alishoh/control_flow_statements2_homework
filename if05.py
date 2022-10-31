def main(n):
    """
    Find the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    a = str(n)
    
    if max(a)==(a[0]):    
         return int(a[0])
    elif max(a)==a[1]:    
         return int(a[1])
    elif max(a)==a[2]:    
         return int(a[2])
    elif max(a)==a[3]:    
         return int(a[3])
    elif max(a)==a[4]:    
         return int(a[4])

print(main(23546))