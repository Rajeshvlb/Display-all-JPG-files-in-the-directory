import os, glob
user_input = input('Please enter the path(Ex: C:/Users/my_Name/Pictures): ') # Simply Enter the path with drive specified 
user_file = input('What type of file you want to scan(Ex: jpg, png, py): ') # Getting an extension to scan
file_type = '*' + user_file
user_input = str(user_input)
print('Retrieving please wait...\n')
os.chdir(user_input) #Users can specify their custom path to scan
for file in glob.glob(file_type):
    print(file)