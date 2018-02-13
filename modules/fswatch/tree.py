import logging

logger=logging.getLogger(__name__)

from pathlib import Path
from ada.module.fswatch.node import Node

class DirTree(object):

    """
        Implements directory tree as a python dict.
    """

    def __init__(self,root):
        self.root=Path(root)
        self.tree=Node(self.root)
