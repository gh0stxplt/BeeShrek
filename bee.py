bee_script = open("bee_script.txt", "rt")
shrek_script = open("shrek_script.txt", "r")
shrek = shrek_script.read()
holy_grail = open("holy_grail.txt", "wt")

for line in bee_script:
    holy_grail.write(line.replace('bee', shrek))

bee_script.close()
shrek_script.close()
holy_grail.close()
