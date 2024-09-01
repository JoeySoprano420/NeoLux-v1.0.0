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

def translate_print_statement(match):
    content = match[1]
    return f'print({content})'

def translate_comments(match):
    return f'# {match[0][1:-1]}'
