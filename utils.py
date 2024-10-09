import random
import math
import time

from matplotlib import pyplot as plt


class Iekarta:
    def __init__(self, id, platums, augstums):
        self.id = id
        self.platums = platums
        self.augstums = augstums
        self.x = 0
        self.y = 0


class Telpa:
    def __init__(self, id, platums, augstums):
        self.id = id
        self.platums = platums
        self.augstums = augstums


def attalums(iek1, iek2):
    """Aprēķina attālumu starp divām iekārtām."""
    return math.sqrt((iek1.x - iek2.x) ** 2 + (iek1.y - iek2.y) ** 2)


def izmaksas(iekartas, savienojumi):
    """Aprēķina kopējās izmaksas."""
    z = 0
    for iek1 in iekartas:
        for iek2 in iekartas:
            if iek1.id != iek2.id:
                z += savienojumi[iek1.id][iek2.id] * attalums(iek1, iek2)
    return z


def uzstadit_iekartu(iek, telpa):
    """Pārvieto iekārtu telpā nejauši."""
    iek.x = random.randint(0, telpa.platums - iek.platums)
    iek.y = random.randint(0, telpa.augstums - iek.augstums)


def parvietot_iekartu(iek, telpa, iekartas, savienojumi):
    """Pārvieto iekārtu, ņemot vērā savienojumus."""
    labakais_x = iek.x
    labakais_y = iek.y
    labakas_izmaksas = izmaksas(iekartas, savienojumi)

    for _ in range(10):  # Try 10 different moves
        # 1. Small Perturbation:
        new_x = iek.x + random.randint(-20, 20)  # Adjust the range as needed
        new_y = iek.y + random.randint(-20, 20)
        new_x = max(0, min(new_x, telpa.platums - iek.platums))  # Keep within bounds
        new_y = max(0, min(new_y, telpa.augstums - iek.augstums))

        iek.x = new_x
        iek.y = new_y
        jaunas_izmaksas = izmaksas(iekartas, savienojumi)

        if jaunas_izmaksas < labakas_izmaksas:
            labakais_x = new_x
            labakais_y = new_y
            labakas_izmaksas = jaunas_izmaksas

        # 2.  Swap with another machine (optional):
        # You can add code here to try swapping the position of 'iek' with another
        # randomly chosen machine and see if it improves the cost.

    iek.x = labakais_x
    iek.y = labakais_y


def visualize_solution(telpa, labakais_risinajums):
    # Vizualizējiet rezultātus
    plt.figure(figsize=(8, 6))
    plt.title('Iekārtu izvietojums')
    plt.xlabel('X koordināta')
    plt.ylabel('Y koordināta')
    for iek in labakais_risinajums:
        plt.gca().add_patch(
            plt.Rectangle((iek.x, iek.y), iek.platums, iek.augstums, fill=True, color='lightgray', edgecolor='black'))
        plt.text(iek.x + iek.platums / 2, iek.y + iek.augstums / 2, str(iek.id), ha='center', va='center')
    plt.xlim([0, telpa.platums])
    plt.ylim([0, telpa.augstums])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

def lahc(iekartas, telpa, savienojumi, vesture_garums, max_iter=10000,
         max_no_improvement=100):
    """Optimizē iekārtu izvietojumu, izmantojot LAHC."""
    start_time = time.time()

    labakais_risinajums = [Iekarta(iek.id, iek.platums, iek.augstums) for iek in iekartas]
    for iek in labakais_risinajums:
        iek.x = iekartas[iek.id].x
        iek.y = iekartas[iek.id].y
    labakas_izmaksas = izmaksas(iekartas, savienojumi)
    vesture = [labakas_izmaksas] * vesture_garums

    iteracija = 0
    no_improvement_count = 0
    while iteracija < max_iter and no_improvement_count < max_no_improvement:
        # Izvēlas nejaušu iekārtu un pārvieto to (var uzlabot ar gudrāku pārvietošanu)
        izveletajai_iek = random.choice(iekartas)
        parvietot_iekartu(izveletajai_iek, telpa, iekartas, savienojumi)

        # Aprēķina jaunās izmaksas
        jaunas_izmaksas = izmaksas(iekartas, savienojumi)

        # Salīdzina ar vēsturi UN labāko risinājumu
        if jaunas_izmaksas < vesture[0] or jaunas_izmaksas < labakas_izmaksas:
            labakais_risinajums = [Iekarta(iek.id, iek.platums, iek.augstums) for iek in iekartas]
            for iek in labakais_risinajums:
                iek.x = iekartas[iek.id].x
                iek.y = iekartas[iek.id].y
            labakas_izmaksas = jaunas_izmaksas
            no_improvement_count = 0  # Reset the counter
        else:
            no_improvement_count += 1  # Increment the counter
        # Atjaunina vēsturi
        vesture.pop(0)
        vesture.append(jaunas_izmaksas)
        iteracija += 1

    end_time = time.time()
    execution_time = end_time - start_time

    return labakais_risinajums, labakas_izmaksas, execution_time
