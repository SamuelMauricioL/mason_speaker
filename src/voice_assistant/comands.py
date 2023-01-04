import os
import webbrowser
from src.utils.respond import respond
from src.utils.selector_cli import selector_cli
from src.core.global_configuration import GlobalConfiguration
from src.core.global_paths import GlobalPaths

global_config = GlobalConfiguration()


def set_project():
    global_config.set_project()


def open_project():
    # TODO: en caso se llame desde create_feature pasar path como parametro
    # TODO: en caso se llame esta como primera función agregar set_project()
    # TODO: en caso de llamen esta como segunda función llamar get_project_path()
    # set_project()
    project_path = global_config.get_project_path()
    os.system("code -n {} ".format(project_path))


def create_feature():
    os.system("mason ls > {}".format(GlobalPaths.output_txt))
    with open('util/output.txt') as f:
        lines = f.readlines()
        bricks = []
        for brick in lines[1:]:
            brick = brick.split("── ")[1]
            brick = brick.split(" ->")[0]
            bricks.append(brick)
    selected_brick = selector_cli(bricks, 'brick')
    respond("where do you want to create the feature?")
    global_config.set_feature()
    feature_path = global_config.get_feature_path()
    os.system(
        "mason make {} -o {}".format(selected_brick['brick'], feature_path))
    open_project()


def search_brick():
    brick_name = input('brick name: ')
    webbrowser.open(
        'https://brickhub.dev/search?q={}'.format(brick_name), new=2)
