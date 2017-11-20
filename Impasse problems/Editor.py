import fileinput
from shutil import copyfile
from os import remove

copyfile('untitled_lastrun.py', 'Almost_Finale.py')

#переменные, чтобы проследить, что все изменения были сделаны
var_change = 0 
var_del_lines = 0
var_del_filses = 0

changes = {'                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)\n':
                                        ['from random import sample, randint, choice',
                                         ],

        'thisProblem = problems.trialList[0]  # so we can initialise stimuli with some values\n':
                                        ["prepand_type = choice((1,0))",
                                          "for num, cond in enumerate(problems.trialList):",
                                          "    cond['delay'] = delay_time[num]",
                                          "    cond['type'] = prepand_type#1 - hint, 0 - distraction"
                                         ],            
                   }

for key,value in changes.items(): #добавим окончание строки \n
	for num, element in enumerate(value):
		value[num] = element + '\n'
	changes[key] =  ''.join(value)




delete_lines = {"import numpy as np  # whole numpy lib is available, prepend 'np.'\n",
                "from numpy import (sin, cos, tan, log, log10, pi, average,\n",
                "                   sqrt, std, deg2rad, rad2deg, linspace, asarray)\n",
                "from numpy.random import random, randint, normal, shuffle\n"
               }

delete_files = ['Almost_Finale.pyc', 'untitled.pyc', 'untitled_lastrun.py']

#дополнительные переменные, чтобы проследить, что всё хорошо
q_changes = len(changes)
q_deletes = len(delete_lines)

with fileinput.FileInput('Almost_Finale.py', inplace = True) as f:
    for line in f:
        if  line in changes:
            line= line.replace(line, line + changes[line])
            var_change +=1
        elif line in delete_lines:
            line = ''
            var_del_lines += 1
        print(line, end = '')

for file_number in range(len(delete_files)):
        remove(delete_files[file_number])
        var_del_filses += 1
        
                        
                
                
print(f'x= {var_change} and y = {var_del_lines}')
print(f'Внесены все измения: {var_change == q_changes}\n'
         f'Удалено всё лишнее:  {var_del_lines == q_deletes}')
print(f'Удалено файлов {var_del_filses}, удалены все файлы: {var_del_filses == len(delete_files)}')



input('Close?: ')
