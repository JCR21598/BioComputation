
import copy
import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import pprint

import GA_Operations as Op
from Population import Population
import functions as func


class GA:

    def __init__(self, settings):
        self.settings = settings


    #   Genetic Algorithm Function - Main Loop
    def execute(self):

        saved_population = {}

        # Create list of Population and calculate initial fitness
        population = Population()
        population.random_populate(self.settings)

        for gen in range(self.settings['general']['generation_num']):

            # Update Fitness
            population.update_fitness(self.settings["FI_settings"])
            func.print_population_section(f"Generation {gen}", population.individuals)

            #   Saving data
            saved_population[f"pop_gen{gen}"] = copy.deepcopy(population.individuals)
            #pprint.pprint(saved_population)

            # Parent Selection
            selected_parents = population.parent_selection(self.settings['PS_settings'])

            func.print_population_section("parents",selected_parents)
            func.print_population_section("lowest", selected_parents)


            # Crossover
            crossover = population.crossover(self.settings['CR_settings'], selected_parents)

            # Mutation
            mutation = population.mutation(self.settings['MU_settings'], crossover)

            # Survivor Selection
            surivor_selection = population.survivor_selection(self.settings["SS_settings"], self.settings["FI_settings"],mutation)
            func.print_population_section(f" Generation {gen}", population.individuals)


            #animation = FuncAnimation(plt.gcf(), func.animate(surivor_selection, gen), interval=500)


        #   Plotting and Visualising Data

        x = list(range(self.settings["general"]["generation_num"]))

        # Pre-process the data

        highest_fitness_list = []
        average_fitness_list = []
        lowest_fitness_list = []

        for saved_gen in saved_population.values():

            # Higher Fitness List
            highest_fitness_list.append(max(x.fitness for x in saved_gen))

            # Average Fitness List
            average_fitness_list.append(sum(x.fitness for x in saved_gen) / len(saved_gen))

            # Lowest Fitness List
            lowest_fitness_list.append(min(x.fitness for x in saved_gen))

        # Plotting



        y_highest = highest_fitness_list
        y_average = average_fitness_list
        y_lowest = lowest_fitness_list

        plt.plot(x, y_highest, label="Highest Fitness")
        plt.plot(x, y_average, label="Average Fitness")
        plt.plot(x, y_lowest, label="Lowest Fitness")

        plt.legend()

        plt.title = "Average Fitness Over Generations"
        plt.xlabel = "Generation"
        plt.ylabel = "Fitness"

        plt.show()


        # Wipe out the file
        open("result.txt", "w").close()