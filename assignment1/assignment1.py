# Write your code here.
def hello():
    a= 'Hello!'
    return a

def greet(name):
    return "Hello, " + name + '!'

def calc(a,b,c='multiply'):
    if c=='add':
        return a+b
    elif c=="subtract":
        return a-b
    elif c=="multiply":
        try:
            return a*b
        except:
            return "You can't multiply those values!"
    elif c=='divide':
        try:
            return a/b
        except:
            return "You can't divide by 0!"
    elif c=='modulo':
        return a%b
    elif c=='int_divide':
        return a//b

# print(calc(10,0,"divide"));