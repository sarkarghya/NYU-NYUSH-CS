import json

def extract_line(input_file, output_file):
    data = {} 
    with open(input_file, 'r') as infile:
        for line in infile:
            parts = line.strip().split(':')
            if len(parts) == 3:  # ensure the line has exactly 3 parts
                clear_passwd = parts[2]
                # store the original line with clear_passwd as key
                data[clear_passwd] = line.strip()

    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)

input_file = 'password.file'
output_file = 'pure_pass.json'

extract_line(input_file, output_file)
