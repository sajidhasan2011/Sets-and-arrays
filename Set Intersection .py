print("\033c")
setx = {"green","blue"}
sety = {"blue","yellow"}

print(f"Original set elements : \n {setx}\n {sety} ")

print("\n Intersection of two said sets :")
setz = setx.intersection(sety)
print(setz)

print("\n Union of two said sets :")
setz = setx.union(sety)
print(setz)

print("\n Difference of two said sets :")
setz = setx.difference(sety)
print(setz)

print("\n Symmetric Difference of two said sets :")
setz = setx.symmetric_difference(sety)
print(setz)