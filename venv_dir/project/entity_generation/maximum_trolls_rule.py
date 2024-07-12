from .rule_teacher import RuleTeacher
from l_star_inexperienced.common.constants import _Const

CONST = _Const()

# Placing this due to DFA and Room restrictions
MAXIMUM_MONSTERS_LIMIT = 5

class MaximumTrollsRule(RuleTeacher):

    def __init__(self, maximum_trolls):
        super().__init__(is_mandatory=True)
        self.maximum_trolls = maximum_trolls

    @property
    def maximum_trolls(self):
        return self._maximum_trolls

    @maximum_trolls.setter
    def maximum_trolls(self, value):
        if value > MAXIMUM_MONSTERS_LIMIT:
            raise Exception("Maximum monsters cannot be more than " + str(MAXIMUM_MONSTERS_LIMIT))
        self._maximum_trolls = value
    
    def membership_query(self, test_word):
        num_orcs = 0
        num_trolls = 0
        for char in test_word.upper():
            if char == 'O':
                num_orcs += 1
            elif char == 'T':
                num_trolls += 1
        if num_trolls > self.maximum_trolls:
            return CONST.NEG
        return CONST.DONT_CARE

    def get_rule_text(self):
        return "More Trolls! Raise maximum trolls to {max}".format(max=self.maximum_trolls)

if __name__ == "__main__":
    print(MaximumTrollsRule(1).membership_query("oT"))
    print(MaximumTrollsRule(1).membership_query("ooT"))
    print(MaximumTrollsRule(1).membership_query("oTT"))
    print(MaximumTrollsRule(1).get_rule_text())