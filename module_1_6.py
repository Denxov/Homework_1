my_dict={'Kosma':269,'Demian':59,'Peter':189,'Pavel':112}
print(my_dict)
print(my_dict['Kosma'],my_dict.get('Angel','Объект не найден'))
my_dict.update({'Nikita':2000,'Danil':2001})
my_dict.__delitem__('Demian')
print(my_dict.get('Demian','Объект не найден'))
print(my_dict)
# Set
my_set={1,True,1.0,'1'}
print(my_set)
my_set.update({2,False})
print(my_set)
my_set.remove(False)
print(my_set)

