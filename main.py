
#
#   Author:         Juan Camilo Rodriguez
#   Date:           29 April 2020
#   Description:    Genetic Algorithm from scratch
#


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
            "generation_num": 100,
            "population_size": 30,
            "find": "maximum",
            "available_finds": ["maximum", "minimum"]
        },
        "FI_settings": {
            "function_type": 1,
            "available_fitness_functions": [0,1,2,3],

            "function_1":{
                "chromosome_size": 8,

            },

            "function_2": {
                "chromosome_size": 10,
            },

            "function_3": {
                "chromosome_size": 8,   # n value
            },

        },
        "PS_settings": {
            "available_methods": ["TO", "RW"],
            "method": "TO",
            "quantity_of_parents": 25,

            "problem_type": None,

            # Tournament Selection
            "TO_K": 3,

        },
        "CR_settings": {
            "rate": 0.5,
            "available_methods": ["OP", "TP"],
            "method": "OP",
            "quantity_crossover_attempts": 5,
        },
        "MU_settings": {
            "rate": 0.5,
            "available_methods": ["BF", "SW"],
            "method": "BF",
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

    # Execute the Genetic Algorithm
    genetic_algorithm.execute()