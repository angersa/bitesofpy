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
    print(formatted_poem)


def solution(poem):
    """You can use textwrap's fill but this worked better for us"""
    for part in poem.split("\n\n"):
        lines = [line.strip() for line in part.splitlines()
                 if line.strip()]       # Necessary to unindent first line. I would never have think of this!
        print(lines[0])
        for line in lines[1:]:
            print(' ' * INDENTS + line)


rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


print_hanging_indents(rosetti_unformatted)
solution(rosetti_unformatted)