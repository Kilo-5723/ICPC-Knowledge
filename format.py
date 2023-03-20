background = {'D': 'Aqua',
              'C': 'Lime',
              'B': 'SkyBlue',
              'A': 'Orange',
              'S': 'Red',
              'T': 'Black',
              'Y': 'HotPink',
              'N': 'Silver'}

text = {'D': 'black',
        'C': 'black',
        'B': 'black',
        'A': 'black',
        'S': 'black',
        'T': 'white',
        'Y': 'black',
        'N': 'black'}


def modify(s):
    s = s[:-1]
    if s[-3] == ',':
        id = s[-1]
        l, r = s.split('-', 1)
        r.strip()
        s = l + '- <span style = "background-color:' + background[id] + ';color:' + \
            text[id]+'">&nbsp;' + r.strip() + '&nbsp;</span>'
    return s


f = open("knowledge-tree.md", "r")
lines = f.readlines()
for line in lines:
    if len(line) > 3:
        print(modify(line))
    else:
        print()
