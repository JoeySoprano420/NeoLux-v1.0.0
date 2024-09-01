import re

# NeoLux Regex Patterns
patterns = {
    'function_def': re.compile(r'\bfunction\s+(\w+)\s*\(([^)]*)\)\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*\+', re.MULTILINE),
    'function_call': re.compile(r'(\w+)\s*\(([^)]*)\)\s*\*', re.MULTILINE),
    'let_statement': re.compile(r'\blet\s+(\w+)\s*=\s*(\[[^\]]*\]|\{[^}]*\}|[^*]+)\s*\*', re.MULTILINE),
    'for_loop': re.compile(r'\bfor\s+(\w+)\s+in\s+(\[[^\]]*\])\s*~\s*\n([\s\S]*?)\s*\*\s*end\s*~\s*', re.MULTILINE),
    'print_statement': re.compile(r'\bprint\(([^)]+)\)\s*\*', re.MULTILINE),
    'comments': re.compile(r'\+.*\+', re.MULTILINE),
}
