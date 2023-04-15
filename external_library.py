

# import  math
#
# print(math.pi)
#
# print(math.ceil(44.1))
# print(math.floor(44.9))
# print(math.pow(3,4))
# print(math.factorial(6))
# print(math.fabs(-5))



""" import os libary """

#
# import os
# print(os.getcwd())
# # os.mkdir('test')
#
# # os.remove('test')  # check
#
# os.system('ls -l')
#
# os.system('touch abc.txt')
#
# # os.system('ifconfig')
#
#
# os.system('systemctl status apache2')
import os


# def load_base_services():
#     service = input("please enter service name: ")
#     os.system(f'systemctl start {service}')
#     os.system(f'systemctl status {service}')
#
#     os.system('ifconfig >> ipconf')
#
#
# load_base_services()


# def remove_application_from_firewall():
#     # service = input("please enter service name: ")
#     os.system(f'sudo ufw allow http')
#     os.system(f'sudo ufw status')
#
#
# remove_application_from_firewall()


#
# print(os.getcwd())
# os.chdir('/home/noha')
# print(os.getcwd())
# # os.mkdir('cybertest')
# os.system('ls -ld cybertest')


###############################################################################
import re   # regular expression


# def askforuser_info():
#     while True:
#         name = input("please enter name: ")
#         if name.isalpha():
#             break
#
#     while True:
#         email  = input("please enter email: ")
#         pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#         res = re.match(pattern, email)  # return with match object
#         if res:
#             print(res)
#             break
#
#     print(name, email)


# askforuser_info(

# email  = input("please enter email: ")
# pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
# res = re.match(pattern, email)  # return with match object
# print(res)

# while True:
#     message = input("please enter your message : ")
#     pattern = r'\b[abc]{4,5}\b'
#     if re.match(pattern, message):
#         break
#     print("----- please enter valid message ")




# def askforuser_info():
#     while True:
#         name = input("please enter name: ")
#         if name.isalpha():
#             break
#
#     while True:
    #     email  = input("please enter email: ")
    #     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    #     # res = re.match(pattern, email)  # return with match object ---> if part of the string
    #     # ## follows the pattern
    #     # if res:
    #     #     print(res)
    #     #     break
    #     res = re.fullmatch(pattern, email)  # return with match object ---> if all the string parts
    #     ## follows the pattern
    #     if res:
    #         print(res)
    #         break
    # print(name, email)


# askforuser_info()


email = input("please enter email: ")
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
res = re.match(pattern, email)  # return with match object ---> if all the string parts
## follows the pattern
print(res)
print(res.span())
print(res.string)
