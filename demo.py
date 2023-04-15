

"""  """

users = []
id = 0
def askforusers():
    global id
    id +=1
    name = input("please enter user ")
    return  name


newname = askforusers()

users.append({"name":newname, 'id':id})


newname = askforusers()

users.append({"name":newname, 'id':id})

newname = askforusers()

users.append({"name":newname, 'id':id})


newname = askforusers()

users.append({"name":newname, 'id':id})

newname = askforusers()

users.append({"name":newname, 'id':id})

print(users)
