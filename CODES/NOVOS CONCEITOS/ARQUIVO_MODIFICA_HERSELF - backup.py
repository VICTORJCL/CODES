import re

var = 5
var2= 'mm'
vark='var=mm'

def modify_var(new_value):
    file_path = __file__
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    pattern = re.compile(r'^var\s*=\s*')
    for i, line in enumerate(lines):
        if pattern.match(line.strip()):
            lines[i] = f'var = {repr(new_value)}\n'
            break
    
    with open(file_path, 'w') as f:
        f.writelines(lines)

# Exemplo de uso:
modify_var(5)