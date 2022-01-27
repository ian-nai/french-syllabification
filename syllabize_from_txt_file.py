import string
import random
import pandas
import csv
import itertools
import nltk
from nltk.corpus import stopwords
import codecs

def indexes(word,letter):
    for i,x in enumerate(word):
         if x == letter:
             yield i


# Using NLTK's default French stopwords
default_stopwords = set(nltk.corpus.stopwords.words('french'))

# Our input file - substitute the file name for your own .txt
input_file = ['beauverie.txt']

lines_cleaned = []

for f in input_file:
    fp = codecs.open(f, 'r', 'utf-8')

    t = fp.read()

    tokenizer = nltk.data.load('tokenizers/punkt/PY3/french.pickle')

    lines_split = tokenizer.tokenize(t)

    for f in lines_split:
        # Tokenize the text into words
        words = nltk.word_tokenize(f)

        # Remove single-character tokens (mostly punctuation)
        words = [word for word in words if len(word) > 1]

        # Remove numbers
        words = [word for word in words if not word.isnumeric()]

        # Lowercase all words (default_stopwords are lowercase too)
        words = [word.lower() for word in words]

        # Remove stopwords
        #words = [word for word in words if word not in default_stopwords]

        str_words = " ".join(words)

        lines_cleaned.append(str_words)

    for line in lines_cleaned:
        if not line:
            lines_cleaned.remove(line)


    complete_text = " ".join(lines_cleaned).split()


def detect_syllables():

    predefined_words = pandas.read_csv("syl_lexique.csv", sep=r'\s*,\s*',
                               header=0, encoding='utf-8', engine='python')

    data = pandas.read_csv("syl_lexique.csv", sep=r'\s*,\s*',
                               header=0, encoding='utf-8', engine='python')

    predefined_words_trimmed = predefined_words.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    data_trimmed = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    list_of_predefined_words = predefined_words_trimmed['word'].values.tolist()
    predefined_syls = predefined_words_trimmed['syls_real'].values.tolist()

    word_text = []
    syls_list = []
    stringed_syls = []


    word_trimmed = data_trimmed['word'].values.tolist()
    actual_syls = data_trimmed['syls_real'].values.tolist()
    for x in actual_syls:
        stringed_syls.append(str(x))



    vowels = ['a', 'e', 'i', 'o', 'u', 'y','à', 'â', 'æ', 'œ', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü', 'ÿ']
    punct = ['-', "'"]
    word_endings_2 = ['ez', 'is']
    word_endings_3 = ['ait', 'ons', 'ont']
    word_endings_4 = ['aient']
    word_endings_5 = ['issent', 'issons']


    for word in complete_text:
        syls = 0

        if word in list_of_predefined_words:
            index_to_match = list_of_predefined_words.index(word)
            syl_count = predefined_syls[index_to_match]
            syls = syl_count
            syls_list.append(str(syls))


        elif word not in list_of_predefined_words:
            end_of_string_counter = 0
            two_cons_counter = 0
            w = str(word)
            print(w)
            syls = 0
            last_ind = len(w)
            print(last_ind)
            last_letter = w[(last_ind - 1)]
            print(last_letter)
            for i,j, in enumerate(range(1,(len(w)))):
                if len(w) - j >= 2:
                    if w[i] in vowels:
                        if w[j] not in vowels and w[j] not in punct:
                            if w[j+1] in vowels:
                                test_result = list( indexes(w, w[j+1]) )
                                if test_result[-1] == (last_ind - 1):
                                        if end_of_string_counter == 0:
                                            if len(word_text) <= 5:
                                                syls += 1
                                                print('end of string')
                                                end_of_string_counter = 1
                                            if len(word_text) >= 6:
                                                syls += 1
                                                print('end of string')
                                if test_result[-1] != (last_ind - 1):
                                        if len(word_text) <= 6:
                                            syls += 1
                                            print('one con added')
                                        if len(word_text) >= 7:
                                            syls += 1
                                            print('one con added')

            # checking verb endings
            for x in word_endings_2:
                if w[-2:] == x:
                    check_con1 = w.split(x)
                    check_con1 = list(filter(None, check_con1))
                    check_con = str(check_con1)
                    if check_con[-1] not in vowels and check_con[-1] not in punct:
                        syls += 1
                        print('ending')
                    else:
                        syls += 1
                        print('pass not added')
                        pass
            for x in word_endings_3:
                if w[-3:] == x:
                    check_con1 = w.split(x)
                    check_con1 = list(filter(None, check_con1))
                    check_con = str(check_con1)
                    print('check_con: ' + check_con[-1])
                    if check_con[-1] not in vowels and check_con[-1] not in punct:
                        syls += 1
                        print('ending')
                    if check_con[-1] in vowels or check_con[-1] in punct:
                        syls += 1
                        print('not added')
                        pass
            for x in word_endings_4:
                if w[-5:] == x:
                        check_con1 = w.split(x)
                        check_con1 = list(filter(None, check_con1))
                        check_con = str(check_con1)
                        print('check_con: ' + check_con[-1])
                        if check_con[-1] not in vowels and check_con[-1] not in punct:
                            syls += 1
                            print('ending')
                        if check_con[-1] in vowels or check_con[-1] in punct:
                            syls += 1
                            print('not added')
                            pass
            for x in word_endings_5:
                if w[-6:] == x:
                    w.split(x)
                    check_con = w.split(x)
                    print('check_con: ' + check_con[-1])
                    if check_con[-1] not in vowels and check_con[-1] not in punct:
                        syls += 1
                        print('ending')
                    if check_con[-1] in vowels or check_con[-1] in punct:
                        print('not added')
                        pass

            # 2 vowels between two consonants
            for i,j, in enumerate(range(1,(len(w)))):
                    if len(w) - j >= 3:
                        if w[i] in vowels:
                            if w[j] not in vowels and w[j] not in punct:
                                if w[j+1] not in vowels and w[j+1] not in punct:
                                    if w[j+2] in vowels:
                                        if len(word_text) <= 6:
                                            syls += 1
                                            print('two cons added')
                                            two_cons_counter = 1
                                        if len(word_text) > 6:
                                            syls += 1
                                            print('two cons added')

            # 3 consonants between 2 vowels
            for i,j, in enumerate(range(1,(len(w)))):
                    if len(w) - j >= 4:
                        if w[i] in vowels:
                            if w[j] not in vowels and w[j] not in punct:
                                if w[j+1] not in vowels and w[j+1] not in punct:
                                    if w[j+2] not in vowels and w[j+2] not in punct:
                                        if w[j+3] in vowels and w[j+3] not in punct:
                                            if len(word_text) <= 6:
                                                syls += 1
                                                print('three cons added')
                                            if len(word_text) > 6:
                                                syls += 1
                                                print('three cons added')

            # consonants with two vowels in between
            for i,j, in enumerate(range(1,(len(w)))):
                    if len(w) - j >= 3:
                        if w[i] not in vowels:
                            if w[j] in vowels and w[j] not in punct:
                                if w[j+1] in vowels and w[j+1] not in punct:
                                        if w[j+2] not in vowels and w[j+2] not in punct:
                                            if len(word_text) <= 6:
                                                syls += 1
                                                print('two vowels row added')
                                            if len(word_text) > 6:
                                                syls += 1
                                                print('two vowels row added')

            # 3 vowels between 2 consonants
            for i,j, in enumerate(range(1,(len(w)))):
                    if len(w) - j >= 4:
                        if w[i] not in vowels:
                            if w[j] in vowels and w[j] not in punct:
                                if w[j+1] in vowels and w[j+1] not in punct:
                                    if w[j+2] in vowels and w[j+2] not in punct:
                                        if w[j+3] not in vowels and w[j+3] not in punct:
                                            if len(word_text) <= 6:
                                                syls += 1
                                                print('three vowels added')
                                            if len(word_text) >= 7:
                                                syls += 1
                                                print('three vowels added')

            #consonant followed by r or l
            for i,j, in enumerate(range(1,(len(w)))):
                if w[i] not in vowels:
                    if w[j] == 'r' or w[j] == 'l':
                        if w[j] != w[-1]:
                            if w[j+1] == 'e':
                                if w.index(w[j]) <= 3:
                                    pass
                                if w.index(w[j]) > 3:
                                    syls -= 1
                                    print('r or l subtracted')


            # dealing with hyphens, e aigu, and apostrophes
            for i,j, in enumerate(range(1,(len(w)))):
                if w[i] == '-':
                        syls += 1
                        print('hyphen added')


            if w[-1:] == 'é':
                        syls += 1
                        print('aigu added')

            for i,j, in enumerate(range(1,(len(w)))):
                if w[i] == "'":
                    if w[j] in vowels:
                        syls += 1
                        print('apostrophe added')

            # two or three vowels in a row (change to between consonants?)
            for i,j, in enumerate(range(1,(len(w)))):
                    if len(w) - j >= 4:
                        if w[i] in vowels:
                            if w[j] in vowels:
                                if w[j+1] in vowels:
                                    if w[j+2] not in vowels:
                                        pass
                                    else:
                                        if len(word_text) <= 6:
                                            syls += 1
                                            print('two vowels subbed')
                                        if len(word_text) >= 7:
                                            syls += 1
                                            print('two vowels subbed')
                                if w[j+1] not in vowels:
                                    if len(word_text) <= 6:
                                        pass
                                    if len(word_text) >= 7:
                                        syls += 1
                                        print('two vowels subbed')


            if syls <= 0:
                if len(w) <= 5:
                    syls = 1


            print(syls)
            syls_list.append(str(syls))

    rows = zip(complete_text, syls_list)

    with open("testing.csv", "w") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)



detect_syllables()
