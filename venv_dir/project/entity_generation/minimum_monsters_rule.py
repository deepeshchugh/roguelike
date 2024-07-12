from .rule_teacher import RuleTeacher
from l_star_inexperienced.common.constants import _Const

CONST = _Const()

class MinimumMonstersRule(RuleTeacher):

    def __init__(self, minimum_monsters):
        super().__init__(is_mandatory=True)
        self.minimum_monsters = minimum_monsters

    @property
    def minimum_monsters(self):
        return self._minimum_monsters

    @minimum_monsters.setter
    def minimum_monsters(self, value):
        if value < 0:
            raise Exception("Minimum monsters cannot be less than 0")
        self._minimum_monsters = value
    
    def membership_query(self, test_word):
        num_monsters = len(test_word)
        if num_monsters < self.minimum_monsters:
            return CONST.NEG
        return CONST.POS
    
    def get_rule_text(self):
        return "More Monsters! Raise minimum monsters to {min}".format(min=self.minimum_monsters)

if __name__ == "__main__":
    print(MinimumMonstersRule(minimum_monsters=1).get_rule_text())