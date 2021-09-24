import click
from pyStrap.CLI.utils.default import create_base_prompt, create_meta_prompt, create_options_prompt
from pyStrap.schemas import BuildSystem, MyPyOptions, PyProject, PyTestOptions, Requirements, SetupCfg, TestingOptions
from pyStrap.strapper import pyStrapper

@click.group()
def create():
    pass

@create.command(name="default")
def default():
    click.echo("Welcome to the pyStrap Project creation tool.")
    base = create_base_prompt()
    meta = create_meta_prompt(pname=base.project_name)
    opts = create_options_prompt()
    setup_cfg = SetupCfg(meta=meta, options=opts, testing=TestingOptions())
    proj = PyProject(
        build_system=BuildSystem(),
        PyTest=PyTestOptions(adopts=base.project_name),
        MyPy=MyPyOptions()
        )
    require = Requirements(requirements=opts.requires)
    strapper = pyStrapper(
        base=base,
        setup=setup_cfg,
        project=proj,
        requirements=require
    )
    strapper.show_base_info()
    strapper.strap()

    

if __name__ == "__main__":
    create()
