# WRITING  a file
with open('myfile.txt','w') as file :
      file.write("Hello,this is a text\n")
      
      print("file written !")
      
# READING a file 
with open('myfile.txt','r') as file :
      content = file.read()
      
print(f'file content :{content}')


# APPENDING a file 
with open ('myfile.txt','a') as file : 
      file.write("its a additional line\n")
print("line appended !")

