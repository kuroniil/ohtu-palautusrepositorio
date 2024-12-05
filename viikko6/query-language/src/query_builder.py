from matchers import PlaysIn, All, HasAtLeast, HasFewerThan, And, Or

class QueryBuilder:
    def __init__(self, query = And()):
        self.query_olio = query

    def plays_in(self, team):
        return QueryBuilder(And(self.query_olio, PlaysIn(team)))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self.query_olio, HasAtLeast(value, attr)))

    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self.query_olio, HasFewerThan(value, attr)))

    def one_of(self, m1, m2):
        return QueryBuilder(Or(m1, m2))

    def build(self):
        return self.query_olio  