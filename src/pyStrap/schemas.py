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


@dataclass
class PythonSetup:
    python3: bool = True
    python2: bool = False
    python3_versions: List[str] = ["3.6", "3.7", "3.8", "3.9"]
    python2_versions: List[str] = []


@dataclass
class MetaData:
    name: str
    description: str
    author: str
    license_type: str = "MIT"
    license_file: str = "LICENSE"
    platforms: List[str] = ["unix", "linux", "osx", "cygwin", "win32"]
    python_settings: PythonSetup = PythonSetup()


@dataclass
class Options:
    package: str
    requires: List[str]
    python_version: str = ">=3.6"
    package_dir: str = "=src"
    zip_safe: str = "no"


@dataclass
class TestingOptions:
    testing: List[str] = [
        "pytest>=6.0",
        "pytest-cov>=2.0",
        "mypy>=0.910",
        "flake8>=3.9",
        "tox>=3.24"
        ]
    flake8_max_line_length: int = 160
    py_typed: bool = True


@dataclass
class SetupCfg:
    meta: MetaData
    options: Options
    testing: TestingOptions


@dataclass
class GitIgnore:
    ignores: List[str]
