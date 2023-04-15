"""
    scripting ---> deal with file --->

    ---> read or write

    ---> open(filename, mode)
        --> mode --> r ---> read ---> read file content starting from the beginning of the file
         mode --> w ---> write ---> write content to the file  from the beginning of the file
         ---> remove old content

          mode --> a ---> write ---> write content to the file  from the end of the file
         ---> keep old content

    ---> operation
        read()
        write(string)


    --> close file ?
    close()





"""


try:
    fileobject = open("mycv.txt", 'r')
except Exception as e:
    print(e)
    print("--- file not found , application will be closed ---")
    exit()
else:
    """ you will use this object to apply operations on the file """
    print(fileobject)  # IO_TEXTIOWRAPPER
    """ read file content into one string  """
    data = fileobject.read()
    # print(len(data), data)
    "read file by line "
    # line = fileobject.readline()
    # print(line)
    "read file lines into a list "
    fileobject.seek(0)
    lines = fileobject.readlines()  # lines ends with \n
    print(lines)


    fileobject.close()


