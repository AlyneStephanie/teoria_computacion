import vispy.plot as vp
import math


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

    response = True

    while response:

        n = int(input("Ingresa el número hasta donde quieres obtener números primos:\nAl aparecer, cierra la imagen para continuar\n"))
        primes, primes_bin = erathostenes_cribe(n)

        with open("C:/Users/bigbo/OneDrive/Escritorio/resultados/primes.txt", "wt+") as f:
            f.write("{\n")
            for i in primes:
                f.write(f"{i}, ")
            f.write("\n}")
        with open("C:/Users/bigbo/OneDrive/Escritorio/resultados/primes_bin.txt", "wt+") as f:
            f.write("{\n")
            for i in primes_bin:
                f.write(f"{i}, ")
            f.write("\n}")


        fig = vp.Fig(size=(1500, 900), show=False)
        fig.title = "Práctica 2"

        primes_count = [x.count('1') for x in primes_bin]
        plotwidget1 = fig[0, 0]
        plotwidget1.plot((primes, primes_count), title="Números primos", marker_size=0, color='k')

        primes_count_log_base_2 = []
        for i in primes_count:
            if primes_count[i] == 0: primes_count_log_base_2.append(0)
            else: primes_count_log_base_2.append(math.log2(primes_count[i]))
        plotwidget2 = fig[1, 0]
        plotwidget2.plot((primes, primes_count_log_base_2), title="Log base 2", marker_size=0, color='k')
        
        primes_count_log_base_10 = []
        for i in primes_count:
            if primes_count[i] == 0: primes_count_log_base_10.append(0)
            else: primes_count_log_base_10.append(math.log10(primes_count[i]))
        plotwidget2 = fig[1, 1]
        plotwidget2.plot((primes, primes_count), title="Log base 10", marker_size=0, color='k')

        fig.show(run=True)

        response = input("¿Deseas calcular otra 'n'?\n")
        neg = ["n", "N", "No", "no", "False", "false", "0", "NO", "negativo", "neg"]
        for res in neg:
            if res == response: response = False
            else: res == True



if __name__ == "__main__":
    main()