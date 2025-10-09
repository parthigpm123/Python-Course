from tkinter import *

root=Tk()

root.title("Retail Billing System")
root.geometry("1270x685")
#root.iconbitmap("icon.ico")

headingLabel=Label(root,text="Retail Billing System",font=("times new roman",30,"bold"),bg="blue2",fg="gold",bd=12,relief=GROOVE)
headingLabel.pack(fill=X,pady=10)

customer_details_frame=LabelFrame(root,text="Customer Details",font=("times new roman",15,"bold"),fg="gold",bd=8,relief=GROOVE,bg="blue2")
customer_details_frame.pack(fill=X)

nameLabel=Label(customer_details_frame,text='Name',font=("times new roman",15,"bold"),bg="blue2",fg="white")
nameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

phoneLabel=Label(customer_details_frame,text='Phone Number',font=("times new roman",15,"bold"),bg="blue2",fg="white")
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

billnumberLabel=Label(customer_details_frame,text='Bill Number',font=("times new roman",15,"bold"),bg="blue2",fg="white")
billnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=("arial",15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7)
searchButton.grid(row=0,column=6,padx=20,pady=8)

productsFrame=Frame(root)
productsFrame.pack(pady=10)

#============COSMETICS====================#
cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='blue2')
cosmeticsFrame.grid(row=0,column=0)


bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=("times new roman",15,"bold"),bg="blue2",fg="white")
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
bathsoapEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
bathsoapEntry.grid(row=0,column=1,pady=9,padx=10)


facecreamLabel=Label(cosmeticsFrame,text='FaceCream',font=("times new roman",15,"bold"),bg="blue2",fg="white")
facecreamLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
facecreamEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,padx=10)

facewashLabel=Label(cosmeticsFrame,text='FaceWash',font=("times new roman",15,"bold"),bg="blue2",fg="white")
facewashLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
facewashEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
facewashEntry.grid(row=2,column=1,padx=10)

hairsprayLabel=Label(cosmeticsFrame,text='HairSpray',font=("times new roman",15,"bold"),bg="blue2",fg="white")
hairsprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
hairsprayEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
hairsprayEntry.grid(row=3,column=1,padx=10)

hairgelLabel=Label(cosmeticsFrame,text='Hairgel',font=("times new roman",15,"bold"),bg="blue2",fg="white")
hairgelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
hairgelEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
hairgelEntry.grid(row=4,column=1,padx=10)

bodyloationLabel=Label(cosmeticsFrame,text='Body Lotion',font=("times new roman",15,"bold"),bg="blue2",fg="white")
bodyloationLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
bodyloationEntry=Entry(cosmeticsFrame,font=("times new roman",15,"bold"),width=10,bd=5)
bodyloationEntry.grid(row=5,column=1,padx=10)

#==========GroceryFrame=====================#
groceryframe=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='blue2')
groceryframe.grid(row=0,column=1)

riceLabel=Label(groceryframe,text='Rice',font=("times new roman",15,"bold"),bg="blue2",fg="white")
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
riceEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
riceEntry.grid(row=0,column=1,pady=9,padx=10)

oilLabel=Label(groceryframe,text='Oil',font=("times new roman",15,"bold"),bg="blue2",fg="white")
oilLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
oilEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
oilEntry.grid(row=1,column=1,padx=10)

daalLabel=Label(groceryframe,text='Daal',font=("times new roman",15,"bold"),bg="blue2",fg="white")
daalLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
daalEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
daalEntry.grid(row=2,column=1,padx=10)

wheatLabel=Label(groceryframe,text='Wheat',font=("times new roman",15,"bold"),bg="blue2",fg="white")
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
wheatEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
wheatEntry.grid(row=3,column=1,padx=10)

sugarLabel=Label(groceryframe,text='Sugar',font=("times new roman",15,"bold"),bg="blue2",fg="white")
sugarLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
sugarEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
sugarEntry.grid(row=4,column=1,padx=10)

teaLabel=Label(groceryframe,text='Tea',font=("times new roman",15,"bold"),bg="blue2",fg="white")
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
teaEntry=Entry(groceryframe,font=("times new roman",15,"bold"),width=10,bd=5)
teaEntry.grid(row=5,column=1,padx=10)

#========COLD DRINKS====================#

ColdDrinks=LabelFrame(productsFrame,text='Cold Drinks',font=('times new roman',15,'bold'),fg='gold',bd=8,relief=GROOVE,bg='blue2')
ColdDrinks.grid(row=0,column=2)

maazaLabel=Label(ColdDrinks,text='Maaza',font=("times new roman",15,"bold"),bg="blue2",fg="white")
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')
maazaEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
maazaEntry.grid(row=0,column=1,pady=9,padx=10)

pepsiLabel=Label(ColdDrinks,text='Pepsi',font=("times new roman",15,"bold"),bg="blue2",fg="white")
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')
pepsiEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
pepsiEntry.grid(row=1,column=1,padx=10)

spriteLabel=Label(ColdDrinks,text='Sprite',font=("times new roman",15,"bold"),bg="blue2",fg="white")
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')
spriteEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
spriteEntry.grid(row=2,column=1,padx=10)

dewLabel=Label(ColdDrinks,text='Dew',font=("times new roman",15,"bold"),bg="blue2",fg="white")
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')
dewEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
dewEntry.grid(row=3,column=1,padx=10)

frootiLabel=Label(ColdDrinks,text='Frooti',font=("times new roman",15,"bold"),bg="blue2",fg="white")
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')
frootiEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
frootiEntry.grid(row=4,column=1,padx=10)

colaLabel=Label(ColdDrinks,text='Coco cola',font=("times new roman",15,"bold"),bg="blue2",fg="white")
colaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')
colaEntry=Entry(ColdDrinks,font=("times new roman",15,"bold"),width=10,bd=5)
colaEntry.grid(row=5,column=1,padx=10)

#==========BILLFRAME==========#
billframe=Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

#============BIL AREA lABEL=======#
billareaLabel=Label(billframe,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

#=====TEXT AREAR========
scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=17,width=55)
textarea.pack()      


root.mainloop() 