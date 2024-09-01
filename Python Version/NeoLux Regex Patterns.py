import re

# Extended NeoLux Regex Patterns
patterns = {
    'function_def': re.compile(r'\bfunction\s+(\w+)\s*\(([^)]*)\)\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*\+', re.MULTILINE),
    'function_call': re.compile(r'(\w+)\s*\(([^)]*)\)\s*\*', re.MULTILINE),
    'let_statement': re.compile(r'\blet\s+(\w+)\s*=\s*(\[[^\]]*\]|\{[^}]*\}|[^*]+)\s*\*', re.MULTILINE),
    'for_loop': re.compile(r'\bfor\s+(\w+)\s+in\s+(\[[^\]]*\])\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*~\s*', re.MULTILINE),
    'if_statement': re.compile(r'\bif\s+([^~]*)\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*~\s*', re.MULTILINE),
    'else_if_statement': re.compile(r'\belse\s+if\s+([^~]*)\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*~\s*', re.MULTILINE),
    'else_statement': re.compile(r'\belse\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*~\s*', re.MULTILINE),
    'while_loop': re.compile(r'\bwhile\s+([^~]*)\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*~\s*', re.MULTILINE),
    'try_catch': re.compile(r'\btry\s*~\s*\n([\s\S]*?)\s*\*\s*catch\s+([^~]*)\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*~\s*', re.MULTILINE),
    'comments': re.compile(r'\+.*\+', re.MULTILINE),
    'array_literal': re.compile(r'\[(.*?)\]', re.MULTILINE),
    'dict_literal': re.compile(r'\{(.*?)\}', re.MULTILINE),
}
