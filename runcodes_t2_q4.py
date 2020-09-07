def signo(dia, mes):
    if dia >= 21 and mes == 3:
        return ('Áries')
    elif dia <=19 and mes == 4:
        return ('Áries')
    elif dia >= 20 and mes == 4:
        return ('Touro')
    elif dia <= 20 and mes == 5:
        return ('Touro')
    elif dia >= 21 and mes == 5:
        return ('Gêmeos')
    elif dia <= 21 and mes == 6:
        return ('Gêmeos')
    elif dia >= 22 and mes == 6:
        return ('Câncer')
    elif dia <= 22 and mes == 7:
        return ('Câncer')
    elif dia >= 23 and mes == 7:
        return ('Leão')
    elif dia <= 22 and mes == 8:
        return ('Leão')
    elif dia >= 23 and mes == 8:
        return ('Virgem')
    elif dia <= 22 and mes == 9:
        return ('Virgem')
    elif dia >= 23 and mes == 9:
        return ('Libra')
    elif dia <= 22 and mes == 10:
        return ('Libra')
    elif dia >= 23 and mes == 10:
        return ('Escorpião')
    elif dia <= 21 and mes == 11:
        return ('Escorpião')
    elif dia >= 22 and mes == 11:
        return ('Sargitário')
    elif dia <= 21 and mes == 12:
        return ('Sargitário')
    elif dia >= 22 and mes == 12:
        return ('Capricórnio')
    elif dia <= 19  and mes == 1:
        return ('Capricórnio')
    elif dia >= 20  and mes == 1:
        return ('Aquário')
    elif dia <= 18  and mes == 2:
        return ('Aquário')
    elif dia >= 19  and mes == 2:
        return ('Peixes')
    else:
        if dia <= 20 and mes == 3:
            return ('Peixes')
    
    

def main():
    d = int(input())
    m = int(input())

    resultado = signo(d, m)

    print(f'{resultado}')

if __name__ == "__main__":
    main()
    
