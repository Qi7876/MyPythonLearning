import re
import sys

specialWordList = set()
wordsCountResult = dict()


def filecounter(filename, result):
    source_file = open(filename, 'r', encoding='utf-8')
    source_file_read = source_file.read()
    result_file = open(result, 'w', encoding='UTF-8')
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
    # Write the result into the file.
    for double in sorted(list(wordsCountResult.items())):
        result_file.write(f'{double[0]:20}==>{double[1]:10d}\n')

    result_file.close()
    source_file.close()


filecounter(sys.argv[0], sys.argv[2])
