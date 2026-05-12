#
#   Ejercicios extra de Excepciones
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
    print(DARK_GREEN);   # Default Color


def ask_name():
    try:
        user_name = input("🔷 Ingrese su nombre: ")
        if user_name.isdigit():
            print(RED); 
            raise ValueError("El nombre no puede ser un número")
    except ValueError as returned_error:
        print(RED)
        print(f"❌ Error: {returned_error}");
        user_name = None
    return user_name


def ask_for_age(p_name):
    if p_name != None:
        try:
            edad = int(input(" 🫵 Ingrese su edad: "))
            return edad;
        except ValueError:
            print(RED); 
            print("❌ Error: La edad no es válida!")
            return None;


def say_hello(n1, a1):
    if a1 is not None:
        print("");
        print(f"🟢  Hola {n1}, su edad es {a1}");
        return;

#
# --- MAIN PROGRAM ---
#

color_setup();
print("");
print("------- OUTPUT -----------");
print("");
name = ask_name();           
age = ask_for_age(name);           
say_hello(name, age);

print("");
print("");
#
# --- END OF MAIN PROGRAM ---
#