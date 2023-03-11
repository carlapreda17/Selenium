import numpy


def GA_Regine(n, dim, alti_parametri_de_control, nmax):
    # rezolvarea problemei celor n regine, pe o tabla n*n

    # I: n - numarul de regine
    #    dim - dimensiune populatie initiala
    #    ...
    #    nmax - numarul maxim de generatii
    # E: sol - permutarea care reprezinta cea mai buna solutie gasita
    #    V - vector cu cea mai buna calitate din fiecare generatie
    # Exemple de utilizare
    #   import GA_Regine as GR
    #   s,v=GR.GA_Regine(8,50,0.8,0.1,50)
    #   s,v=GR.GA_Regine(10,30,0.8,0.1,30)

    # initializari
    vmax = 0  # valoarea celei mai bune solutii gasite
    V = []

    # generare populatie initiala
    pop = gen_pop_perm(dim, n)

    # bucla GA
    t = 0  # contor iteratii
    # evolutie pina la consumarea tuturor iteratiilor sau atingerea calitatii maxime
    while (t < nmax) and (vmax < n * (n - 1) / 2):
        # selectie parinti

        # recombinare

        # mutatie

        # selectie generatie urmatoare

        # alte operatii
        t = t + 1  # am terminat o iteratie
        # retine cea mai buna solutie

    return sol, V


def f_obiectiv(x):
    # functia obiectiv pentru problema reginelor

    # I: x - individul (permutarea) evaluat(a)
    # E: c - calitate (numarul de perechi de regine care nu se ataca)

    n = len(x)
    c = n * (n - 1) / 2
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(x[i] - x[j]):
                c = c - 1
    return c


def gen_pop_perm(dim, n):
    # generare populatie de permutari

    # I: dim - dimensiune populatie (nr. de indivizi)
    #    n - dimensiune individ (numar de gene)
    # E: pop - populatia aleatoare generata, cu calitatea fiecarui individ pe ultima coloana

    pop = numpy.zeros((dim, n + 1), dtype=int)
    for i in range(dim):
        pop[i, :n] = numpy.random.permutation(n)
        pop[i, n] = f_obiectiv(pop[i, :n])
    return pop



