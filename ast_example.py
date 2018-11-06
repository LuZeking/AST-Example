import ast

class GenericVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)
visitor = GenericVisitor()

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

print('-- Example 4 --')
code = 'if True:...'
result = ast.parse(code)
visitor.visit(result)

print('-- Example 5 --')
code = 'if a is True:...'
result = ast.parse(code)
visitor.visit(result)

class Visitor(ast.NodeVisitor):
    def visit_If(self, node):
        statement = "If statement always evaluates to {} on line {}"
        test_condition = node.test
        if isinstance(test_condition, ast.NameConstant):
            print(statement.format(test_condition.value, node.lineno))
        ast.NodeVisitor.generic_visit(self, node)

    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)


visitor = Visitor()
print('-- Example 6 --')
code = 'if True:...'
result = ast.parse(code)
visitor.visit(result)