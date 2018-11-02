import random
import time


f = open("filename.cnf", "r") #change this line

all_lines = []

for line in f:
    if line[0] == 'p':
        # Getting number of literals
        num_literals = int(line.split(" ")[2])
        print(num_literals)
        break

for line in f:
    if line[0] != 'p' and line[0] != 'c' and line[0]!="":
        line = line.strip("").split(" ")
        processed_line = []
        for e in line[:-1]:
            if e != "" and e != "0\n" and e != "0":
                processed_line.append(e)

        processed_line = [int(e) for e in processed_line]
        all_lines.append(processed_line)




def process_input(input_list):
    all_variables = []
    for tup in input_list:
        for e in tup:
            if e < 0:
                all_variables.append(e*-1)

            else:
                all_variables.append(e)


    return list(set(all_variables))


def initialize_dict(unique_list):
    output = dict()
    for var in unique_list:
        output[var] = -1
        output[-var] = 1

    return output

def flip_dict(dict_obj, key):
    dict_obj[key] *=-1
    dict_obj[-key] *=-1

    return dict_obj


def validate_clause(tup, dict_obj):
    sum = 0
    for e in tup:
        sum += dict_obj[e]

    if sum < 0:
        return False

    elif sum >= 0:
        return True


tries = 0


input_list = [(1, 2), (2,-1), (1, -2), (-1,-2)]
assignment = initialize_dict(process_input(input_list))

def satisfiable():
    for tup in input_list:
        # print(validate_clause(tup, assignment))
        if not validate_clause(tup, assignment):
            rand_index = random.randint(1, 2) - 1
            flip_dict(assignment, tup[rand_index])

            return False

    return True

print(input_list)

num_variables = len(process_input(input_list))
print(num_variables)
total_tries = 100 * num_variables ** 2


start = time.time()
while tries <= total_tries:

    if not satisfiable():
        tries +=1

    elif satisfiable():
        print("Satisifiable")
        print(assignment)

        break

    elif tries == total_tries:
        print("Unsatisfiable")


print("Time taken: {}".format(time.time() - start))





