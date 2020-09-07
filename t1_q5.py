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
    p = float(input('Digite seu peso em Kg: '))
    a = float(input('Digite sua altura em m: '))

    IMC = p / (a * a)
    resultado = imc(p, a)

    print(f'IMC: {IMC:.0f}')
    print(f'Classificação: {resultado}')
    
if __name__ == "__main__":
    main()
