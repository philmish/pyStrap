from pyStrap.schemas import BaseSetup, SetupCfg, Requirements, GitIgnore, PyProject
from pyStrap.writer import SetupCfgWriter, PyProjectWriter, RequirementsWriter, GitIgnoreWriter


class pyStrapper:

    def __init__(
        self,
        base: BaseSetup,
        setup: SetupCfg,
        project: PyProject,
        requirements: Requirements,
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
        pass

    def strap(self) -> None:
        self._pre_setup()
        self._setup()
        self._post_setup()
