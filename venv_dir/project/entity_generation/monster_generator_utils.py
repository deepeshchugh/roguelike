
from typing import List
from .rule_teacher import RuleTeacher


# Returns first duplicate
def get_duplicate_rule(ruleset_queue: List[RuleTeacher], rule_to_check: RuleTeacher):
    duplicate_rule_list = [rule for rule in ruleset_queue if type(rule) == type(rule_to_check)]
    
    if len(duplicate_rule_list) > 0:
        return duplicate_rule_list[0]
    
    return None