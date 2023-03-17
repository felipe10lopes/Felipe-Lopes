
def vogal(letra):
    letra = letra.lower()
    if letra in ('a', 'e', 'i', 'o', 'u'):
        return True
    else:
        return False

def main():
    letra = input()
    x = vogal(letra)
    print(x)

if  __name__ == '__main__':
    main()








