def greet():
    print('こんにちは')
    
    greet()
    greet()

def wow():
    print("びっくり")
    
def greet(name):
    print(name+'さん、こんにちは')
    
    greet('松尾')
    
    greet('岩澤')

def greet(name):
    string = name + 'さん、こんにちは'
    return string
string = greet('松尾')
print(string)