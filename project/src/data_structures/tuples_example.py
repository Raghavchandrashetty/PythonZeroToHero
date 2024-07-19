# mutable

list = ['Raghav',"Jagath","Shivu", "Shabarish"]
new_list = list

list[-1] = "Karthik"
print(list)
print(new_list)

# Immutable
tuple_1 = ('Raghav',"Jagath","Shivu", "Shabarish")
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = "Shivu"
print(tuple_1)
print(tuple_2)

for ele in tuple_1:
    print(ele)

tuple_3 = ("Raghav", "BC000026", 9986796686)
for item in tuple_3:
    print(item)

#creating empty tuple
empty_tuple = ()
empty_tuple = tuple()