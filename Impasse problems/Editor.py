import fileinput
from shutil import copyfile

copyfile('untitled_lastrun.py', 'Almost_Finale.py')

#переменные, чтобы проследить, что все изменения были сделаны
x = 0 
y = 0

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




delete = {"import numpy as np  # whole numpy lib is available, prepend 'np.'\n",
                "from numpy import (sin, cos, tan, log, log10, pi, average,\n",
                "                   sqrt, std, deg2rad, rad2deg, linspace, asarray)\n",
                "from numpy.random import random, randint, normal, shuffle\n"
               }

#дополнительные переменные, чтобы проследить, что всё хорошо
q_changes = len(changes)
q_deletes = len(delete)

with fileinput.FileInput('Almost_Finale.py', inplace = True) as f:
    for line in f:
        if  line in changes:
            line= line.replace(line, line + changes[line])
            x +=1
        elif line in delete:
            line = ''
            y += 1
        print(line, end = '')

print(f'x= {x} and y = {y}')
print(f'Внесены все измения: {x == q_changes}\n'
         f'Удалено всё лишнее:  {y == q_deletes}')

input('Close?: ')
