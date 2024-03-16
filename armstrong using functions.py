def arms(n):
    def count(n):
        if n == 0:
            return 0
        return 1 + count(n // 10)
    def armstrong(n, p):
        if n == 0:
            return 0
        return (n % 10) ** p + armstrong(n // 10, p)

    p = count(n)
    result = armstrong(n, p)
    return result == n

number = 153
print(arms(number))  
