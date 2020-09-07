def nome(a):
    return len(a)

def nome_2(b):
    return len(b)

def main():
    n = input('Digite seu nome: ')
    e_c = input('Qual o seu estado civil ("C" pra casado ou "S" para solteiro): ')

    if e_c in 'cC':
        conj = input('Digite o nome do seu cônjuge: ')

        resultado = nome(n)
        resultado_2 = nome_2(conj)

        print(f'O seu nome possui {resultado} caracteres')
        print(f'E o de seu cônjuge posui {resultado_2} caracteres')

    else:
        if e_c in 'sS':
            resultado = nome(n)

            print(f'Seu nome possui {resultado} caracteres')
            
if __name__ == "__main__":
    main()
