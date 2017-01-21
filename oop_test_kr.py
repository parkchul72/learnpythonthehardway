# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "%%% 클래스라는 %%%의 일종을 만든다.", # is-a
    "calss %%%(object):\n\tdef __init__(self, ***)":
        "%%% 클래스는 self와 *** 매개변수를 받는 __init__를 가졌다.", # has-a
    "class %%%(object):\n\tdef ***(self, @@@)":
        "%%% 클래스는 self와 @@@ 매개변수를 받는 이름이 ***인 함수를 가졌다.", # has-a
    "*** = %%%()":
        "*** 변수를 %%% 클래스의 인스턴스 하나로 정한다.",
    "***.***(@@@)":
        "*** 변수에서 *** 함수를 받아 self, @@@ 매개변수를 넣어 호출한다.",
    "***.*** ='***'":
        "*** 변수에서 *** 속성을 받아 *** 값으로 정한다.",
}

# do they want to drill phrases first
if len(sys.argv)  == 2:
    PHRASES_FIRST = True
else:
    PHRASES_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results  = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results


try:
    while  True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASES_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "답: %s\n\n" %answer
except EOFError:
    print "\nBye"