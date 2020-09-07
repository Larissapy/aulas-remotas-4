def data_recente(a, b, c, d, e, f, data_1, data_2):
    if c > f :
        return (f'{data_1}')
    elif f > c:
        return (f'{data_2}')
    elif b > e:
        return (f'{data_1}')
    elif e > b:
        return (f'{data_2}')
    elif a > d:
        return (f'{data_1}')
    elif d > a:
        return (f'{data_2}')
    else:
        if data_1 == data_2:
            return (f'{data_1}')

def main():
    d_1 = int(input())
    m_1 = int(input())
    a_1 = int(input())
    d_2 = int(input())
    m_2 = int(input())
    a_2 = int(input())

    data_1 = (f'{d_1}/{m_1}/{a_1}')
    data_2 = (f'{d_2}/{m_2}/{a_2}')

    resultado = data_recente(d_1, m_1, a_1, d_2, m_2, a_2, data_1, data_2)

    print(f'{resultado}')

if __name__ == "__main__":
    main()
