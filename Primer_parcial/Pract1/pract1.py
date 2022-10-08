import vispy.plot as vp

def main():
    # Context manager: abre y cierra el archivo al terminarlo de usar
    num_bin = []
    with open("C:/Users/bigbo/OneDrive/Escritorio/resultados/combinaciones.txt", "wt+") as f:
        k = int(input("Ingresa m:\n"))
        for i in range(1, k+1):
            f.write("{")
            h = 2**i
            for j in range(h):
                c = bin(j)[2:].zfill(i)
                num_bin.append(c)
                if j+1 == h:
                    f.write(f"{c}")
                else:
                    f.write(f"{c},")
            f.write("}\n")
        
    ones_count = [x.count('1') for x in num_bin]

    num_bin_list = list(range(1, len(num_bin)+1))

    fig = vp.Fig(size=(600, 500), show=False)
    plotwidget = fig[0, 0]
    fig.title = "Práctica 1"
    plotwidget.plot((num_bin_list, ones_count), title="", marker_size=0, color='k')
    fig.show(run=True)

if __name__ == "__main__":
    main()