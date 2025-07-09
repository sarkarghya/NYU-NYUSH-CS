import hashlib
import json

# wordlist file
wordlist_path = 'weakpass_3w.txt'

# hashes/original passwords
# hashes_file_path = './formspring/formspring.txt'
hashes_file_path = './linkedin/SHA1.txt'
# hashes_file_path = './yahoo/pure_pass.json' # json for yahoo


# output file
output_file_path = 'output.txt'

# compare hash against wordlist
def bruteforce_wordlist(hashes):
    match_count = 0
    limit = 100  # Limit to 100 entries
    
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as wordlist, \
        open(output_file_path, 'w') as output_file:
        
        for word in wordlist:
            word = word.replace("\n","")

            # Hash the wordlist word using hashing method as detected by https://www.tunnelsup.com/hash-analyzer/#google_vignette
            # word_hash = hashlib.sha256(word.encode('utf-8')).hexdigest() # for formspring
            word_hash = hashlib.sha1(word.encode('utf-8')).hexdigest() # for linkedin
            # word_hash = word # for yahoo

            if word_hash in hashes:
                output_file.write(f"{word_hash} {word}\n")
                # output_file.write(f"{data[word_hash]} {word}\n") # json for yahoo

                match_count += 1

                # remove the hash from the set once cracked to improve performance
                hashes.remove(word_hash)

                if match_count >= limit:
                    print(f"Reached the limit of {limit} entries. Exiting.")
                    break


with open(hashes_file_path, 'r') as hash_file:
    ## In case of json
    # data = json.load(hash_file)
    # hashes = set(data.keys())

    hashes = set() # lookup table of hashes
    for line in hash_file:
        hashes.add(line.replace("\n",""))

bruteforce_wordlist(hashes)
