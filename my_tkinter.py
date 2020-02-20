from tkinter import *
firstclick=True

def currency_converter():
    input=int(entry_currency2.get())
    mode=(entry_currency1.get())
    if mode.upper()=='KSHS':
        converted=(input/102)#the current conversion rate from KSHS to  USD
        outputlabel1.configure(text="{}Kshs is {} USDs".format(input,converted))
    elif mode.upper()=='USD':
        converted=(input*102)#from USD to KSHS
        outputlabel1.configure(text="{}USD is {} Kshs".format(input,converted))
def length_converter():
    #converts feet to meters and vice versa
    mode1=(entry_length1.get())#gets a string either feet or metre
    input1=int(entry_length2.get())
    if mode1.lower()=='metre':
        converted1=input1*3.028
        outputlabel2.configure(font=('verdana',12),text="{} metres is {}feet".format(input1,converted1))

    elif mode1.lower()== 'feet':
        converted1=float(input1/3.028)
        outputlabel1.configure(font=('verdana',12),text="{} feet is {}metres".format(input1,converted1))
def on_entry_click(event):
    # A function that gets callled when the entry box is clicked to delete the temporary text
    global firstclick
    if firstclick:
        firstclick= False
        entry_currency1.delete(0,END) #deletes text in the currency converter entry box to give room for the string input
        entry_length1.delete(0,END)#deletes text in the lenght converter to give room for the string input

root=Tk()
root.title('The converter')
title=Label(text='welcome to the converter')
title.grid(row=0,column=2)

currency_text=Label(text='USD to KSHS ,KSHS to USD ')
currency_text.grid(row=2,column=1)
length_text=Label(text='feet to metre,metre to feet')
length_text.grid(row=4,column=1)

entry_currency1=Entry(width=10)#to have temporary text
entry_currency1.insert(0,'USD or KSHS?')
entry_currency1.bind('<FocusIn>',on_entry_click)
entry_currency2=Entry(width=15)

entry_currency1.grid(row=2,column=2)
entry_currency2.grid(row=2,column=3)

entry_length1=Entry(width=15)#to have temporary text
entry_length1.insert(0,'feet or metre?')
entry_length1.bind('<FocusIn>',on_entry_click)
entry_length2=Entry(width=15)

entry_length1.grid(row=4,column=2)
entry_length2.grid(row=4,column=3)

button1=Button(text='calculate',command=currency_converter)
button1.grid(row=3,column=1)
button2=Button(text='calculate',command=length_converter)
button2.grid(row =5,column=1)

outputlabel1=Label(font=('verdana',12))
outputlabel1.grid(row=7,column=1)
outputlabel2=Label(font=('arial',14))
outputlabel2.grid(row=10,column=2)
mainloop()

