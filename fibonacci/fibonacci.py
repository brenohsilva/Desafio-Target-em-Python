
def sequencia_fibonacci(n):
    fib_list = [0, 1]
    
    while fib_list[-1] < n:

        fib_list.append(fib_list[-1] + fib_list[-2])
    
    print(f"A sequencia é {fib_list}")

    if n in fib_list:
       return f"{n} pertence a sequência"
    else:
        return f"{n} não pertence a sequência"


numero = int(input("digite o numero para a sequência de fibonacci: "))
print(sequencia_fibonacci(numero))
