try:
    fileobject = open("myfile.txt", 'a')  # old data will be kept
except Exception as e:
    print(e)
    print("--- file not found , application will be closed ---")
    exit()
else:
    """ you will use this object to apply operations on the file """
    print(fileobject)  # IO_TEXTIOWRAPPER
    fileobject.write("Ahmed\n")
    fileobject.write("nnn\n")
    fileobject.writelines(['ahmed\n', 'ali\n'])
    fileobject.seek(10)  # not working as append --> can access only the end of the file ?
    fileobject.write('###########################')
    fileobject.close()
#