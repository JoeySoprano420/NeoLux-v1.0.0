from antlr4 import InputStream, CommonTokenStream
from antlr4.ParseTreeVisitor import ParseTreeVisitor

def parse_with_antlr(code):
    input_stream = InputStream(code)
    lexer = NeoLuxLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = NeoLuxParser(stream)
    tree = parser.start_rule()
    visitor = NeoLuxVisitor()
    return visitor.visit(tree)
