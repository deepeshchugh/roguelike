from cgi import test
from .rule_teacher import RuleTeacher
from l_star_inexperienced.common.constants import _Const

CONST = _Const()

class OrcTrollRatioRule(RuleTeacher):

    def __init__(self, orc_ratio, troll_ratio):
        super().__init__(is_mandatory=False)
        self.orc_ratio = orc_ratio
        self.troll_ratio = troll_ratio
    
    def membership_query(self, test_word: str):
        num_orcs = 0
        num_trolls = 0
        for char in test_word.upper():
            if char == 'O':
                num_orcs += 1
            elif char == 'T':
                num_trolls += 1
        if num_orcs == 0 or num_trolls == 0:
            return CONST.DONT_CARE
        if num_orcs % self.orc_ratio == 0 and num_trolls % self.troll_ratio == 0:
             if int(num_orcs/num_trolls) == int(self.orc_ratio/self.troll_ratio):
                 return CONST.DONT_CARE
        return CONST.NEG