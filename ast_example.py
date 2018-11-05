import ast

class Visitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)
visitor = Visitor()

print('-- Example 1 --')
code = 'pressure = 3'
result = ast.parse(code, mode='exec')
visitor.visit(result)

print('-- Example 2 --')
code = '3'
result = ast.parse(code, mode='eval')
visitor.visit(result)

print('-- Example 3 --')
code = 'print(3 + 4)'
result = ast.parse(code, mode='eval')
visitor.visit(result)