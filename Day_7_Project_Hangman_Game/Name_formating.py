def format_name(f_name,l_name):
    """Making the names into title format without using inbuilt functions"""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"

    f_name.lower()
    l_name.lower()

    first_name = ''
    first_name += f_name[0].upper()
    for letter in range(1,len(f_name)):
        first_name += f_name[letter]

    last_name = ''
    last_name += l_name[0].upper()
    for letter in range(1,len(l_name)):
        last_name += l_name[letter]

    return f"{f_name} {l_name}"

def format_names(f_name,l_name):
    """making the names into title format, using the inbuilt function title()"""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    f_name = f_name.title()
    l_name = l_name.title()

    return f"{f_name} {l_name}"


print(format_name("",""))
print(format_names("ram", "raju"))
