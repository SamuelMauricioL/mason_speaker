import os
from src.utils.selector_cli import selector_cli
from src.core.global_configuration import GlobalConfiguration


def set_project():
    GlobalConfiguration().set_project()


def open_project():
    project_path = GlobalConfiguration().get_project_path()
    os.system("code -n {}".format(project_path))


def create_feature():
    os.system("mason ls > util/output.txt")
    with open('util/output.txt') as f:
        lines = f.readlines()
        bricks = []
        for brick in lines[1:]:
            brick = brick.split("── ")[1]
            brick = brick.split(" ->")[0]
            bricks.append(brick)
    selected_brick = selector_cli(bricks, 'brick')
    open_project()
    # and use Tk() to select the specific path to do "mason make"
    # tip: use GlobalConfiguration().get_project_path() to open the Tk in the path Project
    os.system("mason make {} -o {}".format(
        selected_brick['brick'], '/Users/samuelaimarmauriciolaime/Documents/personal/mason_speaker/bricks'))
