from l_star_inexperienced.teachers import Teacher

'''
Teacher to be used in RulesetTeacher list,
Inherits default membership and equivalence query behaviour.
'''
class RuleTeacher(Teacher):

    '''
    is_mandatory tells us if the teacher 
    can possibly be removed from the list
    or is always present.
    '''
    def __init__(self, is_mandatory):
        self.is_mandatory = is_mandatory