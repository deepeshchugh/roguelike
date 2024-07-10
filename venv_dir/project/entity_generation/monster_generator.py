from .maximum_monsters_rule import MaximumMonstersRule
from .minimum_monsters_rule import MinimumMonstersRule
from .ruleset_teacher import RulesetTeacher

from l_star_inexperienced.grinchtein_et_al.glp_algorithm import GlpAlgorithm

MONSTER_ALPHABET = ['o', 'T']

class MonsterGenerator():

    def __init__(self):
        self.ruleset_teacher = RulesetTeacher()
        self.initialize_default_rules()

    def initialize_default_rules(self):
        new_rule_queue = []
        new_rule_queue.append(MinimumMonstersRule(0))
        new_rule_queue.append(MaximumMonstersRule(1))
        self.ruleset_teacher.set_rule_queue(new_rule_queue=new_rule_queue)

    def get_dfa(self):
        glp_runner = GlpAlgorithm(alphabet=MONSTER_ALPHABET, teacher=self.ruleset_teacher)
        return glp_runner.run()

if __name__ == "__main__":
    monster_generator = MonsterGenerator()
    dfa = monster_generator.get_dfa()
    if dfa is not None:
        dfa.print_parameters()
    


