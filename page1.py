from tkinter import*
from container import user,user_data

def get_data():   
    user.append(entry.get())
    user_data.append({"username": user})
    
    print(user_data)
    print("Enter user:", user)
    Label(root,text=user).pack()
    if len(user) == 1 :
        print(len(user))
        print(user)
        root.destroy()
        import page2
    
    
root = Tk()
root.geometry("300x150")
root.title("User")
root['bg'] = 'azure3'

label = Label(root, text="Enter user:",font=("arial",15,"bold"),fg="red",bg="azure3")
label.pack()

entry = Entry(root,font=("Arial",15,"bold"),fg="orange",bg="ghostwhite")
entry.pack()
entry.focus()

button = Button(root, text="Enter", command=get_data,font=("Arial",15,"bold"),fg="black",bg="cornsilk1")
button.pack()

buttonnext = Button(root, text="Exit",font=("Arial",15,"bold"),fg="black",bg="red",command=root.destroy)
buttonnext.pack()

root.mainloop()