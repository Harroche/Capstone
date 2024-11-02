import ast
import pprint

class CyclomaticComplexity(ast.NodeVisitor):
    
    def __init__(self):
        self.nodes = 0
        self.cyc = 0
    
    def incrementNode(self):
        self.nodes+=1
    
    def walk(self,node):
        self.incrementNode()
        self.generic_visit(node)

    def visit_FunctionDef(self, node):
        self.nodes = 1
        self.generic_visit(node)
        self.cyc=self.nodes

    def visit_If(self, node):
        self.walk(node)
    
    def visit_For(self, node):
        self.walk(node)

    def visit_While(self, node):
        self.walk(node)

    def visit_match_case(self, node):
        self.walk(node)

    def visit_Add(self, node):
        self.walk(node)
    
    def visit_Or(self, node):
        self.walk(node)
    
    def visit_ExceptHandler(self, node):
        self.walk(node)

    
    
    
def cyclomatic(source:str)->int:
    '''Takes in source code and outputs the Cyclomatic Complexity'''
    tree = ast.parse(source)
    result = CyclomaticComplexity()
    result.visit(tree)
    return result.cyc


     

