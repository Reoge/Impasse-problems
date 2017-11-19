#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on 2017_11_19_1557
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
from random import sample, randint, choice
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
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
    text=u'\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0447\u0442\u043e \u043f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u043b',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=1.0, colorSpace='rgb', opacity=1,
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
        problem_control = event.BuilderKeyResponse()
        # keep track of which components have finished
        main_eventComponents = [impacts_distr, this_problem, impacts, problem_control]
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
            
            # *problem_control* updates
            if t >= 0.0 and problem_control.status == NOT_STARTED:
                # keep track of start time/frame for later
                problem_control.tStart = t
                problem_control.frameNStart = frameN  # exact frame index
                problem_control.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(problem_control.clock.reset)  # t=0 on next screen flip
            if problem_control.status == STARTED:
                theseKeys = event.getKeys(keyList=['e', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if problem_control.keys == []:  # then this was the first keypress
                        problem_control.keys = theseKeys[0]  # just the first key pressed
                        problem_control.rt = problem_control.clock.getTime()
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
        if 'e' == problem_control.keys:
            circles.finished = True
            ready_to_shine = 0
            impacts.opacity = 0
        else:
            ready_to_shine = 1
            time_to_stop = 10 + delay
        # check responses
        if problem_control.keys in ['', [], None]:  # No response was made
            problem_control.keys=None
        circles.addData('problem_control.keys',problem_control.keys)
        if problem_control.keys != None:  # we had a response
            circles.addData('problem_control.rt', problem_control.rt)
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
    if Finale.status == STARTED:  # only update if drawing
        Finale.setColor(choice(('red','yellow','green','blue')), colorSpace='rgb', log=False)
    
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
