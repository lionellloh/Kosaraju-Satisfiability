import time

from libKosaraju import Graph as Graph_two
from geeks import Graph

f = open("2sat.cnf", "r")

all_lines = []

for line in f:
    if line[0] == 'p':
        # Getting number of literals
        num_literals = int(line.split(" ")[2])
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

start = time.time()
y = Graph_two(num_literals*2)

vertices_list = []
for i in range(1, num_literals+1):
    vertices_list.append(i)
    vertices_list.append(-i)

map = {}

value = 0
for vertex in vertices_list:
    map[vertex]= value
    value+=1



reverse_map = {v:k for k,v in map.items()}



for clause in all_lines:
    if len(clause)!= 2:
        continue

    y.join(map[-clause[0]], map[clause[1]])
    y.join(map[-clause[1]], map[clause[0]])

list_of_SCCs = (y.returnSCCs())

# Transform based on the reverse map
transformed_list = []
for list_SCC in list_of_SCCs:
    add_list = [reverse_map[i] for i in list_SCC]
    transformed_list.append(add_list)



def satisfiable(transformed_list):

    for scc in transformed_list:
        for i in scc:
            if -i in scc:
                return False

    biggest_scc = sorted(transformed_list, key = lambda k: len(k))[0]
    return sorted(biggest_scc, key = lambda k: max(k, -k))


if satisfiable(transformed_list):
    biggest_scc = satisfiable(transformed_list)
    output = ""
    for e in biggest_scc:
        if e < 0:
            output += "0"
        elif e > 0:
            output += "1"

        output+=" "

    print("Satisfiable!")
    print(output)

else: 
    print("Unsatisifable!")

print("Time taken:", time.time() - start)
