from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
from itertools import count, cycle
import webbrowser
import datetime
import json

#RainbowColors
colors1 = ["#0000ff", "#0000ff", "#4000ff", "#8000ff", "#bf00ff", "#ff00ff", "#ff00bf",
           "#ff0080", "#ff0040", "#ff0000", "#ff4000", "#ff8000", "#ffbf00",
           "#ffff00", "#bfff00", "#80ff00", "#40ff00", "#00ff00", "#00ff40",
           "#00ff80", "#00ffbf", "#00ffff", "#00bfff", "#0080ff", "#0040ff"]

colors2 = ["#4d4dff", "#4d4dff", "#794dff", "#a64dff", "#d24dff", "#ff4dff", "#ff4dd2",
           "#ff4da6", "#ff4d79", "#ff4d4d", "#ff794d", "#ffa64d", "#ffd24d",
           "#ffff4d", '#d2ff4d', "#a6ff4d", "#79ff4d", "#4dff4d", "#4dff79",
           "#4dffa6", "#4dffd2", "#4dffff", "#4dd2ff", "#4da6ff", "#4d79ff"]

#GetDate
current_time = datetime.datetime.now()
dt_ = str(current_time.day) + " / " + str(current_time.month) + " / " + str(current_time.year)

#StockData
Qt_file = open("Data/Qty_Data.json", "r")
Data = json.load(Qt_file)
Qt_file.close()

#BillData
bill_file = open("Data/Bill.json", "r")
BillData = json.load(bill_file)
bill_file.close()

#Bill-List
BillItems = [""]
for bills in BillData.items():
    BillItems.append(str(bills[0])+" - "+bills[1][0])

#======================================================================================================================>
#                                            LOGIN / SELECTOR
#======================================================================================================================>


class LoginScreen:
    def __init__(self, root, uid, upw):
        self.root = root
        self.root.title("GS-Collections")
        positionRight = int(root.winfo_screenwidth() / 2 - 827 / 2)
        positionDown = int(root.winfo_screenheight() / 2.1 - 475 / 2)
        self.root.geometry('827x475+{}+{}'.format(positionRight, positionDown))
        self.root.resizable(width=False, height=False)
        icon = PhotoImage(file='Data/icon.png')
        self.root.iconphoto(False, icon)
        self.root.config(bg="black")
        self.UserId = uid
        self.UserPw = upw

# ----BG Image-------
        self.bgImg = ImageTk.PhotoImage(file='Data/bg1.jpg')
        Label(self.root, image=self.bgImg).place(x=0, y=0, relwidth=1, relheight=1)
# ----Left Image-------
        self.Limg = ImageTk.PhotoImage(file='Data/GS.png')
        Label(self.root, image=self.Limg).place(x=120, y=120, width=225, height=225)
# ----Login Info------
        frame1 = Frame(self.root, bg="#f5f5f5")
        frame1.place(x=345, y=120, width=362, height=225)
        Label(frame1, text="Login Here", font=("impact", 20), bg="#f5f5f5", fg="green").place(x=100, y=14)
# ----Username------
        Label(frame1, text="Username:", font=("times new roman", 12), bg="#f5f5f5", fg="#424242").place(x=40, y=55)
        self.user_var = Entry(frame1, font=("times new roman", 12), bg="#9e9e9e")
        self.user_var.place(x=43, y=80, width=230)
        self.user_var.focus()
# ----Password------
        Label(frame1, text="Password:", font=("times new roman", 12), bg="#f5f5f5", fg="#424242").place(x=40, y=110)
        self.pw_var = Entry(frame1, font=("times new roman", 12), bg="#9e9e9e", show='*')
        self.pw_var.place(x=43, y=135, width=230)
# ----Login Button------
        self.login_btn = Button(frame1, command=self.login_function, text="Login", font=("times new roman", 14),
                                bg="green", fg="white").place(x=250, y=175, width=80)
        self.root.bind("<Return>", lambda e: self.login_function())

    def login_function(self):
        if self.pw_var.get() == "" or self.user_var.get() == "":
            messagebox.showerror("Error", "Credentials Required!!", parent=self.root)
        elif self.pw_var.get() in self.UserPw and self.user_var.get() in self.UserId:
            self.root.destroy()
            master = Tk()
            Switcher(master)
            master.mainloop()
        else:
            messagebox.showerror("Error", "Username or Password is Incorrect", parent=self.root)


class Switcher:
    def __init__(self, master):
        self.master = master
        self.master.title("GS-Collection Switcher")
        positionRight = int(master.winfo_screenwidth() / 2 - 500 / 2)
        positionDown = int(master.winfo_screenheight() / 2.1 - 300 / 2)
        self.master.geometry('506x316+{}+{}'.format(positionRight, positionDown))
        self.master.resizable(width=False, height=False)
        icon = PhotoImage(file='Data/icon.png')
        self.master.iconphoto(False, icon)
        self.master.config(bg="black")
        self.master.overrideredirect(True)

        c1 = "#f2aa4c"
        c2 = "#101820"
        self.choice_bill = Frame(self.master, bg=c1)
        self.choice_bill.place(x=3, y=3, width=500, height=155)
        self.bill_lbl = Label(self.choice_bill, text="Bill Generator", font=("Century Schoolbook", 34, "bold"),
                              fg=c2, bg=c1)
        self.bill_arw = Label(self.choice_bill, text="", font=("Century Schoolbook", 34, "bold"),
                              fg=c2, bg=c1)
        self.bill_arw.place(x=415, y=57)
        self.bill_lbl.place(x=25, y=50)

        self.choice_inventory = Frame(self.master, bg=c2)
        self.choice_inventory.place(x=3, y=158, width=500, height=155)
        self.store_lbl = Label(self.choice_inventory, text="Inventory", font=("Century Schoolbook", 34, "bold"),
                               fg=c1, bg=c2)
        self.store_arw = Label(self.choice_inventory, text="", font=("Century Schoolbook", 34, "bold"),
                               fg=c1, bg=c2)
        self.store_arw.place(x=415, y=57)
        self.store_lbl.place(x=30, y=50)

        self.bill_lbl.bind("<Button-1>", lambda e: self.bill_window())
        self.bill_arw.bind("<Button-1>", lambda e: self.bill_window())
        self.store_lbl.bind("<Button-1>", lambda e: self.store_window())
        self.store_arw.bind("<Button-1>", lambda e: self.store_window())

    def bill_window(self):
        self.master.destroy()
        self.master = Tk()
        GenerateBill(self.master)
        self.master.mainloop()

    def store_window(self):
        self.master.destroy()
        self.master = Tk()
        InventoryManagement(self.master)
        self.master.mainloop()


#======================================================================================================================>
#                                          INVENTORY MANAGEMENT
#======================================================================================================================>


class InventoryManagement:
    def __init__(self, master):
        self.master = master
        self.master.title("GS-Collections-Inventory-Management")
        positionRight = int(master.winfo_screenwidth() / 2 - 800 / 2)
        positionDown = int(master.winfo_screenheight() / 2.3 - 506 / 2)
        master.geometry("+{}+{}".format(positionRight, positionDown))
        self.master.geometry('800x506+{}+{}'.format(positionRight, positionDown))
        self.master.resizable(width=False, height=False)
        icon = PhotoImage(file='Data/icon.png')
        self.master.iconphoto(False, icon)
        self.master.config(bg="#131339")

# ------2nd Half------
        Frame(self.master, bg='white').place(x=396, y=0, width=1, height=506)
        Frame(self.master, bg='#9f9fc6').place(x=397, y=35, width=403, height=1)
        Frame(self.master, bg='#1d1d30').place(x=397, y=36, width=403, height=1)
        self.SecondHalfFrame = LabelFrame(self.master, text="Available Stock", bg="#131339", fg="white")
        self.SecondHalfFrame.place(x=409, y=40, width=380, height=409)

# ------Style treeview-------
        """style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="#e6e6ff",
                        foreground="black",
                        fieldbackground="#e6e6ff")
        style.map("Treeview")"""

# ------TreeView Table-------
        self.trv = ttk.Treeview(self.SecondHalfFrame, height=18)
        self.trv.place(x=3, y=0)

        self.trv['columns'] = "Quantity"
        self.trv.column("#0", anchor=W, width=250, minwidth=25)
        self.trv.column("Quantity", anchor=CENTER, width=118, minwidth=25)
        self.trv.heading("#0", text="Product Name", anchor=W)
        self.trv.heading("Quantity", text="Quantity")

# ------Total------
        Label(self.master, text="Total Items:", font=("arial", 12, 'bold'), bg="#131339", fg="white").place(x=590, y=7)

        self.TotalItem = Entry(self.master, font=("arial", 12, 'bold'), justify='right', state="disabled")
        self.TotalItem.place(x=690, y=5, width=100, height=25)
        self.add_total()

# ------refresh button------
        self.refreshBtn = Button(self.master, text="Refresh", font=("arial", 10), activebackground="#60609f",
                                 bg="#4d4d80", fg="#cccccc", borderwidth=0, command=self.refresh)
        self.refreshBtn.place(x=483, y=0, width=65, height=35)

# ------Transactions button------
        self.transactionBtn = Button(self.master, text="Transaction", font=("arial", 10), activebackground="#60609f",
                                     bg="#4d4d80", fg="#cccccc", borderwidth=0)
        self.transactionBtn.place(x=397, y=0, width=85, height=35)
        self.transactionBtn.bind("<Button>", lambda e: TransactionsList(self.master))

# ------1st Half------
        self.FirstHalfFrame = Frame(self.master)
        self.FirstHalfFrame.pack(fill=Y, expand=1, anchor='nw')

        self.FirstCanvas = Canvas(self.FirstHalfFrame)
        self.FirstCanvas.pack(side=LEFT, fill=Y, expand=1)
        self.FirstScroll = ttk.Scrollbar(self.FirstHalfFrame, orient=VERTICAL, command=self.FirstCanvas.yview)
        self.FirstScroll.pack(side=RIGHT, fill=Y)
        self.FirstCanvas.configure(yscrollcommand=self.FirstScroll.set)
        self.FirstCanvas.bind('<Configure>',
                              lambda e: self.FirstCanvas.configure(scrollregion=self.FirstCanvas.bbox("all")))

        self.cat_frame = Frame(self.FirstCanvas, bg="#99ebff")

        self.FirstCanvas.create_window((0, 0), window=self.cat_frame, anchor='nw')

        self.first_half(Data)

# ------Add/Remove Buttons------
        self.AddItems = Button(self.master, text="Add New Stock", bg='green', fg='white',
                               activebackground="#32cb00")
        self.AddItems.place(x=608, y=458, height=40, width=180)
        self.AddItems.bind("<Button>", lambda e: AddRemoveItem(self.master, mode="A"))

        self.RemoveItems = Button(self.master, text="Remove from Stock", bg='#c62828', fg='white',
                                  activebackground="#f44336")
        self.RemoveItems.place(x=412, y=458, height=40, width=180)
        self.RemoveItems.bind("<Button>", lambda e: AddRemoveItem(self.master, mode="R"))

    def add_total(self):
        v3 = 0
        for category in Data.items():
            for item in category[1].items():
                for k in item[1].items():
                    v3 += k[1]
        self.TotalItem.config(state="normal")
        self.TotalItem.delete(0, END)
        self.TotalItem.insert(0, str(v3) + " ")
        self.TotalItem.config(state="disabled")

    def refresh(self):
        qt_file = open("Data/Qty_Data.json", "r")
        Data_New = json.load(qt_file)
        qt_file.close()

        v3 = 0
        for category in Data_New.items():
            for item in category[1].items():
                for k in item[1].items():
                    v3 += k[1]
        self.TotalItem.config(state="normal")
        self.TotalItem.delete(0, END)
        self.TotalItem.insert(0, v3)
        self.TotalItem.config(state="disabled")

        self.first_half(Data_New)
        self.toStore(" ")

    def first_half(self, data_new):
        categories = data_new.keys()
        for i, category in enumerate(categories):
            if category != "Other":
                v1 = 0
                for item in Data[category].items():
                    for k in item[1].items():
                        v1 += k[1]
                cidx = i % 24
                self.itmbtn = Button(self.cat_frame, text="  " + category, font=('arial', 18, 'bold'), bg=colors2[cidx],
                                     anchor="w", height=1, width=15, activebackground=colors1[cidx],
                                     command=lambda cat=category: self.toStore(cat))
                self.itmbtn.grid(row=i, column=1, padx=10, pady=6)
                self.qtybtn = Button(self.cat_frame, text=str(v1) + "  ", font=('arial', 18), bg=colors2[cidx],
                                     height=1, width=7, activebackground=colors1[cidx], anchor="e",
                                     command=lambda cat=category: self.toStore(cat))
                self.qtybtn.grid(row=i, column=2, padx=10, pady=6)

# --Generate tree------
    def toStore(self, category):
        for old_item in self.trv.get_children():
            self.trv.delete(old_item)

        if category == " ":
            return

        PCount = int(100001)
        CCount = 1

        for item in Data[category].items():
            v2 = 0
            for k in item[1].items():
                v2 += k[1]
            if item[0] != "Other":
                self.trv.insert(parent="", index=END, text=item[0], iid=PCount, values=v2)
            for k in item[1].items():
                if k[0] != "Other":
                    self.trv.insert(parent=PCount, index=END, text=k[0], iid=CCount, values=k[1])
                CCount += 1
            PCount += 1


class AddRemoveItem(Toplevel):
    def __init__(self, master=None, mode=None):
        super().__init__(master=master)
        self.mode = mode
        positionRight = int(master.winfo_screenwidth() / 2 - 700 / 2)
        positionDown = int(master.winfo_screenheight() / 3.8 - 170 / 2)
        if self.mode == "A":
            self.title("Add Products")
        elif self.mode == "R":
            self.title("Remove Products")
        self.geometry("700x170+{}+{}".format(positionRight, positionDown))
        self.resizable(width=False, height=False)
        icon = PhotoImage(file='Data/icon.png')
        self.iconphoto(False, icon)

        # ------Category-----
        Label(self, text="Category:", font=("times new roman", 13)).place(x=20, y=20)
        self.var1 = StringVar()
        self.Category = ttk.Combobox(self, font=("times new roman", 12), textvariable=self.var1, state="readonly")
        self.Category.place(x=20, y=50, width=120)
        self.Category['values'] = tuple(Data.keys())
        self.Category_Other = Entry(self, font=("times new roman", 12), bg="white", state='disabled')
        self.Category_Other.place(x=20, y=85, width=120)

        self.Category.bind("<<ComboboxSelected>>", self.pick_item)

        # ------Item---------
        Label(self, text="Item:", font=("times new roman", 13)).place(x=160, y=20)
        self.var2 = StringVar()
        self.Item = ttk.Combobox(self, font=("times new roman", 12), textvariable=self.var2, state="readonly")
        self.Item.place(x=160, y=50, width=120)
        self.Item['values'] = [" "]
        self.Item.current(0)
        self.Item_Other = Entry(self, font=("times new roman", 12), bg="white", state='disabled')
        self.Item_Other.place(x=160, y=85, width=120)

        self.Item.bind("<<ComboboxSelected>>", self.pick_size)

        # ------Size------
        Label(self, text="Sizes:", font=("times new roman", 13)).place(x=300, y=20)
        self.var3 = StringVar()

        if self.mode == "A":
            self.Size = ttk.Combobox(self, font=("times new roman", 12), textvariable=self.var3, state="readonly")
            self.Size.place(x=300, y=50, width=120)
            self.Size['values'] = ["  "]
            Label(self, text="(Eg: M,L,XL or 32,34,36)", font=("arial", 9), fg="#bdbdbd").place(x=345, y=23)
            self.Size_Other = Entry(self, font=("times new roman", 12), bg="white", state="disabled")
            self.Size_Other.place(x=300, y=85, width=120)
        elif self.mode == "R":
            self.Size = ttk.Combobox(self, font=("times new roman", 12), textvariable=self.var3, state="readonly")
            self.Size.place(x=300, y=50, width=120)
            self.Size['values'] = ["  "]

        self.Size.bind("<<ComboboxSelected>>", self.actvt_size)

        # ------Quantity-----
        Label(self, text="Quantity", font=("times new roman", 13)).place(x=605, y=20)
        self.Quantity = Entry(self, font=("times new roman", 13), justify='right', bg="white")
        self.Quantity.place(x=550, y=50, width=120)

        self.Quantity.bind('<KeyPress>', self.keybind1)

        # ------Price------
        Label(self, text="Price:", font=("times new roman", 14, "bold")).place(x=20, y=125)
        self.Price = Entry(self, font=("times new roman", 14), justify='right', bg="white")
        self.Price.place(x=80, y=128, width=120)

        self.Price.bind('<KeyPress>', self.keybind1)

        # ------Add/Remove Button------
        if self.mode == "A":
            self.add = Button(self, text="Add Product", bg='green', fg='white',
                              activebackground="#32cb00", command=self.add_remove_data)
            self.add.place(x=550, y=115, width=120, height=40)
        elif self.mode == "R":
            self.remove = Button(self, text="Remove Product", bg='#c62828', fg='white',
                                 activebackground="#f44336", command=self.add_remove_data)
            self.remove.place(x=550, y=115, width=120, height=40)

    def add_remove_data(self):
        if self.Category.get() == "":
            messagebox.showerror("Invalid Data", "Select an Category to proceed", parent=self)
            return
        elif self.Category.get() == "Other":
            if self.Item_Other.get() == "" or self.Category_Other.get() == "":
                messagebox.showerror("Invalid Data", "Enter Data in Category to proceed", parent=self)
                return
        elif self.Item.get() == "":
            messagebox.showerror("Invalid Data", "Select an Item to proceed", parent=self)
            return
        elif self.Item.get() == "Other":
            if self.Item_Other.get() == "":
                messagebox.showerror("Invalid Data", "Enter Data in Item to proceed", parent=self)
                return
        elif self.Quantity.get() == "":
            messagebox.showerror("Invalid Data", "Enter quantity to proceed", parent=self)
            return
        elif self.Price.get() == "":
            messagebox.showerror("Invalid Data", "Enter price to proceed", parent=self)
            return

        if self.mode == "R":
            if self.Size.get() == "Other" or self.Item.get() == "Other" or self.Category.get() == "Other":
                messagebox.showerror("Invalid Data", parent=self, message="Cannot remove data from other")
                return

        qtty = int(self.Quantity.get())
        Cprice = int(self.Price.get())

        if self.Category.get() == "Other":
            catgry = self.Category_Other.get()
            itm = self.Item_Other.get()
            siz = self.Size_Other.get()
            Data[catgry] = dict()
            Data[catgry]["Other"] = dict()
            Data[catgry][itm] = dict()
            Data[catgry]["Other"]["Other"] = 0
            Data[catgry][itm]["Other"] = 0
            Data[catgry][itm][siz] = 0

        elif self.Item.get() == "Other":
            catgry = self.Category.get()
            itm = self.Item_Other.get()
            siz = self.Size_Other.get()
            Data[catgry][itm] = dict()
            Data[catgry][itm][siz] = 0
            Data[catgry][itm]["Other"] = 0
        elif self.Size.get() == "Other":
            catgry = self.Category.get()
            itm = self.Item.get()
            siz = self.Size_Other.get()
            Data[catgry][itm][siz] = 0
        else:
            catgry = self.Category.get()
            itm = self.Item.get()
            siz = self.Size.get()

        if self.mode == "A":
            Data[catgry][itm][siz] += qtty
        elif self.mode == "R":
            new_qty = Data[catgry][itm][siz] - qtty
            if new_qty < 0:
                messagebox.showerror("Invalid Data", parent=self,
                                     message="The Quantity you are trying to remove\nis more than item in stock")
                return
            else:
                Data[catgry][itm][siz] = new_qty
        self.destroy()

#------Into the db------
        newData = open("Data/Qty_Data.json", "w")
        json.dump(Data, newData)
        newData.close()

#-------Read Transaction
        TransFile = open("Data/Transactions.json", "r")
        newTrans = json.load(TransFile)
        TransFile.close()

        month = ["", "January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]

        Tdt_ = str(current_time.day) + " " + month[int(current_time.month)] + " " + str(current_time.year)

        trans = []
        if self.mode == "A":
            trans = ["add", catgry + " " + itm + " " + siz, qtty, Cprice*qtty, 0]
        elif self.mode == "R":
            trans = ["remove", catgry + " " + itm + " " + siz, qtty, Cprice*qtty, 0]

        transNo = "Trans_1"
        try:
            if newTrans[Tdt_]:
                transNo = "Trans_" + str(int(list(newTrans[Tdt_].keys())[-1].split("_")[1]) + 1)
        except KeyError:
            newTrans[Tdt_] = dict()
        newTrans[Tdt_][transNo] = trans

# ------Into the transaction------
        TransFile = open("Data/Transactions.json", "w")
        json.dump(newTrans, TransFile)
        TransFile.close()

    def keybind1(self, event):
        v = event.char
        try:
            v = int(v)
        except ValueError:
            if v != "\x08" and v != "":
                return "break"

    def actvt_size(self, event):
        if self.mode == "A":
            if self.Size.get() == "Other":
                self.Size_Other.config(state="normal")
            else:
                self.Size_Other.delete(0, END)
                self.Size_Other.config(state="disabled")

    def pick_size(self, event):
        if self.Item.get() == "Other":
            self.Item_Other.config(state="normal")
            self.Size.config(state="disabled")
            if self.mode == "A":
                self.Size.config(state="disabled")
                self.Size_Other.config(state="normal")
                self.Size_Other.delete(0, END)
        else:
            self.Item_Other.delete(0, END)
            self.Item_Other.config(state="disabled")
            self.Size.config(value=tuple(Data[self.Category.get()][self.Item.get()].keys()))
            self.Size.config(state="readonly")
            if self.mode == "A":
                self.Size_Other.config(state="readonly")

    def pick_item(self, event):
        if self.Category.get() == "Other":
            self.Category_Other.config(state="normal")
            self.Item_Other.config(state="normal")
            if self.mode == "A":
                self.Size_Other.config(state="normal")
            self.Item.delete(0, END)
            self.Size.delete(0, END)
            self.Item.config(state="disabled")
            self.Size.config(state="disabled")
        else:
            self.Item.config(state="readonly")
            self.Item.delete(0, END)
            self.Size.config(state="readonly")
            self.Item.config(value=tuple(Data[self.Category.get()].keys()))

            self.Category_Other.delete(0, END)
            self.Item_Other.delete(0, END)
            self.Size_Other.delete(0, END)
            self.Size_Other.config(state="disabled")
            self.Category_Other.config(state="disabled")
            self.Item_Other.config(state="disabled")


class TransactionsList(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Transcations")
        positionRight = int(master.winfo_screenwidth() / 2 - 525 / 2)
        positionDown = int((master.winfo_screenheight() / 2.2 - 555 / 2) - 10)
        self.geometry('525x558+{}+{}'.format(positionRight, positionDown))
        self.resizable(width=False, height=False)
        icon = PhotoImage(file='Data/icon.png')
        self.iconphoto(False, icon)
        self.config(bg="#131339")

# ------TableFrame------
        self.TableFrame = LabelFrame(self, text="Transactions List", bg="#131339", fg="white")
        self.TableFrame.place(x=10, y=5, width=505, height=492)

# ------TreeView Table-------
        self.trv2 = ttk.Treeview(self.TableFrame, height=22)
        self.trv2.pack(fill=Y, side=LEFT)
        self.trv2.place(x=3, y=3)

        self.trv2['columns'] = ("Quantity", "Purchase", "Sales")
        self.trv2.column("#0", anchor=W, width=267, minwidth=150)
        self.trv2.column("Quantity", anchor=CENTER, width=60, minwidth=80)
        self.trv2.column("Purchase", anchor=E, width=70, minwidth=80)
        self.trv2.column("Sales", anchor=E, width=80, minwidth=80)

        self.trv2.heading("#0", text="Transaction", anchor=W)
        self.trv2.heading("Quantity", text="Quantity", anchor=CENTER)
        self.trv2.heading("Purchase", text="Purchase", anchor=CENTER)
        self.trv2.heading("Sales", text="Sales", anchor=CENTER)

        self.vsb = ttk.Scrollbar(self.TableFrame, orient="vertical", command=self.trv2.yview)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.trv2.configure(yscrollcommand=self.vsb.set)

# ------Insert Data into Table------
        self.gen_trv2()

# ------Help box-------
        self.HelpFrame = LabelFrame(self, text="Help Box", bg="#131339", fg="white")
        self.HelpFrame.place(x=10, y=501, width=505, height=50)
        Frame(self.HelpFrame, bg="#66ff66").place(x=10, y=9, height=10, width=10)
        Frame(self.HelpFrame, bg="#ff6666").place(x=180, y=9, height=10, width=10)
        Frame(self.HelpFrame, bg="#ffc266").place(x=360, y=9, height=10, width=10)
        Label(self.HelpFrame, bg="#131339", fg="white", text="Added to stock",
              font=("ariel", "9")).place(x=25, y=3)
        Label(self.HelpFrame, bg="#131339", fg="white", text="Removed from stock",
              font=("ariel", "9")).place(x=195, y=3)
        Label(self.HelpFrame, bg="#131339", fg="white", text="Bill transaction",
              font=("ariel", "9")).place(x=375, y=3)

    def gen_trv2(self):
        trans_data = open("Data/Transactions.json", 'r')
        transactions = json.load(trans_data)
        trans_data.close()

        Scount = int(100000001)
        Pcount = int(100001)
        Ccount = 1

        self.trv2.tag_configure("add", background="#ccffcc")
        self.trv2.tag_configure("remove", background="#ffcccc")
        self.trv2.tag_configure("bill", background="#ffebcc")

        self.trv2.delete(*self.trv2.get_children())

        for transaction in transactions.items():
            dt_purchase = 0
            dt_sales = 0
            dt_qty = 0
            for transn in transaction[1].items():
                if transn[1][0] == 'add':
                    dt_purchase += transn[1][3]
                    dt_qty += transn[1][2]
                elif transn[1][0] == 'remove':
                    dt_purchase -= transn[1][3]
                    dt_qty -= transn[1][2]
                elif transn[1][0] == 'bill':
                    dt_qty -= transn[1][2]
                dt_sales += transn[1][4]

            v1 = (dt_qty, dt_purchase, dt_sales)
            self.trv2.insert(parent="", index=END, text=transaction[0], iid=Scount, values=v1)

            for transns in transaction[1].items():
                if transns[1][3] == 0:
                    v2 = (transns[1][2], "-", transns[1][4])
                elif transns[1][4] == 0:
                    if transns[1][0] == 'add':
                        t1 = "+"+str(transns[1][3])
                    elif transns[1][0] == 'remove':
                        t1 = "-"+str(transns[1][3])
                    else:
                        t1 = str(transns[1][3])
                    v2 = (transns[1][2], t1, "-")
                else:
                    v2 = (transns[1][2], transns[1][3], transns[1][4])

                if transns[1][0] == 'add':
                    self.trv2.insert(parent=Scount, index=END, text=transns[1][1], iid=Pcount, values=v2,
                                     tags=('add',))
                elif transns[1][0] == 'remove':
                    self.trv2.insert(parent=Scount, index=END, text=transns[1][1], iid=Pcount, values=v2,
                                     tags=('remove',))
                elif transns[1][0] == 'bill':
                    self.trv2.insert(parent=Scount, index=END, text=transns[1][1], iid=Pcount, values=v2,
                                     tags=('bill',))

                if transns[1][0] == 'bill':
                    bill_file = open("Data/Bill.json")
                    bill_data = json.load(bill_file)
                    bill_file.close()

                    bill_no = transns[1][1].split(" ")[1]
                    items = bill_data[bill_no][2]
                    qtty = bill_data[bill_no][3]
                    amts = bill_data[bill_no][5]

                    bill_no_data = []
                    for i in range(len(items)):
                        bill_no_data.append([items[i], qtty[i], amts[i]])
                    for i in range(len(bill_no_data)):
                        tbv = (bill_no_data[i][1], "-", bill_no_data[i][2])
                        self.trv2.insert(parent=Pcount, index=END, text=bill_no_data[i][0], iid=Ccount, values=tbv,
                                         tags=('bill',))
                        Ccount += 1
                Pcount += 1
            Scount += 1


#======================================================================================================================>
#                                              BILL GENERATOR
#======================================================================================================================>


class GenerateBill:

    def __init__(self, master):
        self.master = master
        self.master.title("GS-Collections-Bill-Generator")
        positionRight = int(master.winfo_screenwidth() / 2 - 1100 / 2)
        positionDown = int(master.winfo_screenheight() / 2.1 - 650 / 2)
        self.master.geometry('1100x650+{}+{}'.format(positionRight, positionDown))
        self.master.resizable(width=False, height=False)
        icon = PhotoImage(file='Data/icon.png')
        self.master.iconphoto(False, icon)

# ------Body--------------
        BF1 = Frame(self.master, bg="#e0e0e0").place(x=0, y=40, relwidth=660, height=550)  # bg

# ------Border--------
        Frame(self.master, bg="#a4a4a4").place(x=10, y=50, width=570, height=2)    # h1
        Frame(self.master, bg="#a4a4a4").place(x=10, y=160, width=570, height=2)  # h2
        Frame(self.master, bg="#a4a4a4").place(x=10, y=570, width=572, height=2)  # h3
        Frame(self.master, bg="#a4a4a4").place(x=10, y=50, width=2, height=520)   # v1
        Frame(self.master, bg="#a4a4a4").place(x=580, y=50, width=2, height=520)  # v2

        Frame(self.master, bg="#a4a4a4").place(x=368, y=520, width=214, height=2)  # h4
        Frame(self.master, bg="#a4a4a4").place(x=368, y=520, width=2, height=52)  # v5

# ------Name----------
        Label(BF1, text="Customer Name:", bg="#e0e0e0", font=("times new roman", 13)).place(x=25, y=70)
        self.CustName = Entry(BF1, font=("times new roman", 14), bg="white")
        self.CustName.place(x=150, y=71, width=380)
        self.CustName.focus()

# ------Phone No.-----
        Label(BF1, text="Phone Number:", bg="#e0e0e0", font=("times new roman", 12)).place(x=25, y=110)
        self.CountryCode = Entry(BF1, font=("times new roman", 12), bg="white")
        self.CountryCode.place(x=150, y=111, width=33)
        self.CountryCode.insert(0, "+91")
        self.CustNo = Entry(BF1, font=("times new roman", 12), bg="white")
        self.CustNo.place(x=190, y=111, width=130)
        self.CustNo.bind('<KeyPress>', self.keybind1)

# ------Category-----
        Label(BF1, text="Category:", bg="#e0e0e0", font=("times new roman", 13)).place(x=40, y=190)
        self.var1 = StringVar()
        self.Category = ttk.Combobox(BF1, font=("times new roman", 12), textvariable=self.var1, state="readonly")
        self.Category.place(x=165, y=191, width=120)
        self.Category['values'] = list(Data.keys())
        self.Category_Other = Entry(BF1, font=("times new roman", 12), bg="white", state='disabled')
        self.Category_Other.place(x=335, y=191, width=150)

        self.Category.bind("<<ComboboxSelected>>", self.pick_item)

# ------Item---------
        Label(BF1, text="Item:", bg="#e0e0e0", font=("times new roman", 13)).place(x=40, y=230)
        self.var2 = StringVar()
        self.Item = ttk.Combobox(BF1, font=("times new roman", 12), textvariable=self.var2, state="readonly")
        self.Item.place(x=165, y=231, width=120)
        self.Item['values'] = [" "]
        self.Item.current(0)
        self.Item_Other = Entry(BF1, font=("times new roman", 12), bg="white", state='disabled')
        self.Item_Other.place(x=335, y=231, width=150)

        self.Item.bind("<<ComboboxSelected>>", self.pick_size)

# ------Size------
        Label(BF1, text="Size:", bg="#e0e0e0", font=("times new roman", 13)).place(x=40, y=270)
        self.var3 = StringVar()
        self.Size = ttk.Combobox(BF1, font=("times new roman", 12), textvariable=self.var3, state="readonly")
        self.Size.place(x=165, y=271, width=120)
        self.Size['values'] = ["  "]
        self.Size.current(0)
        self.Size_Other = Entry(BF1, font=("times new roman", 12), bg="white", state='disabled')
        self.Size_Other.place(x=335, y=271, width=150)

        self.Size.bind("<<ComboboxSelected>>", self.actvt_size)

# ------Quantity-----
        Label(BF1, text="Quantity:", bg="#e0e0e0", font=("times new roman", 13)).place(x=40, y=310)
        self.Quantity = Entry(BF1, font=("times new roman", 12), justify='center')
        self.Quantity.insert(0, 1)
        self.Quantity.place(x=190, y=311, width=65)
        self.decBtn = Button(BF1, text="-", bg="#e0e0e0", font=("times new roman", 14, "bold"),
                             borderwidth=1.5, command=self.decQty)
        self.decBtn.place(x=165, y=311, width=25, height=24)
        self.incBtn = Button(BF1, text="+", bg="#e0e0e0", font=("times new roman", 14, "bold"),
                             borderwidth=1.5, command=self.incQty)
        self.incBtn.place(x=255, y=311, width=25, height=24)
        self.Quantity.bind('<KeyPress>', self.keybind1)

# ------Price--------
        Label(BF1, text="Price:", bg="#e0e0e0", font=("times new roman", 13)).place(x=40, y=350)
        Label(BF1, text="₹", bg="#e0e0e0", font=("times new roman", 13, 'bold')).place(x=164, y=350)
        self.Price = Entry(BF1, font=("times new roman", 12), justify='right')
        self.Price.place(x=180, y=351, width=120)
        self.Price.bind('<KeyPress>', self.keybind1)

# ------Payment Method---
        Label(BF1, text="Payment:", bg="#e0e0e0", font=("times new roman", 15, 'bold')).place(x=40, y=530)
        self.var4 = StringVar()
        self.payment = ttk.Combobox(BF1, font=("times new roman", 13), textvariable=self.var4, state="readonly")
        self.payment.place(x=145, y=532, width=160)
        self.payment['values'] = ["Cash", "Debit/Credit Card", "UPI", "Paytm", "Other"]
        self.payment.bind('<<ComboboxSelected>>', self.pymt)

# ------Total Price------
        Label(BF1, text="Total:", bg="#e0e0e0", font=("times new roman", 18, 'bold')).place(x=375, y=530)
        Label(BF1, text="₹", bg="#e0e0e0", font=("times new roman", 18, 'bold')).place(x=450, y=531)
        self.Total = Entry(BF1, font=("times new roman", 18, 'bold'), justify='right')
        self.Total.place(x=470, y=531, width=100)
        self.Total.config(state="readonly")

# ------Seperating Line-----
        Frame(self.master, bg="white").place(x=657, y=40, width=3, height=550)

# ------Item(Add/Remove) Button-------
        Button(self.master, bg="#bdbdbd", fg="#494949", text="ADD\nTO\nBILL", font=("times new roman", 12, 'bold'),
               borderwidth=0, command=self.add_to_bill).place(x=595, y=170, width=62, height=140)
        Button(self.master, bg="#bdbdbd", fg="#494949", text="CUT\nBACK", font=("times new roman", 12, 'bold'),
               borderwidth=0, command=self.remove_from_bill).place(x=595, y=320, width=62, height=140)

# ------Bill View--------
        Frame(self.master, bg="#e0e0e0").place(x=660, y=40, relwidth=2 / 5, height=550)
        Frame(self.master, bg="#4f342d").place(x=660, y=40, relwidth=2 / 5, height=60)
        Frame(self.master, bg="#4f342d").place(x=660, y=530, relwidth=2 / 5, height=60)

    #---Bill------------
        self.BillFrame = Frame(self.master, bg="white")
        self.BillFrame.place(x=685, y=75, width=395, height=490)

    #---Shop Info-------
        Label(self.BillFrame,text="GS",font=("georgia", 42,'bold'),bg="white",fg='#c30000',justify='left') \
            .place(x=55, y=3, height=70, width=120)
        Label(self.BillFrame, text="COLLECTIONS", font=("impact", 22), bg="white", justify='left') \
            .place(x=155, y=10, height=70, width=180)

    #---Customer Details---
        Label(self.BillFrame, text="Customer:", font=("arial", 9, 'bold'), bg="white", justify='left') \
            .place(x=4, y=68, height=30)
        Frame(self.BillFrame, bg="#a4a4a4").place(x=77, y=90, width=180, height=1)
        self.Cust_name = Label(self.BillFrame, font=("arial", 8), bg="white", text=" ")
        self.Cust_name.place(x=79, y=70)
        Label(self.BillFrame, text="Phone No:", font=("arial", 9, 'bold'), bg="white", justify='left') \
            .place(x=4, y=91, height=30)
        Frame(self.BillFrame, bg="#a4a4a4").place(x=77, y=114, width=120, height=1)
        self.Cust_no = Label(self.BillFrame, font=("arial", 8), bg="white", text=" ")
        self.Cust_no.place(x=78, y=94)
        self.Bill_dt = Label(self.BillFrame, text=dt_, font=("arial", 9, 'bold'), bg="white", justify='right')
        self.Bill_dt.place(x=321, y=94)
        self.billno = self.bill_no()
        Label(self.BillFrame, text="Bill No.", font=("arial", 9, 'bold'), bg="white", justify='right')\
            .place(x=321, y=74)
        self.billLabel = Label(self.BillFrame, text=self.billno, font=("arial", 9, 'bold'), bg="white", justify='left')
        self.billLabel.place(x=365, y=74)

    #---Header------
        Label(self.BillFrame, text="Sr.\nNo.", font=("arial", 9), bg="#a4a4a4", justify='left')\
            .place(x=0, y=120, width=30, height=30)
        Label(self.BillFrame, text="Description", font=("arial", 10), bg="#a4a4a4", justify='center') \
            .place(x=30, y=120, width=190, height=30)
        Label(self.BillFrame, text="Qty.", font=("arial", 10), bg="#a4a4a4", justify='center') \
            .place(x=220, y=120, width=35, height=30)
        Label(self.BillFrame, text="Unit Cost", font=("arial", 10), bg="#a4a4a4", justify='center') \
            .place(x=255, y=120, width=65, height=30)
        Label(self.BillFrame, text="Amount", font=("arial", 10), bg="#a4a4a4", justify='center') \
            .place(x=320, y=120, width=75, height=30)

    #---Serial Number---
        self.sr_no = Listbox(self.BillFrame, font=("arial", 10), bg="white", state="disabled", justify='center')
        self.sr_no.place(x=0, y=150, width=40, height=280)
    # ---Bill Item---
        self.bill_item = Listbox(self.BillFrame, font=("arial", 10), bg="white", state="normal", justify='left')
        self.bill_item.place(x=30, y=150, width=190, height=280)
    # ---Bill Quantity---
        self.qty = Listbox(self.BillFrame, font=("arial", 10), bg="white", state="disabled", justify='center')
        self.qty.place(x=220, y=150, width=35, height=280)
    # ---Bill Cost/Unit---
        self.cost_unit = Listbox(self.BillFrame, font=("arial", 10), bg="white", state="disabled", justify='right')
        self.cost_unit.place(x=255, y=150, width=65, height=280)
    # ---Bill Total cost---
        self.total_cost = Listbox(self.BillFrame, font=("arial", 10), bg="white", state="disabled", justify='right')
        self.total_cost.place(x=320, y=150, width=75, height=280)

        self.bill_item.bind('<<ListboxSelect>>', self.getidx)
    # ---Sum Total------
        Label(self.BillFrame, text="Total:", font=("arial", 11, 'bold', 'underline'), bg="white", justify='left')\
            .place(x=237, y=435)
        self.sum_amt = Entry(self.BillFrame, font=("arial", 11), bg="white", state="disabled")
        self.sum_amt.place(x=305, y=430, width=90, height=30)
    # ---Payment method----
        Label(self.BillFrame, text="Payment Method:", font=("arial", 11, 'bold', 'underline'), bg="white", justify='left')\
            .place(x=90, y=465)
        self.pay_mtd = Entry(self.BillFrame, font=("arial", 11), bg="white", state="disabled")
        self.pay_mtd.place(x=235, y=460, width=160, height=30)

# ------Header-----------
        Frame(self.master, bg="orange").place(x=0, y=0, relwidth=1, height=40)

        self.var4 = StringVar()
        self.searchbox = ttk.Combobox(self.master, font=("times new roman", 12), textvariable=self.var4,
                                      state="readonly", height=12)
        self.searchbox.place(x=190, y=9, width=200)
        self.searchbox['values'] = BillItems
        self.searchbox.current(0)

        self.newBtn = Button(self.master, text="New", bg="orange", fg="black", activebackground="#d84315",
                             font=("times new roman", 12), borderwidth=0, command=self.new_bill)
        self.newBtn.place(x=5, y=0, width=55, height=40)
        self.openBtn = Button(self.master, text="Open", bg="orange", fg="black", activebackground="#d84315",
                              font=("times new roman", 12), borderwidth=0,
                              command=self.load_bill)
        self.openBtn.place(x=120, y=0, width=60, height=40)
        self.saveBtn = Button(self.master, text="Save", bg="orange", fg="black", activebackground="#d84315",
                              font=("times new roman", 12), borderwidth=0, command=self.save_bill)
        self.saveBtn.place(x=60, y=0, width=60, height=40)

        dev_icon = PhotoImage(file='Data/dev_icon2.png')
        self.devBtn = Button(self.master, bg="orange", fg="black", image=dev_icon, borderwidth=0,
                             activebackground="#c56000", justify="center")
        self.devBtn.place(x=1055, y=0, width=45, height=40)
        self.devBtn.image = dev_icon
        self.devBtn.bind("<Button>", lambda e: DeveloperCard(self.master))

# ------Bottom-------
    # ---Print---
        Frame(self.master, bg="yellow").place(x=0, y=590, relwidth=1, height=60)

        self.bill_btn = Button(self.master, text="Print", bg="#7b5e57", font=("times new roman", 16),
                               command=self.print_bill)
        self.bill_btn.place(x=930, y=600, width=130, height=40)

#---------------------------------------------------------------------------------------------------------------------->
#                                                METHOD DEFINITIONS
#---------------------------------------------------------------------------------------------------------------------->

        self.idx = int()
        self.item_list = []
        self.qty_list = []
        self.cost_list = []
        self.tcost_list = []

    def keybind1(self, event):
        v = event.char
        try:
            v = int(v)
        except ValueError:
            if v != "\x08" and v != "":
                return "break"

    def incQty(self):
        value = int(self.Quantity.get())
        value += 1
        self.Quantity.delete(0, 'end')
        self.Quantity.insert(0, value)
        if int(self.Quantity.get()) > 1:
            self.decBtn["state"] = NORMAL

    def decQty(self):
        if int(self.Quantity.get()) <= 1:
            self.decBtn["state"] = DISABLED
            return
        value = int(self.Quantity.get())
        value -= 1
        self.Quantity.delete(0, 'end')
        self.Quantity.insert(0, value)

    def pymt(self, event):
        p = (self.payment.get())
        self.pay_mtd.config(state="normal")
        self.pay_mtd.delete(0, END)
        self.pay_mtd.insert(0, p)
        self.pay_mtd.config(state="disabled")

    def pick_item(self, event):
        if self.Category.get() == "Other":
            self.Category_Other.config(state="normal")
            self.Item_Other.config(state="normal")
            self.Size_Other.config(state="normal")
            self.Item.delete(0, END)
            self.Size.delete(0, END)
            self.Size.config(state="disabled")
            self.Item.config(state="disabled")
        else:
            self.Item.config(state="readonly")
            self.Size.config(state="readonly")
            self.Item.delete(0, END)
            self.Item.config(value=tuple(Data[self.Category.get()].keys()))
            self.Item_Other.delete(0, END)
            self.Size_Other.delete(0, END)
            self.Size_Other.config(state="disabled")
            self.Category_Other.config(state="disabled")
            self.Item_Other.config(state="disabled")

    def actvt_size(self, event):
        if self.Size.get() == "Other":
            self.Size_Other.config(state="normal")
        else:
            self.Size_Other.delete(0, END)
            self.Size_Other.config(state="disabled")

    def pick_size(self, event):
        if self.Item.get() == "Other":
            self.Item_Other.config(state="normal")
            self.Size.config(state="disabled")

            self.Size.config(state="disabled")
            self.Size_Other.config(state="normal")
            self.Size_Other.delete(0, END)
        else:
            self.Item_Other.delete(0, END)
            self.Item_Other.config(state="disabled")
            self.Size.config(value=tuple(Data[self.Category.get()][self.Item.get()].keys()))
            self.Size.config(state="readonly")
            self.Size_Other.config(state="disabled")

    def chk_details(self):
        if self.CustName.get() == "":
            messagebox.showerror("Invalid Data", "Enter Name and Phone No.", parent=self.master)
            return False
        elif len(self.CustNo.get()) != 10:
            messagebox.showerror("Invalid Data", "Type a correct Phone No.", parent=self.master)
            return False
        elif self.Category.get() == "":
            messagebox.showerror("Invalid Data", "Select an Category to proceed", parent=self.master)
            return False
        elif self.Category.get() == "Other":
            if self.Item_Other.get() == "" or self.Category_Other.get() == "":
                messagebox.showerror("Invalid Data", "Enter Data in Category to proceed", parent=self.master)
                return False
        elif self.Item.get() == "":
            messagebox.showerror("Invalid Data", "Select an Item to proceed", parent=self.master)
            return False
        elif self.Item.get() == "Other":
            if self.Item_Other.get() == "":
                messagebox.showerror("Invalid Data", "Enter Data in Item to proceed", parent=self.master)
                return False
        elif self.Size.get() == "":
            messagebox.showerror("Invalid Data", "Select an Size to proceed", parent=self.master)
            return False
        elif self.Size.get() == "Other":
            if self.Size_Other.get() == "":
                messagebox.showerror("Invalid Data", "Enter Data in Size to proceed", parent=self.master)
                return False
        elif self.Price.get() == "":
            messagebox.showerror("Invalid Data", "Enter Item price to proceed", parent=self.master)
            return False
        else:
            return True

    def add_to_bill(self):
        if self.chk_details() == False:
            return

    #-------Description String------
        if self.Category.get() == "Other":
            item = [self.Category_Other.get(), self.Item_Other.get(), self.Size_Other.get()]
        elif self.Item.get() == "Other":
            item = [self.Category.get(), self.Item_Other.get(), self.Size_Other.get()]
        elif self.Size.get() == "Other":
            item = [self.Category.get(), self.Item.get(), self.Size_Other.get()]
        else:
            item = [self.Category.get(), self.Item.get(), self.Size.get()]

        Qty = int(self.Quantity.get())
        Cost = int(self.Price.get())
        self.format_bill(qnty=Qty, cost=Cost, item=item, mode="add")

        CName = str(self.CustName.get())
        self.Cust_name["text"] = CName
        CNumber = str(self.CountryCode.get()) + " " + str(self.CustNo.get())
        self.Cust_no["text"] = CNumber

        self.Category.delete(0, END)
        self.Item.delete(0, END)
        self.Size.delete(0, END)
        self.Category_Other.config(state="normal")
        self.Item_Other.config(state="normal")
        self.Size_Other.config(state="normal")
        self.Category_Other.delete(0, END)
        self.Item_Other.delete(0, END)
        self.Size_Other.delete(0, END)
        self.Category_Other.config(state="disabled")
        self.Item_Other.config(state="disabled")
        self.Size_Other.config(state="disabled")
        self.Quantity.delete(0, END)
        self.Quantity.insert(0, 1)
        self.Price.delete(0, END)

    def getidx(self, event):
        self.idx = self.item_list.index((self.bill_item.get(self.bill_item.curselection())).split(" "))

    def remove_from_bill(self):
        indx = self.idx
        self.format_bill(idx=indx, mode="remove", item=[])

    def format_bill(self, item, qnty=0, cost=0, mode="", idx=0):
        if mode == "add":
            self.item_list.append(item)
            self.qty_list.append(qnty)
            self.cost_list.append(cost)
            self.tcost_list.append(qnty*cost)

        elif mode == "remove":
            self.item_list.remove(self.item_list[idx])
            self.qty_list.remove(self.qty_list[idx])
            self.cost_list.remove(self.cost_list[idx])
            self.tcost_list.remove(self.tcost_list[idx])

        self.sr_no.config(state="normal")
        self.qty.config(state="normal")
        self.cost_unit.config(state="normal")
        self.total_cost.config(state="normal")

        self.sr_no.delete(0, END)
        self.bill_item.delete(0, END)
        self.qty.delete(0, END)
        self.cost_unit.delete(0, END)
        self.total_cost.delete(0, END)

        for n in range(1, len(self.item_list)+1):
            self.sr_no.insert(END, n)
        for n in self.item_list:
            item_str = n[0]+" "+n[1]+" "+n[2]
            self.bill_item.insert(END, item_str)
        for n in self.qty_list:
            self.qty.insert(END, n)
        for n in self.cost_list:
            self.cost_unit.insert(END, n)
        for n in self.tcost_list:
            self.total_cost.insert(END, n)

        self.sum_amt.config(state="normal")
        self.sum_amt.delete(0, END)
        self.sum_amt.insert(0, sum(self.tcost_list))
        self.sum_amt.config(state="disabled")

        self.Total.config(state="normal")
        self.Total.delete(0, END)
        self.Total.insert(0, sum(self.tcost_list))
        self.Total.config(state="readonly")

        self.sr_no.config(state="disabled")
        self.qty.config(state="disabled")
        self.cost_unit.config(state="disabled")
        self.total_cost.config(state="disabled")

    def update_stock(self):
        DataFile = open("Data/Qty_Data.json", "r")
        NewData = json.load(DataFile)
        DataFile.close()

        for chk_idx, itm in enumerate(self.item_list):
            qtty = int(self.qty_list[chk_idx])
            if itm[0] in NewData.keys():
                if itm[1] in NewData[itm[0]].keys():
                    if itm[2] in NewData[itm[0]][itm[1]].keys():
                        new_qty = NewData[itm[0]][itm[1]][itm[2]] - qtty
                        if new_qty >= 0:
                            NewData[itm[0]][itm[1]][itm[2]] = new_qty
                        else:
                            NewData[itm[0]][itm[1]][itm[2]] = 0
        DataFile = open("Data/Qty_Data.json", "w")
        json.dump(NewData, DataFile)
        DataFile.close()

    def print_bill(self):
        if self.Cust_no["text"] == "" or self.Cust_name["text"] == "":
            messagebox.showerror("Invalid Data", "Enter data to save & print", parent=self.master)

        for chk_idx, itm in enumerate(self.item_list):
            if itm[0] in Data.keys():
                if itm[1] in Data[itm[0]].keys():
                    if itm[2] in Data[itm[0]][itm[1]].keys():
                        pass
            else:
                msgbox = messagebox.askquestion(title="Item not from your inventory",
                                                message="Some Product in this list is not in your inventory.\n "
                                                        "Are you sure you want to proceed?")
                if msgbox == "No":
                    return

        self.update_stock()
        self.save_bill()
        self.ss_bill()

    def new_bill(self):
        msgbox = messagebox.askquestion(title="New Bill",
                                        message="Generating new bill will delete the current bill without saving.\n "
                                                "Are you sure you want to proceed?")
        if msgbox == "no":
            return

        billno = self.bill_no()
        #Empty the form
        self.CustName.delete(0, END)
        self.CustNo.delete(0, END)
        self.Category.config(state="normal")
        self.Item.config(state="normal")
        self.Size.config(state="normal")
        self.Category_Other.config(state="normal")
        self.Item_Other.config(state="normal")
        self.Size_Other.config(state="normal")

        self.Category.delete(0, END)
        self.Item.delete(0, END)
        self.Size.delete(0, END)
        self.Category_Other.delete(0, END)
        self.Item_Other.delete(0, END)
        self.Size_Other.delete(0, END)

        self.Category.config(state="readonly")
        self.Item.config(state="readonly")
        self.Size.config(state="readonly")
        self.Category_Other.config(state="disabled")
        self.Item_Other.config(state="disabled")
        self.Size_Other.config(state="disabled")

        self.Price.delete(0, END)
        self.Total.config(state="normal")
        self.Total.delete(0, END)
        self.Total.config(state="readonly")

        #Empty the bill
        self.billLabel["text"] = billno
        self.sr_no.config(state="normal")
        self.qty.config(state="normal")
        self.cost_unit.config(state="normal")
        self.total_cost.config(state="normal")
        self.pay_mtd.config(state="normal")
        self.sum_amt.config(state="normal")

        self.Bill_dt["text"] = dt_
        self.Cust_name["text"] = " "
        self.Cust_no["text"] = " "
        self.sr_no.delete(0, END)
        self.bill_item.delete(0, END)
        self.qty.delete(0, END)
        self.cost_unit.delete(0, END)
        self.total_cost.delete(0, END)
        self.pay_mtd.delete(0, END)
        self.sum_amt.delete(0, END)

        self.sum_amt.config(state="disabled")
        self.sr_no.config(state="disabled")
        self.qty.config(state="disabled")
        self.cost_unit.config(state="disabled")
        self.total_cost.config(state="disabled")
        self.pay_mtd.config(state="disabled")

    def load_bill(self):
        if self.searchbox.get() == "":
            messagebox.showerror("Invalid Data", "Please select a bill to load", parent=self.master)
            return
        msgbox = messagebox.askquestion(title="Load Bill",
                                        message="Loading new bill will delete the current bill without saving.\n "
                                                "Are you sure you want to proceed?")
        if msgbox == "no":
            return

        billno = str(self.searchbox.get()).split(" ")[0]
        self.billLabel["text"] = billno
        self.sr_no.config(state="normal")
        self.qty.config(state="normal")
        self.cost_unit.config(state="normal")
        self.total_cost.config(state="normal")
        self.pay_mtd.config(state="normal")

        self.Cust_name["text"] = " "
        self.Cust_no["text"] = " "
        self.sr_no.delete(0, END)
        self.bill_item.delete(0, END)
        self.qty.delete(0, END)
        self.cost_unit.delete(0, END)
        self.total_cost.delete(0, END)
        self.pay_mtd.delete(0, END)

        bill_ffile = open("Data/Bill.json", "r")
        bill_data = json.load(bill_ffile)
        bill_ffile.close()

        self.item_list = bill_data[billno][2]
        self.qty_list = bill_data[billno][3]
        self.cost_list = bill_data[billno][4]
        self.tcost_list = bill_data[billno][5]

        self.Cust_name["text"] = bill_data[billno][0]
        self.Cust_no["text"] = bill_data[billno][1]
        self.Bill_dt["text"] = bill_data[billno][7]

        for n in range(1, len(self.item_list) + 1):
            self.sr_no.insert(END, n)
        for n in self.item_list:
            item_str = n[0] + " " + n[1] + " " + n[2]
            self.bill_item.insert(END, item_str)
        for n in self.qty_list:
            self.qty.insert(END, n)
        for n in self.cost_list:
            self.cost_unit.insert(END, n)
        for n in self.tcost_list:
            self.total_cost.insert(END, n)

        self.pay_mtd.insert(0, bill_data[billno][6])

        self.sum_amt.config(state="normal")
        self.sum_amt.delete(0, END)
        self.sum_amt.insert(0, sum(self.tcost_list))
        self.sum_amt.config(state="disabled")

        self.Total.config(state="normal")
        self.Total.delete(0, END)
        self.Total.insert(0, sum(self.tcost_list))
        self.Total.config(state="readonly")

        self.sr_no.config(state="disabled")
        self.qty.config(state="disabled")
        self.cost_unit.config(state="disabled")
        self.total_cost.config(state="disabled")
        self.pay_mtd.config(state="disabled")

    def bill_no(self, billNo='00'):
        if billNo != '00':
            return billNo
        else:
            bill_ffile = open("Data/Bill.json", "r")
            bill_data = json.load(bill_ffile)
            bill_ffile.close()
            billNo = int(list(bill_data.keys())[-1]) + 1
            return billNo

    def save_bill(self):
        if self.Cust_name["text"] == "" or self.Cust_no["text"] == "":
            messagebox.showerror("Invalid Data", "Enter data to save bill", parent=self.master)

        bill_ffile = open("Data/Bill.json", "r")
        bill_data = json.load(bill_ffile)
        bill_ffile.close()
        bill_data[self.billLabel['text']] = [self.Cust_name["text"], self.Cust_no["text"], self.item_list, self.qty_list,
                                             self.cost_list, self.tcost_list, self.pay_mtd.get(), self.Bill_dt["text"]]
        newBill = open("Data/Bill.json", "w")
        json.dump(bill_data, newBill)
        newBill.close()

        # -------Read Transaction
        TransFile = open("Data/Transactions.json", "r")
        newTrans = json.load(TransFile)
        TransFile.close()

        month = ["", "January", "February", "March", "April", "May", "June",
                 "July", "August", "September", "October", "November", "December"]
        Tdt_ = str(current_time.day) + " " + month[int(current_time.month)] + " " + str(current_time.year)

        trans = ["bill", "Bill " + str(self.billLabel['text']) + " " + str(self.Cust_name["text"]),
                 sum(self.qty_list), 0, sum(self.tcost_list)]

        TransAvailable = "No"
        for trans_N in newTrans[Tdt_].items():
            if trans_N[1] == trans:
                TransAvailable = "Yes"

        if TransAvailable == "No":
            transNo = "Trans_1"
            try:
                if newTrans[Tdt_]:
                    transNo = "Trans_" + str(int(list(newTrans[Tdt_].keys())[-1].split("_")[1]) + 1)
            except KeyError:
                newTrans[Tdt_] = dict()
            newTrans[Tdt_][transNo] = trans

        # ------Into the transaction------
        TransFile = open("Data/Transactions.json", "w")
        json.dump(newTrans, TransFile)
        TransFile.close()



    def ss_bill(self):
        import pygetwindow
        import pyautogui
        from PIL import Image

        path = "Data/temp/tempImg.jpg"
        title = "GS-Collections-Bill-Generator"

        win2 = pygetwindow.getWindowsWithTitle(title)[0]
        x1, y1 = win2.topleft

        x1 = x1 + 693
        y1 = y1 + 105
        x2 = x1 + 395
        y2 = y1 + 490

        pyautogui.screenshot(path)

        im = Image.open(path)
        im = im.crop((x1, y1, x2, y2))
        im.save(path)
        im.show(path)

    def abt_devp(self):
        pass


class DeveloperCard(Toplevel):
    def __init__(self, master=None):
        super().__init__(master=master)
        self.title("Developer")
        positionRight = int(master.winfo_screenwidth() / 2 - 650 / 2)
        positionDown = int(master.winfo_screenheight() / 2.1 - 320 / 2)
        self.geometry('650x320+{}+{}'.format(positionRight, positionDown))
        self.resizable(width=False, height=False)
        icon = PhotoImage(file='Data/bot.gif')
        self.iconphoto(False, icon)
        self.config(bg="#fcfefc")

        self.msg1 = Label(self, text="Hi there!", font=('Arial Rounded MT Bold', 26, 'bold'),
                          bg="#fcfefc", fg="#800000")
        self.msg2 = Label(self, text="This software is developed by Avinash M. Shah "
                                    "\nand is solely the property under his right.\n"
                                    "Any unauthorised duplication / refabrication is \nprohibited\n\n\n\n\n"
                                    "For further details mail on:",
                          font=('Arial Rounded MT Bold', 10), bg="#fcfefc", justify="left")
        self.msg1.place(x=280, y=40)
        self.msg2.place(x=310, y=110)

        self.mailLbl = Label(self,text="shah.avinash616@gmail.com", font=('comic sans ms', 10), fg="blue", bg="#fcfefc")
        self.mailLbl.place(x=370, y=250)
        self.mailLbl.bind("<Button-1>", lambda e: self.callback("http://www.gmail.com"))

        self.BotLabel = Label(self,image=None, borderwidth=0)
        self.BotLabel.place(x=20, y=33)
        self.frames = None
        self.im = Image.open('Data/bot.gif')
        self.load()

    def callback(self, url):
        webbrowser.open_new_tab(url)

    def load(self):
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(self.im.copy()))
                self.im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = self.im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.BotLabel.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.BotLabel.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.BotLabel.config(image=next(self.frames))
            self.BotLabel.after(self.delay, self.next_frame)


UId = ["Avinash"]
UPw = ["111111"]
root = Tk()
LoginScreen(root, UId, UPw)

root.mainloop()
