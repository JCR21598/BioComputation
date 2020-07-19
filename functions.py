
import decorators as dec
from operator import attrgetter



""" ### General Functions ### """


def find_PS_maximum(set):

    # Set the first individual as the highest
    temp_highest = set[0]

    for individual in set:

        if individual.fitness > temp_highest.fitness:

            temp_highest = individual

    return temp_highest


def find_PS_minimum(set):

    # Set the first individual as the highest
    temp_lowest = set[0]

    for individual in set:

        if individual.fitness < temp_lowest.fitness:
            temp_lowest = individual

    return temp_lowest


def restrict_ranges(n, minn, maxn):
    return max(min(maxn, n), minn)


@dec.simple_divider
def mutation_swap(choices, pos1, pos2):

    temp_ch1 = choices[0]
    temp_ch2 = choices[1]

    print("Choice 1 - ID {0}: {1}             fitness: {2}\n"
          "Choice 2 - ID {3}: {4}             fitness: {5}\n"        
          "Split at index: {6}\n\n".
          format(temp_ch1.id, temp_ch1.chromosome, temp_ch1.fitness, temp_ch2.id, temp_ch2.chromosome, temp_ch2.fitness, pos1))

    ch1_split1 = temp_ch1.chromosome[pos1 : pos2]
    ch2_split2 = temp_ch2.chromosome[pos1 : pos2]

    print("split1: {0}"
          "\nsplit2: {1}\n\n".
          format(ch1_split1, ch2_split2))

    temp_ch1.chromosome[pos1 : pos2] = ch2_split2
    temp_ch2.chromosome[pos1: pos2] = ch1_split1

    print("OffSpring 1: {0}\n"
          "OffSpring 2: {1}\n".
          format(temp_ch1.chromosome, temp_ch2.chromosome))

    return [temp_ch1, temp_ch2]


def new_id(group):
    obj = max(group, key=attrgetter('id'))
    print(obj.id)
    return






""" ### Visualisation of data ### """

#   Printing for Population section

def print_divisor():
    print("_" * 100)


@dec.section_divider
def print_population_section(section, group):

    print(f"\nIndividuals in {section} \n\n")

    for person in group:

        print("Individual {}\n"
              "chromosome: {}\n"
              "fitness: {}\n".
              format(person.id, person.chromosome, person.fitness))


@dec.section_divider
def print_population_comparison(group1, group2, message):

    if message:
        print(message)

    print()


def print_individual(person, message):

    if message:
        print(message)

    print("Individual {}\n"
          "chromosome: {}\n"
          "fitness: {}\n".
          format(person.id, person.chromosome, person.fitness))




#   Printing for Parent Selection
@dec.section_divider
def print_PS_section(self):
    pass


#   Printing for Crossover Section
@dec.section_divider
def print_CR_section(self):
    pass


#   Printing for Mutation Section
@dec.section_divider
def print_MU_section(self):
    pass


#   Printing for Survivor Selection
@dec.section_divider
def print_SS_section(self):
    pass




# Matlibplot Functions

def animate(population, gen_number):

    x_values.append(population.individuals.fitness)
    y_values.append(gen_number)

    plt.plot(x_valies)






















