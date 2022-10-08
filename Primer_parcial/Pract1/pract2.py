import vispy.plot as vp


def erathostenes_cribe(n):
    primes = []
    primes_bin = []
    not_primes = set()

    for i in range(2, n+1):
        if i not in not_primes:
            primes.append(str(i))
            primes_bin.append(bin(i)[2:])

            for j in range(i*i, n+1, i):
                not_primes.add(j)
    
    return primes, primes_bin

def main():
    n = int(input("Ingresa el número hasta donde quieres obtener números primos:\n"))

    primes, primes_bin = erathostenes_cribe(n)

    with open("C:/Users/bigbo/OneDrive/Escritorio/resultados/primes.txt", "wt+") as f:
        for i in primes:
            f.write(f"{i}, ")
    with open("C:/Users/bigbo/OneDrive/Escritorio/resultados/primes_bin.txt", "wt+") as f:
        for i in primes_bin:
            f.write(f"{i}, ")

    primes_count = [x.count('1') for x in primes_bin]


    fig = vp.Fig(size=(600, 500), show=False)
    plotwidget = fig[0, 0]

    fig.title = "Práctica 2"
    plotwidget.plot((primes, primes_count), title="Números primos", marker_size=0, color='k')
    fig.show(run=True)


if __name__ == "__main__":
    main()