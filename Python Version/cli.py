import argparse
from .translator import Translator  # Adjust imports as needed

def main():
    parser = argparse.ArgumentParser(description='NeoLux CLI')
    parser.add_argument('command', type=str, help='The command to run')
    parser.add_argument('args', nargs=argparse.REMAINDER, help='Arguments for the command')
    
    args = parser.parse_args()
    
    if args.command == 'translate':
        if len(args.args) < 2:
            print("Usage: neolux translate <source_file> <destination_file>")
            return
        
        source_file = args.args[0]
        destination_file = args.args[1]
        
        translator = Translator()
        with open(source_file, 'r') as src, open(destination_file, 'w') as dst:
            source_code = src.read()
            translated_code = translator.translate(source_code)
            dst.write(translated_code)
            
        print(f"Translation complete: {destination_file}")
    
    else:
        print(f"Unknown command: {args.command}")
        print("Available commands: translate")

if __name__ == "__main__":
    main()
