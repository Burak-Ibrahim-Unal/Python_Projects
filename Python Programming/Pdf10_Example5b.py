from tkinter import*
Options=['euro','dollar','lek','pound']
master=Tk()
master.geometry('600x300')
master.title('Currency converter')
lbl1=Label(bg='lightblue')
lbl1.place(x=0,y=0,width=300,height=600)
lbl2=Label(bg='lightgreen')
lbl2.place(x=300,y=0,width=300,height=600)
variable=StringVar(master)
variable.set('Choose currency')
w=OptionMenu(master,variable,'euro','dollar','lek','pound')#ose['euro', 'dollar','lek','pound']
w.pack()
w.place(x=20,y=80,width=130,height=30)
variable2=StringVar(master)
variable2.set('Choose currency')
s=OptionMenu(master,variable2,'euro','dollar','lek','pound')
s.pack()
s.place(x=450, y=80,width=130,height=30)
ent1=Entry()
ent1.place(x=20,y=130,width=130,height=30)
lbl3=Label(bg='white',anchor=W)
lbl3.place(x=450,y=130,width=130,height=30)
def Convert():
    x=0
    menu1=variable.get()
    menu2=variable2.get()
    entry=ent1.get()
    entry=float(entry)
    if(menu1=='euro' and menu2=='dollar'):
        x=entry*1.13
    elif(menu1=='euro' and menu2=='lek'):
        x=entry*132.15
    elif(menu1=='euro' and menu2=='pound'):
        x=entry*0.88
    elif(menu1=='dollar' and menu2=='euro'):
        x=entry*0.88
    elif(menu1=='dollar' and menu2=='lek'):
        x=entry*116.78
    elif(menu1=='dollar' and menu2=='pound'):
        x=entry*0.77
    elif(menu1=='lek' and menu2=='euro'):
        x=entry*0.0075
    elif(menu1=='lek' and menu2=='dollar'):
        x=entry*0.0086
    elif(menu1=='lek' and menu2=='pound'):
        x=entry*0.0066
    elif(menu1=='pound' and menu2=='euro'):
        x=entry*1.14
    elif(menu1=='pound' and menu2=='dollar'):
        x=entry*1.29
    elif(menu1=='pound' and menu2=='lek'):
        x=entry*150.98
        lbl3.config(text=str(x))

btn1=Button(text='Convert',font=('Arial',20,'bold'),bg='green',command=Convert)
btn1.place(x=235,y=180,width=130,height=50)
lblC=Label(text='Currency Convertor',bg='white',font=('Arial',22,'bold'))
lblC.place(x=160,y=10,width=280,height=40)
mainloop()