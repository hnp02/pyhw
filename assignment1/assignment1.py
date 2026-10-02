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

def data_type_conversion(a,b):
    if b=="int":
        try:
            return int(a)
        except:
            return f"You can't convert {a} into a {b}."
    elif b=="str":
        return str(a)
    elif b=="float":
        return float(a)

def grade(*args):
    try:
        ave= sum(args)/len(args)
    except: 
        return "Invalid data was provided."
    if ave >=90:
        return "A"
    elif ave >= 80 and ave <90:
        return "B"
    elif ave >= 70 and ave <80:
        return "C"
    elif ave >= 60 and ave <70:
        return "D"
    elif ave <60:
        return "F"




# def titleize