#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on 2017_11_06_1506
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
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
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


# Initialize components for Routine "counting"
countingClock = core.Clock()

# Initialize components for Routine "main_event"
main_eventClock = core.Clock()
from time import sleep

ready_to_shine = 0
time_to_stop = 0

this_problem = visual.ImageStim(
    win=win, name='this_problem',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
impacts = visual.ImageStim(
    win=win, name='impacts',
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=u'red', colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)

# Initialize components for Routine "finish"
finishClock = core.Clock()

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
# keep track of which components have finished
countingComponents = []
for thisComponent in countingComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "counting"-------
while continueRoutine:
    # get current time
    t = countingClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "counting" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
problems = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'conditions\\problems.csv'),
    seed=None, name='problems')
thisExp.addLoop(problems)  # add the loop to the experiment
thisProblem = problems.trialList[0]  # so we can initialise stimuli with some values
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
        trialList=data.importConditions(u'conditions\\number_of_circles.csv'),
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
        n = 0
        
        this_problem.setImage(problem)
        impacts.setOpacity(ready_to_shine)
        impacts.setImage(impact)
        problem_control = event.BuilderKeyResponse()
        # keep track of which components have finished
        main_eventComponents = [this_problem, impacts, problem_control]
        for thisComponent in main_eventComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "main_event"-------
        while continueRoutine:
            # get current time
            t = main_eventClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if t <= time_to_stop and ready_to_shine == 1:
                impacts.opacity = (1,0)[n%2]
                n +=1
                sleep(0.5)
            else:
                impacts.opacity = 0
            
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
            if t >= 1.0 and problem_control.status == NOT_STARTED:
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
        else:
            ready_to_shine = 1
            time_to_stop = 10
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
# update component parameters for each repeat
# keep track of which components have finished
finishComponents = []
for thisComponent in finishComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "finish"-------
while continueRoutine:
    # get current time
    t = finishClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
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
# the Routine "finish" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()


# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
