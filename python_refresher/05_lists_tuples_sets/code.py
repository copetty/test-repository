lst = ["Bob", "Rolf", "Anne"] #list allows you to add and remove elements. Maintains order

tple = ("Bob", "Rolf", "Anne") #tuple if immutable cannot add or remove elements. Maintains order

st = {"Bob", "Rolf", "Anne"} #Set an add and remove elements but cannot have duplicates do not keep order

print(lst[0]) 

lst[0] = "Smith" # can't access a set this way but can access tuple and list

print(lst)

#tple[0] = "Smith" does not work

lst.append("Jon") #appends to the list

lst.remove("Jon") # removes from list

st.add("Jon") # adds to set and there is no order so it could go anywhere and sets don't allow for duplicates
