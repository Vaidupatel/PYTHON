#Set is collection of well define data structure
# # print(type(s))
# # s_from_list=set([1,2,3,4,5,6]) #it is a set derived from list
# l=[1,2,3,4,5,6]
# s_from_list=set(l)  #Its also a set derived from list
# print(s_from_list)
# print(type(s_from_list))
s=set()
s.add(1)
s.add(1) #Set only contains the unique values
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s1=s.union({5,6,7,8,9})
s2=s.intersection({5,6,7,8,9})
s3=s.isdisjoint({6,7,8,9})
print(s3)
print(s,s1)
print(s,s2)
print(len(s))
print(min(s))
print(max(s))
print(type(s))
s.remove(1)
print(s)
