#Luke Xing
#3/30/2017
#Chinese Restaurant Name Generator v1

import random

beginning = ['Welcome to']


def read_txt_file(fname):
    temp = []
    with open(fname, 'r', encoding = 'utf-8', errors = 'ignore') as f:
        content = f.readlines()
        temp = [word.strip() for word in content]
        f.close()
        return temp


def chinese_restaurant_name():

    adjs = read_txt_file("adjectives_chinese.txt")
    nouns = read_txt_file("nouns_chinese.txt")
    n_words = random.randint(1, 5)

    beginning_str = beginning[random.randint(0, len(beginning)-1)]

    adj_list = []
    for i in range(n_words):
        adj_list.append(adjs[random.randint(0, len(adjs)-1)])

    adj_str =  ' '.join(adj_list)

    noun_str = nouns[random.randint(0, len(nouns)-1)]

    print("{0} {1} {2}.".format(beginning_str, adj_str, noun_str))


if __name__ == '__main__':
    chinese_restaurant_name()
