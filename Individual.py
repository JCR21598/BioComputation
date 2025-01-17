import math
import sympy
import random as rand

class Individual:

    def __init__(self, id, chromosome):

        self.id = id
        self.chromosome = chromosome
        self.fitness = 0


    def update_fitness(self, FI_settings):

        if FI_settings["function_type"] in FI_settings["available_fitness_functions"]:

            #   Function 0

            if FI_settings["function_type"] is 0 :
                self.fitness = sum([2 ** i for i, gene in enumerate(reversed(self.chromosome)) if gene == 1])



            #   Function 1

            elif FI_settings["function_type"] is 1:

                if len(self.chromosome) is not 8:
                    print("Incorrect amount of chromosomes, should be 8")
                    exit()

                #   Domain
                x_domain = sum([2 ** i for i, gene in enumerate(self.chromosome) if gene == 1])

                # fitness function
                x = x_domain ** 2

                #   Fitness Function
                self.fitness = x



            #   Function 2

            elif FI_settings["function_type"] is 2 :

                if len(self.chromosome) is not 10:
                    print("Incorrect amount of chromosomes, should be 5")
                    exit()

                # Chromosome and what each index mean:
                #
                #   Index:
                #       0 - 3   =>  x value
                #       4       =>  if x is positive or negative
                #
                #       5 - 8   =>  y value
                #       9       =>  if y is positive or negative

                #   Getting each index

                #   For x
                x_value = self.chromosome[0:4]
                x_sign = self.chromosome[4]

                #   For y
                y_value = self.chromosome[5:9]
                y_sign = self.chromosome[9]

                # Positive and negative summation

                #   For x
                x_sum = sum([2 ** i for i, gene in enumerate(x_value) if gene == 1])

                if x_sign is 1:
                    x_sum = - x_sum

                #   For y
                y_sum = sum([2 ** i for i, gene in enumerate(y_value) if gene == 1])

                if y_sign is 1:
                    y_sum = - y_sum

                #   Fitness Function#

                x_squared = math.pow(x_sum, 2)
                y_squared = math.pow(y_sum, 2)
                #print(f"\nsquared: {x_squared, y_squared}")

                first_eq = x_squared + y_squared
                #print(f"x^2 + y^2: {first_eq}")

                second_eq = 0.26 * first_eq
                #print(f"0.26 * first_eq: {second_eq}")

                third_eq = -0.48 * x_sum * y_sum
               # print(f"-0.48 * x * y: {third_eq}")

                self.fitness = second_eq + third_eq

                #print(self.fitness)
                #print(self.chromosome)

            #   Function 3

            elif FI_settings["function_type"] is 3:

                equation_results = []

                print(self.chromosome)

                for gene in self.chromosome:

                    #   x^2
                    first_eq = math.pow(gene, 2)
                    #print(first_eq)

                    # 2 * Pi * x
                    second_eq = 2 * math.pi * gene
                    #print(second_eq)

                    # cos(2 * Pi * x)
                    third_eq = math.cos(math.radians(second_eq))
                    #print(third_eq)

                    # -10 * cos(2 * Pi * x)
                    fourth_eq = -10 * third_eq
                    #print(fourth_eq)

                    # x^2 + (-10) * cos(2 * Pi * x)
                    fifth_eq = first_eq + fourth_eq
                    #print(fifth_eq)

                    # Each equation results
                    equation_results.append(fifth_eq)

                # Sum all the equation results
                sigma_equation_sum = sum(equation_results)

                starting_eq = 10 * len(self.chromosome)

                self.fitness = starting_eq + sigma_equation_sum

            else:
                print("Something went wrong in fitness function")
        else:
            print("Function type is not acceptable")