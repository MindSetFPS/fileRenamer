import os 

# Loop trough the files in the current directory
for f in os.listdir():
    # Get file name and file extension
    f_name, f_ext = os.path.splitext(f)
    # Get directory name
    path = os.path.basename(os.getcwd())
    
    if f_ext == '.mp4':
        # Remove all the text after the first space 
        file_name = f_name.split(" ", 1)[0]

        #Remove all the text after the first _
        file_name = file_name.split("_", 1)[0] 
        print(file_name) 

        # Contatenate
        new_name = path + 'E' + file_name + f_ext
        print(new_name)
        os.rename(f, new_name)
