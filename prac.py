print("Om Namah Shivay")

# def get_formatted_name(first_name,middle_name,last_name):
#     formatted_name = f"{first_name} {middle_name} {last_name}"
#     return formatted_name.title()

# name= get_formatted_name("Leonel","Andres","Messi")
# print(name)

def get_formatted_name(first_name,last_name,middle_name=" "):
    if middle_name:
        formatted_name = f"{first_name} {middle_name} {last_name}"
    else:
        formatted_name = f"{first_name} {last_name}"
    return formatted_name.title()

name= get_formatted_name("Leonel","messi","Andres" )
print(name)