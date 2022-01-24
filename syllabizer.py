import string
import random
import pandas
import csv
import itertools

def indexes(word,letter):
    for i,x in enumerate(word):
         if x == letter:
             yield i

def detect_syllables():
    data = pandas.read_csv("syllables_acc.csv", sep=r'\s*,\s*',
                               header=0, encoding='utf-8', engine='python')

    print(data['word'])
    word_text = []
    syls_list = []
    stringed_syls = []
    data_trimmed = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    word_trimmed = data_trimmed['word'].values.tolist()
    actual_syls = data_trimmed['syls_real'].values.tolist()
    for x in actual_syls:
        stringed_syls.append(str(x))

    print(stringed_syls)
    
    vowels = ['a', 'e', 'i', 'o', 'u', 'y','à', 'â', 'æ', 'œ', 'é', 'è', 'ê', 'ë', 'î', 'ï', 'ô', 'ù', 'û', 'ü', 'ÿ']
    punct = ['-', "'"]
    word_endings_2 = ['ez', 'is']
    word_endings_3 = ['ait', 'ons', 'ont']
    word_endings_4 = ['aient']
    word_endings_5 = ['issent', 'issons']



    for w in word_trimmed:
        end_of_string_counter = 0
        two_cons_counter = 0
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
                w.split(x)
                check_con = w.split(x)[0]
                if check_con[-1] not in vowels and check_con[-1] not in punct:
                    syls += 1
                    print('ending')
                else:
                    print('pass not added')
                    pass
        for x in word_endings_3:
            if w[-3:] == x:
                w.split(x)
                check_con = w.split(x)[0]
                if check_con[-1] not in vowels and check_con[-1] not in punct:
                    syls += 1
                    print('ending')
                if check_con[-1] in vowels or check_con[-1] in punct:
                    print('not added')
                    pass
        for x in word_endings_4:
            if w[-5:] == x:
                    w.split(x)
                    check_con = w.split(x)[0]
                    if check_con[-1] not in vowels and check_con[-1] not in punct:
                        syls += 1
                        print('ending')
                    if check_con[-1] in vowels or check_con[-1] in punct:
                        print('not added')
                        pass
        for x in word_endings_5:
            if w[-6:] == x:
                w.split(x)
                check_con = w.split(x)[0]
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
                                        syls += 2
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

#     Code that was used for testing accuracy:

#     correct = 0
#     incorrect = 0

#     print(syls_list)
#     print(stringed_syls)
#     index_corr = ([index for index, (e1, e2) in enumerate(zip(syls_list, stringed_syls)) if e1 == e2])
#     print('correct number: ' + str(len(index_corr)))
#     accuracy = ((len(index_corr) / len(syls_list)))
#     print('accuracy percent: ' + str(accuracy))

#     rows = zip(word_trimmed, stringed_syls, syls_list)

#     with open("testing.csv", "w") as f:
#         writer = csv.writer(f)
#         for row in rows:
#             writer.writerow(row)

        with open('syllables_count.csv','a') as fd:
            for x in syls_list:
                fd.write(str(x))


detect_syllables()
