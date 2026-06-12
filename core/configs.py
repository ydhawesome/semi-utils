import configparser
import sys
from pathlib import Path

try:
    import tomllib as tomli
except ModuleNotFoundError:
    import tomli


def get_base_path():
    """获取基础路径，支持打包和开发环境"""
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    return Path(__file__).parent.parent


base_path = get_base_path()
CONFIG_PATH = base_path / 'config' / 'config.ini'
PROJECT_INFO = base_path / 'pyproject.toml'

fonts_dir = base_path / 'config' / 'fonts'
logos_dir = base_path / 'config' / 'logos'
templates_dir = base_path / 'config' / 'templates'


def load_config() -> configparser.ConfigParser:
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH, encoding='utf-8')
    return config


def load_project_info():
    with open(PROJECT_INFO, "rb") as f:
        data = tomli.load(f)
    return data
