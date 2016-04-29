from Parse import Parse
from Word import Word


class Rule:
    def __init__(self, tag_a, tag_b):
        self.precision = 0.0
        self.tag_a = tag_a
        self.tag_b = tag_b
        self.text = "Select " + tag_a + " for" + " WORD " + "if the tag of OTHER WORD is " + tag_b

    def apply(self, word, other_word, words):

        condition = (other_word.assigned_parse.tag == self.tag_b)
        tag_a_is_at_least_one_tag_of_morph_parses_of_word = False

        word.sortParses()  # to find the parse which is most likely
        parse_to_assign_to_word = None
        parses = Word.find_word_by_text(word.text, words).parses
        for parse in parses:

            if parse.tag == self.tag_a:
                tag_a_is_at_least_one_tag_of_morph_parses_of_word = True
                parse_to_assign_to_word = parse
                break

        if condition is True and tag_a_is_at_least_one_tag_of_morph_parses_of_word is True:
            word.assigned_parse = parse_to_assign_to_word
            print(word.text + " kelimesinin tagi DEGISTIRILDI!" + parse_to_assign_to_word.text)

class PossibleRules:

    def __init__(self, tags):
        self.rules = []
        for tag_a in tags:
            for tag_b in tags:
                rule = Rule(tag_a=tag_a, tag_b=tag_b)
                self.rules.append(rule)
