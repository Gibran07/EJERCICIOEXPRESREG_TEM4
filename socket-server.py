import socket
import re


#AF_INET se refiere a una familia IP
#SOCK_STREAM indica que es una conexión TCP
socket_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Especificamos la dirección ip y el puerto en el cual
#escuchará nuestro servidor
ip = "127.0.0.1"
port = 8001
socket_server.bind((ip,port))
socket_server.listen(5) #Máximo de conexiones

print(f"\n\nServer Listening on {ip}:{port}")

salir = False
while salir == False:
    conexion, address = socket_server.accept()
    print ("CONEXION ESTABLECIDA")
    archi1=open("mensaje.txt","r")
    contenido=archi1.read()
    print(contenido)
    test_str = contenido
    archi1.close()            

    while True:
        meNsage = conexion.recv(1024)
        meNsage = meNsage.decode()
        print(meNsage)    

        if meNsage == 'adios':
            meNsage = 'Adios...'
            conexion.send(meNsage.encode())
            print("\n")
            salir = True
            break

        elif meNsage == 'hola':                                         
            meNsage = ("¡HOLA!, ELIGE UNA OPCION:\n\n1.- Variables válidas."
                        "\n2.- Enteros y decimales.\n3.- Operadores aritméticos.\n4.- Operadores relacionales.\n"
                        "5.- Palabras reservadas.\n\n")
            conexion.send(meNsage.encode())
        
        elif meNsage == '1':
            regex = r'(?s)^((?!hede)[^ ^$1-9])'                             
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    meNsage = ("SE ENCONTRARON --> {matchNum} resultados. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                           
            if meNsage == '1':
                 meNsage = ("SE ENCONTRARON --> 0 resultados. ")                                                           
            conexion.send(meNsage.encode())            

        elif meNsage == '2':
            regex = r"([0-9]{1,3$}$|[0-9]{1,3}\.[0-9]{1,9})"            
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    meNsage = ("SE ENCONTRARON --> {matchNum} resultados ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                                      
            if meNsage == '1'  or meNsage == '2':
                 meNsage = ("SE ENCONTRARON --> 0 resultados ")                                                           
            conexion.send(meNsage.encode())


        elif meNsage == '3':
            regex = r'([+]|[]^[]|[*]|-|//|/|%)'                                   
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    meNsage = ("SE ENCONTRARON --> {matchNum} resultados ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                       
            if meNsage == '1'  or meNsage == '3':
                 meNsage = ("SE ENCONTRARON --> 0 resultados ")                                                           
            conexion.send(meNsage.encode()) 


        elif meNsage == '4':
            regex = r'(!=|>=|<=|==|<|=|>|<)'                                      
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    meNsage = ("SE ENCONTRARON --> {matchNum} resultados ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                                        
            if meNsage == '1'  or meNsage == '4':
                 meNsage = ("SE ENCONTRARON --> 0 resultados ")                                                           
            conexion.send(meNsage.encode())


        elif meNsage == '5':
            regex = r'(?i)(\W|^)(False|await|else|import|pass|None|break|except|in|raise|True|class|finally|is|return|and|continue|for|lambda|try|as|def|from|nonlocal|while|assert|del|global|not|with|async|elif|if|or|yield)(\W|$)'                                 
            matches = re.finditer(regex, test_str, re.MULTILINE)

            for matchNum, match in enumerate(matches, start=1):
                    
                    meNsage = ("SE ENCONTRARON --> {matchNum} resultados. ".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))                                        
            if meNsage == '1' or meNsage == '5':
                 meNsage = ("SE ENCONTRARON --> 0 resultados. ")                                                           
            conexion.send(meNsage.encode())                            

        else:
            meNsage = 'SELECCIONA UNA OPCION DE LA LISTA'            
            conexion.send(meNsage.encode())

conexion.close()
print("SERVIDOR FINALIZADO")
