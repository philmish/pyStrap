from pyStrap.schemas import BaseSetup, SetupCfg, Requirements
# from pyStrap.writer import SetupCfgWriter, RequirementsWriter


class pyStrapper:

    def __init__(
        self,
        base: BaseSetup,
        setup: SetupCfg,
        requirements: Requirements,
    ) -> None:
        pass

    def pre_setup(self) -> None:
        pass

    def setup(self) -> None:
        pass

    def post_setup(self) -> None:
        pass

    def strap(self) -> None:
        pass
