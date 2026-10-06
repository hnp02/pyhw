# Write your code here.
def hello():
    a= 'Hello!'
    return a

def greet(name):
    return f"Hello, {name}!"

def calc(a,b,c='multiply'):
    try:
        if c=='add':
            return a+b
        elif c=="subtract":
            return a-b
        elif c=="multiply":
            return a*b
        elif c=='divide':
            return a/b
        elif c=='modulo':
            return a%b
        elif c=='int_divide':
            return a//b
        elif c=='power':
            return a**b
    except TypeError:
        return "You can't multiply those values!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
            
        

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

def repeat(text, count):
    out= ""
    for i in range(count):
        out += text
    return out

def student_scores(choice, **kwargs):
    if choice== "best":
        name= max(kwargs, key= kwargs.get)
        return name
    elif choice== 'mean':
        mean= mean = sum(kwargs.values()) / len(kwargs)
        return mean
    
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    word = text.split()
    result = []
    for i, word in enumerate(word):
        if i == 0 or i == len(word) - 1 or word.lower() not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word.lower())
    return " ".join(result)

def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

def pig_latin(text):
    vowels = "aeiou"
    words = []
    for word in text.split():
        i = 0
        while i < len(word) and word[i] not in vowels:
            if word[i] == "q" and word[i + 1:i + 2] == "u":
                i += 2
            else:
                i += 1
        words.append(word[i:] + word[:i] + "ay")
    return " ".join(words)

