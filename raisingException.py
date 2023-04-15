
#
# def ask_for_int(message):
#     while True:
#         num = input(message)
#         try:
#             return int(num)
#         except Exception:
#             print("---- please enter valid number ")
#
# def divnums():
#     num1  = ask_for_int("please enter num1 : ")
#     num2 = ask_for_int("please enter num1 : ")
#     if num2==0:
#         raise Exception("division by zero not allowed ")
#
#     print(f"num1 = {num1}, num2 = {num2}")
#     print(f"num1/ num2= ",end=' ')
#     print(num1/num2)
#
# divnums()





# def sumnums (num1, num2):
#     if (not isinstance(num1, int)) or (not isinstance(num2, int)):
#         raise  Exception("Function sumnums should be called with (int, int) ")
#     res = num1 + num2
#     print(res)
#
#
# # sumnums('2','10')
#
#
# len(20)



def connect_to_server():
    db_user = input("please ente database user: ")
    db_port = input("please enter database port: ")
    if db_port !='5432':
        raise Exception("check server configuration for the correct port number ")
    import os
    os.system(f"""psql -h localhost -p {db_port} -U {db_user} """)
    # os.system('systemctl status postgresql')




connect_to_server()
print("00000000000000 test ------------")