from Parse import Parse
from Word import Word


class Rule:
    def __init__(self, tag_a, tag_b):
        self.precision = 0.0
        self.tag_a = tag_a
        self.tag_b = tag_b
        self.text = "Select " + tag_a + " for" + " WORD " + "if the tag of OTHER WORD is " + tag_b
        self.name = "DSX"

    def apply(self, word, other_word, words):
        rule_changed_any_tag = False
        condition = (other_word.assigned_parse.tag == self.tag_b)
        tag_a_is_at_least_one_tag_of_morph_parses_of_word = False

        parse_to_assign_to_word = None
        unique_word = Word.find_word_by_text(word.text, words)
        for parse in unique_word.parses:

            if parse.tag == self.tag_a:
                tag_a_is_at_least_one_tag_of_morph_parses_of_word = True
                parse_to_assign_to_word = parse
                break

        if condition is True and tag_a_is_at_least_one_tag_of_morph_parses_of_word is True:
            if word.assigned_parse != parse_to_assign_to_word:
                word.assigned_parse = parse_to_assign_to_word
                rule_changed_any_tag = True
                #print(word.text + " changed." + self.text)
        return rule_changed_any_tag

class PossibleRules:

    def __init__(self, tags):
        self.rules = []
        rule_id = 2
        for tag_a in tags:
            for tag_b in tags:
                rule = Rule(tag_a=tag_a, tag_b=tag_b)
                rule.name = "DS" + str(rule_id)
                rule_id += 1
                self.rules.append(rule)
