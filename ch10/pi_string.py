from pathlib import Path

# path = Path('text_files/pi_digits.txt')
path = Path('text_files/pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(f"{pi_string[:51]}...")
print(len(pi_string))