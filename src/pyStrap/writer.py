from pyStrap.schemas import SetupCfg, Requirements, GitIgnore, PyProject

from abc import ABC, abstractmethod
from typing import Any

import toml


class ConfigWriter(ABC):

    @staticmethod
    @abstractmethod
    def write_config(config: Any) -> None:
        pass


class SetupCfgWriter(ConfigWriter):

    @staticmethod
    def write_config(config: SetupCfg):
        conf = config.get_configparser()
        with open("setup.cfg", "w") as setup:
            conf.write(setup)


class PyProjectWriter(ConfigWriter):

    @staticmethod
    def write_config(config: PyProject) -> None:
        data = config.generate_toml()
        with open("pyproject.toml", "w") as proj:
            toml.dump(data, proj)


class RequirementsWriter(ConfigWriter):

    @staticmethod
    def write_config(config: Requirements) -> None:
        with open("requirements.txt", "w") as reqs:
            reqs.writelines([f"{req}\n" for req in config.requirements])

        with open("requirements_dev.txt", "w") as reqs:
            reqs.writelines([f"{req}\n" for req in config.dev])


class GitIgnoreWriter(ConfigWriter):

    @staticmethod
    def write_config(config: GitIgnore) -> None:
        with open(".gitignore", "w") as gitignore:
            gitignore.writelines([f"{ignore}\n" for ignore in config.ignores])
