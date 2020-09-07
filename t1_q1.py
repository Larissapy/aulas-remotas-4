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
    d_atual = int(input('Que dia é hoje?: '))
    m_atual = int(input('Em que mês estamos?: '))
    a_atual = int(input('E o ano?: '))
    d_nasci = int(input('Que dia você nasceu?: '))
    m_nasci = int(input('Em que mês?: '))
    a_nasci = int(input('E em qual foi o ano?: '))

    resultado = idade(d_atual, m_atual, a_atual, d_nasci, m_nasci, a_nasci)

    print(f'Você tem {resultado} anos de idade')

if __name__ == "__main__":
    main()
