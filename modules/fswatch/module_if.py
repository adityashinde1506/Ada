import logging

logger=logging.getLogger(__name__)

from ada.modules.interface import Interface
from ada.modules.fswatch.tree import Tree

class ModuleIface(Interface):

    def __init__(self,config):
        self.config=config
        Interface.__init__(self,"fswatch")

    def init(self):
        self.tree=Tree(self.config["root"])
