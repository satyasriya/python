def digits(n):
    if n==0:
        return
    print(n%10)
    return digits(n//10)
digits(345678)
