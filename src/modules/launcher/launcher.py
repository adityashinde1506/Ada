import logging

logger=logging.getLogger(__name__)

class Launcher(object):

    def __init__(self,config):
        self.apps=config
        self.params=set(["object","name","contains","like"])
        logger.debug("Launcher initialised")

    def __check_args(self,keys):
        for key in keys:
            if key not in self.params:
                return False
        return True

    def file_launch(self,args):
        if "contains" in args.keys():
            self.

    def master(self,args):
        if not self.__check_args(args.keys()):
            logger.error("Invalid params.")
        obj=args["object"]
        args.pop("object")
        if obj == "file":
            self.file_launch(args)
        elif obj == "app":
            self.app_launch(args)
