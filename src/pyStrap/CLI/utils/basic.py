from typing import Union, Optional
import os
from pyStrap.CLI.enums import Confirm, PathType
from pyStrap.schemas import Options


def confirm(user_input: str) -> Confirm:
    positiv = ["y", "yes", "+", "ye"]
    negativ = ["n", "no", "-"]
    if user_input.lower() in positiv:
        return Confirm.YES
    elif user_input.lower() in negativ:
        return Confirm.NO
    else:
        return Confirm.INVALID

def parse_path_type(user_input: str) -> PathType:
    relativ = ["r", "rel", "reltive"]
    absolut = ["a", "ab", "abs", "absoulte"]
    if user_input.lower() in relativ:
        return PathType.RELATIVE
    elif user_input.lower() in absolut:
        return PathType.ABSOLUTE
    else:
        return PathType.INVALID

def choose_pathtype() -> PathType:
    print("Before entering your base path please choose if you want to enter a relativ(r) or absolut(a) path")
    path_type = input("Type: ")
    path_type = parse_path_type(path_type)
    if path_type is PathType.INVALID:
        print("Please enter a valid path type")
        choose_pathtype()
    return path_type

def check_base_path_relativ(
    path: Union[str, os.PathLike]
) -> Union[str, os.PathLike]:
    if path == ".":
        return os.getcwd()
    else:
        path = os.path.join(os.getcwd(), path)
        if not os.path.isdir(path):
            raise IsADirectoryError(f"The path {path} is not a directory.")
        return path

def check_base_path_absolute(
    path: Union[str, os.PathLike]
) -> Union[str, os.PathLike]:
    if not os.path.isdir(path):
        raise IsADirectoryError(f"The path {path} is not a directory")
    return path

def choose_path(ptype: PathType) -> os.PathLike:
    print("Now enter the base path for your project. (. is accepted as a relativ path)")
    path = input("Path: ")
    if ptype is PathType.RELATIVE:
        return check_base_path_relativ(path=path)
    else:
        return check_base_path_absolute(path=path)

def create_default_options(
    reqs: str,
    delimiter: Optional[str] = ",",
) -> Options:
    if delimiter not in reqs:
        raise ValueError(f"Delimiter {delimiter} not in found in your requirements")
    return Options(
        requires=reqs.split(delimiter)
    )

