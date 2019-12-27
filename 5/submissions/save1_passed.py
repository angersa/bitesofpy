NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    dedups = [name.title() for name in names]
    return sorted(list(set(dedups)))


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names = [name.split(' ') for name in names]
    names.sort(key=lambda x: x[1], reverse=True)
    return [' '.join(name) for name in names]
  


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    names = [name.split(' ')[0] for name in names]
    names.sort(key=lambda x: len(x))
    return names[0]