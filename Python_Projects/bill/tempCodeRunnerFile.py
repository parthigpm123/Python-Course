from tkinter import *

root = Tk()
root.title("Retail Billing System")
root.geometry("1270x685")
root.configure(bg="blue2")

#================ HEADING ==================#
headingLabel = Label(
    root, text="Retail Billing System",
    font=("times new roman", 30, "bold"),
    bg="blue2", fg="gold", bd=12, relief=GROOVE
)
headingLabel.pack(fill=X)

#================ CUSTOMER DETAILS ================#
customer_details_frame = LabelFrame(
    root, text="Customer Details",
    font=("times new roman", 15, "bold"),
    fg="gold", bd=8, relief=GROOVE, bg="blue2"
)
customer_details_frame.pack(fill=X, padx=10, pady=5)

Label(customer_details_frame, text='Name', font=("times new roman", 15, "bold"), bg="blue2", fg="white").grid(row=0, column=0, padx=10, pady=5)
Entry(customer_details_frame, font=("arial", 15), bd=7, width=18).grid(row=0, column=1, padx=8, pady=5)

Label(customer_details_frame, text='Phone Number', font=("times new roman", 15, "bold"), bg="blue2", fg="white").grid(row=0, column=2, padx=10, pady=5)
Entry(customer_details_frame, font=("arial", 15), bd=7, width=18).grid(row=0, column=3, padx=8, pady=5)

Label(customer_details_frame, text='Bill Number', font=("times new roman", 15, "bold"), bg="blue2", fg="white").grid(row=0, column=4, padx=10, pady=5)
Entry(customer_details_frame, font=("arial", 15), bd=7, width=18).grid(row=0, column=5, padx=8, pady=5)

Button(customer_details_frame, text='SEARCH', font=('arial', 12, 'bold'), bd=7, bg="gold", fg="black").grid(row=0, column=6, padx=10, pady=5)

#================ PRODUCT FRAMES CONTAINER ================#
productsFrame = Frame(root, bg="blue2", bd=8, relief=GROOVE)
productsFrame.pack(fill=X, padx=10, pady=5)

#================ COSMETICS ==================#
cosmeticsFrame = LabelFrame(
    productsFrame, text='Cosmetics',
    font=('times new roman', 15, 'bold'),
    fg='gold', bd=8, relief=GROOVE, bg='blue2'
)
cosmeticsFrame.grid(row=0, column=0, padx=5, pady=5)

items = ['Bath Soap', 'Face Cream', 'Face Wash', 'Hair Spray', 'Hair Gel', 'Body Lotion']
for i, item in enumerate(items):
    Label(cosmeticsFrame, text=item, font=("times new roman", 13, "bold"), bg="blue2", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky='w')
    Entry(cosmeticsFrame, font=("times new roman", 15, "bold"), width=10, bd=5).grid(row=i, column=1, padx=10, pady=5)

#================ GROCERY ==================#
groceryframe = LabelFrame(
    productsFrame, text='Grocery',
    font=('times new roman', 15, 'bold'),
    fg='gold', bd=8, relief=GROOVE, bg='blue2'
)
groceryframe.grid(row=0, column=1, padx=5, pady=5)

groceries = ['Rice', 'Oil', 'Daal', 'Wheat', 'Sugar', 'Tea']
for i, g in enumerate(groceries):
    Label(groceryframe, text=g, font=("times new roman", 13, "bold"), bg="blue2", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky='w')
    Entry(groceryframe, font=("times new roman", 15, "bold"), width=10, bd=5).grid(row=i, column=1, padx=10, pady=5)

#================ COLD DRINKS ==================#
ColdDrinks = LabelFrame(
    productsFrame, text='Cold Drinks',
    font=('times new roman', 15, 'bold'),
    fg='gold', bd=8, relief=GROOVE, bg='blue2'
)
ColdDrinks.grid(row=0, column=2, padx=5, pady=5)

drinks = ['Maaza', 'Pepsi', 'Sprite', 'Dew', 'Frooti', 'Coca Cola']
for i, d in enumerate(drinks):
    Label(ColdDrinks, text=d, font=("times new roman", 13, "bold"), bg="blue2", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky='w')
    Entry(ColdDrinks, font=("times new roman", 15, "bold"), width=10, bd=5).grid(row=i, column=1, padx=10, pady=5)

#================ BILL AREA ==================#
billframe = Frame(productsFrame, bd=8, relief=GROOVE, bg='blue2')
billframe.grid(row=0, column=3, padx=5, pady=5, sticky='n')

billareaLabel = Label(billframe, text='Bill Area', font=('times new roman', 15, 'bold'), bd=7, relief=GROOVE, bg="gold", fg="black")
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(billframe, height=15, width=55, yscrollcommand=scrollbar.set, bd=5, relief=GROOVE, font=("arial", 12))
textarea.pack()
scrollbar.config(command=textarea.yview)

#================ BILL MENU ==================#
billmenuFrame = LabelFrame(
    root, text='Bill Menu',
    font=('times new roman', 15, 'bold'),
    fg='gold', bd=8, relief=GROOVE, bg='blue2'
)
billmenuFrame.pack(fill=X, padx=10, pady=5)

labels = ['Cosmetic Price', 'Grocery Price', 'Cold Drink Price']
for i, lbl in enumerate(labels):
    Label(billmenuFrame, text=lbl, font=("times new roman", 13, "bold"), bg="blue2", fg="white").grid(row=i, column=0, padx=10, pady=5, sticky='w')
    Entry(billmenuFrame, font=("times new roman", 15, "bold"), width=10, bd=5).grid(row=i, column=1, padx=10, pady=5)

taxes = ['Cosmetic Tax', 'Grocery Tax', 'Cold Drink Tax']
for i, tax in enumerate(taxes):
    Label(billmenuFrame, text=tax, font=("times new roman", 13, "bold"), bg="blue2", fg="white").grid(row=i, column=2, padx=10, pady=5, sticky='w')
    Entry(billmenuFrame, font=("times new roman", 15, "bold"), width=10, bd=5).grid(row=i, column=3, padx=10, pady=5)

#================ BUTTONS ==================#
buttonFrame = Frame(billmenuFrame, bd=8, relief=GROOVE, bg="blue2")
buttonFrame.grid(row=0, column=4, rowspan=3, padx=10, pady=5)

buttons = ['Total', 'Bill', 'Email', 'Print', 'Clear']
for i, btn in enumerate(buttons):
    Button(buttonFrame, text=btn, font=('arial', 16, "bold"), bg='gold', fg='black', bd=5, width=8, pady=10).grid(row=0, column=i, padx=5, pady=10)

root.mainloop()
