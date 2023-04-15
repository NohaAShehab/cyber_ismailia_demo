"""
    scripting ---> deal with file --->

    ---> read or write

    ---> open(filename, mode)
        --> mode --> r ---> read ---> read file content starting from the beginning of the file
         mode --> w ---> write --->
         if file not exists --> try to create it ? ---> according to permission on this dir
         if file exists write content to the file  from the beginning of the file
         ---> remove old content

          mode --> a ---> append --->
           if file not exists --> try to create it ? ---> according to permission on this dir
          append content to the file  from the end of the file
         ---> keep old content

    ---> operation
        read()
        write(string)


    --> close file ?
    close()





"""


try:
    fileobject = open("myfile.txt", 'w')  # old data will be removed
except Exception as e:
    print(e)
    print("--- file not found , application will be closed ---")
    exit()
else:
    """ you will use this object to apply operations on the file """
    print(fileobject)  # IO_TEXTIOWRAPPER
    fileobject.write("Ahmed\n")
    fileobject.write("""Ahmed
Ali
Mohamed#""")
    fileobject.writelines(['ahmed\n', 'ali\n'])
    fileobject.write("""Ahmed
Ali
Mohamed#""")
    fileobject.write("""Ahmed
Ali
Mohamed#""")
    # fileobject.seek(0)
    # fileobject.write("##############################\n")
    # fileobject.close()  ### I am sure I want to save the data to the stream
#



# try:
#     fileobject = open("omarcv.txt", 'w')  # old data will be removed
# except Exception as e:
#     print(e)
#     print("--- file not found , application will be closed ---")
#     exit()
# else:
#     """ you will use this object to apply operations on the file """
#     print(fileobject)  # IO_TEXTIOWRAPPER
#     fileobject.write("Ahmed\n")
#     fileobject.write("nnn\n")
#     fileobject.close()

