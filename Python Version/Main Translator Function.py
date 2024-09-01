def translate_neolux_to_python(neolux_code):
    python_code = neolux_code

    # Apply each pattern and translation function
    for name, pattern in patterns.items():
        matches = pattern.findall(python_code)
        for match in matches:
            translation_func = globals().get(f'translate_{name}')
            if translation_func:
                python_code = python_code.replace(match[0], translation_func(match))

    # Remove leftover NeoLux syntax markers (e.g., '*')
    python_code = python_code.replace('*', '').replace('~', '')
    
    return python_code.strip()
