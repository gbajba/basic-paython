
num=int(input("Enter number of values: "))
values=[];
neg_co=0;
pos_co=0;
i=0;
print("Enter values:")
while i<num:
    val=int(input())
    values.insert(i,val)
    if values[i]<0:
        neg_co=neg_co+1    
    else:
        if values[i]!=0:
            pos_co=pos_co+1
    i=i+1
print("Values: ",values[:])
print("No. of positive values: ",pos_co)
print("No. of negative values: ",neg_co)
    
