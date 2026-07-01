def number_pattern(n):
    nums = []
    if not isinstance(n, int):
        return "Argument must be an integer value."
    if n <= 0:
        return "Argument must be an integer greater than 0."
    else:        
        for i in range(1,n+1):
            nums.append(str(i))
    return " ".join(nums)
