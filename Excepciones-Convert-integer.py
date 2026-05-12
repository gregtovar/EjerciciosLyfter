#
#   Ejercicios extra de Excepciones:
#   Convertir a Entero
#   
# 

def color_setup():
    global GREEN;  
    global RED;
    global YELLOW;
    global DARK_GREEN;
    global BLUE;
    global PURPLE;
    global RESET;
    GREEN = "\033[92m";
    DARK_GREEN  = "\033[32m";    
    RED    = "\033[91m";
    YELLOW = "\033[93m";
    BLUE   = "\033[94m";
    PURPLE = "\033[95m";
    RESET  = "\033[0m";
    print(DARK_GREEN, end="");  # Default Color

def ask_for_list():
    print("Ingrese los valores separados por coma 🐖");
    print("Ejemplo: 4, hola, 10, 5.2")
    
    while True:
        list_input = input("🔷 Ingrese su lista: ")
        
        if "," not in list_input:
            print(RED,end="");
            print("❌ Error: Debe separar los valores con comas. Intente de nuevo.")
            print(DARK_GREEN,end="");
            continue
        
        local_list = list_input.split(",")
        local_list = [element.strip() for element in local_list]
        
        if len(local_list) < 2:
            print(YELLOW, end="");
            print("❌ Error: Debe ingresar al menos 2 valores. Intente de nuevo.")
            print(DARK_GREEN, end="");
            continue
        
        return local_list;



def convert_integer(p_list):
    counter = 0;
    print("--------- OUTPUT ----------")
    for element in p_list:
        counter +=1;
        try:
            num = int(element);
            print("Posicion",counter,f'- "{element}" convertido a {num}');
        except ValueError:
            print(YELLOW, end="");
            if element == "":
                print("Posicion",counter,f"- No se pudo convertir el elemento ESPACIO");
                print(DARK_GREEN, end="");
            else:    
                print("Posicion",counter,f"- No se pudo convertir el elemento: {element}");
                print(DARK_GREEN, end="");

#
# --- MAIN PROGRAM ---
#

color_setup();
my_list = ask_for_list();
convert_integer(my_list);
print();
print();


#
# --- END MAIN PROGRAM ---
#
