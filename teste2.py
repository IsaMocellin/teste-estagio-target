# 2) Sequência de Fibonacci e verificação se um número informado pertence à sequência
def pertence_fibonacci(n):
    a, b = 0, 1
    if n == 0:
        return True
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

num = 21  # Altere o número aqui para verificar outro
if pertence_fibonacci(num):
    print(f"2) O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"2) O número {num} NÃO pertence à sequência de Fibonacci.")
