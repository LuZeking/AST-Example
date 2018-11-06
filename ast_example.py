import ast


def print_example(number, code):
    print('---- Example {}: {} ----'.format(number, code))




class GenericVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        print(type(node).__name__)
        ast.NodeVisitor.generic_visit(self, node)
visitor = GenericVisitor()

code = 'pressure = 3'
print_example(1, code)
result = ast.parse(code, mode='exec')
visitor.visit(result)

code = '3'
print_example(2, code)
result = ast.parse(code, mode='eval')
visitor.visit(result)

code = 'print(3 + 4)'
print_example(3, code)
result = ast.parse(code, mode='eval')
visitor.visit(result)

code = 'if True:...'
print_example(5, code)
result = ast.parse(code)
visitor.visit(result)

code = 'if a is True:...'
print_example(5, code)

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
code = 'if True:...'
print_example(6, code)
result = ast.parse(code)
visitor.visit(result)



