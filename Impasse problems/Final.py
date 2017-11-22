#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on 2017_11_20_2132
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
from random import sample, randint, choice, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Experiments\\Impasse problems\\untitled.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1680, 1050), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
instruction_text = visual.ImageStim(
    win=win, name='instruction_text',
    image='Images\\Instruction.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
from random import sample, randint, choice

# Initialize components for Routine "counting"
countingClock = core.Clock()
counting_training_part_1 = visual.TextStim(win=win, name='counting_training_part_1',
    text=u'\u0418\u043d\u043e\u0433\u0434\u0430 \u043d\u0430 \u043c\u043e\u043d\u0438\u0442\u043e\u0440\u0435 \u0432\u044b \u0431\u0443\u0434\u0435\u0442\u0435 \u0432\u0438\u0434\u0435\u0442\u044c \u043d\u0430\u0434\u043f\u0438\u0441\u044c "\u0421\u0447\u0451\u0442 \u0442\u0440\u043e\u0439\u043a\u0430\u043c\u0438" \u0438 \u0446\u0438\u0444\u0440\u0443, \u0441 \u043a\u043e\u0442\u043e\u0440\u043e\u0439 \u0441\u043b\u0435\u0434\u0443\u0435\u0442 \u043d\u0430\u0447\u0430\u0442\u044c. \u0412 \u0442\u0430\u043a\u043e\u043c \u0441\u043b\u0443\u0447\u0430\u0435, \u0432\u0430\u043c \u043d\u0443\u0436\u043d\u043e \u0431\u0443\u0434\u0435\u0442 \u0432\u0441\u043b\u0443\u0445 \u043d\u0430\u0437\u044b\u0432\u0430\u0442\u044c \u043f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \u0446\u0438\u0444\u0440. \u041d\u0430\u043f\u0440\u0438\u043c\u0435\u0440, \u0441\u0447\u0451\u0442 \u0442\u0440\u043e\u0439\u043a\u0430\u043c\u0438 \u043e\u0442 1 \u0431\u0443\u0434\u0435\u0442 \u0432\u044b\u0433\u043b\u044f\u0434\u0435\u0442\u044c \u0442\u0430\u043a: 1, 4, 7, 10, 13, 16, 19...',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

counting_training_part_2 = visual.TextStim(win=win, name='counting_training_part_2',
    text='default text',
    font='Arial',
    pos=(0, -0.2), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "practice"
practiceClock = core.Clock()
neutral_images = [u'Images\\neutral_1.jpg', u'Images\\neutral_2.jpg']
shuffle(neutral_images)
practice_text = visual.TextStim(win=win, name='practice_text',
    text=u'\u041d\u0430\u0436\u043c\u0438\u0442\u0435 \u043f\u0440\u043e\u0431\u0435\u043b',
    font='Arial',
    pos=(0, 0.4), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
practice_neutral = visual.ImageStim(
    win=win, name='practice_neutral',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.4,0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "main_event"
main_eventClock = core.Clock()
delay_time = sample((0,10),2)

ready_to_shine = 0
time_to_stop = 0

impacts_distr = visual.TextStim(win=win, name='impacts_distr',
    text='default text',
    font='Arial',
    pos=(0, -0.5), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);
this_problem = visual.ImageStim(
    win=win, name='this_problem',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
impacts = visual.ImageStim(
    win=win, name='impacts',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color='red', colorSpace='rgb', opacity=0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "finish"
finishClock = core.Clock()
Finale = visual.TextStim(win=win, name='Finale',
    text=u'\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0437\u0430 \u0443\u0447\u0430\u0441\u0442\u0438\u0435',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruction_end = event.BuilderKeyResponse()

# keep track of which components have finished
instructionComponents = [instruction_text, instruction_end]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_text* updates
    if t >= 0.0 and instruction_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_text.tStart = t
        instruction_text.frameNStart = frameN  # exact frame index
        instruction_text.setAutoDraw(True)
    
    # *instruction_end* updates
    if t >= 0.0 and instruction_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_end.tStart = t
        instruction_end.frameNStart = frameN  # exact frame index
        instruction_end.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruction_end.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instruction_end.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instruction_end.keys = theseKeys[-1]  # just the last key pressed
            instruction_end.rt = instruction_end.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruction_end.keys in ['', [], None]:  # No response was made
    instruction_end.keys=None
thisExp.addData('instruction_end.keys',instruction_end.keys)
if instruction_end.keys != None:  # we had a response
    thisExp.addData('instruction_end.rt', instruction_end.rt)
thisExp.nextEntry()

# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "counting"-------
t = 0
countingClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
distraction = u'Попробуйте считать вслух начиная от %d' % randint(1,10)
counting_training_part_2.setText(distraction)
stop_counting = event.BuilderKeyResponse()
# keep track of which components have finished
countingComponents = [counting_training_part_1, counting_training_part_2, stop_counting]
for thisComponent in countingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "counting"-------
while continueRoutine:
    # get current time
    t = countingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *counting_training_part_1* updates
    if t >= 0.0 and counting_training_part_1.status == NOT_STARTED:
        # keep track of start time/frame for later
        counting_training_part_1.tStart = t
        counting_training_part_1.frameNStart = frameN  # exact frame index
        counting_training_part_1.setAutoDraw(True)
    
    
    # *counting_training_part_2* updates
    if t >= 0.0 and counting_training_part_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        counting_training_part_2.tStart = t
        counting_training_part_2.frameNStart = frameN  # exact frame index
        counting_training_part_2.setAutoDraw(True)
    
    # *stop_counting* updates
    if t >= 0.0 and stop_counting.status == NOT_STARTED:
        # keep track of start time/frame for later
        stop_counting.tStart = t
        stop_counting.frameNStart = frameN  # exact frame index
        stop_counting.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(stop_counting.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if stop_counting.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            stop_counting.keys = theseKeys[-1]  # just the last key pressed
            stop_counting.rt = stop_counting.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in countingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "counting"-------
for thisComponent in countingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# check responses
if stop_counting.keys in ['', [], None]:  # No response was made
    stop_counting.keys=None
thisExp.addData('stop_counting.keys',stop_counting.keys)
if stop_counting.keys != None:  # we had a response
    thisExp.addData('stop_counting.rt', stop_counting.rt)
thisExp.nextEntry()
# the Routine "counting" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice_loop = data.TrialHandler(nReps=3, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='practice_loop')
thisExp.addLoop(practice_loop)  # add the loop to the experiment
thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop.keys():
        exec(paramName + '= thisPractice_loop.' + paramName)

for thisPractice_loop in practice_loop:
    currentLoop = practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop.keys():
            exec(paramName + '= thisPractice_loop.' + paramName)
    
    # ------Prepare to start Routine "practice"-------
    t = 0
    practiceClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    neutral_choice = None
    
    if practice_loop.thisN >= 1:
        neutral_choice = neutral_images.pop()
    
    practice_keyb = event.BuilderKeyResponse()
    practice_neutral.setImage(neutral_choice)
    # keep track of which components have finished
    practiceComponents = [practice_text, practice_keyb, practice_neutral]
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *practice_text* updates
        if t >= 0.0 and practice_text.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_text.tStart = t
            practice_text.frameNStart = frameN  # exact frame index
            practice_text.setAutoDraw(True)
        
        # *practice_keyb* updates
        if t >= 0.0 and practice_keyb.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_keyb.tStart = t
            practice_keyb.frameNStart = frameN  # exact frame index
            practice_keyb.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(practice_keyb.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if practice_keyb.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                practice_keyb.keys = theseKeys[-1]  # just the last key pressed
                practice_keyb.rt = practice_keyb.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # *practice_neutral* updates
        if (practice_loop.thisN >= 1) and practice_neutral.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_neutral.tStart = t
            practice_neutral.frameNStart = frameN  # exact frame index
            practice_neutral.setAutoDraw(True)
        if practice_neutral.status == STARTED and t >= (practice_neutral.tStart + 10.0):
            practice_neutral.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice"-------
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if practice_keyb.keys in ['', [], None]:  # No response was made
        practice_keyb.keys=None
    practice_loop.addData('practice_keyb.keys',practice_keyb.keys)
    if practice_keyb.keys != None:  # we had a response
        practice_loop.addData('practice_keyb.rt', practice_keyb.rt)
    # the Routine "practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 3 repeats of 'practice_loop'


# set up handler to look after randomisation of conditions etc
problems = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions\\problems.csv'),
    seed=None, name='problems')
thisExp.addLoop(problems)  # add the loop to the experiment
thisProblem = problems.trialList[0]  # so we can initialise stimuli with some values
prepand_type = choice((1,0))
for num, cond in enumerate(problems.trialList):
    cond['delay'] = delay_time[num]
    cond['type'] = prepand_type#1 - hint, 0 - distraction
# abbreviate parameter names if possible (e.g. rgb = thisProblem.rgb)
if thisProblem != None:
    for paramName in thisProblem.keys():
        exec(paramName + '= thisProblem.' + paramName)

for thisProblem in problems:
    currentLoop = problems
    # abbreviate parameter names if possible (e.g. rgb = thisProblem.rgb)
    if thisProblem != None:
        for paramName in thisProblem.keys():
            exec(paramName + '= thisProblem.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    circles = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('conditions\\number_of_circles.csv'),
        seed=None, name='circles')
    thisExp.addLoop(circles)  # add the loop to the experiment
    thisCircle = circles.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisCircle.rgb)
    if thisCircle != None:
        for paramName in thisCircle.keys():
            exec(paramName + '= thisCircle.' + paramName)
    
    for thisCircle in circles:
        currentLoop = circles
        # abbreviate parameter names if possible (e.g. rgb = thisCircle.rgb)
        if thisCircle != None:
            for paramName in thisCircle.keys():
                exec(paramName + '= thisCircle.' + paramName)
        
        # ------Prepare to start Routine "main_event"-------
        t = 0
        main_eventClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        blink = 0
        blink_time = delay #также и для дистракции оно же
        distraction = u'Начинайте считать от %d' % randint(1,10)
        impacts_distr.setText(distraction)
        this_problem.setImage(problem)
        impacts.setImage(impact)
        problem_control_impass = event.BuilderKeyResponse()
        problem_control_exit = event.BuilderKeyResponse()
        # keep track of which components have finished
        main_eventComponents = [impacts_distr, this_problem, impacts, problem_control_impass, problem_control_exit]
        for thisComponent in main_eventComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "main_event"-------
        while continueRoutine:
            # get current time
            t = main_eventClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if all((blink_time <= t <= time_to_stop,ready_to_shine == 1,type==1)):
                impacts.opacity = (1,0)[blink%2]
                blink += 1
                blink_time += 1
            
            if t > time_to_stop:
                impacts.opacity = 0
                ready_to_shine = 0
            
            # *impacts_distr* updates
            if (all((blink_time <= t <= time_to_stop,ready_to_shine == 1,type == 0))) and impacts_distr.status == NOT_STARTED:
                # keep track of start time/frame for later
                impacts_distr.tStart = t
                impacts_distr.frameNStart = frameN  # exact frame index
                impacts_distr.setAutoDraw(True)
            if impacts_distr.status == STARTED and bool(ready_to_shine ==0):
                impacts_distr.setAutoDraw(False)
            
            # *this_problem* updates
            if t >= 0.0 and this_problem.status == NOT_STARTED:
                # keep track of start time/frame for later
                this_problem.tStart = t
                this_problem.frameNStart = frameN  # exact frame index
                this_problem.setAutoDraw(True)
            
            # *impacts* updates
            if t >= 0.0 and impacts.status == NOT_STARTED:
                # keep track of start time/frame for later
                impacts.tStart = t
                impacts.frameNStart = frameN  # exact frame index
                impacts.setAutoDraw(True)
            
            # *problem_control_impass* updates
            if t >= time_to_stop and problem_control_impass.status == NOT_STARTED:
                # keep track of start time/frame for later
                problem_control_impass.tStart = t
                problem_control_impass.frameNStart = frameN  # exact frame index
                problem_control_impass.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(problem_control_impass.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if problem_control_impass.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if problem_control_impass.keys == []:  # then this was the first keypress
                        problem_control_impass.keys = theseKeys[0]  # just the first key pressed
                        problem_control_impass.rt = problem_control_impass.clock.getTime()
                        # a response ends the routine
                        continueRoutine = False
            
            # *problem_control_exit* updates
            if t >= 2.0 and problem_control_exit.status == NOT_STARTED:
                # keep track of start time/frame for later
                problem_control_exit.tStart = t
                problem_control_exit.frameNStart = frameN  # exact frame index
                problem_control_exit.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(problem_control_exit.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            if problem_control_exit.status == STARTED:
                theseKeys = event.getKeys(keyList=['e'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    problem_control_exit.keys = theseKeys[-1]  # just the last key pressed
                    problem_control_exit.rt = problem_control_exit.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in main_eventComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "main_event"-------
        for thisComponent in main_eventComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if 'e' == problem_control_exit.keys:
            circles.finished = True
            ready_to_shine = 0
            impacts.opacity = 0
            time_to_stop = 0
        
        
        if 'space' == problem_control_impass.keys:
            ready_to_shine = 1
            time_to_stop = 10 + delay
        
        if 'e' == problem_control_exit.keys and 'space' == problem_control_impass.keys:
            print u'We have a problem Huston'
        # check responses
        if problem_control_impass.keys in ['', [], None]:  # No response was made
            problem_control_impass.keys=None
        circles.addData('problem_control_impass.keys',problem_control_impass.keys)
        if problem_control_impass.keys != None:  # we had a response
            circles.addData('problem_control_impass.rt', problem_control_impass.rt)
        # check responses
        if problem_control_exit.keys in ['', [], None]:  # No response was made
            problem_control_exit.keys=None
        circles.addData('problem_control_exit.keys',problem_control_exit.keys)
        if problem_control_exit.keys != None:  # we had a response
            circles.addData('problem_control_exit.rt', problem_control_exit.rt)
        # the Routine "main_event" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'circles'
    
# completed 1 repeats of 'problems'


# ------Prepare to start Routine "finish"-------
t = 0
finishClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = [Finale]
for thisComponent in finishComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "finish"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finishClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Finale* updates
    if t >= 0.0 and Finale.status == NOT_STARTED:
        # keep track of start time/frame for later
        Finale.tStart = t
        Finale.frameNStart = frameN  # exact frame index
        Finale.setAutoDraw(True)
    frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if Finale.status == STARTED and t >= frameRemains:
        Finale.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finishComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "finish"-------
for thisComponent in finishComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)




# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()