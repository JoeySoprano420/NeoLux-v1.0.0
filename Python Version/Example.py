neolux_code = '''
+ This is a comment +

function greet(name) ~
    print("Hello, ", name) *
end +

function main() ~
    let names = ["Alice", "Bob", "Charlie"] *
    for name in names ~
        greet(name) *
    end ~
end +

main() *
'''

python_code = translate_neolux_to_python(neolux_code)
print(python_code)
