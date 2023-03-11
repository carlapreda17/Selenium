import math
import random

def f(x):
    return math.sin(x - 2)**2 - x * math.cos(x)

def hill_climbing(f, domain, step_size=0.1, max_iterations=1000):
    current_x = random.uniform(domain[0], domain[1]) #se alege un numar random din interval
    for i in range(max_iterations):
        best_x = current_x  #vom spune ca cea mai buna solutie e cea curenta
        for x in [current_x - step_size, current_x + step_size]: #pentru un x oarecare care se afla in vecinatate
            if domain[0] <= x <= domain[1]: #daca apartine domeniului
                if f(x) > f(best_x):  #x-ul ales are calitatea mai buna il inlocuim cu cea mai buna solutie
                    best_x = x
        if best_x == current_x: #daca nu am gasit nicio solutie mai buna atunci ramane cea curenta
            break
        current_x = best_x
    return current_x, f(current_x)


if __name__=='__main__':
    x_max, f_max = hill_climbing(f, [1, 2500]) #intre functie si domeniu
    print("Maximul funcției f(x) este {} în punctul x = {}".format(f_max, x_max))
