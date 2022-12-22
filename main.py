import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Reaading from a file all the subject information and credit information
fopen = open('courses.txt')
f = fopen.read().split("\n")
fread = []
for i in f :
    fread.append(i.split(","))

# Creating the main window of the GUI
window = tk.Tk()
window.geometry('400x200')
window.title('CGPA Calculator')

t = tk.IntVar()
grades = ["O", "A+", "A", "B+", "B", "RA", "SA"]

# Function to convert grade input into grade points
def grade(n) :
    if n == 'O' :
        return 10
    elif n == 'A+' :
        return 9
    elif n == 'A' :
        return 8
    elif n == 'B+' :
        return 7
    elif n == 'B' :
        return 6
    elif n == 'RA' :
        return 0
    elif n == 'SA' :
        return 0
    else :
        return -1

# Function to be invoked when the semester is entered
def sem_get() :
    global ent_sem, fread
    sem = t.get()
    print(sem)

    subs = []
    if sem <= 10 and sem >= 1 :
        for i in fread :
            if i[0] == str(sem) :
                subs.append(i)
        print(subs)

        s = ['s{}'.format(i) for i in range(len(subs))]

        for i in range(len(subs)) :
            s[i] = tk.StringVar()

        def dis_cgpa() :
            sum = 0
            cre_sum = 0
            flag = False
            for i in range(len(subs)) :
                g = s[i].get()

                if g == "" :
                    flag = True

                sum += grade(g)*int(subs[i][2])
                cre_sum += int(subs[i][2])

            if flag :
                dan = messagebox.showwarning("Invalid Input", "Please select some values for grades")
            else :
                cgpa = sum / cre_sum
                cgpa_txt = "CGPA     :    " + str(float(f'{cgpa:.3f}'))

                bck = tk.Label(height = 30, width = 30).place(x = 18, y = len(subs)*40 + 238)
                res = tk.Label(text = cgpa_txt, font = ('Cambria', 14)).place(x = 20, y = len(subs)*40 + 240)

        window.geometry('400x{}'.format(300 + len(subs)*40))
        back = tk.Label(height = len(subs)*50, width = 390).place(x = 10, y = 180)
        ent_grd = tk.Label(text = "Enter the Grades obtained in each Subject : ", font = ('Cambria', 14)).place(x = 20, y = 180)

        for i in range(len(subs)) :
            exec('l{} = tk.Label(text = "{}", font = ("Arial", 10)).place(x = {}, y = {})'.format(i, subs[i][1], 20, i*40 + 230))
            exec('e{} = ttk.Combobox(width = 10, textvariable = s[{}])'.format(i, i))
            exec('e{}.place(x = {}, y = {})'.format(i, 300, i*40 + 230))
            exec("e{}['values'] = grades".format(i))
            sumbit = tk.Button(text = "Get CGPA", height = 2, width = 16, command = dis_cgpa).place(x = 260, y = 230 + len(subs)*40)


    else :
        messagebox.showwarning("Invalid Input", "The number you have entered is not valid !!")

tit = tk.Label(text = 'CGPA Calculator', font = ('Cambria', 28)).place(x = 70, y = 30)
lab_sem = tk.Label(text = "Enter the semester : ", font = ('Cambria', 14)).place(x = 20, y = 120)
ent_sem = tk.Entry(textvariable = t).place(x = 195, y = 127)
but_sem = tk.Button(text = "Next", command = sem_get).place(x = 335, y = 123)

window.resizable(0, 0)
window.mainloop()
