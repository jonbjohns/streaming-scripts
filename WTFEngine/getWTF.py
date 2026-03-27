import json
import sys
from random import randint

contents = []


def main():
    """
    This script is expected currently to pass a single parameter, this triggers the match/case block below.
    This main method essentially selects which json file to be used for the current execution.
    :return: Within the Match/Case, this returns a randomized string based on the selected json file.
    """
    args = sys.argv[1:]

    match args[0]:
        case "1":
            # load template 1
            return print(get_phrase("PATH_TO_JSON_FILE"))
        case "2":
            # load template 2
            return print(get_phrase("PATH_TO_JSON_FILE"))
    # you can chain additional cases if you want to use additional json files for different purposes

    return


def evaluate(word):
    """
    This method is used when a reference to a key is found, it checks to see if there are multiple values to a key.
    In this case, a random value string is selected to build the final string. Values can contain multiple key
    references.
    :param word: string, expected to be one of the keys within the json file
    :return: recursively returns a randomized string based on the evaluated keys
    """
    test = len(contents[word])
    if test == 1:
        return build_template(contents[word][0].split(" "))
    else:
        return build_template(contents[word][randint(0, len(contents[word]) - 1)].split(" "))


def build_template(template):
    """
    This method iterates through the string array and builds a string. It looks to see if one of the values is a
    reference to a key in the json file, if a key is found, it calls evaluate() to recursively resolve the key.
    :param template: string[]
    :return: string
    """
    resolved = ""
    # check each word, if it isn't a keyword, add to response
    for word in template:
        if word[0] == '@':
            # recursively evaluating the key that was found and building the string, skipping the leading @
            resolved += evaluate(word[1:])
        else:
            # the current work is not a key, adding to the string
            resolved += word + " "

    return resolved


def get_phrase(path):
    """
    After receiving the json path from main, this builds the final phrase. This is currently written in the way that
    we don't expect the heading or response values to contain references to keys. We send the selected template to
    build_template to catch keys in the value and evaluate them in evaluate().
    :param path: path to json file to be read and parsed into a string
    :return:
    """
    global contents
    # load json file
    with open(path, 'r') as j:
        contents = json.loads(j.read())

    # start building the phrase
    phrase = contents['heading'][randint(0, len(contents['heading']) - 1)]
    template = contents['template'][randint(0, len(contents['template']) - 1)]
    response = contents['response'][randint(0, len(contents['response']) - 1)]

    phrase += build_template(template.split(" ")) + response
    return phrase


if __name__ == '__main__':
    main()
