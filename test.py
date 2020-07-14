#Print out each element of the following array on a separate line:

x = ["Joe", "2", "Ted", "4.98", "14", "Sam", "void *", "42", "float", "pointers", "5006"]
#You may use whatever programming language you'd like.
#Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

# print(x[0])
# print(x[1])
# print(x[2])
# print(x[3])
# print(x[4])
# print(x[5])
# print(x[6])
# print(x[7])
# print(x[8])
# print(x[9])
# print(x[10])

# for i in range(len(x)):
#     print(x[i])

# print(*x, sep = "\n")

# for elem in x:
#     print(elem)



x = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

def print_list(lst):

    for i in lst:
        if type(i) != type([]):
             print(i)
        else:
              print_list(i)
print_list(x)


