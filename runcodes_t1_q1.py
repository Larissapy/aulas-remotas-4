def idade(a, b, c, d, e, f):
    idade = c - f
    if e > b:
        idade -= 1
        return idade
    elif b == e:
        if a < d:
            idade -= 1
        return idade
    else:
        return idade

def main():
    d_atual = int(input())
    m_atual = int(input())
    a_atual = int(input())
    d_nasci = int(input())
    m_nasci = int(input())
    a_nasci = int(input())

    resultado = idade(d_atual, m_atual, a_atual, d_nasci, m_nasci, a_nasci)

    print(f'{resultado}')

if __name__ == "__main__":
    main()

