def first(string):
    first_ = []
    if string in non_terminals:
        alts = productions_dict[string]
        for alt in alts:
            first1 = first(alt[0])
            if first1 not in first_:
                first_.extend(first1)
    elif string in terminals or string == "@":
        if string not in first_:
            first_.extend(string)
            return string
    return first_

noOfTerminals = int(input("Enter no. of terminals:"))
terminals = []
print("Enter Terminals:")
for _ in range(noOfTerminals):
    terminals.append(input())
noOfNonTerminals = int(input("Enter no. of non terminals:"))
non_terminals = []
print("Enter Non Terminals:")
for _ in range(noOfNonTerminals):
    non_terminals.append(input())
productions_dict = dict()
for nt in non_terminals:
    productions_dict[nt] = []
productions_dict = dict()
for nt in non_terminals:
    productions_dict[nt] = []
print("Enter Productions:")
for _ in range(len(non_terminals)):
    lhs, rhs = input().split("->")
    alts = rhs.split("/")
    for alt in alts:
        productions_dict[lhs].append(alt)

first_dict = dict()
for nt in non_terminals:
    first_dict[nt] = set(first(nt))
for k, v in first_dict.items():
    print("FIRST(" + k + ") : ", end="{ ")
    for i in v:
        print(i, end=" ")
    print("}")
