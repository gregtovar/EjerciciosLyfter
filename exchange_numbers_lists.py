#
# App: Print String backwards
#

#
# Variables
#

# Lists
my_list = [4, 3, 6, 1, 7];
swapped_list = [1,1,1,1,1];  # the new list will be stored here, dummy values = "1"
i = 0;

#
# Logic
#
print();
print("---- Program Output ---------");
print();
print(f"Original list: {my_list}")

print(my_list[-1]);
print(my_list[-3]);
print(my_list[0]);
print(my_list[1]);

swapped_list[0] = my_list[-1];
swapped_list[-1] = my_list[0];
print(f"Swapped list:  {swapped_list}");
print();
print("---- End ---------");
print("--------------------------");
#
# End of program
#