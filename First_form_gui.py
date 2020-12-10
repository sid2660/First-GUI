## Python tkinter toutorial
## tee-kinter , tk-inter, kinter 

## starter code
import tkinter as tk
from tkinter import ttk
from csv import DictWriter 
import os
win = tk.Tk()
win.title('Form')

## Create labels
## Widgets --> label , buttons, radio button --tk ,ttk
## pack, grid

name_lable =ttk.Label(win,text='Enter your first name : ')
name_lable.grid(row=0,column=0,sticky=tk.W)

email_lable = ttk.Label(win,text='Enter your email : ')
email_lable.grid(row=1,column=0,sticky=tk.W)

age_lable = ttk.Label(win,text='Enter your age : ')
age_lable.grid(row=2,column=0,sticky=tk.W)

gender_lable = ttk.Label(win,text='Select your gender : ')
gender_lable.grid(row=3,column=0,sticky=tk.W)

##### Create entry box 
name_var = tk.StringVar()
name_entrybox = ttk.Entry(win,width=16,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

email_var = tk.StringVar()
email_entrybox = ttk.Entry(win,width=16,textvariable=email_var)
email_entrybox.grid(row=1,column=1)


age_var = tk.StringVar()
age_entrybox = ttk.Entry(win,width=16,textvariable=age_var)
age_entrybox.grid(row=2,column=1)

##### Create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(win,width=13,textvariable=gender_var,state='readonly')
gender_combobox['values'] = ('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

##### Radio Button 
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(win,text='Student',value='Student',variable=usertype)
radiobtn1.grid(row=4,column=0)

radiobtn2 = ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=usertype)
radiobtn2.grid(row=4,column=1)

####### Check button 
checkbtn_var = tk.IntVar()
check_btn= ttk.Checkbutton(win,text='Check if you want to subscribe our newslettor',variable=checkbtn_var)
check_btn.grid(row=5,columnspan=3)

##### Button

# def action():
#     username = name_var.get()
#     useremail = email_var.get()
#     userage= age_var.get()
#     usergender= gender_var.get()
#     usertypes = usertype.get()
#     if checkbtn_var.get() == 0:
#         subscribe = "No"
#     else:
#         subscribe = "Yes"
#     print(f"{username} is {userage} years old, gender is {usergender} and email is {useremail} and he/she is {usertypes}, Subscribed {subscribe}")


# ## store in file

#     with open('file.txt','a') as f:
#         f.write(f"{username},{useremail},{userage},{usergender},{usertypes},{subscribe}\n")
    
    
    
############# Create CSV file####  

def action():
    username = name_var.get()
    useremail = email_var.get()
    userage= age_var.get()
    usergender= gender_var.get()
    usertypes = usertype.get()
    if checkbtn_var.get() == 0:
        subscribe = "No"
    else:
        subscribe = "Yes"
        
    #### write in csv file
    with open('file.csv','a',newline='')as f:
        dict_writer = DictWriter(f,fieldnames=['Username','UserEmail','UserAge','Usergender','Usertype','Subscribe'])
        if os.stat('file.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'Username':username,
            'UserEmail':useremail,
            'UserAge':userage,
            'Usergender':usergender,
            'Usertype':usertypes,
            'Subscribe':subscribe
        })
        
    
##### clear after submit
    name_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END) 

###### change color
    name_lable.configure(foreground='Red',background='White')
    email_lable.configure(foreground='Red',background='White')
    age_lable.configure(foreground='Red',background='White')



submit_button = ttk.Button(win,text='Submit',command=action)
submit_button.grid(row=6,column=0)



win.mainloop()