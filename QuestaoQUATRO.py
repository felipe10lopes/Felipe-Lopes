

def letra_numero(letra):
    letra = letra.lower()
    if letra in ('a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'):
        return True

    elif letra in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return True
    
    else:
        return False

def main():
    letra = input()
    x = letra_numero(letra)
    print(x)

if  __name__ == '__main__':
    main()
