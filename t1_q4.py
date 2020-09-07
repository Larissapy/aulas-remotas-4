def maior(a, b, c, d, e, media):
    if a > media and b > media:
        return (a, b) 
def main():
    n_1 = int(input())
    n_2 = int(input())
    n_3 = int(input())
    n_4 = int(input())
    n_5 = int(input())

    media = (n_1 + n_2 + n_3 + n_4 + n_5) / 5
    resultado = maior(n_1, n_2, n_3, n_4, n_5, media )

    print(f'{media:.2f}')
    print(f'{resultado:.2f}')

    if n_2 > media:
        return print(f'{n_2:.2f}')
    
if __name__ == "__main__":
    main()
