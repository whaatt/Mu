from mu import mu as f

factorial = f('return a*t(a-1) if a>1 else 1') #Factorial Function
fibonacci = f('return t(a-1)+t(a-2) if a>2 else 1') #Fibonacci Function
comprehend = f('return [n+a for n in range(1,13)]') #List Comprehension
example = f('salary = a*a; return salary') #Defining Variables

print(factorial(6)) #Result: 720
print(fibonacci(8)) #Result: 21
print(comprehend(5)) #Result: [6...17]
print(example(4)) #Result: 16

print(f('return a*3')(4)) #Result: 12
print(f('cube = a**3; return cube')(4)) #Result: 64

print(f('if a==1:; :return 1; elif a%2 == 0:; :return t(a/2); else:; :return t(3*a+1)')(31)) #Result: 1
print(f('def hello(number):; :if number==3:; ::return 3; :else:; ::return 0; return hello(a)')(3)) #Result: 3
print(f('def pi():; :return 3.1415926535897932384626433832795028841971693993751; return pi()')()) #Result: PI
