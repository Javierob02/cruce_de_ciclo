def cycle_crossover(parent1, parent2):
    ciclos = []
    cruce = []
    result = []

    for i in parent1:
        valor = parent2[parent1.index(i)]
        ciclo = []
        ciclo.append(i)
        if i != valor:
            ciclo.append(valor)
        while valor != i:
            valor = parent2[parent1.index(valor)]
            if valor != i:
                ciclo.append(valor)
        ciclos.append(ciclo)

    for i in parent1:
        for j in range(len(ciclos)):
            if i in ciclos[j]:
                cruce.append(j+1)
                break

    count = 0
    for element in cruce:
        if (element % 2 == 0):
            result.append(parent2[count])
        else:
            result.append(parent1[count])
        count += 1

    return resultc