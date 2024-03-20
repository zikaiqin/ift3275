# Script credited to https://github.com/yhuag/Crib-Dragging-Auto-Cracker

import re
import csv
import enchant

# Name of the dictionary used to validate words
LANG = "fr_FR"
d = enchant.Dict(LANG)

# Minimum length of the crib word
MIN_CRIB_LEN = 4

# Minimun length of the internal partial matching word
# This should be less or equal to MIN_CRIB_LEN
MIN_INTERNAL_LEN = MIN_CRIB_LEN - 1

# Load the list of most common words as crib word candidates
DICT_FILE = 'dict.csv'
with open(DICT_FILE, 'r', encoding='utf-8-sig') as f:
    reader = csv.reader(f)
    crib_list = list(reader)

# Remove the header and filter words of insufficient length
crib_list = [w for line in crib_list[1:] if len(w := line[0]) >= MIN_CRIB_LEN]

# Provide the filename of the cipher text
INPUT_FILE = 'cipher.txt'
with open(INPUT_FILE, 'r') as cipher:
    CIPHER_HEX = next(cipher)

# Decode the hexadecimal cipher text
cipher_text = bytes.fromhex(CIPHER_HEX).decode('latin_1')

# Provide the name of the output file
OUTPUT_FILE = 'results.txt'

# Function credited to https://github.com/SpiderLabs/cribdrag
# @param ctext:     The cipher text to be crib dragged
# @param crib:      The crib word to drag on the cipher text
# @return results:  A list of matches
def sxor(ctext, crib):
    results = []
    single_result = ''
    crib_len = len(crib)
    positions = len(ctext)-crib_len+1
    for index in range(positions):
        single_result = ''
        for a,b in zip(ctext[index:index+crib_len],crib):
            single_result += chr(ord(a) ^ ord(b))

        # Split between whitespaces
        split_results = [w for w in re.split(r'\s+', single_result) if len(w) >= MIN_INTERNAL_LEN]

        # Add result if all parts form a valid word
        if len(split_results) > 0 and all(result_partial.isalpha() and d.check(result_partial) for result_partial in split_results):
            results.append(single_result + "(" + str(index) + ")")

    return results

# This function executes the crib dragging of a single word on the cipher text
# And write/append the result to the target output file
def writeResultGivenCrib(ctext, crib):
    results = sxor(ctext, crib)
    if (results_len := len(results)) > 0:
        # Write to the output (Append)
        with open(OUTPUT_FILE, 'a', encoding='utf-8-sig') as text_file:
            text_file.write(crib + "(" + str(results_len) + "): [ " + ', '.join(results) + " ]\n")

# Clear the content of the output file before starting to append
open(OUTPUT_FILE, 'w').close()

# Iterate through the crib word list
for idx, crib_word in enumerate(crib_list):
    # Write the result to the file
    print(str(idx) + ': ' + crib_word)
    writeResultGivenCrib(cipher_text, crib_word)
