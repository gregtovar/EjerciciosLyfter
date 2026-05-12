#
#   Ejercicios extra de Excepciones
#   
# 

def color_setup():
    return {
        "GREEN":      "\033[92m",
        "DARK_GREEN": "\033[32m",
        "RED":        "\033[91m",
        "YELLOW":     "\033[93m",
        "BLUE":       "\033[94m",
        "PURPLE":     "\033[95m",
        "RESET":      "\033[0m",
    }


def ask_name(colors):   # Colors agregado como parametro
    try:
        user_name = input("🔷 Ingrese su nombre: ")
        if user_name.isdigit():
            raise ValueError("El nombre no puede ser un número")
        return user_name
    except ValueError as returned_error:
        print(f"{colors['RED']}❌ Error: {returned_error}{colors['DARK_GREEN']}")
        return None


def ask_for_age(p_name, colors): # Colors agregado como parametro
    if p_name is None:
        return None
    try:
        return int(input("🫵 Ingrese su edad: "))
    except ValueError:
        print(f"{colors['RED']}❌ Error: La edad no es válida!{colors['DARK_GREEN']}")
        return None


def say_hello(name, age, colors): # Colors agregado como parametro
    if age is not None:
        print(f"\n{colors['GREEN']}🟢  Hola {name}, su edad es {age}{colors['DARK_GREEN']}")


#
# --- MAIN PROGRAM ---
#

colors = color_setup()
print(colors["DARK_GREEN"], end="")
print("\n------- OUTPUT -----------\n")
name = ask_name(colors)
age  = ask_for_age(name, colors)
say_hello(name, age, colors)
print(colors["RESET"])


#
# --- END OF MAIN PROGRAM ---
#