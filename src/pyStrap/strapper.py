from pyStrap.schemas import BaseSetup, SetupCfg, Requirements, GitIgnore, PyProject
from pyStrap.writer import SetupCfgWriter, PyProjectWriter, RequirementsWriter, GitIgnoreWriter


class pyStrapper:

    def __init__(
        self,
        base: BaseSetup,
        setup: SetupCfg,
        project: PyProject,
        requirements: Requirements = Requirements(),
        gitignore: GitIgnore = GitIgnore()
    ) -> None:
        self.base = base
        self.setup = setup
        self.project = project
        self.requirements = requirements
        self.gitignore = gitignore

    def _pre_setup(self) -> None:
        self.base.setup_dirs()
        self.base.setup_files()

    def _setup(self) -> None:
        SetupCfgWriter.write_config(config=self.setup)
        PyProjectWriter.write_config(config=self.project)
        RequirementsWriter.write_config(config=self.requirements)
        GitIgnoreWriter.write_config(config=self.gitignore)

    def _post_setup(self) -> None:
        with open(f"{self.base.base_path}/setup.py", "w") as s:
            lines = ["from setuptools import setup\n", "if __name__ == '__main__':\n", "\tsetup()"]
            s.writelines(lines)
        open(f"{self.base.base_path}/src/{self.base.project_name}/__init__.py", "w").close()

    def _get_base_info(self):
        return f"Name: {self.base.project_name}\nDescription: {self.setup.meta.description}\nAuthor: {self.setup.meta.author}"
    
    def show_base_info(self):
        print(self._get_base_info())

    def strap(self) -> None:
        self._pre_setup()
        self._setup()
        self._post_setup()
