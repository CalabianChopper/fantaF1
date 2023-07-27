import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk
    
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

punteggi = {}

iniziale = 0

for elemento in elements:
    punteggi[elemento] = iniziale

print ("Lista piloti iniziale: ")  
print (elements)
print("Punteggi iniziali: ")
print (punteggi)

def get_selected_values(option_menus):
    selected_values = []
    for option_menu in option_menus:
        selected_value = option_menu.var.get()
        selected_values.append(selected_value)
    return selected_values

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
    
# def confirm_q():
#     global q;
#     q = get_selected_values(option_menus4)
#     print("Risultati delle Qualifiche: ")
#     print(q)
#     return(q)
    
# def confirm_part():
#     global part;
#     part = get_selected_values(option_menus5)
#     print("Griglia di partenza: ")
#     print(part)
#     return(part)
    
# def confirm_arr():
#     global arr;
#     arr = get_selected_values(option_menus6)
#     print("Griglia di arrivo: ")
#     print(arr)
#     return(arr)
    
def confirm_all():
    fp1_data = confirm_fp1()
    fp2_data = confirm_fp2()
    fp3_data = confirm_fp3()
    #q_data = confirm_q()
    #part_data = confirm_part()
    #arr_data = confirm_arr()
    
    for i in range(0, 16):
        el = fp1_data[i]
        if el:
            punteggi[el] += 2
            
    for i in range(0, 8):
        el = fp2_data[i]
        if el:
            punteggi[el] += 4
            
    for i in range(0, 4):
        el = fp3_data[i]
        if el:
            punteggi[el] += 6
            
    # el = q_data[0]
    # if el:
    #     punteggi[el] += 4
        
    # for i in range(1, 11):
    #     el = q_data[i]
    #     if el:
    #         punteggi[el] += 2
            
    # for i in range(11, 16):
    #     el = q_data[i]
    #     if el:
    #         punteggi[el] += 1
            
    # for i in range(0, 10):
    #     if i == 0:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 25
    #     elif i == 1:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 18
    #     elif i == 2:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 15
    #     elif i == 3:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 12
    #     elif i == 4:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 10
    #     elif i == 5:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 8 
    #     elif i == 6:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 6   
    #     elif i == 7:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 4  
    #     elif i == 8:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 2   
    #     elif i == 9:
    #         el = arr_data[i]
    #         if el:
    #             punteggi[el] += 1 
                
    # for partenza, arrivo in zip(part_data, arr_data):
    #     indice_partenza = elements.index(partenza)
    #     indice_arrivo = elements.index(arrivo)
    #     differenza_posizione = indice_arrivo - indice_partenza
    #     punteggio_pilota = 0.5 * differenza_posizione
    #     punteggi[arrivo] += punteggio_pilota  
    
    return punteggi
    print("Risultati finali: ")
    print(punteggi)
        
    


root = tk.Tk()
root.title("Selezione i piloti in ordine di arrivo alle prove: ")

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
