def apply_septinarty_logic(condition):
    states = {
        0: 'is',
        1: 'is not',
        2: 'is both',
        3: 'is neither',
        4: 'is undefined',
        5: 'is flexible/mutable',
        6: 'is dependent on variables'
    }
    
    # Example application of Septinarty logic
    # This is a placeholder; actual implementation will depend on specific use cases
    return states.get(condition, 'unknown state')

def analyze_condition(condition):
    # Tokenize and analyze the condition based on Septinarty Logic
    tokens = condition.split()
    analyzed = [apply_septinarty_logic(int(token)) if token.isdigit() else token for token in tokens]
    return ' '.join(analyzed)
