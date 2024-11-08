from tkinter import*
from container import user,point,item,c,selected_item,lst,price,new_price

page2 = Tk()
page2.geometry('600x600')
page2.title('page2')
page2['bg'] = 'azure3'
Label(page2,text="User :",font=('arial', 15, "bold"),fg="white",bg="azure3").grid(row=0, column=0)
Label(page2,text=user,font=('arial', 15, "bold"), bg="azure3", fg="black").grid(row=0, column=1)

def add_item():
    selected_item = entry1.get()
    try:
        selected_item = int(selected_item)
        if 0 <= selected_item < len(lst):
            item.append(lst[selected_item])
            c.append(new_price[selected_item])
            title_label = Label(page2,text="In selected", font=('arial', 10, "bold"), bg="red", fg="blue")
            title_label.grid(row=3, column=3)
            print(c)
            print(item)

            item_label = Label(page2, text=lst[selected_item], font=('arial', 10, "bold"), bg="azure3", fg="black")
            item_label.grid(row=len(item) + 3, column=3,sticky=W)
        else:
            return("Invalid item selection")
    except ValueError:
        print("Invalid input,Type only number 0-11")
    entry1.delete(0,END)


Label(page2, text="List menu", font=('arial', 15, "bold"), bg="azure3", fg="deeppink2").grid(row=1, column=1)

for i in range(len(lst)):
    
    Label(page2, text=f"{i}. {lst[i]}", font=('arial', 15, 'bold'), bg='azure3').grid(row=i + 2, column=1,sticky=W)

for i in range(len(price)):
    
    Label(page2, text=f"{price[i]}B", font=('arial', 15, 'bold'), bg='azure3', fg="red").grid(row=i + 2, column=2,sticky=W)

entry1 = Entry(page2, font=("Arial", 12, "bold"), fg="orange", bg="azure2")
entry1.grid(row=1, column=2,padx=3,pady=5)
entry1.insert(0,"Put Number of item")

# Create an "Add Item" button
add_item_button = Button(page2, text="Add Item", font=('arial', 12, "bold"), fg="black", bg="lightblue1", command=add_item)
add_item_button.grid(row=2, column=3)

def cleartext():
    entry1.delete(0,END)
    entry1.focus()
    print("clear text successed")

def nextpage () :
    page2.destroy()
    import page3


clear_button = Button(page2,text="Clear text", font=("Arial", 10, "bold"), fg="orange", bg="gainsboro",command=cleartext).grid(row=1,column=3)
exit_button = Button(page2,text="Exit", font=("Arial", 14, "bold"), fg="black", bg="red",command=page2.destroy).grid(row=14,column=0)
next_button = Button(page2,text="confirm to next page", font=("Arial", 14, "bold"), fg="white", bg="darkorchid1",command=nextpage).grid(row=14,column=1)


page2.mainloop()
