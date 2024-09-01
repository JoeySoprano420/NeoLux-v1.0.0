def test_translator():
    test_cases = {
        'Simple Function': {
            'input': '''
+ This is a comment +

function greet(name) ~
    print("Hello, ", name) *
end +
''',
            'expected': '''
# This is a comment

def greet(name):
    print("Hello, ", name)
'''
        },
        'Complex Case with Advanced Data Structures': {
            'input': '''
function process_data() ~
    let data = { "key1": [1, 2, 3], "key2": {"subkey": 4} } *
    print(data) *
end +
''',
            'expected': '''
def process_data():
    data = { "key1": [1, 2, 3], "key2": {"subkey": 4} }
    print(data)
'''
        },
        'Ambiguous String Challenge': {
            'input': '''
function ambiguous_example() ~
    let ambiguous = "value" + 1 *
    print(ambiguous) *
end +
''',
            'expected': '''
def ambiguous_example():
    ambiguous = "value" + 1
    print(ambiguous)
'''
        },
        'Code-Switching Test': {
            'input': '''
function hello_world() ~
    let message = "Hello, World!" *
    print(message) *
end +

function hola_mundo() ~
    let mensaje = "¡Hola, Mundo!" *
    print(mensaje) *
end +

hello_world() *
hola_mundo() *
''',
            'expected': '''
def hello_world():
    message = "Hello, World!"
    print(message)

def hola_mundo():
    mensaje = "¡Hola, Mundo!"
    print(mensaje)

hello_world()
hola_mundo()
'''
        }
    }

    for name, test in test_cases.items():
        input_code = test['input']
        expected_output = test['expected']
        output_code = translate_neolux_to_python(input_code)
        if output_code.strip() == expected_output.strip():
            print(f'{name}: Passed')
        else:
            print(f'{name}: Failed')
            print(f'Expected:\n{expected_output}')
            print(f'Got:\n{output_code}')

# Run tests
test_translator()
