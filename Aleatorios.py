import nacl.utils

'''
def aleatorio(num):
    return nacl.utils.random(num)


res = input("¿generar números aleatorios? s/n  ")
while res != "n" and res != "n":

    print(aleatorio(64))
    res= input("quieres seguir s/n  ")'''

def aleatorio() -> bytes:
    return nacl.utils.random()

def main():
    print(aleatorio())

if __name__ == '__main__':
    main()


