import os
import shutil

from_dir="/Users/kartikeynair/C102 Project" 
to_dir="/Users/kartikeynair/C102 Project/Documents" 

list_of_files = os.listdir(from_dir) 
print(list_of_files) 

for x in list_of_files: 
    name, extension=os.path.splitext(x) 
    print(name) 
    print(extension) 
    
    if extension == '': 
        continue 
    if extension in ['.pdf']: 
        path1= from_dir + '/' + x
        path2= to_dir
        path3= to_dir + '/' + x 
        
        print("path1", path1) 
        print("path2", path2)
        print("path3", path3) 
        
        if os.path.exists(path2):
            shutil.move(path1, path3) 
        
        else:
          os.mkdir(path2) 
          shutil.move(path1, path3)
        