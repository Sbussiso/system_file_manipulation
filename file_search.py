import os
import time
from pathlib import Path
import subprocess


def permissions_to_string(permissions_octal):
    permission_str = ''
    permission_dict = {4: 'r', 2: 'w', 1: 'x'}

    for digit in str(permissions_octal)[-3:]:
        digit = int(digit)
        permission_str += ''.join([permission_dict.get(bit, '-') for bit in (4, 2, 1) if digit & bit])
        permission_str += ''.join(['-' for bit in (4, 2, 1) if not digit & bit])

    return permission_str


def full_system_specific_file_search_tool():

    print('NOTE: This program searches the entire C drive for a user-specified file')
    user_input = input("Enter the filename you want to search for: ")

    # Finds specified files in the local directory
    matched_files = []
    search = ['C:\\']
    print(f'Searching for {user_input} files.....')
    for i in search:
        for root, dirs, files in os.walk(i):
            for file in files:
                if file == user_input:
                    file_path = os.path.join(root, file)
                    matched_files.append(file_path)
    print(f'{user_input} files found!')

    # Prints the file paths and additional information of the matched files
    print(f'Displaying the paths and information of the {user_input} files:')
    for file_path in matched_files:
        file_info = os.stat(file_path)
        file_size = file_info.st_size
        date_created = time.ctime(file_info.st_ctime)
        date_modified = time.ctime(file_info.st_mtime)
        file_extension = os.path.splitext(file_path)[1]
        file_permissions = permissions_to_string(file_info.st_mode & 0o777) #makes permissions readable




        print(f'File path: {file_path}')
        print(f'File size: {file_size} bytes')
        print(f'Date created: {date_created}')
        print(f'Date modified: {date_modified}')
        print(f'File extension: {file_extension}')
        print(f"File permissions: {file_permissions}")
        print('---')
    

def system_ext_search_tool(): #searches the C drive for all files containing user specified extension
    print('NOTE: This program searches the entire C drive for a user-specified file')
    user_input = input ("Enter the extension you want to search for: ")
    
    #Finds specified files in the local directory
    matched_files = []
    search = ['C:\\']
    print(f'Searching for files containing {user_input}.....')
    for i in search:
        for root, dirs, files in os.walk(i):
            for file in files:
                if file.endswith(user_input):
                    file_path = os.path.join(root, file)
                    matched_files.append(file_path)
        count = len(matched_files) #counts how many matching files have been found
        print(f'{count} matching files found!')
        print('preparing to display files.....')
        time.sleep(2)
        print(matched_files) #displays contents in terminal

        

        #TODO: get this to create the text file in the current folder the program is in
        
        #writes output to file
        with open('search_results.txt', 'w') as f:
            f.write(f'Number of files found: {count}\n')
            for file_path in matched_files:
                file_info = os.stat(file_path)
                file_size = file_info.st_size
                date_created = time.ctime(file_info.st_ctime)
                date_modified = time.ctime(file_info.st_mtime)
                file_extension = os.path.splitext(file_path)[1]
                file_permissions = permissions_to_string(file_info.st_mode & 0o777)

                f.write(f'File path: {file_path}\n')
                f.write(f'File size: {file_size} bytes\n')
                f.write(f'Date created: {date_created}\n')
                f.write(f'Date modified: {date_modified}\n')
                f.write(f'File extension: {file_extension}\n')
                f.write(f"File permissions: {file_permissions}\n")
                f.write('---\n')
        
        #opens file
        try:
            subprocess.call(["open", "search_results.txt"])
        except FileNotFoundError:
            print("file cannot be found :(")



if __name__ == "__main__":
    
    while True:
    
        print("search for a specific file.......1")
        print("search files by extension........2")

        user_input = input("Enter: ")
        if user_input == str(1):
            full_system_specific_file_search_tool()
        elif user_input == str(2):
            system_ext_search_tool()
        else:
            print("invalid input try again :(")
