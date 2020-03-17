INDENTS = 4


def print_hanging_indents(poem):
    poem = poem.split("\n")
    formatted_poem = ''
    new_line = True
    for line in poem:
        if line == '':
            new_line = True
            continue
        if new_line:
            formatted_poem += line.strip() + '\n'
            new_line = False
        else:
            formatted_poem += ' ' * INDENTS + line.strip() + '\n'
    print(formatted_poem.strip())
