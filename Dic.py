my_dic={
    'name':'Lemon',
    'age':21,
    'city':"khanna"
}
print(my_dic)
print(my_dic['name'])

my_dic['age']=13
print(my_dic['age'])

my_dic['job']='engineer'
print(my_dic)

del my_dic['city']
print()

for key in my_dic:
    print(key)
print("*****************")
for value in my_dic:
    print(value)