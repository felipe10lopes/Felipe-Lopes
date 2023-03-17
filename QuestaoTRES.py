
def consoante(letra):
    letra = letra.lower()
    if letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',
            'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
        return True
    else:
        return False

def main():
    letra = input()
    x = consoante(letra)
    print(x)

if  __name__ == '__main__':
    main()
