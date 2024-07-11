from .rule_teacher import RuleTeacher
from l_star_inexperienced.common.constants import _Const

CONST = _Const()

class MinimumTrollsRule(RuleTeacher):

    def __init__(self, minimum_trolls):
        super().__init__(is_mandatory=True)
        self.minimum_trolls = minimum_trolls

    @property
    def minimum_trolls(self):
        return self._minimum_trolls

    @minimum_trolls.setter
    def minimum_trolls(self, value):
        if value < 0:
            raise Exception("Minimum monsters cannot be less than 0")
        self._minimum_trolls = value
    
    def membership_query(self, test_word):
        num_orcs = 0
        num_trolls = 0
        for char in test_word.upper():
            if char == 'O':
                num_orcs += 1
            elif char == 'T':
                num_trolls += 1
        if num_trolls < self.minimum_trolls:
            return CONST.NEG
        return CONST.DONT_CARE

if __name__ == "__main__":
    print(MinimumTrollsRule(1).membership_query("o"))
    print(MinimumTrollsRule(1).membership_query("ooT"))
    print(MinimumTrollsRule(1).membership_query("oTT"))