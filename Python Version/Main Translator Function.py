def translate_function_def(match):
    name = match[1]
    params = match[2]
    body = match[3].replace('\n', '\n    ').strip()
    return f'def {name}({params}):\n    {body}'

def translate_function_call(match):
    name = match[1]
    args = match[2]
    return f'{name}({args})'

def translate_let_statement(match):
    var_name = match[1]
    value = match[2]
    value = value.replace('[', '[').replace(']', ']')  # Handling array
    value = value.replace('{', '{').replace('}', '}')  # Handling dictionary
    return f'{var_name} = {value}'

def translate_for_loop(match):
    var_name = match[1]
    iterable = match[2]
    body = match[3].replace('\n', '\n    ').strip()
    return f'for {var_name} in {iterable}:\n    {body}'

def translate_if_statement(match):
    condition = match[1]
    body = match[2].replace('\n', '\n    ').strip()
    return f'if {condition}:\n    {body}'

def translate_else_if_statement(match):
    condition = match[1]
    body = match[2].replace('\n', '\n    ').strip()
    return f'elif {condition}:\n    {body}'

def translate_else_statement(match):
    body = match[1].replace('\n', '\n    ').strip()
    return f'else:\n    {body}'

def translate_while_loop(match):
    condition = match[1]
    body = match[2].replace('\n', '\n    ').strip()
    return f'while {condition}:\n    {body}'

def translate_try_catch(match):
    try_body = match[1].replace('\n', '\n    ').strip()
    exception = match[2]
    catch_body = match[3].replace('\n', '\n    ').strip()
    return f'try:\n    {try_body}\nexcept {exception}:\n    {catch_body}'

def translate_comments(match):
    return f'# {match[0][1:-1]}'
