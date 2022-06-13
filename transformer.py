from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# =========== main window==========
root = Tk()
root.title("TRANSFORMER WINDINGS")
root.iconbitmap('icon\icon.ico')
root.geometry("830x395")
root.configure(background='white')
# root.resizable(0, 0)
# ==================================
# ============frames in main window============
f = Frame(root)
f.configure(background='yellow', height=50, width=830)
f.place(x=0, y=0)
frame1 = Frame(root)
frame1.configure(background='black', height=325, width=415)
frame1.place(x=0, y=50)
frame2 = Frame(root)
frame2.configure(background='light green', height=50, width=415)
frame2.place(x=415, y=50)
frame3 = Frame(root)
frame3.configure(background='powder blue', padx=1, height=50, width=415)
frame3.place(x=415, y=325)
display_frame = Frame(frame2)
# ===================================

# ========Scrollbar===============
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
# =================================

# ========== Variables ===========
secondary_volatages = [6, 12, 14, 18, 24, 36, 48]
viet_nums = ['Iron Core Trans.', 'Ferrite Core Trans.', 'Toroidal Trans.']
frequency_hz = IntVar()
country_VOLT = IntVar()
length = DoubleVar()
breath = DoubleVar()
secondary = IntVar()
secondary_volt = IntVar()
ticked_box = IntVar()
constant_value = 42
viet = StringVar()
# =================================

# ========= functions ==============


def parameter_check():
    if ticked_box.get() == 1:
        pass
    elif ticked_box.get() == 0:
        messagebox.askquestion('SOME PARAMETERS ARE MISING',
                               'ARE YOU SURE THAT ALL FIELDS ARE CHECKED?')


def all_set():
    if ticked_box.get() == 0:
        messagebox.showerror('CHECK BOX NOT CHECKED',
                             'PLEASE ALL ENTRY BOXES ARE REQUIRED')
    elif length.get() == 0 or breath.get() == 0 or ticked_box.get == 0:
        messagebox.showerror('CHECK BOXEX NOT SELECTED',
                             'PRODUCE THE REQUIREMENTS')
    else:
        btn1.configure(state=NORMAL)


def select():
    if frequency_hz.get() == 1 and country_VOLT.get() == 3:
        frequency = 60
        voltage = 110
    elif frequency_hz.get() == 2 and country_VOLT.get() == 4:
        frequency = 50
        voltage = 220


def reset():
    if frequency_hz.get() != 0 or country_VOLT != 0 or length.get() != 0 or breath.get() != 0 or ticked_box.get() != 0 or secondary_volt.get():
        frequency_hz.set(value=0)
        country_VOLT.set(value=0)
        length.set(value=0.0)
        breath.set(value=0.0)
        ticked_box.set(value=0)
        combo.set(value=0)
        frma1_lbl3.destroy()
        btn1.configure(state=DISABLED)


def our_command():
    pass

# ==============================================

# =============Main calculation================


def turns_calculator():
    core_and_area = (length.get()*breath.get())
    turns_per_volt = (constant_value/core_and_area)
    if frequency_hz.get() == 1 and country_VOLT.get() == 3:
        frequency = 60
        voltage = 110
    elif frequency_hz.get() == 2 and country_VOLT.get() == 4:
        frequency = 50
        voltage = 220
    primary_windings = voltage*turns_per_volt
    secondary_winding = (secondary_volt.get()*turns_per_volt)
    frma1_lbl3.configure(text=(f'''
    {(primary_windings.__ceil__())} turns 
    is required for the primary windings
    {(secondary_winding.__ceil__())} turns 
    is required for the secondary windings'''), font=(
        'airial', 12, 'bold'), width=34, height=12, foreground='white')
    frma1_lbl3.place(x=30, y=59)
# ==============================================


# ==============f frame label==================
f_lab = Label(f, text='', background="RED",
              font=('airial', 10, 'bold'))
# =============================================

# =============frame1 label===================
frame1_lbl = Label(frame1, fg='white', background='black', text='Form Work Length(L)', width=18, height=1, foreground='white',
                   font=('airial', 15, 'bold'))
frame1_lbl.place(x=0, y=0)
frame1_entry = Entry(frame1, width=10, textvariable=length,
                     font=('airial', 15, 'bold'))
frame1_entry.place(x=220, y=0)

frame1_lbl2 = Label(frame1, fg='white', background='black', text='Form Work Width(W)', width=18, height=1, foreground='white',
                    font=('airial', 15, 'bold'))
frame1_lbl2.place(x=0, y=30)
frame1_entry2 = Entry(frame1, width=10, textvariable=breath,
                      font=('airial', 15, 'bold'))
frame1_entry2.place(x=220, y=30)
frma1_lbl3 = Label(frame1, background='black')

# ==============================================
# ================== Menus ======================
my_menu = Menu(root)
root.config(menu=my_menu)
# Menu item
file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label='New', command=lambda: our_command())
file_menu.add_command(label='Exit', command=lambda: quit())
file_menu.add_command(label='Exit', command=lambda: quit())


# ==============================================
# =============Radio Buttons===================
f2_label_60hz = Radiobutton(frame2, cursor='hand2', command=lambda: select(), variable=frequency_hz, value=1, text=('60Hz'), font=(
    'airial', 10, 'bold'), background='light green')
f2_label_60hz.place(x=1, y=1)
f2_label_50hz = Radiobutton(frame2, cursor='hand2', command=lambda: select(), variable=frequency_hz, value=2, text=('50Hz'), font=(
    'airial', 10, 'bold'), background='light green')
f2_label_50hz.place(x=1, y=20)
f_lab.place(x=0, y=0)
f2_country_110V = Radiobutton(frame2, cursor='hand2', command=lambda: select(), variable=country_VOLT, value=3, text=('110V'), font=(
    'airial', 10, 'bold'), background='light green')
f2_country_110V.place(x=340, y=1)
f2_country_220V = Radiobutton(frame2, cursor='hand2', command=lambda: select(), variable=country_VOLT, value=4, text=('220V'), font=(
    'airial', 10, 'bold'), background='light green')
f2_country_220V.place(x=340, y=20)
# ====================================

# =========combobox==================
combo = ttk.Combobox(frame2, background='white',
                     values=(secondary_volatages), cursor='hand2', textvariable=secondary_volt, width=10)
combo.place(x=60, y=10)
combo2 = ttk.Combobox(frame2, background='white', textvariable=viet, values=(
    viet_nums), cursor='hand2', width=10)
combo2.place(x=220, y=10)
# ===================================

# ==========Check boxes==============
check_box = ttk.Checkbutton(frame2, text='AREA',
                            variable=ticked_box, cursor="hand2", command=lambda: parameter_check())
check_box.place(x=160, y=10)
# ===================================

# ===========Buttons==================
btn1 = Button(frame3, state=DISABLED, cursor='hand2', command=lambda: turns_calculator(), background='powder blue', text=(
    'CALCULATE'), font=('airial', 15, 'bold'), height=1, width=10)
btn1.place(x=2, y=5)
btn2 = Button(frame3, cursor='hand2', command=lambda: reset(), background='powder blue', text=('CLEAR'),
              font=('airial', 15, 'bold'), height=1, width=10)
btn2.place(x=139, y=5)
btn3 = Button(frame3, cursor='hand2', command=lambda: all_set(), background='powder blue', text=('INSERT'),
              font=('airial', 15, 'bold'), height=1, width=9)
btn3.place(x=276, y=5)
# ====================================

root.mainloop()
