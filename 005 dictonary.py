#Dictionary is nothing but key value pairs
d1={}
# print(type(d1))
d2={"vaidu":508,"sahil":515,"prince":510,"darshan":491,"nirjal":{"m":"i","t":"t","a":"l"}}
# print(d2)
# print(d2["nirjal"])
# print(d2["nirjal"]["t"])
# d2["devanshi"]=497
# print(d2)
# del d2["prince"]
# print(d2)


x=d2.copy()	#Returns a copy of the dictionary
print(x)

y=0
print(d2.fromkeys(d2,y))            #Returns a dictionary with the specified keys and value

print(d2.get("vaidu"))	            #Returns the value of the specified key

print(d2.items())	                #Returns a list containing a tuple for each key value pair

print(d2.keys())	                #Returns a list containing the dictionary's keys

d2.pop("prince")	                #Removes the element with the specified key
print(d2)

d2.popitem()	                    #Removes the last inserted key-value pair
print(d2)

a=d2.setdefault("vaidu","devanshi")	#Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print(a)

d2.update({"vaidu":497})	        #Updates the dictionary with the specified key-value pairs
print(d2)

print(d2.values())	        #Returns a list of all the values in the dictionary

# clear()	                        #Removes all the elements from the dictionary
