filename = input("Enter the name of the file you want to read: ")

try:
     
    with open(filename, 'r') as file:
        content = file.read()
    
    modified_content = content.upper()
 
    with open('modified_' + filename, 'w') as new_file:
        new_file.write(modified_content)   

    print("Modified content has been saved.")
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    print("Error: Could not read or write the file.")  
