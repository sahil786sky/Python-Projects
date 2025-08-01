import tkinter as tk
from tkinter import Frame, IntVar, StringVar,Text
import time,os

root = tk.Tk()
root.geometry('900x750+200+10')
root.title('Bill Calculator')


#Heading
main_name = tk.Label(text='Hotel Management',font=("Arial Rounded",23, "bold"),fg='#1A237E')
main_name.place(x=80,y=20)

#Item Menu
menu_bg = Frame(root, bg="#a2c8f2", width=350, height=490)
menu_bg.place(x=30,y=100)
menu_name = tk.Label(menu_bg,text='Item and Quantity',bg='#a2c8f2',font=("Arial Rounded",17))
menu_name.place(x=80,y=10)

#Menu List and Quantity
menu_item1 = tk.Label(menu_bg,text='Drink',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item1.place(x=10,y=60)
menu1_store = StringVar()
menu_entry1 = tk.Entry(menu_bg,textvariable=menu1_store)
menu_entry1.place(x=150,y=65)

menu_item2 = tk.Label(menu_bg,text='Burger King',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item2.place(x=10,y=110)
menu2_store = StringVar()
menu_entry2 = tk.Entry(menu_bg,textvariable=menu2_store)
menu_entry2.place(x=150,y=115)

menu_item3 = tk.Label(menu_bg,text='Cherry',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item3.place(x=10,y=160)
menu3_store = StringVar()
menu_entry3 = tk.Entry(menu_bg,textvariable=menu3_store)
menu_entry3.place(x=150,y=165)

menu_item4 = tk.Label(menu_bg,text='Nacho Fries',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item4.place(x=10,y=210)
menu4_store = StringVar()
menu_entry4 = tk.Entry(menu_bg,textvariable=menu4_store)
menu_entry4.place(x=150,y=215)

menu_item5 = tk.Label(menu_bg,text='Pizza',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item5.place(x=10,y=260)
menu5_store = StringVar()
menu_entry5 = tk.Entry(menu_bg,textvariable=menu5_store)
menu_entry5.place(x=150,y=265)

menu_item6 = tk.Label(menu_bg,text='Biscuit',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item6.place(x=10,y=310)
menu6_store = StringVar()
menu_entry6 = tk.Entry(menu_bg,textvariable=menu6_store)
menu_entry6.place(x=150,y=315)

menu_item7 = tk.Label(menu_bg,text='Roll',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item7.place(x=10,y=360)
menu7_store = StringVar()
menu_entry7 = tk.Entry(menu_bg,textvariable=menu7_store)
menu_entry7.place(x=150,y=365)

menu_item8 = tk.Label(menu_bg,text='Tea',bg='#a2c8f2',font=("Arial Rounded",15))
menu_item8.place(x=10,y=410)
menu8_store = StringVar()
menu_entry8 = tk.Entry(menu_bg,textvariable=menu8_store)
menu_entry8.place(x=150,y=415)

# order calculation logic
item_quantity = {'Drink':menu1_store,'Burger King':menu2_store,'Cherry':menu3_store,'Nacho Fries':menu4_store,'Pizza':menu5_store,'Biscuit':menu6_store,
                 'Roll':menu7_store,'Tea':menu8_store}
price_items = {'Drink':15,'Burger King':80,'Cherry':30,'Nacho Fries':50,'Pizza':110,'Biscuit':10,'Roll':60,'Tea':10}

total_var = tk.StringVar()
total_cost = tk.StringVar()
total_var.set('')
total_cost.set('')
def price_calc():
    total = 0
    for i in item_quantity:
        try:
            quantity = int(item_quantity[i].get())
        except:
            quantity = 0
        price  = price_items[i]
        total += quantity * price
        total_var.set(f"Cost                                                 {total}")
        service_cost = 6.75
        taxes = 45
        total_costs = total + service_cost + taxes
        total_cost.set(f"Total                                                {total_costs:.2f}")
        service_cst.place(x=50, y=200)
        Tax_cst.place(x=50, y=250)
    order_num = get_order_number()
    order_label.config(text=f"Order Number                                  {order_num}")
    save_order_number(order_num + 1)
    return total

#New Frame for Order Summary and button for total price
order_summ = tk.Frame(root, bg="#a694df", width=470, height=490)
order_summ.place(x=400,y=100)
order_name = tk.Label(order_summ,text='Order Summary',bg='#a694df',font=("Arial Rounded",17))
order_name.place(x=150,y=10)
price_display = tk.Label(order_summ,textvariable=total_var,bg="#a694df",font=("Arial Rounded",15))
price_display.place(x=50,y=150)
service_cst = tk.Label(order_summ,text='Service Cost                                     6.75',bg='#a694df',font=("Arial Rounded",15))
Tax_cst = tk.Label(order_summ,text='Tax                                                  45',bg='#a694df',font=("Arial Rounded",15))
Total_price = tk.Label(order_summ,textvariable=total_cost,bg='#a694df',font=("Arial Rounded",15))
Total_price.place(x= 50,y=300)

total_price = tk.Button(text='Total', bg='#7380d6', font=("Arial Rounded",15),command=price_calc)
total_price.place(x=150,y=630)

#Notes for Extra written
note_frame = tk.Frame(root,bd=2,width=220, height=146,highlightbackground="black",highlightthickness=2)
note_frame.place(x=410, y=440)
note_frame.lift()

notes_name = tk.Label(note_frame,text='Notes')
notes_name.place(x=85,y=0)
notes_area = tk.Text(note_frame, width=26,height=6,highlightbackground="black",highlightthickness=1)
notes_area.place(x=0,y=20)


#Calculator for Bill calculation
calc_frame = tk.Frame(root,bd=2,width=220, height=300,highlightbackground="black",highlightthickness=2,)
calc_frame.place(x=650, y=440)
calc_frame.lift()

exp = []
operators = ['+','-','*','/']
#button pressed
def button_click(num):
    global exp
    exp.append(str(num))
    input_num.set("".join(exp))

# calci logic
def calc_logic():
    global exp, operators
    nums = []
    ops = []
    number = ''

    for i in exp:
        if i in operators:
            nums.append(number)
            ops.append(i)
            number = ''
        else:
            number += i
    nums.append(number)

    i = 0
    while i < len(ops):
        if ops[i] == '*' or ops[i] == '/':
            if ops[i] == '*':
                result = float(nums[i]) * float(nums[i + 1])
            else:
                result = float(nums[i]) / float(nums[i + 1])

            nums[i] = result
            nums.pop(i + 1)
            ops.pop(i)
        else:
            i += 1

    i = 0
    while i < len(ops):
        if ops[i] == '+' or ops[i] == '-':
            if ops[i] == '+':
                result = float(nums[i]) + float(nums[i + 1])
            else:  # it's '-'
                result = float(nums[i]) - float(nums[i + 1])

            nums[i] = result
            nums.pop(i + 1)
            ops.pop(i)
        else:
            i += 1

    calc_entry.delete(0, tk.END)
    calc_entry.insert(0, str(nums[0]))

#clear button on calculator logic
def clear():
    global exp
    exp = []
    calc_entry.delete(0,tk.END)


input_num = StringVar()
calc_entry = tk.Entry(calc_frame,bd=1,textvariable=input_num,relief="solid",font=("Arial Rounded",22),width=13)
calc_entry.place(x=0,y=0)
calc_1 = tk.Button(calc_frame,bd=1,relief='solid',text='1',height=3,width=6,command=lambda:button_click(1))
calc_1.place(x=0,y=37)
calc_2 = tk.Button(calc_frame,bd=1,relief='solid',text='2',height=3,width=6,command=lambda:button_click(2))
calc_2.place(x=50,y=37)
calc_3 = tk.Button(calc_frame,bd=1,relief='solid',text='3',height=3,width=6,command=lambda:button_click(3))
calc_3.place(x=100,y=37)
calc_4 = tk.Button(calc_frame,bd=1,relief='solid',text='4',height=3,width=6,command=lambda:button_click(4))
calc_4.place(x=0,y=91)
calc_5 = tk.Button(calc_frame,bd=1,relief='solid',text='5',height=3,width=6,command=lambda:button_click(5))
calc_5.place(x=50,y=91)
calc_6 = tk.Button(calc_frame,bd=1,relief='solid',text='6',height=3,width=6,command=lambda:button_click(6))
calc_6.place(x=100,y=91)
calc_7 = tk.Button(calc_frame,bd=1,relief='solid',text='7',height=3,width=6,command=lambda:button_click(7))
calc_7.place(x=0,y=145)
calc_8 = tk.Button(calc_frame,bd=1,relief='solid',text='8',height=3,width=6,command=lambda:button_click(8))
calc_8.place(x=50,y=145)
calc_9 = tk.Button(calc_frame,bd=1,relief='solid',text='9',height=3,width=6,command=lambda:button_click(9))
calc_9.place(x=100,y=145)
calc_clr = tk.Button(calc_frame,bd=1,relief='solid',text='C',height=3,width=6,command=clear)
calc_clr.place(x=0,y=199)
calc_0 = tk.Button(calc_frame,bd=1,relief='solid',text='0',height=3,width=6,command=lambda:button_click(0))
calc_0.place(x=50,y=199)
calc_eql = tk.Button(calc_frame,bd=1,relief='solid',text='=',height=3,width=6,command=calc_logic)
calc_eql.place(x=100,y=199)
calc_add = tk.Button(calc_frame,bd=1,relief='solid',text='+',height=3,width=7,command=lambda:button_click('+'))
calc_add.place(x=150,y=37)
calc_sub = tk.Button(calc_frame,bd=1,relief='solid',text='-',height=3,width=7,command=lambda:button_click('-'))
calc_sub.place(x=150,y=91)
calc_mul = tk.Button(calc_frame,bd=1,relief='solid',text='*',height=3,width=7,command=lambda:button_click('*'))
calc_mul.place(x=150,y=145)
calc_div = tk.Button(calc_frame,bd=1,relief='solid',text='/',height=3,width=7,command=lambda:button_click('/'))
calc_div.place(x=150,y=199)
calc_dec = tk.Button(calc_frame,bd=1,relief='solid',text='.',height=2,width=7,command=lambda:button_click('.'))
calc_dec.place(x=150,y=253)


# Price of Every Item in New Window
def price_call():
    global store_data
    price_window = tk.Toplevel(root)
    price_window.title('Price Summary')
    price_window.geometry('400x300')
    price_head = tk.Label(price_window,text='Price for One Unit of Each Item')
    price_head.pack()
    price_drink = tk.Label(price_window,text='Drink   =   15 INR')
    price_drink.pack()
    price_BurgerKing = tk.Label(price_window,text='Burger King   =   80 INR')
    price_BurgerKing.pack()
    price_Cherry = tk.Label(price_window,text='Cherry   =   30 INR')
    price_Cherry.pack()
    price_NachoFries = tk.Label(price_window,text='Nacho Fries   =   50 INR')
    price_NachoFries.pack()
    price_Pizza = tk.Label(price_window,text='Pizza   =   110 INR')
    price_Pizza.pack()
    price_Biscuit = tk.Label(price_window,text='Biscuit   =   10 INR')
    price_Biscuit.pack()
    price_Roll = tk.Label(price_window,text='Roll   =   60 INR')
    price_Roll.pack()
    price_Tea = tk.Label(price_window,text='Tea   =   10 INR')
    price_Tea.pack()
    exit_price = tk.Button(price_window,text='Exit',command=price_window.destroy)
    exit_price.place(x=350,y=250)

#Price Button for Main Window
Price_Btn = tk.Button(text='Price', bg='#568edf', font=("Arial Rounded",15),command=price_call)
Price_Btn.place(x=30,y=630)

#Reset Button to Reset the screen
def reset():
    try:
        menu1_store.set("")
        menu2_store.set("")
        menu3_store.set("")
        menu4_store.set("")
        menu5_store.set("")
        menu6_store.set("")
        menu7_store.set("")
        menu8_store.set("")

        total_var.set("")
        total_cost.set("")
        service_cst.place_forget()
        Tax_cst.place_forget()
        order_label.config(text="")
        notes_area.delete("1.0", tk.END)
    except Exception as e:
        print("Error in reset:", e)

Reset_Btn = tk.Button(text='Reset', bg='#6273cc', font=("Arial Rounded",15),command=reset)
Reset_Btn.place(x=270,y=630)

#Quit Button to exit this project
Quit_btn = tk.Button(text='Quit', bg='#5759ab', font=("Arial Rounded",15),command=root.destroy)
Quit_btn.place(x=390,y=630)

#Show Time
def update_time():
    current_time = time.strftime('%H:%M:%S')  # Shows hours, minutes, and seconds
    time_label.config(text=current_time)
    time_label.after(1000, update_time)
time_label = tk.Label(root, font=('arial', 18, 'bold'), fg='white', bg='#324179')
time_label.place(x=700, y=20)  # Adjust x, y based on your layout
update_time()

#Order Number and to save it and use multiple times
if not os.path.exists("order_number.txt"):
    with open("order_number.txt", "w") as f:
        f.write("100")

def get_order_number():
    with open("order_number.txt", "r") as g:
        return int(g.read())

def save_order_number(num):
    with open("order_number.txt", "w") as h:
        h.write(str(num))

order_label = tk.Label(order_summ,bg='#a694df',font=("Arial Rounded",15))
order_label.place(x=50,y=100)

root.mainloop()