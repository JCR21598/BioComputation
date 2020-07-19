
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
            "run_count":1,
            "generation_num": 80,
            "population_size": 100,
            "find": "maximum",
            "available_finds": ["maximum", "minimum"]
        },
        "FI_settings": {
            "function_type": 2,
            "available_fitness_functions": [0,1,2,3],

            "function_1":{
                "chromosome_size": 8,

            },

            "function_2": {
                "chromosome_size": 10,
            },

            "function_3": {

                # FUnction sets n as == 10 or 20 ( But Lecturer says that belives that other values can be used)

                "chromosome_size": 5,   # this is the n valuf of the function
            },

        },
        "PS_settings": {
            "available_methods": ["TO"],
            "method": "TO",
            "quantity_of_parents": 20,

            "problem_type": None,

            # Tournament Selection
            "TO_K": 3,

        },
        "CR_settings": {
            "rate": 0.1,
            "available_methods": ["OP", "BC"],
            "method": "BC",

            # Real-Value Encoding Settings
            "lower_range" : -5.12,
            "higher_range" : 5.12,
            "ALPHA": 0.25,
        },
        "MU_settings": {
            "rate": 0.5,
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
            "FB_suvivor_quantity" : 10,
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

    # Execute the Genetic Algorithm
    for x in range(GA_settings["general"]["run_count"]):
        genetic_algorithm.execute()
