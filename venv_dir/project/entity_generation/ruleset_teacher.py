from l_star_inexperienced.common.constants import _Const
from l_star_inexperienced.teachers import Teacher
from l_star_inexperienced.dfa.dfa import DFA

from .rule_teacher import RuleTeacher
from typing import List

import random

CONST = _Const()
ITER_LIMIT = 1000

class RulesetTeacher(Teacher):

    def __init__(self):
        self.rule_queue: List[RuleTeacher] = []

    def add_rule(self, new_rule: RuleTeacher):
        new_rule_queue = [rule for rule in self.rule_queue if type(rule) != type(new_rule)]
        self.rule_queue = new_rule_queue
        self.rule_queue.append(new_rule)
    
    def get_rule_queue(self):
        return self.rule_queue
    
    def set_rule_queue(self, new_rule_queue: List[RuleTeacher]):
        self.rule_queue = new_rule_queue

    '''
    If even one rule rejects the word, reject it.
    If any rule accepts the word and none reject it, accept it.
    If all rules don't care, we don't either (This is to allow simpler DFAs).
    '''
    def membership_query(self, test_word):
        atleast_one_acceptor = False

        for rule in self.rule_queue:
            rule_result = rule.membership_query(test_word=test_word)
            if rule_result == CONST.NEG:
                return CONST.NEG
            elif rule_result == CONST.POS:
                atleast_one_acceptor = True

        if atleast_one_acceptor:
            return CONST.POS
        return CONST.DONT_CARE

    def equivalence_query(self, proposed_dfa: DFA):
        counter_example = self.find_counterexample(proposed_dfa=proposed_dfa)
        if counter_example is None:
            return True, None
        return False, counter_example
    
    '''
    Presuming Proposed DFA alphabet matches ruleset alphabet.
    '''
    def find_counterexample(self, proposed_dfa: DFA):
        itr = 0
        while itr < ITER_LIMIT:
            print(itr)
            random_word = self.get_random_word(alphabet=proposed_dfa.alphabet)
            if self.is_valid(random_word) is None:
                itr += 1
                continue
            if proposed_dfa.is_word_accepted(random_word) != \
                self.is_valid(random_word):
                return random_word
            itr += 1
        print("couldn't find a counterexample so presuming solved")
        return None

    def is_valid(self, test_word):
        state = self.membership_query(test_word)
        if state == CONST.NEG:
            return False
        if state == CONST.POS:
            return True
        return None

    def get_random_word(self, alphabet):
        word_array = [""]
        end_reached = False
        num_of_letters = len(alphabet)
        while not end_reached:
            new_char_idx = random.randint(0, num_of_letters)
            if new_char_idx == num_of_letters:
                end_reached = True
            else:
                word_array.append(alphabet[new_char_idx])
        return ''.join(word_array)
