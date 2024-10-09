from utils import *


def run_tests():
    test_datasets = [
        {
            "telpa": Telpa(0, 200, 150),
            "iekartas": [
                Iekarta(0, 30, 20),
                Iekarta(1, 25, 35),
                Iekarta(2, 40, 15),
                Iekarta(3, 15, 25),
                Iekarta(4, 35, 30)
            ],
            "savienojumi": [
                [0, 8, 5, 2, 1],
                [8, 0, 3, 6, 4],
                [5, 3, 0, 7, 2],
                [2, 6, 7, 0, 9],
                [1, 4, 2, 9, 0]
            ]
        },
        {
            "telpa": Telpa(0, 800, 600),
            "iekartas": [
                Iekarta(0, 50, 80),
                Iekarta(1, 70, 60),
                Iekarta(2, 40, 90),
                Iekarta(3, 60, 50),
                Iekarta(4, 80, 70),
                Iekarta(5, 30, 40),
                Iekarta(6, 50, 60),
                Iekarta(7, 20, 30)
            ],
            "savienojumi": [
                [0, 2, 1, 0, 0, 3, 1, 0],
                [2, 0, 5, 2, 1, 0, 0, 0],
                [1, 5, 0, 0, 3, 0, 2, 1],
                [0, 2, 0, 0, 8, 1, 0, 3],
                [0, 1, 3, 8, 0, 0, 4, 2],
                [3, 0, 0, 1, 0, 0, 6, 0],
                [1, 0, 2, 0, 4, 6, 0, 5],
                [0, 0, 1, 3, 2, 0, 5, 0]
            ]
        }, {
            "telpa": Telpa(0, 800, 600),
            "iekartas": [
                Iekarta(0, 50, 80),
                Iekarta(1, 70, 60),
                Iekarta(2, 40, 90),
                Iekarta(3, 60, 50),
                Iekarta(4, 80, 70),
                Iekarta(5, 30, 40),
                Iekarta(6, 50, 60),
                Iekarta(7, 20, 30)
            ],
            "savienojumi": [
                [0, 10, 2, 0, 1, 5, 0, 0],
                [10, 0, 1, 3, 0, 0, 2, 1],
                [2, 1, 0, 0, 4, 1, 0, 0],
                [0, 3, 0, 0, 15, 2, 0, 8],
                [1, 0, 4, 15, 0, 0, 6, 1],
                [5, 0, 1, 2, 0, 0, 12, 0],
                [0, 999, 0, 0, 6, 100, 0, 4],
                [0, 1, 1000, 8, 1, 0, 4, 0]
            ]
        }
    ]

    for i, dataset in enumerate(test_datasets):
        print(f"Running test {i + 1}...")
        telpa = dataset["telpa"]
        iekartas = dataset["iekartas"]
        savienojumi = dataset["savienojumi"]

        # Izvietojiet iekārtas sākotnēji nejauši
        for iek in iekartas:
            uzstadit_iekartu(iek, telpa)

        # Optimizējiet izvietojumu ar LAHC
        vesture_garums = 100
        labakais_risinajums, labakas_izmaksas, execution_time = lahc(
            iekartas, telpa, savienojumi, vesture_garums
        )

        # Izvadiet rezultātus
        print("Labākais risinājums:")
        for iek in labakais_risinajums:
            print(f"  Iekārta {iek.id}: ({iek.x}, {iek.y})")
        print(f"Labākās izmaksas: {labakas_izmaksas}")
        print(f"Izpildes laiks: {execution_time:.4f} sekundes\n")

        visualize_solution(telpa, labakais_risinajums)


if __name__ == "__main__":
    run_tests()
