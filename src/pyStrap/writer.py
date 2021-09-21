from pyStrap.schemas import SetupCfg, Requirements, GitIgnore

from abc import ABC, abstractmethod

class ConfigWriter(ABC):

    @staticmethod
    @abstractmethod
    def write_config():
        pass

class SetupCfgWriter(ConfigWriter):

    @staticmethod
    def write_config(config: SetupCfg):
        conf = config.get_configparser()
        with open("setup.cfg", "w") as setup:
            conf.write(setup)

class RequirementsWriter(ConfigWriter):

    @staticmethod
    def write_config(config: Requirements):
        with open("requirements.txt", "w") as reqs:
            reqs.writelines([f"{req}\n" for req in config.requirements])

        with open("requirements_dev.txt", "w") as reqs:
            reqs.writelines([f"{req}\n" for req in config.dev])

        
class GitIgnoreWriter(ConfigWriter):

    @staticmethod
    def write_config(config: GitIgnore):
        with open(".gitignore", "w") as gitignore:
            gitignore.writelines([f"{ignore}\n" for ignore in config.ignores])


        
