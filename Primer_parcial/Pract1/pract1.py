import vispy.plot as vp
import math

def main():
    response = True

    while response:

        num_bin = []
        accumulated = ""
        strings_64_bits = []
        num_bits = 64
        with open("combinaciones.txt", "wt+") as f:
            k = int(input("Ingresa m:\nAl aparecer, cierra la imagen para continuar\n"))
            f.write("{\n")
            for i in range(1, k+1):
                f.write("{")
                h = 2**i
                for j in range(h):
                    c = bin(j)[2:].zfill(i)
                    num_bin.append(c)
                    accumulated = f"{accumulated}{c}"
                    if j+1 == h:
                        f.write(f"{c}")
                    else:
                        f.write(f"{c},")
                f.write("}\n")
            f.write("}")
            num_of_strings_64_bits = math.floor(len(accumulated) / num_bits)
            for i in range(num_of_strings_64_bits):
                x = slice(i * num_bits, (i + 1) * num_bits)
                strings_64_bits.append(accumulated[x])
            # print(accumulated)
            # print(strings_64_bits)


        fig = vp.Fig(size=(1600, 900), show=False)
        fig.title = "Práctica 1"

        ones_count_bin = [x.count('1') for x in num_bin]
        num_bin_list = list(range(1, len(num_bin)+1))
        plotwidget_bin = fig[0, 0]
        plotwidget_bin.plot((num_bin_list, ones_count_bin), title="Número de unos", marker_size=0, color='k')

        ones_count_64_bits = [x.count('1') for x in strings_64_bits]
        num_strings_64_bits_list = list(range(1, len(strings_64_bits)+1))
        plotwidget_64_bits = fig[1, 0]
        plotwidget_64_bits.plot((num_strings_64_bits_list, ones_count_64_bits), title="Número de unos en cadenas de 64 bits", marker_size=0, color='k')

        # log_ones_count_64_bits = [math.log10(x.count('1')) for x in strings_64_bits if x =! 0]
        log_ones_count_64_bits = []
        for i in strings_64_bits:
            x = i.count('1')
            if x == 0: log_ones_count_64_bits.append(0)
            else: log_ones_count_64_bits.append(math.log10(x))

        num_strings_log_64_bits_list = list(range(1, len(strings_64_bits)+1))
        plotwidget_64_bits = fig[1, 1]
        plotwidget_64_bits.plot((num_strings_log_64_bits_list, log_ones_count_64_bits), title="Logaritmo base 10 del número de unos en cadenas de 64 bits", marker_size=0, color='k')
        
        fig.show(run=True)

        response = input("¿Deseas calcular otra 'm'?\n")
        neg = ["NO", "No", "no", "False", "false", "0", "NO", "negativo", "neg"]
        for res in neg:
            if res == response: response = False
            else: res == True

if __name__ == "__main__":
    main()