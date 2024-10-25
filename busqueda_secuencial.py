import tkinter as tk
from tkinter import messagebox

def sequential_search(arr, target):
    result = ""
    comparison_count = 0
    
    # Búsqueda secuencial en el arreglo
    for i in range(len(arr)):
        comparison_count += 1
        result += f"\n¿Es {arr[i]} igual que {target}?\n"
        if arr[i] == target:
            result += f"Si, y está en la posición {i}.\nComparación {comparison_count}\n"
            return result
        else:
            result += f"No, {arr[i]} diferente que {target}. \nComparación {comparison_count}\n"
    
    result += f"Elemento no encontrado.\nTotal de comparaciones: {comparison_count}\n"
    return result

def create_arr(elements_list):
    arr = [int(x) for x in elements_list.split(',')]
    return arr

def search(ascending=True):
    elements_list = entry_elements.get()
    target = int(entry_target.get())

    arr = create_arr(elements_list)
    if not ascending:
        arr = arr[::-1]
    
    result = sequential_search(arr, target)
    
    text_result.delete(1.0, tk.END)
    text_result.insert(tk.END, result)

def open_main_window():
    splash_screen.destroy()
    
    global root
    root = tk.Tk()
    root.title("Sequential Search")
    root.attributes('-fullscreen', True)

    tk.Label(root, text="Ingrese los elementos del arreglo separados por comas:", font=("Helvetica", 24)).pack(pady=20)
    global entry_elements
    entry_elements = tk.Entry(root, width=60, font=("Helvetica", 24))
    entry_elements.pack(pady=20)

    tk.Label(root, text="\nIngrese el elemento a buscar:", font=("Helvetica", 24)).pack(pady=20)
    global entry_target
    entry_target = tk.Entry(root, width=10, font=("Helvetica", 24))
    entry_target.pack(pady=20)

    btn_search_asc = tk.Button(root, text="Buscar Ascendente", font=("Helvetica", 24), command=lambda: search(True))
    btn_search_asc.pack(pady=20)

    btn_search_desc = tk.Button(root, text="Buscar Descendente", font=("Helvetica", 24), command=lambda: search(False))
    btn_search_desc.pack(pady=20)

    global text_result
    text_result = tk.Text(root, height=20, width=80, font=("Helvetica", 24))
    text_result.pack(pady=20)

    root.mainloop()

# Create the splash screen
splash_screen = tk.Tk()
splash_screen.title("Bienvenido")
splash_screen.attributes('-fullscreen', True)

# Add explanation and team members
tk.Label(splash_screen, text="Método de Búsqueda Secuencial", font=("Helvetica", 36)).pack(pady=40)
tk.Label(splash_screen, text="Este método busca un elemento en un arreglo comparando cada elemento secuencialmente hasta encontrar el objetivo.", wraplength=800, font=("Helvetica", 24)).pack(pady=40)
tk.Label(splash_screen, text="Integrantes del equipo:", font=("Helvetica", 30)).pack(pady=40)
tk.Label(splash_screen, text="1. Danna Negron\n2. Hugo Patiño\n3. Sebastian Rios", font=("Helvetica", 24)).pack(pady=40)

# Add button to proceed to the main window
btn_proceed = tk.Button(splash_screen, text="Continuar", font=("Helvetica", 24), command=open_main_window)
btn_proceed.pack(pady=40)

# Run the splash screen
splash_screen.mainloop()