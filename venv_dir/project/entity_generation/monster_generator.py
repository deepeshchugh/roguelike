from .monster_generator_utils import get_duplicate_rule
from .rule_teacher import RuleTeacher
from .maximum_monsters_rule import MaximumMonstersRule
from .minimum_monsters_rule import MinimumMonstersRule
from .ruleset_teacher import RulesetTeacher

from l_star_inexperienced.grinchtein_et_al.glp_algorithm import GlpAlgorithm

import random


MONSTER_ALPHABET = ['o', 'T']

class MonsterGenerator():

    def __init__(self):
        self.ruleset_teacher = RulesetTeacher()
        self.initialize_default_rules()
        self.current_dfa = self.get_new_dfa() # Will always succeed

    def initialize_default_rules(self):
        new_rule_queue = []
        new_rule_queue.append(MinimumMonstersRule(0))
        new_rule_queue.append(MaximumMonstersRule(1))
        self.ruleset_teacher.set_rule_queue(new_rule_queue=new_rule_queue)

    def get_new_dfa(self):
        glp_runner = GlpAlgorithm(alphabet=MONSTER_ALPHABET, teacher=self.ruleset_teacher)
        return glp_runner.run()

    def add_rule(self, new_rule : RuleTeacher) -> bool:
        old_rule_queue = self.ruleset_teacher.get_rule_queue()
        
        duplicate_rule = get_duplicate_rule(old_rule_queue, new_rule)
        
        new_rule_queue = [rule for rule in old_rule_queue if rule != duplicate_rule]
        new_rule_queue.append(new_rule)
        self.ruleset_teacher.set_rule_queue(new_rule_queue=new_rule_queue)

        removed_rules = []
        new_dfa = self.get_new_dfa()

        while new_rule_queue[0] != new_rule:
            if new_dfa is None:
                popped_rule = new_rule_queue.pop(0)
                if popped_rule.is_mandatory:
                    new_rule_queue.append(popped_rule)
                else:
                    removed_rules.append(popped_rule)
                    self.ruleset_teacher.set_rule_queue(new_rule_queue=new_rule_queue)
                    new_dfa = self.get_new_dfa()
            else:
                break
        
        if new_dfa is None or len(new_dfa.final_states) == 0:
            print("Oh no!")
            self.ruleset_teacher.set_rule_queue(old_rule_queue)
            # TODO add exception to replace rule in selection box
        else:
            print("success!")
            self.current_dfa = new_dfa

            if duplicate_rule is not None:
                removed_rules.append(duplicate_rule)
            # TODO raise messages of deleted rules
    
    def get_monster_string(self) -> str:
        search_queue = []
        first_state = self.current_dfa.first_state
        choose_last_string_probability = 15
        valid_string_found = False
        valid_string = None

        search_queue.append([first_state, 0, ""])
        current_depth = 0
        
        if self.current_dfa.is_state_final(first_state):
            valid_string = ""
            valid_string_found = True
        while True:
            popped_entry = search_queue.pop(0)
            current_depth = popped_entry[1]

            if valid_string_found:
                print(valid_string)
                choose_last_string = random.choices([True, False], weights=[choose_last_string_probability, 100 - choose_last_string_probability])
                if choose_last_string[0]:
                    return valid_string
                elif len(search_queue) > 0 and search_queue[0][1] > current_depth:
                    choose_last_string_probability += 10
            
            orc_entry = [
                self.current_dfa.delta[popped_entry[0]]['o'],
                popped_entry[1] + 1,
                popped_entry[2] + 'o'
            ]
            if self.current_dfa.is_state_final(orc_entry[0]):
                valid_string_found = True
                valid_string = orc_entry[2]
            troll_entry = [
                self.current_dfa.delta[popped_entry[0]]['T'],
                popped_entry[1] + 1,
                popped_entry[2] + 'T'
            ]
            if self.current_dfa.is_state_final(troll_entry[0]):
                valid_string_found = True
                valid_string = troll_entry[2]
            search_queue.append(orc_entry)
            search_queue.append(troll_entry)
            

if __name__ == "__main__":
    monster_generator = MonsterGenerator()
    dfa = monster_generator.current_dfa
    if dfa is not None:
        dfa.print_parameters()
    monster_generator.add_rule(MaximumMonstersRule(2))
    dfa = monster_generator.current_dfa
    if dfa is not None:
        dfa.print_parameters()
    monster_generator.add_rule(MinimumMonstersRule(3))
    dfa = monster_generator.current_dfa
    if dfa is not None:
        dfa.print_parameters()
    monster_generator.add_rule(MinimumMonstersRule(1))
    dfa = monster_generator.current_dfa
    if dfa is not None:
        dfa.print_parameters()

    print(monster_generator.get_monster_string())
        


