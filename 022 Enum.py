l1 = ["vid", "abhay", "pratik", "prince", "nirjal"]

# i =  1
# for iteam in l1:
#     if i%2 !=0:
#         print(f"Jarvis please call {iteam}")
#     i+=1

# Upper case is very complicated to do same thing
# For this we have use the enumerate function

for index, iteam in enumerate(l1):  # it will give item and index both
    if index %2 == 0:
        print(f"Jarvis please call {iteam}")

