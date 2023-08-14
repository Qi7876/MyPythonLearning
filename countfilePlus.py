import re
import sys
import os

fileList = os.listdir()
specialWordList = set()
wordsCountResult = dict()


def filecounterplus(result):
    try:
        result_file = open(result, 'w', encoding='UTF-8')
    except:
        result_file = open(result, 'x', encoding='UTF-8')
    for unknownfile in fileList:
        if unknownfile[0].lower() == 'a':
            source_file = open(unknownfile, 'r', encoding='utf-8')
            source_file_read = source_file.read()
            # Extract the special words appear in the essay to split the whole essay.
            for word in source_file_read:
                if 'a' <= word <= 'z' or 'A' <= word <= 'Z':
                    continue
                elif word in ['?', '.', '+', '$', '*', '^', '(', ')', '{', '}', '[', ']', '|', '\\', '/', '\"', '\'']:
                    specialWordList.add('\\' + word)
                else:
                    specialWordList.add(word)
            special_words = '|'.join(list(specialWordList))
            # To gather statistics data of the words.
            words_list = re.split(special_words, source_file_read)
            for word in words_list:
                word = word.lower()
                if word == '':
                    continue
                elif word not in wordsCountResult:
                    wordsCountResult[word] = 1
                else:
                    wordsCountResult[word] += 1
            source_file.close()
    # Write the result into the file.
    for double in sorted(list(wordsCountResult.items())):
        result_file.write(f'{double[0]:20}==>{double[1]:10d}\n')
    result_file.close()


filecounterplus(sys.argv[1])
