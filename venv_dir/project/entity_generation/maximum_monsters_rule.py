from .rule_teacher import RuleTeacher
from l_star_inexperienced.common.constants import _Const

CONST = _Const()

# Placing this due to DFA and Room restrictions
MAXIMUM_MONSTERS_LIMIT = 5

class MaximumMonstersRule(RuleTeacher):

    def __init__(self, maximum_monsters):
        super().__init__(is_mandatory=True)
        self.maximum_monsters = maximum_monsters

    @property
    def maximum_monsters(self):
        return self._maximum_monsters

    @maximum_monsters.setter
    def maximum_monsters(self, value):
        if value > MAXIMUM_MONSTERS_LIMIT:
            raise Exception("Maximum monsters cannot be more than " + str(MAXIMUM_MONSTERS_LIMIT))
        self._maximum_monsters = value
    
    def membership_query(self, test_word):
        num_monsters = len(test_word)
        if num_monsters > self.maximum_monsters:
            return CONST.NEG
        return CONST.POS

    def get_rule_text(self):
        return "More Monsters! Raise maximum monsters to {max}".format(max=self.maximum_monsters)
    
if __name__ == "__main__":
    print(MaximumMonstersRule(1).membership_query("oT"))
    print(MaximumMonstersRule(2).membership_query("oT"))
    print(MaximumMonstersRule(2).get_rule_text())