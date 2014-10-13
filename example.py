from mu import mu

#here is some brief documentation on how you can use Mu in your programs
#mu(function, [inline = True], [recurseName = 'this'], [paramName = 'param'])
    
    #function specifies the anonymous function where it is a string of Python
    #delimited by semicolons to specify new lines; colons specify an indent level
    #as well as leading tabs at the beginning of a line [OR] is simply a triple
    #quoted string indented like normal Python code [see below]

    #inline specifies whether the input is specified in single or double quotes [True]
    #OR if it is in the triple quoted Python style mentioned previously [False]
    
    #recurseName specifies a function name that refers to the anonymous function itself
    #paramName specifies a variable name that refers to function input variable

#quirk: the global keyword may not work as expected within your larger program
#quirk: escape characters in triple quoted strings are two backslashes; e.g. \\n
#quirk: in inline mode, semicolons escape an arbitrary number of subsequent semicolons

#f is just a convenience wrapper for
#using inline mode examples where
#recursion is done using t() and
#input is specified by variable a

#g is similarly a convenience wrapper
#for multiline mode using the same
#altered recursion and parameter names

def f(function): return mu(function, True, recurseName = 't', paramName = 'a')
def g(function): return mu(function, False, recurseName = 't', paramName = 'a')

#temporary and anonymous functions
#and then some more complicated examples

print(f('return a*3')(4)) #Result: 12
print(f('cube = a**3; return cube')(4)) #Result: 64

print(f('if a==1:; :return 1; elif a%2 == 0:; :return t(a/2); else:; :return t(3*a+1)')(31)) #Result: 1
print(f('def hello(number):; :if number==3:; ::return 3; :else:; ::return 0; return hello(a)')(3)) #Result: 3
print(f('def pi():; :return 3.1415926535897932384626433832795028841971693993751; return pi()')()) #Result: PI

#example of multiline syntax designed to look native
#tabbing needs to only be internally consistent and
#it does not matter the indentation of the first line

#fibonacci
print(g('''
    if a > 2:
        return t(a - 1) + t(a - 2)
    else:
        return 1
''')(9)) #Result: 34
    
#example of using this with filter or map
#compare with limits of traditional lambda
foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]

print ([i for i in filter(g('''
    for i in range(2, round(a ** 0.5) + 1): #check primality
        if a % i == 0: return False #comments are amazing
    return True #and they are entirely valid with Mu
'''), foo)]) #Result: [2, 17]

#use Mu as a convenience tool to compactly assign named methods
factorial = f('return a*t(a-1) if a>1 else 1') #Factorial Function
fibonacci = f('return t(a-1)+t(a-2) if a>2 else 1') #Fibonacci Function
comprehend = f('return [n+a for n in range(1,13)]') #List Comprehension
example = f('codes = a*a; return codes') #Defining Variables

print(factorial(6)) #Result: 720
print(fibonacci(8)) #Result: 21
print(comprehend(5)) #Result: [6...17]
print(example(4)) #Result: 16