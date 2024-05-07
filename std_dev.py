# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 05/07/2024
# Description: Program that returns the standard deviation for all of the ages in a defined class. 

class Person:
    def __init__(self, name, age):
        '''Defines Person Attributes name and age'''
        self.__name = name
        self.__age = age

    def get_age(self):
        '''Returns the age of the person.'''
        return self.__age

def std_dev(person_list):
    '''Calculates the population standard deviation of ages in a list of Person objects. If the list is empty, returns None.'''
    if not person_list:
        return None
    
    n = len(person_list)
    total_age = sum(person.get_age() for person in person_list)
    mean_age = total_age / n
    
    sum_of_squares = sum((person.get_age() - mean_age) ** 2 for person in person_list)
    
    variance = sum_of_squares / n
    standard_deviation = variance ** 0.5
    return standard_deviation

# p1 = Person("Kyoungmin", 73)
# p2 = Person("Mercedes", 24)
# p3 = Person("Beatrice", 48)
# person_list = [p1, p2, p3]
# answer = std_dev(person_list)
# print(answer)
