with open("requirements.txt") as requirement_file:
        requirement_list = requirement_file.readlines()     # reading each line from the file
requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]    # Removing '\n' from the list of libraries
    
# if HYPHEN_E_DOT in requirement_list:
#     requirement_list.remove(HYPHEN_E_DOT)      # Removing '-e .' as it is not required

print(requirement_list)
