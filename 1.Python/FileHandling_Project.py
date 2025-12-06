from pathlib import Path
import os 

def read_FileFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f'{i+1}: {items}')
        

def createFile():
    try:
        read_FileFolder()
        name = input("Please tell your file name:")
        p = Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data = input("What you want to write in this file:")
            print(f"FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exist")
    
    except Exception as err:
        print(f"An error occured: {err}")
        
def readFile():
    try:
        read_FileFolder()
        name = input("Which file you want to read:")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("READ SUCCESSFUL")
        else:
            print("The file does not exist")
    except Exception as err:
        print(f"An error occured:{err}")
        
def updateFile():
    try:
        read_FileFolder()
        name = input("Tell which file you want to update:")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for Changing the name of your file")
            print("Press 2 for Overwritting the data of your file")
            print("Press 3 for Appending some content in your file")
            res = int(input("Tell Your Response:"))
            
            if res == 1:
                name2 = input("Tell your new file name:")
                p2 = Path(name2)
                p.rename(p2)
            elif res == 2:
                with open(p,'w') as fs:
                    data = input("Tell what you want to write, this will overwrite the data:")
                    fs.write(data)
            elif res == 3:
                with open(p,'a') as fs:
                    data = input("Tell what You want to append:")
                    fs.write(" " + data)
    except Exception as err:
        print(f"An error occured: {err}")
        
        
def deleteFile():
    try:
        read_FileFolder()
        name = input("Enter the file name you want to delete:")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p) or os.remove(name)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("No Such File Exists")
    except Exception as err:
        print(f"An Error Occured: {err}")
        

print("Press 1 for CREATING a file")
print("Press 2 for READING a file")
print("Press 3 for UPDATING a file")
print("Press 4 for DELETION a file")

check = int(input("Please tell your response:"))


if check == 1:
    createFile()
elif check == 2:
    readFile()
elif check == 3:
    updateFile()
elif check == 4:
    deleteFile()