#Folder raport

import os





def AskFolders():
    folder = " "
    raport_location = " "
    
    while True:
        folder = input("From wich folder do you want raport: ")
        if  os.path.exists(folder):
            break
        else:
            print("Please give proper folder")
            
    while True:
        raport_location = input("Where do you want your raport ")
        if  os.path.exists(raport_location):
            break
        else:
            print("Please give proper folder")




    raport_location = raport_location.replace("\\", "/")
    raport_location = raport_location + "/raport_location.txt"
    return [folder, raport_location]




def getSize(file, folder):
        location = os.path.join(folder, file)
        item_info = os.stat(location)
        size = item_info.st_size
        if size >= (1024 ** 4):
            size = round(size / (1024 ** 4), 2)
            return str(size) + "Tb"
        elif size >= (1024 ** 3):
            size = round(size / (1024 ** 3), 2)
            return str(size) + "Gb"
        elif size >= (1024 ** 2):
            size = round(size / (1024 ** 2), 2)
            return str(size) + "Mb"
        elif size >= (1024 ):
            size = round(size / (1024), 2)
            return str(size) + "Kb"
        else:
            size = round(size, 2)
            return str(size) + "b"


def locate_file(desktop, Desktop_items):
    for tiedosto in os.listdir(desktop):
        Desktop_items.append(tiedosto)

def write_raport(folder, file_path, Desktop_items):
    with open(file_path, "w") as file:
        file.write("DESKTOP APPLICATIONS" + "\n")
        for item in Desktop_items:
            size = getSize(item, folder)
            name, suffix = os.path.splitext(item)
            if suffix == "": suffix = "folder"
            file.write(f"{name:40} {suffix:20} {size:} \n")



def main():
    Desktop_items = []

    locations = AskFolders()#folder, raport_folder

    locate_file(locations[0], Desktop_items) 
    write_raport(locations[0], locations[1], Desktop_items)
    print("Valmis")

main()