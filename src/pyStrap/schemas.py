from dataclasses import dataclass, field
from typing import List, Union
import os
import configparser


@dataclass
class BaseSetup:
    project_name: str
    base_path: Union[str, os.PathLike]
    files: List[Union[str, os.PathLike]] = field(default_factory=lambda: [
        "tox.ini",
        "setup.py",
        "setup.cfg",
        ".gitignore",
        "README.md",
        "pyproject.toml",
        "LICENSE",
        "requirements.txt",
        "requirements_dev.txt",
        ])
    dirs: List[Union[str, os.PathLike]] = field(default_factory=lambda: [
        "src",
        "tests",
    ])

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
    python3_versions: List[str] = field(default_factory=lambda: ["3.6", "3.7", "3.8", "3.9"])
    python2_versions: List[str] = field(default_factory=lambda: [])

    def generate_classifiers(self) -> str:
        base = "\n"
        if self.python3 and self.python2:
            base += "Programming Language :: Python :: 3\n"
            for version in self.python3_versions:
                base += f"Programming Language :: Python :: {version}\n"
            base += "Programming Language :: Python :: 2\n"
            for version in self.python2_versions:
                base += f"Programming Language :: Python :: {version}\n"
        elif self.python3 and not self.python2:
            base += "Programming Language :: Python :: 3\n"
            base += "Programming Language :: Python :: 3 :: Only\n"
            for version in self.python3_versions:
                base += f"Programming Language :: Python :: {version}\n"
        else:
            pass

        return base


@dataclass
class MetaData:
    name: str
    description: str
    author: str
    license_type: str = "MIT"
    license_file: str = "LICENSE"
    platforms: List[str] = field(default_factory=lambda: ["unix", "linux", "osx", "cygwin", "win32"])
    python_settings: PythonSetup = PythonSetup()

    def generate_platforms(self) -> str:
        return ", ".join(self.platforms)


@dataclass
class Options:
    requires: List[str]
    python_version: str = ">=3.6"
    package_dir: str = "=src"
    zip_safe: str = "no"

    def generate_requirements(self) -> str:
        base = "\n"
        for requirement in self.requires:
            base += f"{requirement}\n"
        return base


@dataclass
class TestingOptions:
    testing: List[str] = field(default_factory=lambda: [
        "pytest>=6.0",
        "pytest-cov>=2.0",
        "mypy>=0.910",
        "flake8>=3.9",
        "tox>=3.24"
        ])
    flake8_max_line_length: int = 160
    py_typed: bool = True

    def generate_testing_reqs(self) -> str:
        base = "\n"
        for requirement in self.testing:
            base += f"{requirement}\n"
        return base

    def get_pytyped(self) -> str:
        if self.py_typed:
            return "yes"
        else:
            return "no"


@dataclass
class SetupCfg:
    meta: MetaData
    options: Options
    testing: TestingOptions

    def get_configparser(self) -> configparser.ConfigParser:
        conf = configparser.ConfigParser()
        conf["metadata"] = {
            "name": self.meta.name,
            "description": self.meta.description,
            "author": self.meta.author,
            "license": self.meta.license_type,
            "license_file": self.meta.license_file,
            "platforms": self.meta.generate_platforms(),
            "classifiers": self.meta.python_settings.generate_classifiers()
        }
        conf["options"] = {
            "package": f"\n{self.meta.name}\n",
            "install_requires": self.options.generate_requirements(),
            "python_requires": self.options.python_version,
            "package_dir": f"\n{self.options.package_dir}\n",
            "zip_safe": self.options.zip_safe
        }
        conf["options.extras_require"] = {"testing": self.testing.generate_testing_reqs()}
        conf["options.package_data"] = {f"{self.meta.name}": self.testing.get_pytyped()}
        conf["flake8"] = {"max-line-length": str(self.testing.flake8_max_line_length)}
        return conf


@dataclass
class BuildSystem:
    requires: List[str] = field(default_factory=lambda: ["setuptools>=42.0", "wheel"])
    build_backend: str = "setuptools.build_meta"

    def dict(self):
        return self.__dict__


@dataclass
class PyTestOptions:
    adopts: str
    testpaths: List[str] = field(default_factory=lambda: ["tests"])

    def dict(self):
        return self.__dict__


@dataclass
class MyPyOptions:
    mypy_path: str = "src"
    check_untyped_defs: bool = True
    disallow_any_generics: bool = True
    ignore_missing_imports: bool = True
    no_implicit_optional: bool = True
    show_error_codes: bool = True
    strict_equality: bool = True
    warn_redundant_casts: bool = True
    warn_return_any: bool = True
    warn_unreachable: bool = True
    warn_unused_configs: bool = True
    no_implicit_reexport: bool = True

    def dict(self):
        return self.__dict__


@dataclass
class PyProject:
    build_system: BuildSystem
    PyTest: PyTestOptions
    MyPy: MyPyOptions

    def generate_toml(self):
        return {
            "build-system": self.build_system.dict(),
            "tool.pytest.ini_options": self.PyTest.dict(),
            "tool.mypy": self.MyPy.dict()
            }


@dataclass
class Requirements:
    requirements: List[str] = field(default_factory=lambda: [])
    dev: List[str] = field(default_factory=lambda: [
        "flake8==3.9.2",
        "tox==3.24.3",
        "pytest==6.2.5",
        "pytest-cov==2.12.1",
        "mypy===0.910"
        ])


@dataclass
class GitIgnore:
    ignores: List[str] = field(default_factory=lambda: [
        "__pycache__/",
        "*.py[cod]",
        "*$py.class",
        "*.so",
        ".Python",
        "build/",
        "develop-eggs/",
        "dist/",
        "downloads/",
        "eggs/",
        ".eggs/",
        "lib/",
        "lib64/",
        "parts/",
        "sdist/",
        "var/",
        "wheels/",
        "pip-wheel-metadata/",
        "share/python-wheels/",
        "*.egg-info/",
        ".installed.cfg",
        "*.egg",
        "MANIFEST",
        "*.manifest",
        "*.spec",
        "pip-log.txt",
        "pip-delete-this-directory.txt",
        "htmlcov/",
        ".tox/",
        ".nox/",
        ".coverage",
        ".coverage.*",
        ".cache",
        "nosetests.xml",
        "coverage.xml",
        "*.cover",
        "*.py,cover",
        ".hypothesis/",
        ".pytest_cache/",
        ".env",
        ".venv",
        "env/",
        "venv/",
        "ENV/",
        "env.bak/",
        "venv.bak/",
        ".mypy_cache/",
        ".dmypy.json",
        "dmypy.json",
        ".pyre/",
        "*.db"
    ])
