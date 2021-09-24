from pyStrap.schemas import BaseSetup, MetaData, Options
from pyStrap.CLI.utils.basic import choose_pathtype, choose_path, create_default_options


def create_base_prompt() -> BaseSetup:
    print("Please enter a name for your project")
    name = input("Name: ")
    ptype = choose_pathtype()
    path = choose_path(ptype)
    return BaseSetup(project_name=name,base_path=path)

def create_meta_prompt(pname: str) -> MetaData:
    print("Please enter the following information to create your project's meta data")
    desc = input("Description: ")
    author = input("Author: ")
    return MetaData(name=pname, description=desc, author=author)

def create_options_prompt() -> Options:
    print("Please enter a delimiter for your requirements. To use ',' as a default enter a 'd'")
    delim = input("Delimiter: ")
    print("Now enter your requirements as a string using your delimiter. The String must end with your delimiter.")
    reqs = input("Requirements: ")
    if delim == "d":
        return create_default_options(reqs=reqs)
    return create_default_options(reqs=reqs, delimiter=delim)



    

