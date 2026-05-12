#
# Ejercicio 7.0: 
# Cree una función que acepte una lista de números y retorne una lista con
# los números primos de la misma.
#

#
# Function Declaration
#
# First we need to know if the number is prime:
#
def is_it_prime(num_param):
    if num_param < 2:           #is N is less than 2 is not prime
        return False;  # not prime
    for i in range(2, num_param):  #if bigger than 2, then we need to iterate and try to figure it out if prime
        if num_param % i == 0:
            return False;
    return True;   # Otherwse is prime

#
#  Variables
#  
global_list_of_numeros = [1, 4, 6, 7, 13, 9, 67, 113];     # declare list
global_lenght_of_list = len(global_list_of_numeros)-1;  # calculate lenght of list

#
#  Main Program
#  
print();
print("------ OUTPUT--------"); 
print(global_list_of_numeros, "→ ", "[",end= " ");
for i, numero_index in enumerate(global_list_of_numeros):    #needs this for formating the output correctly
    if is_it_prime(numero_index):
        if i == global_lenght_of_list:        # if true - last item
            print(numero_index, "]",  end="");           # no comma is the end, added the ] also
        else:
            print(numero_index, ",", end=" ");          # not true, needs a comma is not the end yet

print();
print("------ OUTPUT--------");                     
print();
#
#  End of Main Program
#  