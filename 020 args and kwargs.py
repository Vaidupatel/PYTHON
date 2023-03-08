# In below example if we want to print any new name or strintg than we have to add argument in function
# def functon_name_print(a,b,c,d):
#     print(a, b, c, d)

# functon_name_print("vaidu","abhay","mehul","jaydeep")


def funargs(normal, *argsvaid, **vaidu):

    # print(args)
    # print(type(args))
    print(normal)
    for i in argsvaid:
        print(i)
    print("\nThis is some of our heroes")
    for key,value in vaidu.items():
        print(f"{key} is a {value}")


normal = "I am normal argument and students are"
vaid = ["vaidu", "abhay", "mehul", "jaydeep", "prince"]
vaidu = {"vaidu":1, "prinece":2, "jaydeep":3, "nirjal":4}
funargs(normal, *vaid, **vaidu)
