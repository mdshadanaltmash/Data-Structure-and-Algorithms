a=[1,3,7,4]
b=10

{1:4}


for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==b:
            print(True)
            break
else:
    print(False)




# c={}
# for i in a:
#     c[i]=c.get(i,0)+1
# print(c)
# max=0
# max2=0
# k=-1
# k2=-1
# for keys,values in c.items():
#     if c[keys]>max:
#         max=values
#         k=keys
#     if c[keys]<max and c[keys]>max2:
#         max2=values
#         k2=keys
# print (k,max)
# print(k2,max2)










# players(id,name,c_id,runs,wickets)
# country(c_id,c_name,rank)

# select p.* from players p join country c on p.c_id=c.c_id where c.c_name='INDIA';


# 49(5*6+3)+ 6*6