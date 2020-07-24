
#
#   Author:         Juan Camilo Rodriguez
#   Date:           29 April 2020
#   Description:    Genetic Algorithm from scratch
#


import matplotlib.pyplot as plt

from GA import GA

'''
#   Keywords for the Program
#
#   FI = Fitness
#   PS = Parent Selection
#   CR = Crossover
#   MU = Mutation
#   SS = Survivor Selection

#   PS_method: "TO" = tournament, "RW" = roulette wheel
#   CR_method: "OP" = one point, "TP" = two point
#   MU_method: "BF" = bit flip, "SW" = swap
#   SS_method: "
'''


if __name__ == '__main__':

    GA_settings = {
        "general": {
            "run_count": 10,
            "generation_num": 120,
            "population_size": 100,
            "find": "minimum",
            "available_finds": ["maximum", "minimum"]
        },
        "FI_settings": {
            "function_type": 3,
            "available_fitness_functions": [0,1,2,3],

            "function_1":{
                "chromosome_size": 8,

            },

            "function_2": {
                "chromosome_size": 10,
            },

            "function_3": {

                # FUnction sets n as == 10 or 20 ( But Lecturer says that belives that other values can be used)

                "chromosome_size": 10,   # this is the n valuf of the function
            },

        },
        "PS_settings": {
            "available_methods": ["TO"],
            "method": "TO",
            "quantity_of_parents": 25,

            "problem_type": None,

            # Tournament Selection
            "TO_K": 3,

        },
        "CR_settings": {
            "rate": 0.5,
            "available_methods": ["OP", "BC"],
            "method": "BC",

            # Real-Value Encoding Settings
            "lower_range" : -5.12,
            "higher_range" : 5.12,
            "ALPHA": 0.25,
        },
        "MU_settings": {
            "rate": 0.15,
            "available_methods": ["BF", "ND"],
            "method": "ND",

            # Real-Value Encoding Settings
            "mutation_range": 0.5,    # ex: x= 3.12 => mutation will be within 2.62 - 3.62

            "lower_range": None,
            "higher_range": None,

        },
        "SS_settings": {
            "available_methods": ["FB"],
            "method": "FB",

            "problem_type": None,

            # Fitness based settings
            "FB_suvivor_quantity" : 15,
        }
    }

    #   Setting the values of the Nones to the value needed
    GA_settings["PS_settings"]["problem_type"] = GA_settings["general"]["find"]
    GA_settings["SS_settings"]["problem_type"] = GA_settings["general"]["find"]

    GA_settings["MU_settings"]["lower_range"] = GA_settings["CR_settings"]["lower_range"]
    GA_settings["MU_settings"]["higher_range"] = GA_settings["CR_settings"]["higher_range"]

    ###     Validation of data before sent      ###

    if GA_settings["PS_settings"]["quantity_of_parents"] > GA_settings["general"]["population_size"]:
        print("\n\n\nError: There cannot be more parents than there is in the population")
        exit()

    if GA_settings["SS_settings"]["FB_suvivor_quantity"] > GA_settings["PS_settings"]["quantity_of_parents"]:
        print("\n\n\nError: There cannot be more survivrs than there is in the population")
        exit()

    if GA_settings["general"]["find"] not in GA_settings["general"]["available_finds"]:
        print("Not a valid problem type - check the avaible finds")
        exit()

    # Instantiate the GA with the settings set by user
    genetic_algorithm = GA(GA_settings)

    x = []
    y = []

    # Execute the Genetic Algorithm
    for count in range(GA_settings["general"]["run_count"]):

        x, y_highest, y_average, y_lowest = genetic_algorithm.execute()




        highest_plot = plt.figure(0)
        plt.plot(x, y_highest, label="Test {}".format(count + 1))

        plt.legend()

        plt.title("Highest Fitness per generation", fontsize=15)
        plt.xlabel("Generation", fontsize=13)
        plt.ylabel("Fitness", fontsize=13)




        average_plot = plt.figure(1)
        plt.plot(x, y_average, label="Test {}".format(count + 1))

        plt.legend()

        plt.title("Average Fitness per generation", fontsize=15)
        plt.xlabel("Generation", fontsize=13)
        plt.ylabel("Fitness", fontsize=13)




        lowest_plot = plt.figure(2)
        plt.plot(x, y_lowest, label="Test {}".format(count + 1))

        plt.legend()

        plt.title("Lowest Fitness per generation", fontsize=15)
        plt.xlabel("Generation", fontsize=13)
        plt.ylabel("Fitness", fontsize=13)




    plt.show()
