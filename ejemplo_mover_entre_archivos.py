import os
import shutil

>>> for folderName, subfolders, filenames in os.walk(r'C:\Users\Daniel\Desktop\Institue Of coding(Futurelearning)'):
	print('the folder is ' + foldername)
	print('the subfolders in ' + foldername + ' are: ' + str(subfolders))
	print('the filenames in ' + foldername + ' are: ' + str(filenames))
	print()

    for subfolder in subfolders:
        if 'fish' in subfolder:
           #os.rmdir(subfolder)
            print('rmdir on ' + subfolder)
    for file in filenames:
        if file.endswith('.py'):
            #shutil.copy(ps.join(folderName, file), os.join(folderName, file + '.backup')
                        
