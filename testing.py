import libcst as cst

tree=(cst.parse_expression("(1 + 2 / 4 + 7 * 3)"))
class Visitor(cst.CSTVisitor):
    def __init__(self):
        super().__init__()
        self.sum=[]

    def visit_Integer(self,node:cst.Integer):
        print(node.value)
        self.sum.append(int(node.value))

v=Visitor()

tree.visit(v)
print(sum(v.sum))
