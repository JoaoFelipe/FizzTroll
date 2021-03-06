def fizz_buzz(numero):
    texto = ""
    if numero % 3 == 0:
        texto += "fizz"    
    if numero % 5 == 0:
        texto += "buzz"
    return texto or numero

def fizz_alt(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "fizzbuzz"
    elif numero % 3 == 0:
        return "fizz"
    elif numero % 5 == 0:
        return "buzz"
    else:
        return numero

def fizz_tern(numero):
    return (("fizz" if numero % 3 == 0 else "") + ("buzz" if numero % 5 == 0 else "")) or numero

def fizz_dict(numero):
    texto = ""
    for k,v in {3: "fizz", 5: "buzz"}.items(): 
        if numero % k == 0:
            texto += v
    return texto or numero

def fizz_bit(numero):
    lista = [numero, "fizz", "buzz", "fizzbuzz"]
    fizz = 1 if numero % 3 == 0 else 0
    buzz = 2 if numero % 5 == 0 else 0 
    return lista[fizz|buzz]

fizz = lambda x: x % 3 == 0 and "fizz" or ""
buzz = lambda x: x % 5 == 0 and "buzz" or ""
fizz_func = lambda x: (fizz(x)+buzz(x)) or x

def fizz_matriz(numero):
    return [
        [numero, "buzz"],
        ["fizz", "fizzbuzz"],
    ][numero % 3 == 0][numero % 5 == 0]

def fizz_gen(numero):    
    def generator(numero):
        if numero % 3 == 0: yield "fizz"
        if numero % 5 == 0: yield "buzz"
        
    return "".join(text for text in generator(numero)) or numero

class FizzLong(object):

    def __init__(self, numero):
        self.numero = numero

    def _divisivel(self, divisor):
        return not self.numero % divisor 

    def is_fizz(self):
        return self._divisivel(3)

    def is_buzz(self):
        return self._divisivel(5)

    def is_fizzbuzz(self):
        return self.is_fizz() and self.is_buzz()

    def __call__(self):
        if self.is_fizzbuzz():
            return "fizzbuzz"
        if self.is_fizz():
            return "fizz"
        if self.is_buzz():
            return "buzz"
        return self.numero

def fizz_long(numero):
    return FizzLong(numero)()



