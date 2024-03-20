import re

INPUT_FILE = ''
OUTPUT_FILE = ''

with open(INPUT_FILE, 'r') as f:
    str_bin = re.sub(r'[^0-1]', '', ''.join(line for line in f))

SIZE = 8
with open(OUTPUT_FILE, 'w') as f:
    str_hex = ''.join('{:02x}'.format(int(str_bin[i:i + SIZE], 2)) for i in range(0, len(str_bin), SIZE))
    f.write(str_hex)
