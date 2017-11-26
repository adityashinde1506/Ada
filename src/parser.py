import logging

logger=logging.getLogger(__name__)

class Parser(object):

    def __init__(self):
        logger.info("Parser initialised.")

    def __make_command_dict(self,_string):
        unit=_string.split(":")
        if len(unit)!=2:
            logger.error("Could not parse command string {}".format(_string))
            return None
        else:
            return {unit[0]:unit[1]}

    def parse_command(self,command_string):
        command={}
        command_string=command_string.split()
        commands_list=list(map(self.__make_command_dict,command_string))
        if None in commands_list:
            return None
        else:
            for unit in commands_list:
                command.update(unit)
            logger.debug("Got command {}".format(command))
            return command
