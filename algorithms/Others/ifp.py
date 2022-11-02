#!/usr/bin/env python3

import yaml
import pathlib
import logging
from abc import ABC, abstractmethod
from typing import List

__author__ = 'Pedro Gomes'
__license__ = 'GPL v3+'


def load_configs(config_file_path: pathlib.Path):
    with open(config_file_path, "r", encoding="UTF-8") as config_file:
        return yaml.safe_load(config_file)


def configure_logging():
    logger_handler = logging.StreamHandler()
    logger_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(levelname)s %(name)s : %(message)s',
                                              datefmt='%d-%m-%Y %H:%M:%S%z'))
    logging.basicConfig(level=logging.ERROR, handlers=[logger_handler])


class IFParser(ABC):
    def __init__(self, feed_url: str, threats_to_parse: List[str], ioc_status: str, time: int):
        self.feed_url = feed_url
        self.threats_to_parse = threats_to_parse
        self.ioc_status = ioc_status
        self.time = time
        self.logger = None

    @abstractmethod
    def parse_feed(output_file_name: str):
        pass

    def clean_ouput_file(self, output_file_name: str):
        try:
            pathlib.Path(output_file_name).unlink()
        except FileNotFoundError:
            self.logger.warning(f'"{output_file_name}" not cleaned !')
# TODO