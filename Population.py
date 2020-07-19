import random
import csv
import copy

from Individual import Individual
from GA_Operations import Operations


class Population:

    def __init__(self):

        self.individuals = []
        self.operations = Operations()


###     Creating Population Methods     ###

    def create_csv_population(self):

        with open("PopulationDatasets/Pop1.csv", "w") as file:

            file_writer = csv.writer(file, delimiter=",")


    def set_csv_population(self, file):
        pass


    def random_populate(self, settings):


        id = 0

        population_size = settings["general"]["population_size"]
        which_function = settings["FI_settings"]["function_type"]
        chromosome_size = settings["FI_settings"][f"function_{which_function}"]["chromosome_size"]

        for person in range(population_size):
            chromosome = []

            # Depending on function there are different encodings
            if which_function in [1,2]:

                #   Binary Encoding
                chromosome = random.choices([0, 1], k=chromosome_size)

            elif which_function in [3]:

                #   Real Number Encoding
                for x in range(chromosome_size):
                    gene = round(random.uniform(settings["CR_settings"]["lower_range"], settings["CR_settings"]["higher_range"]), 2)
                    chromosome.append(gene)

            else:
                print("Error: at random_populate method in Population file")
                exit()

            # Create Individual and add to list
            self.individuals.append(Individual(id,chromosome))

            id += 1



 ###    Genetic Algorithm Operation Calls   ###

    def update_fitness(self, FI_settings):

        for person in self.individuals:
            person.update_fitness(FI_settings)


    def parent_selection(self, PS_settings):

        if PS_settings["method"].upper() in PS_settings["available_methods"]:

            # Using String of selected method to call method in Operations object
            parents = getattr(self.operations, "PS_" + PS_settings["method"].upper()) (PS_settings, self.individuals)

            return parents

        else:
            print("PARENT SELECTION - Check Selected Method in PS_settings")
            exit()

    def crossover(self, CR_settings, parents):

        if CR_settings["method"].upper() in CR_settings["available_methods"]:

            # Using String of selected method to call method in Operations object
            crossover = getattr(self.operations, "CR_" + CR_settings["method"].upper()) (CR_settings, parents)

            return crossover

        else:
            print("CROSSOVER - Check Selected Method in CR_settings")
            exit()

    def mutation(self, MU_settings, crossover):

        if MU_settings["method"].upper() in MU_settings["available_methods"]:

            # Using String of selected method to call method in Operations object
            mutation = getattr(self.operations, "MU_" + MU_settings["method"].upper()) (MU_settings, crossover)

            return mutation

        else:
            print("MUTATION - Check Selected Method in PS_settings")
            exit()

    def survivor_selection(self, SS_settings, FI_settings, mutation):

        if SS_settings["method"].upper() in SS_settings["available_methods"]:

            # Update fitness
            for person in mutation:
                person.update_fitness(FI_settings)

            # Using String of selected method to call method in Operations object
            survivor_selection = getattr(self.operations, "SS_" + SS_settings["method"].upper()) (SS_settings, mutation, self.individuals)


            # Replaces old population with current
            self.individuals = copy.deepcopy(survivor_selection)

            return survivor_selection

        else:
            print("SURVIVOR SELECTION - Check Selected Method in SS_settings")
            exit()
