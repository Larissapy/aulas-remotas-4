def maior(a, b, c, d, e):
    if a > b and a > c and a > d and a > e:
        return a
    elif b > a and b > c and b > d and b > e:
        return b
    elif c > a and c > b and c > d and c > e:
        return c
    elif d > a and d > b and d > c and d > e:
        return d
    else:
        return e

def menor(a, b, c, d, e):
    if a < b and a < c and a < d and a < e:
        return a
    elif b < a and b < c and b < d and b < e:
        return b
    elif c < a and c < b and c < d and c < e:
        return c
    elif d < a and d < b and d < c and d < e:
        return d
    else:
        return e

def main():
    n_1 = int(input())
    n_2 = int(input())
    n_3 = int(input())
    n_4 = int(input())
    n_5 = int(input())

    resultado_1 = maior(n_1, n_2, n_3, n_4, n_5)
    resultado_2 = menor(n_1, n_2, n_3, n_4, n_5)

    print(f'{resultado_1}')
    print(f'{resultado_2}')

if __name__ == "__main__":
    main()
