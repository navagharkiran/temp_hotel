from tkinter import*
from PIL import Image,ImageTk #pip Install pillow
from tkinter import ttk
import random
#import mysql.connector #check later
from tkinter import messagebox

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1295x550+230+220")

        #================== Variables================
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
        
        #================title======================
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold")
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #===================logo=====================
        img2=Image.open(r"C:\Users\DELL\OneDrive\Desktop\hotel management\1633410403702hotel-images\hotel images\logohotel.png") #logoimage insert 
        img2=img2.resize((100,40),Image.LANCZOS) # ANTIALIAS CHANGE TO LANCZOS
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)
        

        # ==============LabelFrame===============
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="RoomBooking  Details",font=("arial",12,"bold"),padx=2,pady=6)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        

        # ================labels and entrys=================
        # Customer Contact 
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",13,"bold"),width=20)
        enty_contact.grid(row=0,column=1,sticky=W)

        #Fetch Data Button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact ,text="Fetch Data",font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btnFetchData.place(x=335,y=4)

        # Check_in Date
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin, font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=1,column=1)

        # Check_out Date
        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_Out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=2,column=0,sticky=W)
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,font=("arial",13,"bold"),width=29)
        txtcheck_in_date.grid(row=2,column=1)

        # Room Type
        lbl_room_type=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        lbl_room_type.grid(row=3,column=0,sticky=W)
        
        combo_RoomType=ttk.Combobox(labelframeleft, textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)

        # Available Room
        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available Room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,font=("arial",13,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)

        # Meal
        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)

        # No of Days
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft, textvariable=self.var_meal,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)

        #Paid tax
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Paid Tax:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)

        # Sub Total
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft, textvariable=self.var_actualtotal ,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)

        # Total Cost
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft, textvariable=self.var_total,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)

        # ==============Bill Button============================
        btnBill=Button(labelframeleft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
       
       
         # ==================btns============================
        btns_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btns_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btns_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate=Button(btns_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)

        btnDelete=Button(btns_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        btnReset=Button(btns_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=3,padx=1)

        #================= RightSide Image==========================
        img3=Image.open(r"C:\Users\DELL\OneDrive\Desktop\hotel management\1633410403702hotel-images\hotel images\bed.jpg") #bed.jpg insert 
        img3=img3.resize((520,200),Image.LANCZOS) # ANTIALIAS CHANGE TO LANCZOS
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)

        #===================tabel frame system========================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("arial",12,"bold"),padx=2,pady=6)
        Table_Frame.place(x=435,y=280,width=860,height=260)


        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()

        combo_Search=ttk.Combobox(Table_Frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()

        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Search",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)

        # ==================show data Table ==============
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        self.room_table.heading("contact",text="Mobile")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
        # self.room_table.heading("nationality",text="Nationality")
        # self.room_table.heading("idproof",text="Id Proof")
        # self.room_table.heading("idnumber",text="Id Number")
        # self.room_table.heading("address",text="Address")

        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        # self.room_table("nationality",width=100)
        # self.room_table("idproof",width=100)
        # self.room_table("idnumber",width=100)
        # self.room_table("address",width=100)

        self.room_table.pack(fill=BOTH,expand=1)
  
# ===================== All Data Fetch ================================
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Contact No. must be filled",parent=self.root) #for showing valid or invalid 
        else:
            conn=pymysql.connect(host="localhost",user="root",password="1234",database="project1") # mysql.connector changes to pymysql
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            values=(self.var_contact.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()

            if row==None:
                messagebox.showerror("Error","This number Not Found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                # ================== Name ===========================

                showDataframe=Frame(self.root,bd=4,relief=Ridge,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lbl.place(x=0,y=0)

                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)

                # ================== Gender ===========================

                conn=pymysql.connect(host="localhost",user="root",password="1234",database="project1") # mysql.connector changes to pymysql
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                values=(self.var_contact.get(),)
                my_cursor.execute(query,values)
                row=my_cursor.fetchone() 

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lbl.place(x=0,y=30)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)

                # ====================== Email ===================


                conn=pymysql.connect(host="localhost",user="root",password="1234",database="project1") # mysql.connector changes to pymysql
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                values=(self.var_contact.get(),)
                my_cursor.execute(query,values)
                row=my_cursor.fetchone() 

                lblGender=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lbl.place(x=0,y=60)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=60)  

                # ======================== Nationality ==================== 

                conn=pymysql.connect(host="localhost",user="root",password="1234",database="project1") # mysql.connector changes to pymysql
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                values=(self.var_contact.get(),)
                my_cursor.execute(query,values)
                row=my_cursor.fetchone() 

                lblGender=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lbl.place(x=0,y=90)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=90)   

                # =========================== Address ===========================

                conn=pymysql.connect(host="localhost",user="root",password="1234",database="project1") # mysql.connector changes to pymysql
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                values=(self.var_contact.get(),)
                my_cursor.execute(query,values)
                row=my_cursor.fetchone() 

                lblGender=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lbl.place(x=0,y=10)

                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=120)  
                  



        












if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()