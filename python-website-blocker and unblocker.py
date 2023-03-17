
host_path = 'C:\Windows\System32\drivers\etc\hosts'

ip_address = '127.0.0.1'




#block function
#the main function which will get the link entered in the GUI and put it in the host file which will block the link

def Blocker():

    website_lists = Websites.get(1.0,END)

    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:

        file_content = host_file.read()

        for website in Website:

            if website in file_content:

                Label(root, text = 'Already Blocked' , font = 'arial 12 bold').place(x=200,y=200)
                pass

            else:

                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)




#Unblock function
#the main function which will get the link entered in the GUI and remove it from the host file which will unblock the link

def Unblock():

    website_lists = Websites.get(1.0,END)

    Website = list(website_lists.split(","))

    with open (host_path , 'r+') as host_file:

        file_content = host_file.readlines()
        
        host_file.seek(0)
        
        
        for line in file_content:

            if not any(site in line for site in Website):
                
                host_file.write(line)
                
                Label(root, text = "UnBlocked", font = 'arial 12 bold').place(x=350,y =200)
        
        host_file.truncate()







#creating the block button in the GUI

block_btn = Button(root, text = 'BLOCK' , font = 'arial 13 bold', command = Blocker , height = 2, width = 8, bg = 'red', activebackground = 'black')



                    
    
        
#creating the unblock button in the GUI

unblock_button = Button(root, text = 'UNBLOCK',font = 'arial 13 bold',command = Unblock , height = 2, width = 10, bg = 'GREEN', activebackground = 'black')

    
