import os

def rename_files_to_sequence(folder_name):
    # folder_name = "man"
    folder_man = os.listdir(folder_name)
    numero = 1
    for name in folder_man:
        a = folder_name+"/"+name
        b = folder_name+"/"+str(numero)+".jpg"
        os.rename(a,b)
        numero+=1
    
# rename_files_to_sequence("man")
rename_files_to_sequence("woman")