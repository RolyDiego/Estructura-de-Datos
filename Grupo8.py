def maximo (a,b):
    if x>y:
        return x
    else:
        return y
    
    def minimo (a,b):
        if x<y:
            return x
        else:
            return y
        
        
        x = int(input("Un numero: "))
        y = int (input("Otro numero: "))
        print(maximo(x-3, minimo(x+2,y-5)))