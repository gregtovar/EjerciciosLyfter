#
#  Ejercicio 4:
#  eliminar keys de un diccionario.
#

#
# Declaracion de Diccionario
#
employee = {
    'name': 'Greg',
    'email': 'greg@abc.com',
    'access': 5,
    'age' : 30
}
#
# Declaracion de lista que se usara para eliminar los keys en el dicc.
#
# 
list_of_keys = ["access", "age" ];             

print();
print('------- program output -----------');
print();
print("Dictionary BEFORE removal of keys:");
print(employee)
print();
#
# Remove values
#
del employee[list_of_keys[0]];     #remove access - positon 0
del employee[list_of_keys[1]];     #remove age - position 1
print("Dictionary AFTER removal of keys:");
print(employee);
print();
print('------- end of program -----------');

