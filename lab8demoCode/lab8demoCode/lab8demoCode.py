import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from myQueue import myQueue
from myBST import myBST

q = myQueue()
btree = myBST()

def customer_view():
    customer = tk.Toplevel(root)
    customer.title("Customer View")
    customer.geometry("300x300")
    input = tk.Entry(customer)
    input.grid(row=0, column=0)
    queue = ttk.Combobox(customer)
    queue.grid(row=2, column=0)

    def addItem():
        item = input.get()
        q.push(item);
        updateQueue();

    def updateQueue():
        print("")
        queuevalues = q.contents()
        queue['values'] = queuevalues

    button = tk.Button(customer, text="Add Request", command = addItem).grid(row=1, column=0)


def technician_view():
    technician = tk.Toplevel(root)
    technician.title("Technician View")
    technician.geometry("300x300")
    input = tk.Entry(technician)
    input.grid(row=0, column=0)
    BST = ttk.Combobox(technician)
    BST.grid(row=2, column=0)

    def addItem():
        item = input.get()
        print(item)
        btree.clearList()
        btree.insert(item)
        btree.inOrder(btree.getRoot())
        updateBST()

    def updateBST():
        print(btree.getList())
        bstvalues = btree.getList()
        print(bstvalues)
        BST['values'] = bstvalues

    button = tk.Button(technician, text="Add Request", command = addItem).grid(row=1, column=0)

    


root = tk.Tk();
root.title("Start Window")
root.geometry("600x700")

customer_label = tk.Label(root, text="Open Customer View")
customer_label.grid(row=0, column=0)
customer_button = tk.Button(root, command=customer_view)
customer_button.grid(row=1, column=0)

customer_label = tk.Label(root, text="Open Technician View")
customer_label.grid(row=2, column=0)
customer_button = tk.Button(root, command=technician_view)
customer_button.grid(row=3, column=0)

root.mainloop()