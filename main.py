"""
def print_dict(dictionary):
    for x in dictionary:
        print("Subdivision ID: " + str(x), end="    ")
        print("Number of trees: " + str(dictionary[x]))


def change_entry(dictionary):
    key = int(input("Please enter the id where you'd like to change the number of trees: "))
    print("The current value at " + str(key) + " is " + str(dictionary.get(key)))
    dictionary[key] = input("Please enter the new value you'd like to replace at id " + str(key) + ": ")
    print("The new value at " + str(key) + " is " + str(dictionary.get(key)))


def get_size(dictionary):
    print("There are {}".format(len(dictionary)) + " entries in this dictionary")


def add_25(dictionary):
    num_trees = 10
    for sub_id in range(25):
        dictionary[sub_id] = num_trees
        num_trees += 5


def fill_dictionary(dictionary):
    dont_stop = True
    while dont_stop:
        key = int(input("Enter the subdivision id: "))
        value = int(input("Enter the number of trees: "))

        dictionary[key] = value
        stop = input("Do you want to stop making entries? If so, Press Y, otherwise, press enter: ")
        if stop == 'y' or stop == 'Y':
            dont_stop = False

fundraiser_dict = {}

# add_25(fundraiser_dict)

fill_dictionary(fundraiser_dict)

print_dict(fundraiser_dict)

get_size(fundraiser_dict)

change_entry(fundraiser_dict)

"""

lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [00.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]


def print_info(student):
    print("Name: " + str(student["name"]))
    print("Homework: " + str(student["homework"]))
    print("Quizzes: " + str(student["quizzes"]))
    print("Tests: " + str(student["tests"]))


for x in range(3):
    print_info(students[x])
    print()


def average(numbers):
    total = sum(numbers)
    # print(total)
    items_in_list = len(numbers)
    # print(items_in_list)
    return total / items_in_list


def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    homework = homework * 0.1
    quizzes = quizzes * 0.3
    tests = tests * 0.6

    total = homework + quizzes + tests

    return total
    # print(homework)
    # print(quizzes)
    # print(tests)


print(get_average(students[0]))
