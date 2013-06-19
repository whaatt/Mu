from mu import mu as f

#Usage: from mu import mu --> all you need to get started. import it as something for brevity's sake
#Usage: mu(function) --> where function is a string of Python delimited by ':' and ';' as shown below
#Usage: mu(function, False) --> where function looks like regular Python inside ''' this ''', as shown below
#Usage: the variable *a* refers to your passed parameter, and the variable *t* refers to the function itself (for recursion)

#Known Quirk: the global keyword will not work as expected within the context of your larger program
#Known Quirk: In ''' mode, escape characters in strings Must Have Two Backslashes, e.g. '\\t' instead of '\t'
#Known Quirk: In string mode, semicolons in strings must be doubled up ';;' to work properly.

#Temporary, Anonymous Functions
print(f('return a*3')(4)) #Result: 12
print(f('cube = a**3; return cube')(4)) #Result: 64

print(f('if a==1:; :return 1; elif a%2 == 0:; :return t(a/2); else:; :return t(3*a+1)')(31)) #Result: 1
print(f('def hello(number):; :if number==3:; ::return 3; :else:; ::return 0; return hello(a)')(3)) #Result: 3
print(f('def pi():; :return 3.1415926535897932384626433832795028841971693993751; return pi()')()) #Result: PI

#Example of False Flag, Designed to Look Like Native Syntax
#Functions inside ''' ''' must only be internally consistent for indentation, and first line need not be indented properly

if True:
	print(f('''
		if a > 2:
			return t(a - 1) + t(a - 2)
		else:
			return 1
	''', False)(9)) #Result: 34
	
#Example of using this with filter/map, compare with traditional lambda
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print ([i for i in filter(f('''
	for i in range(2, round(a**0.5) + 1): #check primality
		if a%i == 0: return False
	return True
''', False), foo)]) #Result: [2, 17]
	
#Functions As Variables

factorial = f('return a*t(a-1) if a>1 else 1') #Factorial Function
fibonacci = f('return t(a-1)+t(a-2) if a>2 else 1') #Fibonacci Function
comprehend = f('return [n+a for n in range(1,13)]') #List Comprehension
example = f('codes = a*a; return codes') #Defining Variables

print(factorial(6)) #Result: 720
print(fibonacci(8)) #Result: 21
print(comprehend(5)) #Result: [6...17]
print(example(4)) #Result: 16