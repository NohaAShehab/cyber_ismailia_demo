
'''

    errors

    1----> syntax errors $----> parser in the interpreter ---> must be solved
    2----> runtime errors (Exceptions)
        ---> unexpected event caused the application to stop

    3----> logical error $---->

'''
#
# def sumnum(x,y):
#     print(x * y )
#
# sumnum(2,2)
# sumnum(2,3)

print("--------------------------")

""" the below line may raise the following exception 

ValueError: invalid literal for int() with base 10: 'kjk'


"""
# age  = int(input("please enter age: "))
#
# print(age)

# age = input("please enter age: ")
# if age.isdigit():  # doesn't accept anything rather than digits 0-->9
#     age = int(age)
#     print(age)
# else:
#     print("operation not allowed ")




# try:
#     age = int(input("please enter age: "))
#
#     print(age)
#
# except:  # exception handling
#     print("---- cannot cast input to int:  ")
#
#
# print("------------------- program ended --------------------")


# try:
#     age = int(input("please enter age: "))
#     print(age)
#
# except:  # exception handling
#     print("---- cannot cast input to int:  ")
#     age = 0
#
# print("------------------- program ended --------------------")
# print(age) # NameError: name 'age' is not defined
#


############################
# print(name) # NameError: name 'name' is not defined
# name=''
# try:
#     print(name)
#     num = int(input("please enter num:  "))
#
# except Exception as e :  # exception handling
#     print(f"---- couldn't find variable : {e}")
#
# print("------------------- program ended --------------------")




# try:
#     num1 = int(input("please enter num1: "))
#     num2 = int(input("please enter num2: "))
#     res = num1/num2
#     print(res)
#
# except ValueError as e:
#     print(e)
#     res = 0
# except ZeroDivisionError as ze:
#     print(ze)
#     res = 10
# except Exception as e:
#     print(e)
#
# print("------------end of the program -----------------")

""" """
#
# import os
# #
# # try:
# #     website = input("please enter website: ")
# #     res =os.system(f'ping {website}')
# #     print(res)
# # except Exception as e:
# #     print("---- pinning www.google.com")
# #     os.system(f'ping www.google.com')
# #
#
# #timestamp
# import time
# mytime = time.time()
# # print(time)
# # exit()
#
#
# try:
#     dirname = input("please enter directory name: ")
#     res =os.mkdir(dirname)
#     print(res)
# except Exception as e:
#     print(e)
#     current_time_stamp = round(time.time())
#     new_name = f"{dirname}{current_time_stamp}"
#     res = os.mkdir(new_name)

""" optional blocks ---> else  """

#
# try:
#     name='python'
#     num1 = int(input("please enter num1: "))
#     num2 = int(input("please enter num2: "))
#     res= num1/num2
#     # print(res)
#     print(name)
# except Exception as e:
#     print(e)
# else:
#     ## this block will be executed if there are no exceptions
#     print(res)




""" finally blocks """


try:
    name='python'
    num1 = int(input("please enter num1: "))
    num2 = int(input("please enter num2: "))
    res= num1/num2
    # print(res)
    print(name)
except Exception as e:
    print(e)
else:   # optional
    ## this block will be executed if there are no exceptions
    print(res)

finally: # optional block
    # this block will be executed always
    print("----------- end of the danger -----------------")









