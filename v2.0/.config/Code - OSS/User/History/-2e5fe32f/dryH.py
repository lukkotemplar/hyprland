def sum(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a,b):
    return a * b

def div(a,b):
    try:
        return a / b
    except:
        print("Cannot divide by zero")