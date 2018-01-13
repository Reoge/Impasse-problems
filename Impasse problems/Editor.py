import fileinput
from shutil import copyfile
from os import remove
from time import sleep


try:
        copyfile('untitled_lastrun.py', 'Final.py')
except FileNotFoundError:
        print("Файл с изменениями внесеными через билдер не найден")
        input = 'Закроется при нажатии Enter'
        exit()

#переменные, чтобы проследить, что все изменения были сделаны
var_change = 0 
var_del_lines = 0
var_del_filses = 0

changes = {'                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)\n':
                                        [
                                           'from random import sample, randint, choice, shuffle',
                                         ],
                    'os.chdir(_thisDir)\n':
                                         [
                                          "sys.path.append(_thisDir + '\\tweaks')",
                                          "sys.path.append(os.path.join(_thisDir, os.listdir(_thisDir)[-2]))",
                                          "import statistic",
                                          ],

                    'thisProblem = problems.trialList[0]  # so we can initialise stimuli with some values\n':
                                         [
                                          "statistic.look_up(os.path.join(_thisDir, 'Overall_statistics\\groups.txt'))",
                                          "prepand_type = {'Hint': 1, 'Distractor': 0, 'Control': 2}",
                                          "cond_to_delete = list(statistic.changes_to_do.values()).count('10')",
                                          "cond_was_del = 0",
                                          "for condition, value in statistic.changes_to_do.items():",
                                          "    if cond_to_delete == 2 and value == '10':",
                                          "          del prepand_type[condition]",
                                          "          cond_was_del += 1",
                                          "          if cond_was_del == 2:",
                                          "               prepand_type = prepand_type.popitem()[1]",
                                          "               break",
                                          "    elif value == '20':",
                                          "        del prepand_type[condition]",
                                          "else:",
                                          "    prepand_type = choice( prepand_type.values() )",
                                           "for num, cond in enumerate(problems.trialList):",
                                           "    cond['delay'] = delay_time[num]",
                                           "    cond['type'] = prepand_type #1 - hint, 0 - distraction, 2 - control",
                                          ],
                   "# these shouldn't be strictly necessary (should auto-save)\n":
                                          [
                                           "Decipher = {1: 'Hint', 0: 'Distractor', 2: 'Control'}",
                                           "prepand_type = Decipher[prepand_type]",
                                           "statistic.save_down(os.path.join(_thisDir, 'Overall_statistics\\groups.txt'), prepand_type)",
                                          ]
                   }

for key,value in changes.items(): #добавим окончание строки \n
	for num, element in enumerate(value):
		value[num] = element + '\n'
	changes[key] =  ''.join(value)




delete_lines = [
                "import numpy as np  # whole numpy lib is available, prepend 'np.'",
                "from numpy import (sin, cos, tan, log, log10, pi, average,",
                "                   sqrt, std, deg2rad, rad2deg, linspace, asarray)",
                "from numpy.random import random, randint, normal, shuffle",
                         ]
delete_lines = [line+'\n' for line in delete_lines]

delete_files = ['untitled_lastrun.py', 'untitled.pyc',  'Final.pyc']

#дополнительные переменные, чтобы проследить, что всё хорошо
q_changes = len(changes)
q_deletes = len(delete_lines)
q_delets_f = len(delete_files)

with fileinput.FileInput('Final.py', inplace = True) as f:
    for line in f:
        if  line in changes:
            line= line.replace(line, line + changes[line])
            var_change +=1
        elif line in delete_lines:
            line = ''
            var_del_lines += 1
        print(line, end = '')

while q_delets_f !=0:
        try:
                file_to_delete = delete_files.pop()
                remove(file_to_delete)
                var_del_filses += 1
        except FileNotFoundError:
                continue
        
                        
                
                
print(f'x= {var_change} and y = {var_del_lines}')
print(f'Внесены все измения: {var_change == q_changes}\n'
         f'Удалено всё лишнее:  {var_del_lines == q_deletes}')
print(f'Удалено файлов {var_del_filses}, удалены все файлы, которые планировались: {var_del_filses == len(delete_files)}')



input = 'Закроется при нажатии Enter'
exit()
