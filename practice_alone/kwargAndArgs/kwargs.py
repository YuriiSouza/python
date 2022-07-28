def show_names_with_args(**kwargs):
    for key, name in kwargs.items():
        print(f"The {key} is {name}")

show_names_with_args(name_of_mymon = 'Claudia', name_of_mydad = 'Edmar', name_of_mybro = 'Gabriel')
