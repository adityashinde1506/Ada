import logging

logger=logging.getLogger(__name__)

class Node(object):

    """
        This class implements a single node in the tree. 
    """
    def __init__(self,node_path):

        self.full_path=node_path
        self.name=self.full_path.parts[-1]
        logger.debug(f"Created node {self.name} under {self.full_path}.")
        
        self.children=[Node(child) for child in self.full_path.iterdir()]

    @property
    def name(self):
        return self.name

    @property
    def full_path(self):
        return self.full_path

    @property
    def children(self):
        return self.children
