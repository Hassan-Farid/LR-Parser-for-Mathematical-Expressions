import json
#Node class to contain values in a tree node structure
class Node:
    
    #Node takes into consideration a root value 
    #and left and right children values
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right
        
    #Node provides a method to make its object json serializable
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
        
    #Node provides a method to display the contents
    #of the node via print function
    def __repr__(self):
        return "{}".format({'root': self.root,
                'children': {
                    'left': self.left,
                    'right': self.right,
                }
               })
