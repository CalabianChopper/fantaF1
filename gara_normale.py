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
    
#Bottone di conferma

button = tk.Button(frame1, text="Conferma", command=confirm_all)
button.grid(row=23, column=0, padx=10, pady=10)

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