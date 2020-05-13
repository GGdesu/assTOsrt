from subtools import *
from time import sleep
from os import path


print(f'Coloque as legendas a serem convertida na pasta:{pathsub(True)}')
sleep(3)
subtittles_files = pathsub()

counter_sub = 1
counter_line = 1
for subtitles in subtittles_files:

    sub = r'\\' + f'{subtitles[:-4]}' + f'_copy_({counter_sub}).srt'
    origin = open(subtitles, 'r', encoding='utf-8')
    deposit = open(path.abspath('legenda') + sub, 'w', encoding='utf-8')
    ler = origin.readlines()

    for linha in ler:
        if 'Dialogue' in linha:
            inicio = linha[12].zfill(2) + linha[13:16] + linha[16:20] + linha[20:22].ljust(3, '0')
            fim = ' --> ' + linha[23].zfill(2) + linha[24:27] + linha[27:31] + linha[31:33].ljust(3, '0')
            tempo = inicio + fim

            speech = linha[linha.rfind(',,') + 2:]
            speech = stylesub(speech)
            speech = tagremove(speech)

            deposit.write(str(counter_line) + '\n')
            deposit.write(tempo + '\n')
            deposit.write(speech + '\n')
            counter_line += 1
    deposit.close()
    origin.close()
    counter_sub += 1
    counter_line = 1
sleep(5)
print('\n\nProcesso concluido! O programa irá ser encerrado...')
sleep(2)

