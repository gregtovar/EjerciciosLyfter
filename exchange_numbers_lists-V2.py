#
# App: Print String backwards V2

#
# Variables
#
my_list = [4, 3, 6, 1, 7];
swap_list = [];  
i = 0;
start = -1;
stop = 0;
step = -1;
length_list = 0;
#
# Logic
#
length_list = len(my_list);
length_list = length_list -1;
print();
print("---- Program Output ---------");
print();
for i in range(length_list, start, step):
    swap_list.append(my_list[i])
print(f"Original list: {my_list}")
print(f"Inverted list: {swap_list}")
print();
print("------------ End ---------");
print("--------------------------");

#
# End of program
#