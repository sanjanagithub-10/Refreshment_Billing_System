from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests
import json
#Functions

def reset():
    textReceipt.delete(1.0, END)
    e_roti.set('0')
    e_daal.set('0')
    e_fish.set('0')
    e_sabji.set('0')
    e_kabab.set('0')
    e_chawal.set('0')
    e_mutton.set('0')
    e_paneer.set('0')
    e_chicken.set('0')

    e_lassi.set('0')
    e_coffee.set('0')
    e_faluda.set('0')
    e_shikanji.set('0')
    e_badammilk.set('0')
    e_masalatea.set('0')
    e_colddrinks.set('0')
    e_roohafza.set('0')
    e_jaljeera.set('0')

    e_oreo.set('0')
    e_apple.set('0')
    e_banana.set('0')
    e_kitkat.set('0')
    e_vanilla.set('0')
    e_blackforest.set('0')
    e_brownie.set('0')
    e_chocolate.set('0')
    e_pineapple.set('0')

    textroti.config(state=DISABLED)
    textdaal.config(state=DISABLED)
    textfish.config(state=DISABLED)
    textsabji.config(state=DISABLED)
    textkabab.config(state=DISABLED)
    textchawal.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textpaneer.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    
    textlassi.config(state=DISABLED)
    textcoffee.config(state=DISABLED)
    textfaluda.config(state=DISABLED)
    textshikanji.config(state=DISABLED)
    textbadammilk.config(state=DISABLED)
    textmasalatea.config(state=DISABLED)
    textcolddrinks.config(state=DISABLED)
    textroohafza.config(state=DISABLED)
    textjaljeera.config(state=DISABLED)
    
    textoreo.config(state=DISABLED)
    textapple.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textkitkat.config(state=DISABLED)
    textvanilla.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textbrownie.config(state=DISABLED)
    textchocolate.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costoffoodvar.set('')
    costofdrinksvar.set('')
    costofcakesvar.set('')
    subtotalvar.set('')
    servicetaxvar.set('')
    totalcostvar.set('')


def send_msg():
    message = textarea.get(1.0, END)
    number = numberfield.get()
    auth = 'wWOVgfLFy7Q3qN2kjBuDx54v0EZrApdMonTXKasHbIJ91PStmY3rUzjeatMybwfxuAdPLBXDHER7qZQC'   
    url = 'https://www.fast2sms.com/dev/bulk'

    params = {
        'authorization': auth,
        'message': message,
        'numbers': number,
        'sender_id': 'FSTSMS',
        'route': 'q',
        'language': 'english'
    }
    response = requests.get(url, params=params)
    dic = response.json()
    result = dic.get('return')
    if result == True:
        messagebox.showinfo('Send Successfully', 'Message sent successfully')
    else:
        messagebox.showerror('Error', 'Something went wrong!')

def send():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        global root2
        root2 = Toplevel()
        root2.title('Send Bill')
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')

        logoImage = PhotoImage(file='image/sender.png')
        label = Label(root2, image=logoImage, bg='red4')
        label.pack(pady=5)

        numberLabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold', 'underline'), bg='red4',
                            fg='white')
        numberLabel.pack(pady=5)

        global numberfield
        numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold', 'underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        global textarea
        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

        if costoffoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Food\t\t\t{priceoffood}Rs\n')
        if costofdrinksvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Drinks\t\t\t{priceofdrinks}Rs\n')
        if costofcakesvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of Cakes\t\t\t{priceofcakes}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofitems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalofitems + 50}Rs\n')

        sendButton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE,
                            command=send_msg)
        sendButton.pack(pady=5)

        root2.mainloop()


def save():
    if textReceipt.get(1.0,END)=='\n':
       pass
    else:
        url=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
        if url==None:
           pass
        else:
            bill_data=textReceipt.get(1.0,END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information','Your Bill Is Successfully Saved')


def receipt():
    global billnumber, date
    if costoffoodvar.get() != '' or costofdrinksvar.get() != '' or costofcakesvar.get() != '':
        textReceipt.delete(1.0, END)
        x=random.randint(100, 10000)
        billnumber='BILL'+str(x)
        date=time.strftime('%d/%m/%y')
        textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        textReceipt.insert(END, '***************************************************************\n')
        textReceipt.insert(END, 'Items:\t\t Cost Of Items(Rs)\n')
        textReceipt.insert(END, '***************************************************************\n')

        if e_roti.get() != '0':
            textReceipt.insert(END, f'Roti\t\t{int(e_roti.get())*10}\n\n')
            
        if e_daal.get() != '0':
            textReceipt.insert(END, f'Daal\t\t{int(e_daal.get())*60}\n\n')   
            
        if e_fish.get() != '0':
            textReceipt.insert(END, f'Fish\t\t{int(e_fish.get())*100}\n\n')
     

        if e_sabji.get() != '0':
            textReceipt.insert(END, f'Sabji\t\t{int(e_sabji.get())*50}\n\n')
            
            
        if e_kabab.get() != '0':
            textReceipt.insert(END, f'Kabab\t\t{int(e_kabab.get())*40}\n\n')
            
        if e_chawal.get() != '0':
            textReceipt.insert(END, f'Chawal\t\t{int(e_chawal.get())*30}\n\n')
    
         
        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton\t\t{int(e_mutton.get())*120}\n\n')
                
        if e_paneer.get() != '0':
            textReceipt.insert(END, f'Paneer\t\t{int(e_paneer.get())*100}\n\n') 
            
        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken\t\t{int(e_chicken.get())*60}\n\n')           
                
        if e_lassi.get() != '0':
            textReceipt.insert(END, f'Lassi\t\t{int(e_lassi.get())*50}\n\n')

        if e_coffee.get() != '0':
            textReceipt.insert(END, f'Coffee\t\t{int(e_coffee.get())*40}\n\n')

        if e_faluda.get() != '0':
            textReceipt.insert(END, f'Faluda\t\t{int(e_faluda.get())*80}\n\n')

        if e_shikanji.get() != '0':
            textReceipt.insert(END, f'Shikanji\t\t{int(e_shikanji.get())*30}\n\n')
            
        if e_badammilk.get() != '0':
            textReceipt.insert(END, f'Badam Milk\t\t{int(e_badammilk.get())*50}\n\n') 
            
        if e_masalatea.get() != '0':
            textReceipt.insert(END, f'Masala tea\t\t{int(e_masalatea.get())*10}\n\n')
            
        if e_colddrinks.get() != '0':
            textReceipt.insert(END, f'Cold Drinks\t\t{int(e_colddrinks.get())*60}\n\n')   
            
        if e_roohafza.get() != '0':
            textReceipt.insert(END, f'Roohafza\t\t{int(e_roohafza.get())*80}\n\n') 
                
        if e_jaljeera.get() != '0':
            textReceipt.insert(END, f'Jaljeera\t\t{int(e_jaljeera.get())*40}\n\n')
       
        if e_oreo.get() != '0':
            textReceipt.insert(END, f'Oreo\t\t{int(e_oreo.get())*120}\n\n')

        if e_apple.get() != '0':
            textReceipt.insert(END, f'Apple\t\t{int(e_apple.get())*300}\n\n')
            
        if e_banana.get() != '0':
            textReceipt.insert(END, f'Banana\t\t{int(e_banana.get())*450}\n\n')    

        if e_kitkat.get() != '0':
            textReceipt.insert(END, f'Kitkat\t\t{int(e_kitkat.get())*500}\n\n')
            
        if e_vanilla.get() != '0':
            textReceipt.insert(END, f'Vanilla\t\t{int(e_vanilla.get())*800}\n\n')
             
        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest\t\t{int(e_blackforest.get())*550}\n\n')
   
        if e_brownie.get() != '0':
            textReceipt.insert(END, f'Brownie\t\t{int(e_brownie.get())*800}\n\n')
            
        if e_chocolate.get() != '0':
            textReceipt.insert(END, f'Chocolate\t\t{int(e_chocolate.get())*750}\n\n')    

        if e_pineapple.get() != '0':
            textReceipt.insert(END, f'Pineapple\t\t{int(e_pineapple.get())*620}\n\n')

        textReceipt.insert(END, '***************************************************************\n')

        if costoffoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost of Food\t\t\t{priceoffood}Rs\n\n')
        if costofdrinksvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost of Drinks\t\t\t{priceofdrinks}Rs\n\n')
        if costofcakesvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost of Cakes\t\t\t{priceofcakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofitems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total Cost\t\t\t{subtotalofitems + 50}Rs\n\n')

        textReceipt.insert(END, '***************************************************************\n')

    else:
        messagebox.showerror('Error', 'No Item Is Selected')

    
def totalcost():
    global priceoffood, priceofdrinks, priceofcakes, subtotalofitems

    # Check if any item has been selected
    if var1.get()!=0 or var2.get()!=0 or var3.get()!=0 or var4.get()!=0 or var5.get()!=0 or \
       var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var9.get()!=0 or var10.get()!=0 or \
       var11.get()!=0 or var12.get()!=0 or var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or \
       var16.get()!=0 or var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0 or \
       var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or \
       var26.get()!=0 or var27.get()!=0:
       
        item1 = int(e_roti.get()) if e_roti.get() else 0
        item2 = int(e_daal.get()) if e_daal.get() else 0
        item3 = int(e_fish.get()) if e_fish.get() else 0
        item4 = int(e_sabji.get()) if e_sabji.get() else 0
        item5 = int(e_kabab.get()) if e_kabab.get() else 0
        item6 = int(e_chawal.get()) if e_chawal.get() else 0
        item7 = int(e_mutton.get()) if e_mutton.get() else 0
        item8 = int(e_paneer.get()) if e_paneer.get() else 0
        item9 = int(e_chicken.get()) if e_chicken.get() else 0
        item10 = int(e_lassi.get()) if e_lassi.get() else 0
        item11 = int(e_coffee.get()) if e_coffee.get() else 0
        item12 = int(e_faluda.get()) if e_faluda.get() else 0
        item13 = int(e_shikanji.get()) if e_shikanji.get() else 0
        item14 = int(e_badammilk.get()) if e_badammilk.get() else 0
        item15 = int(e_masalatea.get()) if e_masalatea.get() else 0
        item16 = int(e_colddrinks.get()) if e_colddrinks.get() else 0
        item17 = int(e_roohafza.get()) if e_roohafza.get() else 0
        item18 = int(e_jaljeera.get()) if e_jaljeera.get() else 0
        item19 = int(e_oreo.get()) if e_oreo.get() else 0
        item20 = int(e_apple.get()) if e_apple.get() else 0
        item21 = int(e_banana.get()) if e_banana.get() else 0
        item22 = int(e_kitkat.get()) if e_kitkat.get() else 0
        item23 = int(e_vanilla.get()) if e_vanilla.get() else 0
        item24 = int(e_blackforest.get()) if e_blackforest.get() else 0
        item25 = int(e_brownie.get()) if e_brownie.get() else 0
        item26 = int(e_chocolate.get()) if e_chocolate.get() else 0
        item27 = int(e_pineapple.get()) if e_pineapple.get() else 0
        
        priceoffood = (item1*10) + (item2*60) + (item3*100) + (item4*50) + (item5*40) + \
                      (item6*30) + (item7*120) + (item8*100) + (item9*120)
        
        priceofdrinks = (item10*50) + (item11*40) + (item12*80) + (item13*30) + (item14*40) + \
                        (item15*60) + (item16*20) + (item17*50) + (item18*80)
        
        priceofcakes = (item19*400) + (item20*300) + (item21*500) + (item22*550) + (item23*450) + \
                       (item24*800) + (item25*620) + (item26*700) + (item27*550)

        costoffoodvar.set(str(priceoffood)+ ' Rs')
        costofdrinksvar.set(str(priceofdrinks)+ ' Rs')
        costofcakesvar.set(str(priceofcakes)+ ' Rs')

        subtotalofitems = priceoffood + priceofdrinks + priceofcakes
        subtotalvar.set(str(subtotalofitems)+' Rs')

        servicetaxvar.set('50 Rs')

        totalcost = subtotalofitems + 50
        totalcostvar.set(str(totalcost)+' Rs')

    else:
        messagebox.showerror('Error', 'No Item Is Selected')

def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def daal():
    if var2.get()==1:
       textdaal.config(state=NORMAL)
       textdaal.delete(0,END)
       textdaal.focus()
    else:
       textdaal.config(state=DISABLED)
       e_daal.set('0')  

def fish():
    if var3.get()==1:
       textfish.config(state=NORMAL)
       textfish.delete(0,END)
       textfish.focus()
    else:
       textfish.config(state=DISABLED)
       e_fish.set('0')  

def sabji():
    if var4.get()==1:
       textsabji.config(state=NORMAL)
       textsabji.focus()
       textsabji.delete(0,END)
    elif var4.get() == 0:
       textsabji.config(state=DISABLED)
       e_sabji.set('0')  

def kabab():
    if var5.get()==1:
       textkabab.config(state=NORMAL)
       textkabab.focus()
       textkabab.delete(0,END)
    elif var5.get() == 0:
       textkabab.config(state=DISABLED)
       e_kabab.set('0') 

def chawal():
    if var6.get()==1:
       textchawal.config(state=NORMAL)
       textchawal.focus()
       textchawal.delete(0,END)
    elif var6.get() == 0:
       textchawal.config(state=DISABLED)
       e_chawal.set('0') 
       
def mutton():
    if var7.get()==1:
       textmutton.config(state=NORMAL)
       textmutton.focus()
       textmutton.delete(0,END)
    elif var7.get() == 0:
       textmutton.config(state=DISABLED)
       e_mutton.set('0')        
    
def paneer():
    if var8.get()==1:
       textpaneer.config(state=NORMAL)
       textpaneer.focus()
       textpaneer.delete(0,END)
    elif var8.get() == 0:
       textpaneer.config(state=DISABLED)
       e_paneer.set('0')   
       
def chicken():
    if var9.get()==1:
       textchicken.config(state=NORMAL)
       textchicken.focus()
       textchicken.delete(0,END)
    elif var9.get() == 0:
       textchicken.config(state=DISABLED)
       e_chicken.set('0')  

def lassi():
    if var10.get()==1:
       textlassi.config(state=NORMAL)
       textlassi.focus()
       textlassi.delete(0,END)
    elif var10.get() == 0:
       textlassi.config(state=DISABLED)
       e_lassi.set('0')
       
def coffee():
    if var11.get()==1:
       textcoffee.config(state=NORMAL)
       textcoffee.focus()
       textcoffee.delete(0,END)
    elif var11.get() == 0:
       textcoffee.config(state=DISABLED)
       e_coffee.set('0') 
      
def faluda():
    if var12.get()==1:
       textfaluda.config(state=NORMAL)
       textfaluda.focus()
       textfaluda.delete(0,END)
    elif var12.get() == 0:
       textfaluda.config(state=DISABLED)
       e_faluda.set('0')   

def shikanji():
    if var13.get()==1:
       textshikanji.config(state=NORMAL)
       textshikanji.focus()
       textshikanji.delete(0,END)
    elif var13.get() == 0:
       textshikanji.config(state=DISABLED)
       e_shikanji.set('0')  
       
def badammilk():
    if var14.get()==1:
       textbadammilk.config(state=NORMAL)
       textbadammilk.focus()
       textbadammilk.delete(0,END)
    elif var14.get() == 0:
       textbadammilk.config(state=DISABLED)
       e_badammilk.set('0') 
       
def masalatea():
    if var15.get()==1:
       textmasalatea.config(state=NORMAL)
       textmasalatea.focus()
       textmasalatea.delete(0,END)
    elif var15.get() == 0:
       textmasalatea.config(state=DISABLED)
       e_masalatea.set('0') 
       
def colddrinks():
    if var16.get()==1:
       textcolddrinks.config(state=NORMAL)
       textcolddrinks.focus()
       textcolddrinks.delete(0,END)
    elif var16.get() == 0:
       textcolddrinks.config(state=DISABLED)
       e_colddrinks.set('0')
       
def roohafza():
    if var17.get()==1:
       textroohafza.config(state=NORMAL)
       textroohafza.focus()
       textroohafza.delete(0,END)
    elif var17.get() == 0:
       textroohafza.config(state=DISABLED)
       e_roohafza.set('0')                              

def jaljeera():
    if var18.get()==1:
       textjaljeera.config(state=NORMAL)
       textjaljeera.focus()
       textjaljeera.delete(0,END)
    elif var18.get() == 0:
       textjaljeera.config(state=DISABLED)
       e_jaljeera.set('0') 
       
def oreo():
    if var19.get()==1:
       textoreo.config(state=NORMAL)
       textoreo.focus()
       textoreo.delete(0,END)
    elif var19.get() == 0:
       textoreo.config(state=DISABLED)
       e_oreo.set('0') 

def apple():
    if var20.get()==1:
       textapple.config(state=NORMAL)
       textapple.focus()
       textapple.delete(0,END)
    elif var20.get() == 0:
       textapple.config(state=DISABLED)
       e_apple.set('0')
       
def banana():
    if var21.get()==1:
       textbanana.config(state=NORMAL)
       textbanana.focus()
       textbanana.delete(0,END)
    elif var21.get() == 0:
       textbanana.config(state=DISABLED)
       e_banana.set('0')       

def kitkat():
    if var22.get()==1:
       textkitkat.config(state=NORMAL)
       textkitkat.focus()
       textkitkat.delete(0,END)
    elif var22.get() == 0:
       textkitkat.config(state=DISABLED)
       e_kitkat.set('0') 

def vanilla():
    if var23.get()==1:
       textvanilla.config(state=NORMAL)
       textvanilla.focus()
       textvanilla.delete(0,END)
    elif var23.get() == 0:
       textvanilla.config(state=DISABLED)
       e_vanilla.set('0')  
       
def blackforest():
    if var24.get()==1:
       textblackforest.config(state=NORMAL)
       textblackforest.focus()
       textblackforest.delete(0,END)
    elif var24.get() == 0:
       textblackforest.config(state=DISABLED)
       e_blackforest.set('0')         

def brownie():
    if var25.get()==1:
       textbrownie.config(state=NORMAL)
       textbrownie.focus()
       textbrownie.delete(0,END)
    elif var25.get() == 0:
       textbrownie.config(state=DISABLED)
       e_brownie.set('0')   
       
def chocolate():
    if var26.get()==1:
       textchocolate.config(state=NORMAL)
       textchocolate.focus()
       textchocolate.delete(0,END)
    elif var26.get() == 0:
       textchocolate.config(state=DISABLED)
       e_chocolate.set('0')                                                                                                                                                                                                 

def pineapple():
    if var27.get()==1:
       textpineapple.config(state=NORMAL)
       textpineapple.focus()
       textpineapple.delete(0,END)
    elif var27.get() == 0:
       textpineapple.config(state=DISABLED)
       e_pineapple.set('0') 
       
root=Tk()

root.geometry('1270x690+0+0')

root.resizable(0,0)

root.title('Hotel Billing System created by Sanjana Yadav')

root.config(bg='firebrick4')

topFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle=Label(topFrame,text='Hotel Billing System',font=('arial',30,'bold'),fg='yellow',bd=9,
                 bg='red4',width=51)
labelTitle.grid(row=0,column=0)

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
receiptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#Variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_daal=StringVar()
e_fish=StringVar()
e_sabji=StringVar()
e_kabab=StringVar()
e_chawal=StringVar()
e_mutton=StringVar()
e_paneer=StringVar()
e_chicken=StringVar()

e_lassi=StringVar()
e_coffee=StringVar()
e_faluda=StringVar()
e_shikanji=StringVar()
e_badammilk=StringVar()
e_masalatea=StringVar()
e_colddrinks=StringVar()
e_roohafza=StringVar()
e_jaljeera=StringVar()

e_oreo=StringVar()
e_apple=StringVar()
e_banana=StringVar()
e_kitkat=StringVar()
e_vanilla=StringVar()
e_blackforest=StringVar()
e_brownie=StringVar()
e_chocolate=StringVar()
e_pineapple=StringVar()

costoffoodvar=StringVar()
costofdrinksvar=StringVar()
costofcakesvar=StringVar()
subtotalvar=StringVar()
servicetaxvar=StringVar()
totalcostvar=StringVar()


e_roti.set('0')
e_daal.set('0')
e_fish.set('0')
e_sabji.set('0')
e_kabab.set('0')
e_chawal.set('0')
e_mutton.set('0')
e_paneer.set('0')
e_chicken.set('0')

e_lassi.set('0')
e_coffee.set('0')
e_faluda.set('0')
e_shikanji.set('0')
e_badammilk.set('0')
e_masalatea.set('0')
e_colddrinks.set('0')
e_roohafza.set('0')
e_jaljeera.set('0')

e_oreo.set('0')
e_apple.set('0')
e_banana.set('0')
e_kitkat.set('0')
e_vanilla.set('0')
e_blackforest.set('0')
e_brownie.set('0')
e_chocolate.set('0')
e_pineapple.set('0')

#Food

roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1
                 ,command=roti)
roti.grid(row=0,column=0,sticky=W)

daal=Checkbutton(foodFrame,text='Daal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2
                 ,command=daal)
daal.grid(row=1,column=0,sticky=W)

fish=Checkbutton(foodFrame,text='Fish',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3
                 ,command=fish)
fish.grid(row=2,column=0,sticky=W)

sabji=Checkbutton(foodFrame,text='Sabji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4
                  ,command=sabji)
sabji.grid(row=3,column=0,sticky=W)

kabab=Checkbutton(foodFrame,text='Kabab',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5
                  ,command=kabab)
kabab.grid(row=4,column=0,sticky=W)

chawal=Checkbutton(foodFrame,text='Chawal',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6
                   ,command=chawal)
chawal.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7
                   ,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

paneer=Checkbutton(foodFrame,text='Paneer',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8
                   ,command=paneer)
paneer.grid(row=7,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9
                    ,command=chicken)
chicken.grid(row=8,column=0,sticky=W)

#Entry Fields for food item
             
textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdaal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_daal)
textdaal.grid(row=1,column=1)

textfish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fish)
textfish.grid(row=2,column=1)

textsabji=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sabji)
textsabji.grid(row=3,column=1)

textkabab=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kabab)
textkabab.grid(row=4,column=1)

textchawal=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chawal)
textchawal.grid(row=5,column=1)

textmutton=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=6,column=1)

textpaneer=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_paneer)
textpaneer.grid(row=7,column=1)

textchicken=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=8,column=1)


#drinks

lassi=Checkbutton(drinksFrame,text='Lassi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10
                  ,command=lassi)
lassi.grid(row=0,column=0,sticky=W)
           
coffee=Checkbutton(drinksFrame,text='Coffee',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11
                   ,command=coffee)
coffee.grid(row=1,column=0,sticky=W)

faluda=Checkbutton(drinksFrame,text='Faluda',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12
                   ,command=faluda)
faluda.grid(row=2,column=0,sticky=W)

shikanji=Checkbutton(drinksFrame,text='Shikanji',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13
                     ,command=shikanji)
shikanji.grid(row=3,column=0,sticky=W)

badammilk=Checkbutton(drinksFrame,text='Badam Milk',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14
                      ,command=badammilk)
badammilk.grid(row=4,column=0,sticky=W)

masalatea=Checkbutton(drinksFrame,text='Masalatea',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15
                      ,command=masalatea)
masalatea.grid(row=5,column=0,sticky=W)

colddrinks=Checkbutton(drinksFrame,text='Cold Drinks',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16
                       ,command=colddrinks)
colddrinks.grid(row=6,column=0,sticky=W)

roohafza=Checkbutton(drinksFrame,text='Roohafza',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17
                     ,command=roohafza)
roohafza.grid(row=7,column=0,sticky=W)

jaljeera=Checkbutton(drinksFrame,text='Jaljeera',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18
                     ,command=jaljeera)
jaljeera.grid(row=8,column=0,sticky=W)        

#Entry fields for drinks  items

textlassi=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lassi)
textlassi.grid(row=0,column=1)

textcoffee=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coffee)
textcoffee.grid(row=1,column=1)

textfaluda=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_faluda)
textfaluda.grid(row=2,column=1)

textshikanji=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_shikanji)
textshikanji.grid(row=3,column=1)

textbadammilk=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_badammilk)
textbadammilk.grid(row=4,column=1)

textmasalatea=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_masalatea)
textmasalatea.grid(row=5,column=1)

textcolddrinks=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_colddrinks)
textcolddrinks.grid(row=6,column=1)

textroohafza=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roohafza)
textroohafza.grid(row=7,column=1)

textjaljeera=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jaljeera)
textjaljeera.grid(row=8,column=1)


#Cakes

oreocake=Checkbutton(cakesFrame,text='Oreo',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19
                     ,command=oreo)
oreocake.grid(row=0,column=0,sticky=W)
           
applecake=Checkbutton(cakesFrame,text='Apple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20
                      ,command=apple)
applecake.grid(row=1,column=0,sticky=W)

bananacake=Checkbutton(cakesFrame,text='Banana',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21
                       ,command=banana)
bananacake.grid(row=2,column=0,sticky=W)

kitkatcake=Checkbutton(cakesFrame,text='Kitkat',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22
                       ,command=kitkat)
kitkatcake.grid(row=3,column=0,sticky=W)

vanillacake=Checkbutton(cakesFrame,text='Vanilla',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23
                        ,command=vanilla)
vanillacake.grid(row=4,column=0,sticky=W)

blackforestcake=Checkbutton(cakesFrame,text='Black Forest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24
                            ,command=blackforest)
blackforestcake.grid(row=5,column=0,sticky=W)

browniecake=Checkbutton(cakesFrame,text='Brownie',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25
                        ,command=brownie)
browniecake.grid(row=6,column=0,sticky=W)

chocolatecake=Checkbutton(cakesFrame,text='Chocolate',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26
                          ,command=chocolate)
chocolatecake.grid(row=7,column=0,sticky=W)

pineapplecake=Checkbutton(cakesFrame,text='Pineapple',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27
                          ,command=pineapple)
pineapplecake.grid(row=8,column=0,sticky=W)


#Entry fields for cakes  items

textoreo=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oreo)
textoreo.grid(row=0,column=1)

textapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=1,column=1)

textbanana=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=2,column=1)

textkitkat=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_kitkat)
textkitkat.grid(row=3,column=1)

textvanilla=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vanilla)
textvanilla.grid(row=4,column=1)

textblackforest=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=5,column=1)

textbrownie=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_brownie)
textbrownie.grid(row=6,column=1)

textchocolate=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocolate)
textchocolate.grid(row=7,column=1)

textpineapple=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=8,column=1)


#costlabels & entry fields

labelCostofFood=Label(costFrame,text='Cost of Food',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofFood.grid(row=0,column=0)

textCostofFood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFood.grid(row=0,column=1,padx=41)

labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinksvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakesvar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)

labelTotalCost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='firebrick4',fg='white')
labelTotalCost.grid(row=2,column=2)

textTotalCost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
textTotalCost.grid(row=2,column=3,padx=41)

#Buttons

buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=totalcost)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                     command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                  command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                  command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,
                   command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt

textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#calculator

operator='' 
def buttonClick(numbers): 
    global operator
    operator=operator+numbers 
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('9'))
button9.grid(row=1,column=2)

buttonPlus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+'))
buttonPlus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('6'))
button6.grid(row=2,column=2)

buttonMinus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-'))
buttonMinus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('3'))
button3.grid(row=3,column=2)

buttonMult=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*'))
buttonMult.grid(row=3,column=3)

buttonAns=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer)
buttonAns.grid(row=4,column=0)

buttonClear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=clear)
buttonClear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0'))
button0.grid(row=4,column=2)

buttonDiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/'))
buttonDiv.grid(row=4,column=3)

root.mainloop()