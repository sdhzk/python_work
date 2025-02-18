from pathlib import Path

path = Path('text_files/pi_million_digits.txt')
contents = path.read_text()
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()

birthday = input("Enter you birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appers in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")