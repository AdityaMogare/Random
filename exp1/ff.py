# Grammar productions
productions = [
    'S -> A',
    'S -> B',
    'A -> aB',
    'A -> aS',
    'B -> bA',
    'B -> bS',
    'B -> c'
]

# Function to find the first set of a nonterminal symbol
def find_first(symbol):
    # Base case: symbol is a terminal
    if symbol.islower():
        return set([symbol])
    # Recursive case: symbol is a nonterminal
    first_set = set()
    for production in productions:
        left, right = production.split(' -> ')
        if left == symbol:
            first_set |= find_first(right[0])
    return first_set

# Find the first set of each nonterminal symbol
first_sets = {}
for production in productions:
    left, right = production.split(' -> ')
    if left not in first_sets:
        first_sets[left] = find_first(left)

# Print the first sets
for nonterminal, first_set in first_sets.items():
    print(f'FIRST({nonterminal}) = {first_set}')



from collections import defaultdict

# A sample grammar in CNF
grammar = {
    'S': [('A', 'B'), ('C', 'D')],
    'A': [('B',), ('a',)],
    'B': [('C', 'D'), ('b',)],
    'C': [('A',), ('c',)],
    'D': [('d',)],
}

# Calculate the first sets of all non-terminals in the grammar
first = defaultdict(set)
for nonterm, prods in grammar.items():
    for prod in prods:
        if prod[0].islower():
            first[nonterm].add(prod[0])
        else:
            first[nonterm] |= first[prod[0]]

# Calculate the follow sets of all non-terminals in the grammar
follow = defaultdict(set)
follow['S'].add('$')
for nonterm, prods in grammar.items():
    for prod in prods:
        for i, symbol in enumerate(prod):
            if symbol.isupper():
                if i == len(prod) - 1:
                    follow[symbol] |= follow[nonterm]
                else:
                    next_symbols = {prod[j] for j in range(i + 1, len(prod))}
                    next_first = set.union(*[first[s] for s in next_symbols])
                    if '' in next_first:
                        follow[symbol] |= (next_first - {''}) | follow[nonterm]
                    else:
                        follow[symbol] |= next_first

# Print the follow sets
for nonterm, follow_set in follow.items():
    print(f"Follow({nonterm}): {', '.join(sorted(follow_set))}")
