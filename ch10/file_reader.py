from pathlib import Path

path = Path('text_files/pi_digits.txt')
contents = path.read_text()
# contents = contents.rstrip()
# print(contents)
lines = contents.splitlines()
for line in lines:
    print(line)