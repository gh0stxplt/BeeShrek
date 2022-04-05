with open('bee_script.txt', 'rt') as f:
    bee_script = f.read()

with open('shrek_script.txt', 'r') as f:
    shrek_script = f.read()

with open('holy_grail.txt', 'w') as f:
    f.write(bee_script.replace('bee', shrek_script))