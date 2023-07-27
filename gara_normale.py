import tkinter as tk

from screeninfo import get_monitors

elements = ["Verstappen",
                   "Russell",
                   "Hamilton",
                   "Ocon",
                   "Alonso",
                   "Stroll",
                   "Sainz Jr.",
                   "Albon",
                   "Hulkenberg",
                   "Magnussen",
                   "Leclerc",
                   "Norris",
                   "Gasly",
                   "Ricciardo",
                   "Tsunoda",
                   "Piastri",
                   "Yu Zhou",
                   "Sargeant",
                   "Bottas",
                   "Perez"]

elements.sort()

punteggi_da_assegnare = {0: 25, 1: 18, 2: 15, 3: 12, 4: 10, 5: 8, 6: 6, 7: 4, 8: 2, 9: 1}

app_running = True

punteggi = {}

iniziale = 0

for elemento in elements:
    punteggi[elemento] = iniziale
    
root = tk.Tk()
root.title("Selezione i piloti in ordine di arrivo alle prove: ")
    
def get_selected_values(option_menus):
    selected_values = []
    for option_menu in option_menus:
        selected_value = option_menu.var.get()
        selected_values.append(selected_value)
    return selected_values

def show_results():
    global app_running  
    results_window = tk.Toplevel(root)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    results_window.geometry(f"{screen_width}x{screen_height}")
    results_window.title("Risultati Finali")
    results_text = tk.Text(results_window, font=("Helvetica", 20))
    results_text.pack(fill=tk.BOTH, expand=True)

    for pilota, punteggio in punteggi.items():
        results_text.insert(tk.END, f"{pilota}: {punteggio}\n")

    def close_results():
        results_window.destroy()
        app_running = False
        
    results_window.protocol("WM_DELETE_WINDOW", close_results)
    
    if root.winfo_exists():
        root.withdraw()
        
        
def confirm_fp1():
    global fp1
    fp1 = get_selected_values(option_menus1)
    print("Risultati delle FP1: ")
    print(fp1)
    return(fp1)

def confirm_fp2():
    global fp2
    fp2 = get_selected_values(option_menus2)
    print("Risultati delle FP2: ")
    print(fp2)
    return(fp2)

def confirm_fp3():
    global fp3
    fp3 = get_selected_values(option_menus3)
    print("Risultati delle FP3: ")
    print(fp3)
    return(fp3)

def confirm_q():
    global q;
    q = get_selected_values(option_menus4)
    print("Risultati delle Qualifiche: ")
    print(q)
    return(q)
    
def confirm_part():
    global part;
    part = get_selected_values(option_menus5)
    print("Griglia di partenza: ")
    print(part)
    return(part)
    
def confirm_arr():
    global arr;
    arr = get_selected_values(option_menus6)
    print("Griglia di arrivo: ")
    print(arr)
    return(arr)

def confirm_all():
    
    fp1_data = confirm_fp1()
    valid_fp1_data = [pilota for pilota in fp1_data if pilota and pilota in elements]
    for pilota in valid_fp1_data:
        punteggi[pilota] += 2
    
    fp2_data = confirm_fp2()
    valid_fp2_data = [pilota for pilota in fp2_data if pilota and pilota in elements]
    for pilota in valid_fp2_data:
        punteggi[pilota] += 4
        
    fp3_data = confirm_fp3()
    valid_fp3_data = [pilota for pilota in fp3_data if pilota and pilota in elements]
    for pilota in valid_fp3_data:
        punteggi[pilota] += 6
        
    q_data = confirm_q()
    el = q_data[0]
    if el and el in elements:
        punteggi[el] += 4

    for i in range(1, 11):
        if i < len(q_data):  # Controlla che l'indice i sia valido
            el = q_data[i]
            if el and el in elements:
                punteggi[el] += 2

    for i in range(11, 16):
        if i < len(q_data):  # Controlla che l'indice i sia valido
            el = q_data[i]
            if el and el in elements:
                punteggi[el] += 1
                
    part_data = confirm_part()
    arr_data = confirm_arr()
    
    print("Partenza data:", part_data)
    print("Arrivo data:", arr_data)

    for partenza, arrivo in zip(part_data, arr_data):
        if partenza and arrivo and partenza in elements and arrivo in elements:
            indice_partenza = elements.index(partenza)
            indice_arrivo = elements.index(arrivo)

            if part_data[-1] == arr_data[-1]:
                # Calcolo punti per pilota che parte ultimo e arriva primo
                differenza_posizione = len(elements) - 1
                punteggio_pilota = 25 + 0.5 * differenza_posizione
                punteggi[arrivo] += punteggio_pilota
            else:
                differenza_posizione = abs(indice_arrivo - indice_partenza)
                punteggio_pilota = int(0.5 * differenza_posizione)
                punteggi[arrivo] += punteggio_pilota

    
    if app_running:
        show_results()

#Prove 1

frame1 = tk.Frame(master=root, width=100, bg='white', bd=2, relief='raised')
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, )

label = tk.Label(frame1, text="FP1: ")
label.grid(row=0, column=0, padx=10, pady=10)
option_menus1 = []
for i in range(1, 17):
    label = tk.Label(frame1, text=f"OptionMenu {i}")
    selected_option = tk.StringVar()
    option_menu = tk.OptionMenu(frame1, selected_option, *elements)
    option_menu.grid(row=i, column=0, padx=10, pady=1)
    option_menus1.append(option_menu)
    option_menu.var=selected_option
    
#Prove 2

frame2 = tk.Frame(master=root, width=100, bg='white', bd=2, relief='raised')
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, )

label = tk.Label(frame2, text="FP2: ")
label.grid(row=0, column=1, padx=10, pady=10)
option_menus2 = []
for i in range(1, 9):
    label = tk.Label(frame2, text=f"OptionMenu {i}")
    selected_option = tk.StringVar()
    option_menu = tk.OptionMenu(frame2, selected_option, *elements)
    option_menu.grid(row=i, column=1, padx=10, pady=1)
    option_menus2.append(option_menu)
    option_menu.var=selected_option
    
#Prove 3

frame3 = tk.Frame(master=root, width=100, bg='white', bd=2, relief='raised')
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, )

label = tk.Label(frame3, text="FP3: ")
label.grid(row=0, column=2, padx=10, pady=10)
option_menus3 = []
for i in range(1, 5):
    label = tk.Label(frame3, text=f"OptionMenu {i}")
    selected_option = tk.StringVar()
    option_menu = tk.OptionMenu(frame3, selected_option, *elements)
    option_menu.grid(row=i, column=1, padx=10, pady=1)
    option_menus3.append(option_menu)
    option_menu.var=selected_option
    
#Qualifiche

frame4 = tk.Frame(master=root, width=100, bg='white', bd=2, relief='raised')
frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, )

label = tk.Label(frame4, text="Qualifiche: ")
label.grid(row=0, column=3, padx=10, pady=10)
option_menus4 = []
for i in range(1, 16):
    label = tk.Label(frame4, text=f"OptionMenu {i}")
    selected_option = tk.StringVar()
    option_menu = tk.OptionMenu(frame4, selected_option, *elements)
    option_menu.grid(row=i, column=1, padx=10, pady=1)
    option_menus4.append(option_menu)
    option_menu.var=selected_option

#Partenza 

frame5 = tk.Frame(master=root, width=100, bg='white', bd=2, relief='raised')
frame5.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, )

label = tk.Label(frame5, text="Partenza:")
label.grid(row=0, column=4, padx=10, pady=10)
option_menus5 = []
for i in range(1, 21):
    label = tk.Label(frame5, text=f"OptionMenu {i}")
    selected_option = tk.StringVar()
    option_menu = tk.OptionMenu(frame5, selected_option, *elements)
    option_menu.grid(row=i, column=1, padx=10, pady=1)
    option_menus5.append(option_menu)
    option_menu.var=selected_option

#Arrivo

frame6 = tk.Frame(master=root, width=100, bg='white', bd=2, relief='raised')
frame6.pack(fill=tk.BOTH, side=tk.LEFT, expand=True, )

label = tk.Label(frame6, text="Arrivo:")
label.grid(row=0, column=5, padx=10, pady=10)
option_menus6 = []
for i in range(1, 21):
    label = tk.Label(frame6, text=f"OptionMenu {i}")
    selected_option = tk.StringVar()
    option_menu = tk.OptionMenu(frame6, selected_option, *elements)
    option_menu.grid(row=i, column=1, padx=10, pady=1)
    option_menus6.append(option_menu)
    option_menu.var=selected_option
    
#Bottone di conferma

button = tk.Button(frame6, text="Conferma", command=confirm_all)
button.grid(row=23, column=5, padx=10, pady=10)

#Risultati e programma main

result = tk.Label(root, text="")
result.pack()

root.mainloop()

print ("Lista piloti iniziale: ")  
print (elements)
print("Punteggi iniziali: ")
print (punteggi)
print("Risulati finali:")
print(confirm_all())