#functions with Output

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Incorrect input"
    first = f_name.title()
    last = l_name.title()
    return f"{first}  {last}"

print(format_name("","phllips"))