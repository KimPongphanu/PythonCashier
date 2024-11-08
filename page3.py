from tkinter import *
from container import user, price, item, lst, new_price, c,user_data

# Create a Tkinter window for page3
page3 = Tk()
page3.geometry('350x400')
page3.title('page3')
page3['bg'] = 'white'

Label(page3, text="Selected item", font=('arial', 10, "bold"), bg="blue", fg="gold", justify="left").grid(row=0, column=0, sticky="W",padx=10)
Label(page3, text="Value", font=('arial', 10, "bold"), bg="blue", fg="gold", padx=5).grid(row=0, column=1,sticky="W",padx=10)  # Adjust the column placement
Label(page3, text="Price", font=('arial', 10, "bold"), bg="blue", fg="gold").grid(row=0, column=2,sticky="W",padx=20)

# Create a dictionary to store counts and prices
item_info = {}

# Iterate through the list
for select in item:
    if select in item_info:
        item_info[select]["count"] += 1
        item_info[select]["total_price"] += c[item.index(select)]
    else:
        item_info[select] = {"count": 1, "total_price": c[item.index(select)]}

# Iterate through the dictionary and print the results
for select, info in item_info.items():
    count = info["count"]
    total_price = info["total_price"]
    print(f"{select} @{count} {total_price}")
    purchase_amount = total_price
    

i = 0
select_label = Label(page3, text="\n".join([f"{select}" for select, info in item_info.items()]), font=('arial', 10, "bold"), bg="white", fg="black", justify="left")
select_label.grid(row=i + 2, column=0, sticky="W")

count_label = Label(page3, text="\n".join([f"@{info['count']}" for select, info in item_info.items()]), font=('arial', 10, "bold"), bg="white", fg="black")
count_label.grid(row=i + 2, column=1)  # Adjust the column placement

info_label = Label(page3, text="\n".join([f"{info['total_price']}" for select, info in item_info.items()]), font=('arial', 10, "bold"), bg="white", fg="black", justify="left")
info_label.grid(row=i + 2, column=2)

# Calculate and display the total price
total_price = sum(c)
Label(page3, text="_________", font=('arial', 10, 'bold'), bg='white', fg="black").grid(row=len(item) + 1, column=0,sticky="W")
Label(page3, text=f"Total price: {total_price}  Bath", font=('arial', 10, 'bold'), bg='white', fg="black").grid(row=len(item) + 2, column=0,sticky="W",columnspan=1)
dis = sum(c) * 95 / 100
Label(page3, text=f"Net with Discount 5% : \n {dis:.2f}  Bath", font=('arial', 10, 'bold'), bg='white', fg="black").grid(row=len(item) + 3, column=0,sticky="W",columnspan=1)
Label(page3, text="_________", font=('arial', 10, 'bold'), bg='white', fg="black").grid(row=len(item) + 4, column=0,sticky="W")


point = total_price/3000

user_data.append({"username": user,"total":total_price,"points":point})
print({"username":user})
print({"total":total_price})
print({"points":point})
print(user_data)   

Label(page3,text=f"User :{user}", font=('arial', 10, 'bold'), bg='white', fg="black").grid(row=len(item) + 5, column=0,sticky="W")
Label(page3,text=f"total :{total_price} Bath", font=('arial', 10, 'bold'), bg='white', fg="black").grid(row=len(item) + 6, column=0,sticky="W")
Label(page3,text=f"point :{point:.2f} P", font=('arial', 10, 'bold'), bg='white', fg="black").grid(row=len(item) + 7, column=0,sticky="W")

endbtn = Button(page3,text="Exit",font=('arial', 13, 'bold'), bg='red', fg="black",command=page3.destroy).grid(row=len(item) + 7, column=2,sticky="W")

page3.mainloop()
