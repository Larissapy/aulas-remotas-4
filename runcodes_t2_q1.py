def nome(a):
    return len(a)

def nome_2(b):
    return len(b)

def main():
    n = input()
    e_c = input()

    if e_c in 'cC' or e_c in '1':
        conj = input()

        resultado = nome(n)
        resultado_2 = nome_2(conj)
        resultado_3 = resultado + resultado_2

        return print(f'{resultado_3}')
        

    else:
        if e_c in 'sS':
            resultado = nome(n)

            return print(f'{resultado}')
            
if __name__ == "__main__":
    main()

