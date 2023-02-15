# casos base dos palindromos, 1 - strings de uma letra, 2 - string vazia

"""def palindromo(s):
    if len(s)<=1:
        return True
    else:
        return s[0] == s[-1] and palindromo(s[1:-1])"""

def palindromo(s):
    def to_chars(s): # converte todas as letras para maiusculo
        s = s.lower() 
        return s
    def is_palindromo(s):
        if len(s)<=1:
            return True
        else:
            return s[0] == s[-1] and is_palindromo(s[1:-1])
    return is_palindromo(to_chars(s))

print(palindromo(""))
print(palindromo("ANNA"))
print(palindromo("sol"))
print(palindromo("Anna"))