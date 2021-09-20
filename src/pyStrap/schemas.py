from dataclasses import dataclass
from typing import List, Union
import os


@dataclass
class BaseSetup:
    project_name: str
    base_path: Union[str, os.PathLike[str]] = os.getcwd()
    files: List[Union[str, os.PathLike[str]]] = [
        "tox.ini",
        "setup.py",
        "setup.cfg",
        ".gitignore",
        "README.md",
        "pyproject.toml",
        "LICENSE",
        "requirements.txt",
        "requirements_dev.txt",
        ]
    dirs: List[Union[str, os.PathLike[str]]] = [
        "src",
        "tests",
    ]

    def setup_files(self):
        for file in self.files:
            open(f'{os.path.join(self.base_path, file)}', "a").close()

    def setup_dirs(self):
        for dir in self.dirs:
            os.makedirs(dir)
        os.mkdir(f"src/{self.project_name}")
