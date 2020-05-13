def stylesub(text, font=False):
    """
    estilos
        bold: negrito
        italic: italico
        underline: sublinhado
        font color: cor da fonte

    :param text: texto que vai ser analisado
    :param font: quando TRUE é adicionado uma cor amarela ao texto
    :return: retorna o texto para o programa principal
    """

    style = {'bold': ('<b>', '</b>'),
             'italic': ('<i>', '</i>'),
             'underline': ('<u>', '</u>'),
             'break line': '\n',
             'font color': ('<font color="yellow">', '</font>')}
    line = text

    if r'{\b1}' in line:
        line = line.replace(r'{\b1}', style['bold'][0])
        if r'{\b0}' in line:
            line = line.replace(r'{\b0}', style['bold'][1])

    if r'{\i1}' in line:
        line = line.replace(r'{\i1}', style['italic'][0])
        if r'{\i0}' in line:
            line = line.replace(r'{\i0}', style['italic'][1])

    if r'{\u1}' in line:
        line = line.replace(r'{\u1}', style['underline'][0])
        if r'{\u0}' in line:
            line = line.replace(r'{\u0}', style['underline'][1])

    if r'\N' in line:
        line = line.replace(r'\N', style['break line'])

    if font:
        line = [line]
        line.insert(0, style['font color'][0])
        line.append(style['font color'][1])
    line = ''.join(line)
    return line


def tagremove(text):

    newtxt = text
    while True:
        indices = list()
        if newtxt.find('{') < newtxt.find('}'):
            indices.append(newtxt.find('{'))
            indices.append(newtxt.find('}'))
        else:
            indices.append(newtxt.rfind('{'))
            indices.append(newtxt.rfind('}'))

        if indices == [-1, -1] or indices == [indices[0], -1] or indices == [-1, indices[1]]:
            break
        elif '}{' in newtxt:
            newtxt = newtxt.replace('}{', '')
        else:
            newtxt = newtxt.replace(newtxt[indices[0]:indices[1]+1], '')

        indices.clear()
    return newtxt


def pathsub(show=False):
    from glob import glob
    from sys import exit, path

    sublist = [sub for sub in glob("*.ass")]

    if show:
        return path[0]

    if not sublist:
        print(f'\033[31mnão há nenhuma legenda no diretorio\033[m \033[30m{path[0]}\033[m')
        return exit(-1)
    else:
        print('-' * 40)
        print(f'{"Lista de legendas a serem convertidas":^40}'.upper())
        print('-' * 40)
        for i, name in enumerate(sublist):
            print(i, name)
        return sublist


