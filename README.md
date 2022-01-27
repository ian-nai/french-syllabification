# french-syllabification
A rule-based algorithm to split French words into syllables.

## Getting Started
```
pip install -r requirements.txt
```
## The Scripts

### syllabize_from_txt_file.py
This script cleans your input .txt file, tokenizes it into words, and then tries to count the syllables in each word in two ways:
* By getting the verified syllable count from the [Lexique](http://www.lexique.org/) list contained in syl_lexique.csv
* Or, if the word is not in the Lexique list, by running the algorithm to count the syllables itself

The words and their syllable counts are then output to a .csv file.

### syllabizer.py 
This is the algorithm to count syllables in a text. It will take values from your input .csv and output its prediction for how many syllables each word contains.

### compare_and_syllabize_csv.py
This script compares the inputs in your .csv file to words with verified syllable counts from [Lexique](http://www.lexique.org/). These counts are included in the syl_lexique.csv file.
