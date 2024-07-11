from .rule_teacher import RuleTeacher
from l_star_inexperienced.common.constants import _Const

CONST = _Const()

# Placing this due to DFA and Room restrictions
MAXIMUM_MONSTERS_LIMIT = 5

class MaximumOrcsRule(RuleTeacher):

    def __init__(self, maximum_orcs):
        super().__init__(is_mandatory=True)
        self.maximum_orcs = maximum_orcs

    @property
    def maximum_orcs(self):
        return self._maximum_orcs

    @maximum_orcs.setter
    def maximum_orcs(self, value):
        if value < 0:
            raise Exception("Minimum monsters cannot be less than 0")
        self._maximum_orcs = value
    
    def membership_query(self, test_word):
        num_orcs = 0
        num_trolls = 0
        for char in test_word.upper():
            if char == 'O':
                num_orcs += 1
            if char == 'T':
                num_trolls += 1
        if num_orcs > self.maximum_orcs:
            return CONST.NEG
        return CONST.DONT_CARE

if __name__ == "__main__":
    print(MaximumOrcsRule(1).membership_query("oT"))
    print(MaximumOrcsRule(1).membership_query("ooT"))