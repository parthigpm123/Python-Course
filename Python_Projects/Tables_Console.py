"''Tables Generator Program in Python"
while True:
      try:
            num = int(input("\nEnter Table Number!: "))
            print(f"\n{num}th TABLES")
            print("---------------") 
            for i in range(1,17):
                   print(i, "X", num, "=",i*num)
      except ValueError:
            print("\nPlease Enter A Valid Integer Number!!!")               