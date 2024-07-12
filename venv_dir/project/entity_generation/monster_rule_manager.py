from .minimum_monsters_rule import MinimumMonstersRule
from .minimum_orcs_rule import MinimumOrcsRule
from .minimum_trolls_rule import MinimumTrollsRule
from .maximum_monsters_rule import MaximumMonstersRule
from .maximum_orcs_rule import MaximumOrcsRule
from .maximum_trolls_rule import MaximumTrollsRule
from .orc_troll_ratio_rule import OrcTrollRatioRule

import random

MAXIMUM_MONSTERS_LIMIT = 7

class MonsterRuleManager():
    def __init__(self, minimum_monsters, maximum_monsters):
        self.min_total = minimum_monsters
        self.max_total = maximum_monsters
        self.min_orcs = 0
        self.min_trolls = 0
        self.max_orcs = 1
        self.max_trolls = 0
        self.is_max_orcs_set = False
        self.is_max_trolls_set = True

    
    def get_new_potential_rules(self):
        possible_rules = [
            "MinMonsters",
            "MaxMonsters",
            "MinOrcs",
            "MaxOrcs",
            "MinTrolls",
            "MaxTrolls",
            "OrcTrollRatio",
        ]
        potential_rules = []
        while len(potential_rules) < 3 and len(possible_rules) > 0:
            new_rule_type = random.choice(possible_rules)
            match new_rule_type:
                case "MinMonsters":
                    if self.is_min_monsters_possible():
                        potential_rules.append(
                            MinimumMonstersRule(self.min_total + 1)
                        )
                case "MaxMonsters":
                    if self.is_max_monsters_possible():
                        potential_rules.append(
                            MaximumMonstersRule(self.max_total + 1)
                        )
                case "MinOrcs":
                    if self.is_min_orcs_possible():
                        potential_rules.append(
                            MinimumOrcsRule(self.min_orcs + 1)
                        )
                case "MaxOrcs":
                    if self.is_max_orcs_possible():
                        potential_rules.append(
                            MaximumOrcsRule(self.max_orcs + 1)
                        )
                case "MinTrolls":
                    if self.is_min_trolls_possible():
                        potential_rules.append(
                            MinimumTrollsRule(self.min_trolls + 1)
                        )
                case "MaxTrolls":
                    if self.is_max_trolls_possible():
                        potential_rules.append(
                            MaximumTrollsRule(self.max_trolls + 1)
                        )
                case "OrcTrollRatio":
                    if self.is_orc_troll_ratio_possible():
                        potential_rules.append(self.get_orc_troll_ratio())
            possible_rules = [x for x in possible_rules if x != new_rule_type]
        return potential_rules
    
    def is_min_monsters_possible(self) -> bool:
        if self.min_total < self.max_total:
            return True
        return False
    
    def is_max_monsters_possible(self) -> bool:
        if self.max_total < MAXIMUM_MONSTERS_LIMIT:
                return True
        return False
    
    def is_min_orcs_possible(self) -> bool:
        if self.min_orcs < self.max_total:
            if self.is_max_orcs_set and self.min_orcs >= self.max_orcs:
                return False
            return True
        return False
    
    def is_max_orcs_possible(self) -> bool:
        if self.max_orcs < self.max_total:
            return True
        return False
            
    def is_min_trolls_possible(self) -> bool:
        if self.min_trolls < self.max_total:
            if self.is_max_trolls_set and self.min_trolls >= self.max_trolls:
                return False
            return True
        return False
    
    def is_max_trolls_possible(self) -> bool:
        if self.max_trolls < self.max_total:
            return True
        return False
    
    def is_orc_troll_ratio_possible(self) -> bool:
        # No point of ratio if only one is possible
        if self.max_total > 1:
            return True
        return False
                    
    def get_orc_troll_ratio(self) -> OrcTrollRatioRule:
        min = self.min_total
        if self.min_total <= 1:
            min = 2
        ratio_sum = random.choice([*range(min, self.max_total + 1)])
        print("ratio_sum", ratio_sum)
        ratio_orcs = random.choice([*range(1, ratio_sum)])
        ratio_trolls = ratio_sum - ratio_orcs
        return OrcTrollRatioRule(orc_ratio=ratio_orcs, troll_ratio=ratio_trolls)

if __name__ == "__main__":
    potential_rules = MonsterRuleManager(
        minimum_monsters=1,
        maximum_monsters=3
        ).get_new_potential_rules()
    
    for rule in potential_rules:
        print(rule)