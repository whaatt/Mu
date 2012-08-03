from mu import mu as f

factorial = f('return a*t(a-1) if a>1 else 1')
fibonacci = f('return t(a-1)+t(a-2) if a>2 else 1')
comprehend = f('return [n+a for n in range(1,13)]')
example = f('salary = a*a; return salary')

print(factorial(6))
print(fibonacci(8)) 
print(comprehend(5)) 
print(example(4))