def imc(peso, altura):
    IMC = peso / (altura * altura)
    if IMC < 18.5:
        return ('Abaixo do peso')
    elif IMC < 25:
        return ('Peso normal')
    elif IMC < 30:
        return ('Sobrepeso')
    elif IMC < 35:
        return ('Obeso leve')
    elif IMC < 40:
        return ('Obeso moderado')
    else:
        if IMC >= 40:
            return ('Obeso mórbido')

def main():
    p = float(input())
    a = float(input( ))

    IMC = p / (a * a)
    resultado = imc(p, a)

    print(f'{IMC:.0f}')
    print(f'{resultado}')
    
if __name__ == "__main__":
    main()

