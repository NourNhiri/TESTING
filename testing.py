import libcst as cst
from libcst.display import dump
tree=(cst.parse_expression("2 * (3 * 4) + 5"))

class Visitor(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self.sum=[]
    

    def visit_Integer(self,node:cst.Integer):
        print(node.value)
        self.sum.append(int(node.value))




class MultiplicationOperandVisualizer(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self.num=[]
   
    def visit_BinaryOperation(self, node:cst.BinaryOperation):
        if isinstance(node.operator,cst.Multiply):
            v=Visitor()
            tree=node
            tree.visit(v)
            self.num=v.sum  
            return False
               


v=MultiplicationOperandVisualizer()
tree.visit(v)
        





