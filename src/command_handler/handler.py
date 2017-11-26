import logging

logger=logging.getLogger(__name__)

class Handler(object):

    def __init__(self):
        logger.debug("Command handler initialised.")

    def match_command(self,command_dict):
        name=command_dict["name"]
        command_dict.pop("name")
        arg_dict=command_dict
