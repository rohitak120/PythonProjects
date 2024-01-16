# It is a Billing Software made on pure python using tkinter GUI module. 
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile
from time import strftime

class Bill_App:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        # ================ variable ====================
        self.c_name=StringVar()
        self.c_phone=StringVar()
        self.bill_no=StringVar()
        z=random.randint(1000,9999)
        self.bill_no.set(z)
        self.c_email=StringVar()
        self.search_bill=StringVar()
        self.product=StringVar()
        self.prices=IntVar()
        self.qty=IntVar()
        self.sub_total=StringVar()
        self.tax_input=StringVar()
        self.total=StringVar()

        # Product Categories list
        self.Category=["Select Option","Clothing","LifeStyle","Mobiles"]
        
        #SubCatClothing
        self.SubCatClothing=["Pant","T-shirt","Shirt"]
        self.pant=["Levis","Mufti","Spyker"]
        self.price_levis=5000
        self.price_mufti=700
        self.price_spyker=8000

        self.T_shirt=["Polo","Roadster","Jack&Jones"]
        self.price_Polo=1500
        self.price_Roadster=1800
        self.price_JackJones=1700

        self.Shirt=["Peter England","Louis Phillipe","Park Avenue"]
        self.price_Peter=2100
        self.price_Louis=2700
        self.price_Park=1740

        # SubCatLifeStyle
        self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
        self.Bath_soap=["LifeBoy","Lux","Santoor","Pears"]
        self.price_lifeboy=20
        self.price_lux=20
        self.price_santoor=20
        self.price_pears=30

        self.Face_cream=["Fair&Lovely","Ponds","Olay","Garnier"]
        self.price_fair=20
        self.price_ponds=20
        self.price_olay=20
        self.price_garnier=30

        self.Hair_oil=["Parachute","Jasmin","Bajaj"]
        self.price_para=25
        self.price_jasmin=22
        self.price_bajaj=30

        # SubCatMobiles
        self.SubCatMobiles=["Iphone","Samsung","Xiomi","RealMe","OnePlus"]
        self.Iphone=["Iphone_13","Iphone_14","Iphone_15"]
        self.price_i13=55000
        self.price_i14=75000
        self.price_i15=90000

        self.Samsung=["Samsung M16","Samsung M12","Samsung M21"]
        self.price_sm16=16000
        self.price_sm12=12000
        self.price_sm21=18000

        self.Xiomi=["Redmi 11","Redmi 12","Redmi 12 Pro"]
        self.price_r11=11000
        self.price_r12=12000
        self.price_r12pro=16000

        self.RealMe=["RealMe 12","RealMe 13","RealMe Pro"]
        self.price_rel12=25000
        self.price_rel13=22000
        self.price_relpro=30000

        self.OnePlus=["OnePlus 7","OnePlus 9","OnePlus 11"]
        self.price_one7=35000
        self.price_one9=42000
        self.price_one11=55000

        self.SubCatLifeStyle=["Bath Soap","Face Cream","Hair Oil"]
        self.SubCatMobiles=["Iphone","Samsung","Xiomi","RealMe","OnePlus"]

        # Image1
        img=Image.open("./image/b1.jpg")
        img = img.resize((450,130))
        self.photoimg=ImageTk.PhotoImage(img)

        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=450, height=130)

         # Image2
        img_1=Image.open("./image/b4.jpg")
        img_1 = img_1.resize((450,130))
        self.photoimg_1=ImageTk.PhotoImage(img_1)

        lbl_img_1=Label(self.root,image=self.photoimg_1)
        lbl_img_1.place(x=450,y=0,width=450, height=130)

         # Image3
        img_2=Image.open("./image/b6.jpg")
        img_2 = img_2.resize((460,130))
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        lbl_img_2=Label(self.root,image=self.photoimg_2)
        lbl_img_2.place(x=900,y=0,width=460, height=130)

        # Main Title
        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=("times new roman",35,'bold'),bg='white',fg='red')
        lbl_title.place(x=0,y=130,width=1360,height=45)

        # Live Time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(lbl_title, font = ('arial', 14, 'bold'),background= 'white',foreground='blue')
        lbl.place(x=0,y=(-5),width=125,height=50)
        time()

        # Main Frame
        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg='white')
        Main_Frame.place(x=0,y=175,width=1365,height=525)

        # Customer LabelFrame
        Cust_Frame=LabelFrame(Main_Frame,text="Customer",font=("times new roman",12,'bold'),bg='white',fg='red')
        Cust_Frame.place(x=10,y=5,width=350,height=140)

        # Customer Info

        # Mobile No.
        self.lbl_mob=Label(Cust_Frame,text="Mobile No.",font=("arial",12,'bold'),bg='white')
        self.lbl_mob.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.entry_mob=ttk.Entry(Cust_Frame,textvariable=self.c_phone,font=("arial",12,'bold'),width=21)
        self.entry_mob.grid(row=0,column=1)
        # Customer Name
        self.lblCustName=Label(Cust_Frame,font=('arial',12,'bold'),bg='white',text='Customer Name',bd=4)
        self.lblCustName.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtCustName=ttk.Entry(Cust_Frame,textvariable=self.c_name,font=('arial',12,'bold'),width=21)
        self.txtCustName.grid(row=1,column=1,sticky=W,padx=5,pady=2)
        # Customer Email
        self.lblEmail=Label(Cust_Frame,font=('arial',12,'bold'),bg='white',text='Email',bd=4)
        self.lblEmail.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtEmail=ttk.Entry(Cust_Frame,textvariable=self.c_email,font=('arial',12,'bold'),width=21)
        self.txtEmail.grid(row=2,column=1,sticky=W,padx=5,pady=2)


        # Product LabelFrame
        Product_Frame=LabelFrame(Main_Frame,text="Product",font=("times new roman",12,'bold'),bg='white',fg='red')
        Product_Frame.place(x=370,y=5,width=620,height=140)
        
        # Category
        self.lblCategory=Label(Product_Frame,font=('arial',12,'bold'),bg='white',text='Select Categories',bd=4)
        self.lblCategory.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.Combo_Category=ttk.Combobox(Product_Frame,value=self.Category,font=('arial',10,'bold'),width=24,state='readonly')
        self.Combo_Category.current(0)
        self.Combo_Category.grid(row=0, column=1,sticky=W,padx=5,pady=2)
        self.Combo_Category.bind("<<ComboboxSelected>>",self.Categories)


        #SubCategory
        self.lblSubCategory=Label(Product_Frame,font=('arial',12,'bold'),bg='white',text='Subcategories',bd=4)
        self.lblSubCategory.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.ComboSubCategory=ttk.Combobox(Product_Frame, value=[""],state='readonly',font=('arial',10,'bold'),width=24)
        self.ComboSubCategory.grid(row=1, column=1,sticky=W,padx=5,pady=2)
        self.ComboSubCategory.bind("<<ComboboxSelected>>",self.product_add)

        # Product Name
        self.lblproduct=Label(Product_Frame,font=('arial',12,'bold'),bg='white',text='Product Name',bd=4)
        self.lblproduct.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.ComboProduct=ttk.Combobox(Product_Frame,textvariable=self.product,font=('arial',10,'bold'),width=24,state='readonly')
        self.ComboProduct.grid(row=2, column=1,sticky=W,padx=5,pady=2)
        self.ComboProduct.bind("<<ComboboxSelected>>",self.price)

        
        # Price
        self.lblPrice=Label(Product_Frame,font=('arial',12,'bold'),bg='white',text='Price',bd=4)
        self.lblPrice.grid(row=0,column=2,sticky=W,padx=5,pady=2)

        self.ComboPrice=ttk.Entry(Product_Frame,textvariable=self.prices,font=('arial',10,'bold'),width=24,state='readonly')
        self.ComboPrice.grid(row=0, column=3,sticky=W,padx=5,pady=2)


        # Qty
        self.lblQty=Label(Product_Frame,font=('arial',12,'bold'),bg='white',text='Qty',bd=4)
        self.lblQty.grid(row=1,column=2,sticky=W,padx=5,pady=2)

        self.ComboQty=ttk.Entry(Product_Frame,textvariable=self.qty,font=('arial',10,'bold'),width=24)
        self.ComboQty.grid(row=1, column=3,sticky=W,padx=5,pady=2)


        # Middle Frame
        MiddleFrame=Frame(Main_Frame,bd=10)
        MiddleFrame.place(x=10,y=150,width=980, height=340)


         # Image1
        img12=Image.open("./image/b3.jpg")
        img12 = img12.resize((490,340))
        self.photoimg12=ImageTk.PhotoImage(img12)

        lbl_img12=Label(MiddleFrame,image=self.photoimg12)
        lbl_img12.place(x=(-20),y=(-20),width=490, height=340)

         # Image2
        img13=Image.open("./image/b5.jpg")
        img13 = img13.resize((510,340))
        self.photoimg13=ImageTk.PhotoImage(img13)

        lbl_img13=Label(MiddleFrame,image=self.photoimg13)
        lbl_img13.place(x=470,y=(-20),width=510, height=340)



        # Search the Bill
        Search_Frame=Frame(Main_Frame,bd=2,bg='white')
        Search_Frame.place(x=1015,y=15,width=325,height=40)

        self.lblBill=Label(Search_Frame,font=('arial',12,'bold'),bg='red',fg='white',text='Bill Number')
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_Entry_Search=ttk.Entry(Search_Frame,textvariable=self.search_bill,font=('arial',12,'bold'),width=15)
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)

        self.BtnSearch=Button(Search_Frame,command=self.find_bill,text="Search",font=('arial',10,'bold'),bg="orangered",fg='white',width=8,cursor="hand2")
        self.BtnSearch.grid(row=0,column=2)




        # RightFrame Bill Area
        RightLabelFrame=LabelFrame(Main_Frame,text="Bill Area",font=("times new roman",12,"bold"),bg='white',fg="red")
        RightLabelFrame.place(x=1000,y=45,width=350,height=350)

        scroll_y=Scrollbar(RightLabelFrame,orient=VERTICAL)
        self.textarea=Text(RightLabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        # Bill Counter LabelFrame
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=("times new roman",12,'bold'),bg='white',fg='red')
        Bottom_Frame.place(x=0,y=395,width=1355,height=125)

        # Sub Total
        self.lblSubTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg='white',text='Sub Total',bd=4)
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,textvariable=self.sub_total,font=('arial',10,'bold'),width=24)
        self.EntrySubTotal.grid(row=0, column=1,sticky=W,padx=5,pady=2)


        # Gov Tax
        self.lbl_tax=Label(Bottom_Frame,font=('arial',12,'bold'),bg='white',text='Gov Tax',bd=4)
        self.lbl_tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txt_tax=ttk.Entry(Bottom_Frame,textvariable=self.tax_input,font=('arial',10,'bold'),width=24)
        self.txt_tax.grid(row=1, column=1,sticky=W,padx=5,pady=2)


        # Total
        self.lblAmountTotal=Label(Bottom_Frame,font=('arial',12,'bold'),bg='white',text='Total',bd=4)
        self.lblAmountTotal.grid(row=2,column=0,sticky=W,padx=5,pady=2)

        self.txtAmountTotal=ttk.Entry(Bottom_Frame,textvariable=self.total,font=('arial',10,'bold'),width=24)
        self.txtAmountTotal.grid(row=2, column=1,sticky=W,padx=5,pady=2)


        # Button Frame
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg='white')
        Btn_Frame.place(x=320,y=0)

        # Add to Cart
        self.BtnAddToCart=Button(Btn_Frame,command=self.AddItem,height=2,text="Add to Cart",font=('arial',15,'bold'),bg="orangered",fg='white',width=12,cursor="hand2")
        self.BtnAddToCart.grid(row=0,column=0)

        # Generate Bill
        self.BtnGenerate_bill=Button(Btn_Frame,command=self.gen_bill,height=2,text="Generate Bill",font=('arial',15,'bold'),bg="orangered",fg='white',width=12,cursor="hand2")
        self.BtnGenerate_bill.grid(row=0,column=1)

        # Save Bill
        self.BtnSave=Button(Btn_Frame,command=self.save_bill,height=2,text="Save Bill",font=('arial',15,'bold'),bg="orangered",fg='white',width=12,cursor="hand2")
        self.BtnSave.grid(row=0,column=2)

        # Print
        self.BtnPrint=Button(Btn_Frame,command=self.iprint,height=2,text="Print",font=('arial',15,'bold'),bg="orangered",fg='white',width=12,cursor="hand2")
        self.BtnPrint.grid(row=0,column=3)

        # Clear
        self.BtnClear=Button(Btn_Frame,command=self.clear,height=2,text="Clear",font=('arial',15,'bold'),bg="orangered",fg='white',width=12,cursor="hand2")
        self.BtnClear.grid(row=0,column=4)

        # Exit
        self.BtnExit=Button(Btn_Frame,command=self.root.destroy,height=2,text="Exit",font=('arial',15,'bold'),bg="orangered",fg='white',width=12,cursor="hand2")
        self.BtnExit.grid(row=0,column=5)
        self.welcome()  # Calling welcome function
        
        self.l=[]
    # =====================================Function Declaration===================================
    def welcome(self):
        self.textarea.delete(1.0,END)
        self.textarea.insert(END,"\t Welcome New Mini Mall")
        self.textarea.insert(END,f"\n Bill Number:{self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name:{self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number:{self.c_phone.get()}")
        self.textarea.insert(END,f"\n Customer Email:{self.c_email.get()}")

        self.textarea.insert(END,f"\n ===================================")
        self.textarea.insert(END,f"\n Products\t\tQTY\t\tPrice")
        self.textarea.insert(END,f"\n ===================================\n")


    def AddItem(self):
        Tax=1
        self.n=self.prices.get()
        self.m=self.qty.get()*self.n
        self.l.append(self.m)
        if self.product.get()=="":
            messagebox.showerror("Error","Please select the Product Name")
        else:
            self.textarea.insert(END,f"\n {self.product.get()}\t\t{self.qty.get()}\t\t{self.m}")
            self.sub_total.set(str('Rs.%.2f'%(sum(self.l))))
            self.tax_input.set(str('Rs.%.2f'%((((sum(self.l))-(self.prices.get())*Tax)/100))))
            self.total.set(str('Rs.%.2f'%(((sum(self.l)) + ((((sum(self.l)) - (self.prices.get()))*Tax)/100)))))


    def gen_bill(self):
        if self.product.get()=="":
            messagebox.showerror("Error","Please Add to Cart Product")
        else:
            text=self.textarea.get(10.0,(10.0+float(len(self.l))))
            self.welcome()
            self.textarea.insert(END,text)
            self.textarea.insert(END,f"\n ===================================")
            self.textarea.insert(END,f"\n Sub Amount:\t\t\t{self.sub_total.get()}")
            self.textarea.insert(END,f"\n Tax Amount:\t\t\t{self.tax_input.get()}")
            self.textarea.insert(END,f"\n Total Amount:\t\t\t{self.total.get()}")
            self.textarea.insert(END,f"\n ===================================")


    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
        if op>0:
            self.bill_data=self.textarea.get(1.0,END)
            f1=open('bills/'+str(self.bill_no.get())+".txt",'w')
            f1.write(self.bill_data)
            op=messagebox.showinfo("Saved",f"Bill NO:{self.bill_no.get()} saved successfully")
            f1.close()


    def iprint(self):
        q=self.textarea.get(1.0,"end-1c")
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")


    def find_bill(self):
        found="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f'bills/{i}','r')
                self.textarea.delete(1.0,END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                found="yes"
        if found=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear(self):
        self.textarea.delete(1.0,END)
        self.c_name.set("")
        self.c_phone.set("")
        self.c_email.set("")
        x=random.randint(1000,9999)
        self.bill_no.set(str(x))
        self.product.set("")
        self.prices.set("")
        self.qty.set("")
        self.l=[0]
        self.total.set("")
        self.sub_total.set("")
        self.tax_input.set("")
        self.welcome()





        
    def Categories(self,event=""):
        if self.Combo_Category.get()=="Clothing":
            self.ComboSubCategory.config(value=self.SubCatClothing)
            self.ComboSubCategory.current(0)

        elif self.Combo_Category.get()=="LifeStyle":
            self.ComboSubCategory.config(value=self.SubCatLifeStyle)
            self.ComboSubCategory.current(0)

        elif self.Combo_Category.get()=="Mobiles":
            self.ComboSubCategory.config(value=self.SubCatMobiles)
            self.ComboSubCategory.current(0)


    def product_add(self, event=""):
        # Conditions for LifeStyle subcategories
        if self.ComboSubCategory.get() == "Bath Soap":
            self.ComboProduct.config(value=self.Bath_soap)
            self.ComboProduct.current(0)

        elif self.ComboSubCategory.get() == "Face Cream":
            self.ComboProduct.config(value=self.Face_cream)
            self.ComboProduct.current(0)

        elif self.ComboSubCategory.get() == "Hair Oil":
            self.ComboProduct.config(value=self.Hair_oil)
            self.ComboProduct.current(0)

        # Conditions for Clothing subcategories
        elif self.ComboSubCategory.get() == "Pant":
            self.ComboProduct.config(value=self.pant)
            self.ComboProduct.current(0)

        elif self.ComboSubCategory.get() == "T-shirt":
            self.ComboProduct.config(value=self.T_shirt)
            self.ComboProduct.current(0)
        
        elif self.ComboSubCategory.get() == "Shirt":
            self.ComboProduct.config(value=self.Shirt)
            self.ComboProduct.current(0)

        # Conditions for Mobiles subcategories
        elif self.ComboSubCategory.get() == "Iphone":
            self.ComboProduct.config(value=self.Iphone)
            self.ComboProduct.current(0)

        elif self.ComboSubCategory.get() == "Samsung":
            self.ComboProduct.config(value=self.Samsung)
            self.ComboProduct.current(0)

        elif self.ComboSubCategory.get() == "Xiomi":
            self.ComboProduct.config(value=self.Xiomi)
            self.ComboProduct.current(0)

        elif self.ComboSubCategory.get() == "RealMe":
            self.ComboProduct.config(value=self.RealMe)
            self.ComboProduct.current(0)

        elif self.ComboSubCategory.get() == "OnePlus":
            self.ComboProduct.config(value=self.OnePlus)
            self.ComboProduct.current(0)


    def price(self,event=""):
        # Pant
        if self.ComboProduct.get()=="Levis":
            self.ComboPrice.config(value=self.price_levis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Mufti":
            self.ComboPrice.config(value=self.price_mufti)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Spyker":
            self.ComboPrice.config(value=self.price_spyker)
            self.ComboPrice.current(0)
            self.qty.set(1)


        # T-Shirt
        if self.ComboProduct.get()=="Polo":
            self.ComboPrice.config(value=self.price_Polo)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Roadster":
            self.ComboPrice.config(value=self.price_Roadster)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jack&Jones":
            self.ComboPrice.config(value=self.price_JackJones)
            self.ComboPrice.current(0)
            self.qty.set(1)

        
        # Shirt
        if self.ComboProduct.get()=="Peter England":
            self.ComboPrice.config(value=self.price_Peter)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Louis Phillipe":
            self.ComboPrice.config(value=self.price_Louis)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Park Avenue":
            self.ComboPrice.config(value=self.price_Park)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Bath Soap
        if self.ComboProduct.get()=="LifeBoy":
            self.ComboPrice.config(value=self.price_lifeboy)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Lux":
            self.ComboPrice.config(value=self.price_lux)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Santoor":
            self.ComboPrice.config(value=self.price_santoor)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Pears":
            self.ComboPrice.config(value=self.price_pears)
            self.ComboPrice.current(0)
            self.qty.set(1)

        
        # Face Cream
        if self.ComboProduct.get()=="Fair&Lovely":
            self.ComboPrice.config(value=self.price_fair)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Ponds":
            self.ComboPrice.config(value=self.price_ponds)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Olay":
            self.ComboPrice.config(value=self.price_olay)
            self.ComboPrice.current(0)
            self.qty.set(1)
        
        if self.ComboProduct.get()=="Garnier":
            self.ComboPrice.config(value=self.price_garnier)
            self.ComboPrice.current(0)
            self.qty.set(1)


        # Hair Oil
        if self.ComboProduct.get()=="Parachute":
            self.ComboPrice.config(value=self.price_para)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Jasmin":
            self.ComboPrice.config(value=self.price_jasmin)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Bajaj":
            self.ComboPrice.config(value=self.price_bajaj)
            self.ComboPrice.current(0)
            self.qty.set(1)

        # Mobiles
        if self.ComboProduct.get()=="Iphone_13":
            self.ComboPrice.config(value=self.price_i13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_14":
            self.ComboPrice.config(value=self.price_i14)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Iphone_15":
            self.ComboPrice.config(value=self.price_i15)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M16":
            self.ComboPrice.config(value=self.price_sm16)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M12":
            self.ComboPrice.config(value=self.price_sm12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Samsung M21":
            self.ComboPrice.config(value=self.price_sm21)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redmi 11":
            self.ComboPrice.config(value=self.price_r11)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redmi 12":
            self.ComboPrice.config(value=self.price_r12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="Redmi 12 Pro":
            self.ComboPrice.config(value=self.price_r12pro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 12":
            self.ComboPrice.config(value=self.price_rel12)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe 13":
            self.ComboPrice.config(value=self.price_rel13)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="RealMe Pro":
            self.ComboPrice.config(value=self.price_relpro)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus 7":
            self.ComboPrice.config(value=self.price_one7)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus 9":
            self.ComboPrice.config(value=self.price_one9)
            self.ComboPrice.current(0)
            self.qty.set(1)

        if self.ComboProduct.get()=="OnePlus 11":
            self.ComboPrice.config(value=self.price_one11)
            self.ComboPrice.current(0)
            self.qty.set(1)





if __name__ == '__main__':
    root=Tk()
    obj=Bill_App(root)
    root.mainloop()