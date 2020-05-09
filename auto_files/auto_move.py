import os, shutil

os.mkdir('/Users/jonaslaurinaitis/Desktop/core/PY/other')
path = '/Users/jonaslaurinaitis/Desktop/core/PY/other'

for folderName, subFolders, fileName in os.walk('/Users/jonaslaurinaitis/Desktop/core'):
    print('Folder name is ' + folderName)
    print('The subfolders name in ' + folderName + ' are: ' + str(subFolders))
    print('The filenames in ' + folderName + ' are: ' + str(fileName))
    print()

    #for file in fileName:
        #if file in ["file.txt", "files.py", "shelfiles"]:
            try:
                shutil.copy(os.path.join(folderName, file), path)
            except shutil.SameFileError:
                pass

        
              
