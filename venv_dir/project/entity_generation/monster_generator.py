from .monster_generator_utils import get_duplicate_rule
from .rule_teacher import RuleTeacher
from .maximum_monsters_rule import MaximumMonstersRule
from .minimum_monsters_rule import MinimumMonstersRule
from .ruleset_teacher import RulesetTeacher

from l_star_inexperienced.grinchtein_et_al.glp_algorithm import GlpAlgorithm

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
        


