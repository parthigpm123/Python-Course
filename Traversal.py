
lst =["mango","banana","graphs","orange"]
 
 #method 1
for i in range (len(lst)):
      
      print(lst[i])
      
print("----------------------------")
# method 2 
count=0
for i in lst:
      count+=1
      print(count,i,sep=".")
           




#Slicing

string ="python"

print(string[0:5])      

lst1=[1,2,3,4,5]

print(lst1[1:5])