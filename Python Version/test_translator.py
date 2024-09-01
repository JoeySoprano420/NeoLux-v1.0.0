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
        'For Loop': {
            'input': '''
function main() ~
    let names = ["Alice", "Bob", "Charlie"] *
    for name in names ~
        print(name) *
    end ~
end +
''',
            'expected': '''
def main():
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        print(name)
'''
        },
        'Nested Data Structures': {
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
        'Conditional Statements': {
            'input': '''
function check_value(value) ~
    if value > 10 ~
        print("Greater than 10") *
    else ~
        print("10 or less") *
    end ~
end +
''',
            'expected': '''
def check_value(value):
    if value > 10:
        print("Greater than 10")
    else:
        print("10 or less")
'''
        },
        'Try-Catch Block': {
            'input': '''
function safe_divide(a, b) ~
    try ~
        let result = a / b *
    catch ZeroDivisionError ~
        print("Cannot divide by zero") *
    end ~
end +
''',
            'expected': '''
def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
'''
        },
        'Complex Case': {
            'input': '''
function complex_example() ~
    let numbers = [1, 2, 3] *
    while len(numbers) > 0 ~
        let num = numbers.pop(0) *
        print(num) *
    end ~
end +
''',
            'expected': '''
def complex_example():
    numbers = [1, 2, 3]
    while len(numbers) > 0:
        num = numbers.pop(0)
        print(num)
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
