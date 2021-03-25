# set the next variable to the full path of your output HISTORY_*.txt file

input_file = open("./tl.txt", encoding="utf16")

# set the next variable to the full path / name of the output file you wish to save

output_file = open("./parsed_tl.txt", 'w')

all_lines = input_file.readlines()

count = 0

# Strips the newline character
for line in all_lines:
    # Skip the first line that is always this
    #	Artwork	Track Title	Artist	Album	Genre	BPM	Rating	Time	Key	Date Added
    if count is 0:
        count += 1
    else:
        out_terms = line.split('\t')
        original = "(Original)"
        original_mix = "(Original Mix)"
        test = out_terms[2].find(original)
        test2 = out_terms[2].find(original_mix)
        print("test: " + str(test) + " test2: " + str(test2))
        fix_title = "" 

        if test > 0:
            fix_title = out_terms[2].replace(original, "")
        elif test2 > 0:
            fix_title = out_terms[2].replace(original_mix, "")
        else:
            fix_title = out_terms[2]

        out_string = fix_title + " - " + out_terms[3] + "\n\n"   
        output_file.write(out_string)
        
        count += 1
# close files
input_file.close
output_file.close