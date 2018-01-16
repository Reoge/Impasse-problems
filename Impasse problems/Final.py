#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.4),
    on 2018_01_16_1050
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
sys.path.append(os.path.join(_thisDir, 'tweaks'))
sys.path.append(os.path.join(_thisDir, os.listdir(_thisDir)[-2]))
import statistic

# Store info about the experiment session
expName = 'untitled'  # from the Builder filename that created this script
expInfo = {u'participant': u'', u'experimentator': u'Makarov'}
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

# Initialize components for Routine "instruction_overall"
instruction_overallClock = core.Clock()
instruction_text = visual.ImageStim(
    win=win, name='instruction_text',
    image='Images\\Instruction.png', mask=None,
    ori=0, pos=(0, 0), size=(1.6,1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "counting"
countingClock = core.Clock()
counting_training_part_1 = visual.ImageStim(
    win=win, name='counting_training_part_1',
    image='Images\\counting_training_part_1.png', mask=None,
    ori=0, pos=(0, 0.3), size=None,
    color=[1.000,1.000,1.000], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

counting_training_part_2 = visual.TextStim(win=win, name='counting_training_part_2',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.1, wrapWidth=1.5, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);

# Initialize components for Routine "instruction_problem"
instruction_problemClock = core.Clock()
problem_instruction_text = visual.ImageStim(
    win=win, name='problem_instruction_text',
    image='Images\\problem_instruction_text.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "practice"
practiceClock = core.Clock()
neutral_images = [u'Images\\neutral_1.jpg', u'Images\\neutral_2.jpg']
shuffle(neutral_images)
practice_problem = visual.ImageStim(
    win=win, name='practice_problem',
    image='Images\\Practice_problem.png', mask=None,
    ori=0, pos=(0, 0.3), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
practice_neutral = visual.ImageStim(
    win=win, name='practice_neutral',
    image='sin', mask=None,
    ori=0, pos=(0, -0.4), size=(0.4,0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

# Initialize components for Routine "instruction_problem_remind"
instruction_problem_remindClock = core.Clock()
instruction_problem_reminder_text = visual.ImageStim(
    win=win, name='instruction_problem_reminder_text',
    image='Images\\instruction_problem_reminder_text.png', mask=None,
    ori=0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "main_event"
main_eventClock = core.Clock()
main_eventTimer = core.CountdownTimer(start=300)
delay_time = sample((0,15),2)

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
impacts_control_group = visual.ImageStim(
    win=win, name='impacts_control_group',
    image='Images\\Control_group_neutral.jpg', mask=None,
    ori=0, pos=(0, -0.5), size=(0.4,0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-6.0)
game_over = visual.TextStim(win=win, name='game_over',
    text=u'\u0412\u0440\u0435\u043c\u044f \u0432\u044b\u0448\u043b\u043e',
    font='Arial',
    pos=(0, 0.5), height=0.25, wrapWidth=None, ori=0, 
    color='red', colorSpace='rgb', opacity=1,
    depth=-7.0);

# Initialize components for Routine "finish"
finishClock = core.Clock()
Finale = visual.TextStim(win=win, name='Finale',
    text=u'\u0421\u043f\u0430\u0441\u0438\u0431\u043e \u0437\u0430 \u0443\u0447\u0430\u0441\u0442\u0438\u0435',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction_overall"-------
t = 0
instruction_overallClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruction_end = event.BuilderKeyResponse()
# keep track of which components have finished
instruction_overallComponents = [instruction_text, instruction_end]
for thisComponent in instruction_overallComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction_overall"-------
while continueRoutine:
    # get current time
    t = instruction_overallClock.getTime()
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
    for thisComponent in instruction_overallComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_overall"-------
for thisComponent in instruction_overallComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruction_end.keys in ['', [], None]:  # No response was made
    instruction_end.keys=None
thisExp.addData('instruction_end.keys',instruction_end.keys)
if instruction_end.keys != None:  # we had a response
    thisExp.addData('instruction_end.rt', instruction_end.rt)
thisExp.nextEntry()
# the Routine "instruction_overall" was not non-slip safe, so reset the non-slip timer
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

# ------Prepare to start Routine "instruction_problem"-------
t = 0
instruction_problemClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruction_problem_keyb = event.BuilderKeyResponse()
# keep track of which components have finished
instruction_problemComponents = [problem_instruction_text, instruction_problem_keyb]
for thisComponent in instruction_problemComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction_problem"-------
while continueRoutine:
    # get current time
    t = instruction_problemClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *problem_instruction_text* updates
    if t >= 0.0 and problem_instruction_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        problem_instruction_text.tStart = t
        problem_instruction_text.frameNStart = frameN  # exact frame index
        problem_instruction_text.setAutoDraw(True)
    
    # *instruction_problem_keyb* updates
    if t >= 0.0 and instruction_problem_keyb.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_problem_keyb.tStart = t
        instruction_problem_keyb.frameNStart = frameN  # exact frame index
        instruction_problem_keyb.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruction_problem_keyb.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instruction_problem_keyb.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instruction_problem_keyb.keys = theseKeys[-1]  # just the last key pressed
            instruction_problem_keyb.rt = instruction_problem_keyb.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_problemComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_problem"-------
for thisComponent in instruction_problemComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruction_problem_keyb.keys in ['', [], None]:  # No response was made
    instruction_problem_keyb.keys=None
thisExp.addData('instruction_problem_keyb.keys',instruction_problem_keyb.keys)
if instruction_problem_keyb.keys != None:  # we had a response
    thisExp.addData('instruction_problem_keyb.rt', instruction_problem_keyb.rt)
thisExp.nextEntry()
# the Routine "instruction_problem" was not non-slip safe, so reset the non-slip timer
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
    practiceComponents = [practice_problem, practice_keyb, practice_neutral]
    for thisComponent in practiceComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "practice"-------
    while continueRoutine:
        # get current time
        t = practiceClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *practice_problem* updates
        if t >= 0.0 and practice_problem.status == NOT_STARTED:
            # keep track of start time/frame for later
            practice_problem.tStart = t
            practice_problem.frameNStart = frameN  # exact frame index
            practice_problem.setAutoDraw(True)
        
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


# ------Prepare to start Routine "instruction_problem_remind"-------
t = 0
instruction_problem_remindClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
instruction_problem_reminder_keyb = event.BuilderKeyResponse()
# keep track of which components have finished
instruction_problem_remindComponents = [instruction_problem_reminder_text, instruction_problem_reminder_keyb]
for thisComponent in instruction_problem_remindComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction_problem_remind"-------
while continueRoutine:
    # get current time
    t = instruction_problem_remindClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruction_problem_reminder_text* updates
    if t >= 0.0 and instruction_problem_reminder_text.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_problem_reminder_text.tStart = t
        instruction_problem_reminder_text.frameNStart = frameN  # exact frame index
        instruction_problem_reminder_text.setAutoDraw(True)
    
    # *instruction_problem_reminder_keyb* updates
    if t >= 0.0 and instruction_problem_reminder_keyb.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction_problem_reminder_keyb.tStart = t
        instruction_problem_reminder_keyb.frameNStart = frameN  # exact frame index
        instruction_problem_reminder_keyb.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(instruction_problem_reminder_keyb.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if instruction_problem_reminder_keyb.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            instruction_problem_reminder_keyb.keys = theseKeys[-1]  # just the last key pressed
            instruction_problem_reminder_keyb.rt = instruction_problem_reminder_keyb.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction_problem_remindComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction_problem_remind"-------
for thisComponent in instruction_problem_remindComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if instruction_problem_reminder_keyb.keys in ['', [], None]:  # No response was made
    instruction_problem_reminder_keyb.keys=None
thisExp.addData('instruction_problem_reminder_keyb.keys',instruction_problem_reminder_keyb.keys)
if instruction_problem_reminder_keyb.keys != None:  # we had a response
    thisExp.addData('instruction_problem_reminder_keyb.rt', instruction_problem_reminder_keyb.rt)
thisExp.nextEntry()
# the Routine "instruction_problem_remind" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
problems = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions\\problems.csv'),
    seed=None, name='problems')
thisExp.addLoop(problems)  # add the loop to the experiment
thisProblem = problems.trialList[0]  # so we can initialise stimuli with some values
statistic.look_up(os.path.join(_thisDir, 'Overall_statistics\groups.txt'))
prepand_type = {'Hint': 1, 'Distractor': 0, 'Control': 2}
cond_to_delete = list(statistic.changes_to_do.values()).count('10')
if cond_to_delete == 3:
     print '='*27, '\nAll subjects were gathered!\n', '='*27
     core.quit()
cond_was_del = 0
for condition, value in statistic.changes_to_do.items():
    if cond_to_delete == 2 and value == '10':
          del prepand_type[condition]
          cond_was_del += 1
          if cond_was_del == 2:
               prepand_type = prepand_type.popitem()[1]
               break
    elif value == '10':
        del prepand_type[condition]
else:
    prepand_type = choice( prepand_type.values() )
for num, cond in enumerate(problems.trialList):
    cond['delay'] = delay_time[num]
    cond['type'] = prepand_type #1 - hint, 0 - distraction, 2 - control
if prepand_type != 1:
    cond_variants = ('distraction', None, 'control')
    for cond_list in problems.trialList:
        cond_list['impact'] = cond_variants[prepand_type]
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
        if lapse == 1:            main_eventTimer.reset()
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        blink = 0
        blink_time = delay #также и для дистракции оно же
        distraction = u'Начинайте считать от %d' % randint(1,10)
        impacts_distr.setText(distraction)
        this_problem.setImage(problem)
        impacts.setImage(None)
        if prepand_type == 1:
            impacts.setImage(impact)
        problem_control_impass = event.BuilderKeyResponse()
        problem_control_exit = event.BuilderKeyResponse()
        # keep track of which components have finished
        main_eventComponents = [impacts_distr, this_problem, impacts, problem_control_impass, problem_control_exit, impacts_control_group, game_over]
        for thisComponent in main_eventComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "main_event"-------
        while continueRoutine:
            # get current time
            t = main_eventClock.getTime()
            t2 = main_eventTimer.getTime()
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
            if (all((blink_time <= t <= time_to_stop,ready_to_shine == 1, type == 0))) and impacts_distr.status == NOT_STARTED:
                # keep track of start time/frame for later
                impacts_distr.tStart = t
                impacts_distr.frameNStart = frameN  # exact frame index
                impacts_distr.setAutoDraw(True)
            if impacts_distr.status == STARTED and bool(ready_to_shine == 0):
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
            
            # *impacts_control_group* updates
            if (all((blink_time <= t <= time_to_stop,ready_to_shine == 1, type == 2))) and impacts_control_group.status == NOT_STARTED:
                # keep track of start time/frame for later
                impacts_control_group.tStart = t
                impacts_control_group.frameNStart = frameN  # exact frame index
                impacts_control_group.setAutoDraw(True)
            if impacts_control_group.status == STARTED and bool(ready_to_shine == 0):
                impacts_control_group.setAutoDraw(False)
            
            # *game_over* updates
            if (t2 < 0) and game_over.status == NOT_STARTED:
                # keep track of start time/frame for later
                game_over.tStart = t
                game_over.frameNStart = frameN  # exact frame index
                game_over.setAutoDraw(True)
            
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
Decipher = {1: 'Hint', 0: 'Distractor', 2: 'Control'}
prepand_type = Decipher[prepand_type]
statistic.save_down(os.path.join(_thisDir, 'Overall_statistics\groups.txt'), prepand_type)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
