# 1.average of dictionery:

# dic={"a":23,"b":{"c":28,"d":45}}
# sum=0
# c=0
# for i in dic:
#     if type (dic[i])==type({}):
#         for j in dic[i]:
#             sum+=dic[i][j]
#             c+=1
#     else:
#         sum=sum+dic[i]
#         c+=1
# print(sum/c)


# "my name is swathi my age 20 years old"


# dic="my name is swathi my age 20 years old"
# a=input("enter any char")
# d1=dic.split()
# j=0
# c=0
# dic1={}
# while j<len(d1):
#     if d1[j]==a:
#         c+=1
#     j+=1
#     dic1[a]=cic="my name is swathi my age 20 years old"
# a=input("enter any char")
# d1=dic.split()
# j=0
# c=0
# dic1={}
# while j<len(d1):
#     if d1[j]==a:
#         c+=1
#     j+=1
#     dic1[a]=c
# print(dic1)

# print(dic1)

# reverse keys and values:

# dic={1:23,4:25,6:27}
# d={}
# for i in dic:
#     d[dic[i]]=i
# print(d)

# singel dictionary converted into multiple dictionary:

# dic={"a":23,"b":2,"c":28,"d":45}
# dic1={}
# for i in dic:
#     dic1[i]=dic
# print(dic1)

# #two dictionaries converted into singel dictionary:


# dic={"a":23,"b":2,"c":28,"d":45}
# dic1={1:2,3:5,4:8,6:5}
# dic2={}
# for i in dic:
#     dic2[i]=dic[i]
# for j in dic1:
#     dic2[j]=dic1[j]
# print(dic2)
# a={'data':{
#     'jan':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'feb':{'mon':5,'tues':5,'wed':4,'thurs':7,'fri':2,'sat':3,'sun':7},
#     'march':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'april':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'may':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'june':{'mon':2,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'july':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'aug':{'mon':3,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'sep':{'mon':8,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'oct':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'nov':{'mon':7,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4},
#     'dec':{'mon':5,'tues':4,'wed':3,'thurs':4,'fri':5,'sat':3,'sun':4}}
# }
# sum=0
# sum=0
# for i in a["data"]:
# 	print("values:",a["data"][i]["mon"])
# for i in a.values():
#     for j in i.values():
#         for k in  j.values():
#             sum=sum+k
#             if k>=4:
#                 print("greater than 4:",k)
# print("total sum:",sum)
    



# # even numbers in dictionary:

# dic={"a":[1,4,7,8,9],"b":[7,4,9,2,3],"c":[5,7,6,8,9,2,4]}
# for i in dic:
#     d={}
#     k=dic[i]
#     empty=[]
#     for j in k:
#         if j%2==0:
#             empty.append(j)
#         d[i]=empty
# print(d)

# odd numbers in dictionary:

# dic={"a":[1,4,7,8,9],"b":[7,4,9,2,3],"c":[5,7,6,8,9,2,4]}
# for i in dic:
#     d={}
#     k=dic[i]
#     empty=[]
#     for j in k:
#         if j%2!=0:
#             empty.append(j)
#         d[i]=empty
# print(d)

# # # sum of values:

# dic={"a":2,"b":3,"c":1}
# sum=0
# for i in dic:
#     sum=sum+dic[i]
# print(sum)


# dic1=[1,2,3,4]
# dic2=[10,20,30,40]

# dic3={}
# for i in dic1:
#     for j in dic2:
#         dic3[i]=j
#         dic2.remove(j)
#         break
# print(dic3)



    