#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on Tue 21 Nov 2017 03:10:41 PM CET
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
expName = 'textInputTest'  # from the Builder filename that created this script
expInfo = {u'handedness': u'', u'session': u'', u'participant': u'', u'sex': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/home/ryan/Dropbox/ryancallihan_fabian/WordExp/mandarin_experiment/mandarin_exp.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1600, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text=u'\u60a8\u597d!\n\u8acb\u6309\u7a7a\u767d\u9375\u7e7c\u7e8c\u3002',
    font='Arial',
    pos=[0, 0], height=0.075, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text_instruction = visual.TextStim(win=win, name='text_instruction',
    text=u'\u5728\u6bcf\u4e00\u984c\u4e2d\uff0c\u60a8\u6703\u807d\u5230\u4e00\u500b\u4e2d\u6587\u8a5e\uff0c\u8acb\u60a8\uff1a\n1. \u6c7a\u5b9a\u60a8\u662f\u5426\u7406\u89e3\u9019\u500b\u8a5e\u3002\n2. \u6253\u51fa\u9019\u500b\u8a5e\u3002\n\u8acb\u6309\u7a7a\u767d\u9375\u7e7c\u7e8c\u3002',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "sound_stimuli"
sound_stimuliClock = core.Clock()
text_fixation = visual.TextStim(win=win, name='text_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
sound_test = sound.Sound('A', secs=-1)
sound_test.setVolume(1)

# Initialize components for Routine "gatherText"
gatherTextClock = core.Clock()
inputText = u""
text_type = visual.TextStim(win=win, name='text_type',
    text='default text',
    font='Arial',
    pos=[-0.5, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "begin"
beginClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u'\u4f60\u51c6\u5907\u597d\u5f00\u59cb\u4e86\u5417\uff1f\n\n\u51c6\u5907\u597d\u540e\u6309\u7a7a\u683c\u952e',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "sound_stimuli"
sound_stimuliClock = core.Clock()
text_fixation = visual.TextStim(win=win, name='text_fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);
sound_test = sound.Sound('A', secs=-1)
sound_test.setVolume(1)

# Initialize components for Routine "gatherText"
gatherTextClock = core.Clock()
inputText = u""
text_type = visual.TextStim(win=win, name='text_type',
    text='default text',
    font='Arial',
    pos=[-0.5, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "end"
endClock = core.Clock()
text_end = visual.TextStim(win=win, name='text_end',
    text=u'\u5be6\u9a57\u7d50\u675f\uff0c\u8b1d\u8b1d\u60a8\u7684\u53c3\u8207\uff01',
    font='Arial',
    pos=[0, 0], height=0.08, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
t = 0
welcomeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_welcome = event.BuilderKeyResponse()
# keep track of which components have finished
welcomeComponents = [ISI, text_welcome, key_resp_welcome]
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    if t >= 0.0 and text_welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_welcome.tStart = t
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.setAutoDraw(True)
    
    # *key_resp_welcome* updates
    if t >= 0.0 and key_resp_welcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_welcome.tStart = t
        key_resp_welcome.frameNStart = frameN  # exact frame index
        key_resp_welcome.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_welcome.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_welcome.status == STARTED:
        theseKeys = event.getKeys(keyList=['space', ' '])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_welcome.keys = theseKeys[-1]  # just the last key pressed
            key_resp_welcome.rt = key_resp_welcome.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    # *ISI* period
    if t >= 0.0 and ISI.status == NOT_STARTED:
        # keep track of start time/frame for later
        ISI.tStart = t
        ISI.frameNStart = frameN  # exact frame index
        ISI.start(0.5)
    elif ISI.status == STARTED:  # one frame should pass before updating params and completing
        ISI.complete()  # finish the static period
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_welcome.keys in ['', [], None]:  # No response was made
    key_resp_welcome.keys=None
thisExp.addData('key_resp_welcome.keys',key_resp_welcome.keys)
if key_resp_welcome.keys != None:  # we had a response
    thisExp.addData('key_resp_welcome.rt', key_resp_welcome.rt)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_instruction = event.BuilderKeyResponse()
# keep track of which components have finished
instructionComponents = [text_instruction, key_resp_instruction]
for thisComponent in instructionComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instruction* updates
    if t >= 0.0 and text_instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruction.tStart = t
        text_instruction.frameNStart = frameN  # exact frame index
        text_instruction.setAutoDraw(True)
    
    # *key_resp_instruction* updates
    if t >= 0.0 and key_resp_instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instruction.tStart = t
        key_resp_instruction.frameNStart = frameN  # exact frame index
        key_resp_instruction.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_instruction.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_instruction.status == STARTED:
        theseKeys = event.getKeys(keyList=['space', ' '])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instruction.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instruction.rt = key_resp_instruction.clock.getTime()
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
if key_resp_instruction.keys in ['', [], None]:  # No response was made
    key_resp_instruction.keys=None
thisExp.addData('key_resp_instruction.keys',key_resp_instruction.keys)
if key_resp_instruction.keys != None:  # we had a response
    thisExp.addData('key_resp_instruction.rt', key_resp_instruction.rt)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('test.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "sound_stimuli"-------
    t = 0
    sound_stimuliClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_sound = event.BuilderKeyResponse()
    sound_test.setSound(file, secs=-1)
    # keep track of which components have finished
    sound_stimuliComponents = [text_fixation, key_resp_sound, sound_test]
    for thisComponent in sound_stimuliComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sound_stimuli"-------
    while continueRoutine:
        # get current time
        t = sound_stimuliClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fixation* updates
        if t >= 0.0 and text_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_fixation.tStart = t
            text_fixation.frameNStart = frameN  # exact frame index
            text_fixation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_fixation.status == STARTED and t >= frameRemains:
            text_fixation.setAutoDraw(False)
        
        # *key_resp_sound* updates
        if t >= 0.0 and key_resp_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_sound.tStart = t
            key_resp_sound.frameNStart = frameN  # exact frame index
            key_resp_sound.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_sound.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_sound.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_sound.keys = theseKeys[-1]  # just the last key pressed
                key_resp_sound.rt = key_resp_sound.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_test
        if t >= 0.5 and sound_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_test.tStart = t
            sound_test.frameNStart = frameN  # exact frame index
            sound_test.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sound_stimuli"-------
    for thisComponent in sound_stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_sound.keys in ['', [], None]:  # No response was made
        key_resp_sound.keys=None
    trials.addData('key_resp_sound.keys',key_resp_sound.keys)
    if key_resp_sound.keys != None:  # we had a response
        trials.addData('key_resp_sound.rt', key_resp_sound.rt)
    sound_test.stop()  # ensure sound has stopped at end of routine
    # the Routine "sound_stimuli" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "gatherText"-------
    t = 0
    gatherTextClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    theseKeys=u""
    shift_flag = False
    text_type.alignHoriz ='left'
    key_resp_type = event.BuilderKeyResponse()
    # keep track of which components have finished
    gatherTextComponents = [text_type, key_resp_type]
    for thisComponent in gatherTextComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "gatherText"-------
    while continueRoutine:
        # get current time
        t = gatherTextClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n= len(theseKeys)
        i = 0
        while i < n:
        
            if theseKeys[i] == u'return':
                # pressing RETURN means time to stop
                continueRoutine = False
                break
        
            elif theseKeys[i] == u'backspace':
                inputText = inputText[:-1]  # lose the final character
        
            elif theseKeys[i] == u'space':
                inputText += ' '
        
            else:
                if len(theseKeys[i]) == 1:
                    inputText += theseKeys[i]
        
            i += 1
        
        
        
        
        
        
        # *text_type* updates
        if t >= 0 and text_type.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_type.tStart = t
            text_type.frameNStart = frameN  # exact frame index
            text_type.setAutoDraw(True)
        if text_type.status == STARTED:  # only update if drawing
            text_type.setText(('What did you hear?\n' + inputText), log=False)
        
        # *key_resp_type* updates
        if t >= 0 and key_resp_type.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_type.tStart = t
            key_resp_type.frameNStart = frameN  # exact frame index
            key_resp_type.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_type.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_type.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_type.keys.extend(theseKeys)  # storing all keys
                key_resp_type.rt.append(key_resp_type.clock.getTime())
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in gatherTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "gatherText"-------
    for thisComponent in gatherTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # let's store the final text string into the results finle...
    thisExp.addData('inputText', inputText)
    inputText=""
    # check responses
    if key_resp_type.keys in ['', [], None]:  # No response was made
        key_resp_type.keys=None
    trials.addData('key_resp_type.keys',key_resp_type.keys)
    if key_resp_type.keys != None:  # we had a response
        trials.addData('key_resp_type.rt', key_resp_type.rt)
    # the Routine "gatherText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "begin"-------
t = 0
beginClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
beginComponents = [text, key_resp_2]
for thisComponent in beginComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "begin"-------
while continueRoutine:
    # get current time
    t = beginClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in beginComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "begin"-------
for thisComponent in beginComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "begin" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuli.csv'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    # ------Prepare to start Routine "sound_stimuli"-------
    t = 0
    sound_stimuliClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_sound = event.BuilderKeyResponse()
    sound_test.setSound(file, secs=-1)
    # keep track of which components have finished
    sound_stimuliComponents = [text_fixation, key_resp_sound, sound_test]
    for thisComponent in sound_stimuliComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "sound_stimuli"-------
    while continueRoutine:
        # get current time
        t = sound_stimuliClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_fixation* updates
        if t >= 0.0 and text_fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_fixation.tStart = t
            text_fixation.frameNStart = frameN  # exact frame index
            text_fixation.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_fixation.status == STARTED and t >= frameRemains:
            text_fixation.setAutoDraw(False)
        
        # *key_resp_sound* updates
        if t >= 0.0 and key_resp_sound.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_sound.tStart = t
            key_resp_sound.frameNStart = frameN  # exact frame index
            key_resp_sound.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_sound.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_sound.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_sound.keys = theseKeys[-1]  # just the last key pressed
                key_resp_sound.rt = key_resp_sound.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_test
        if t >= 0.5 and sound_test.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_test.tStart = t
            sound_test.frameNStart = frameN  # exact frame index
            sound_test.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in sound_stimuliComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "sound_stimuli"-------
    for thisComponent in sound_stimuliComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_sound.keys in ['', [], None]:  # No response was made
        key_resp_sound.keys=None
    trials_2.addData('key_resp_sound.keys',key_resp_sound.keys)
    if key_resp_sound.keys != None:  # we had a response
        trials_2.addData('key_resp_sound.rt', key_resp_sound.rt)
    sound_test.stop()  # ensure sound has stopped at end of routine
    # the Routine "sound_stimuli" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "gatherText"-------
    t = 0
    gatherTextClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    theseKeys=u""
    shift_flag = False
    text_type.alignHoriz ='left'
    key_resp_type = event.BuilderKeyResponse()
    # keep track of which components have finished
    gatherTextComponents = [text_type, key_resp_type]
    for thisComponent in gatherTextComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "gatherText"-------
    while continueRoutine:
        # get current time
        t = gatherTextClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        n= len(theseKeys)
        i = 0
        while i < n:
        
            if theseKeys[i] == u'return':
                # pressing RETURN means time to stop
                continueRoutine = False
                break
        
            elif theseKeys[i] == u'backspace':
                inputText = inputText[:-1]  # lose the final character
        
            elif theseKeys[i] == u'space':
                inputText += ' '
        
            else:
                if len(theseKeys[i]) == 1:
                    inputText += theseKeys[i]
        
            i += 1
        
        
        
        
        
        
        # *text_type* updates
        if t >= 0 and text_type.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_type.tStart = t
            text_type.frameNStart = frameN  # exact frame index
            text_type.setAutoDraw(True)
        if text_type.status == STARTED:  # only update if drawing
            text_type.setText(('What did you hear?\n' + inputText), log=False)
        
        # *key_resp_type* updates
        if t >= 0 and key_resp_type.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_type.tStart = t
            key_resp_type.frameNStart = frameN  # exact frame index
            key_resp_type.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_type.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_type.status == STARTED:
            theseKeys = event.getKeys()
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_type.keys.extend(theseKeys)  # storing all keys
                key_resp_type.rt.append(key_resp_type.clock.getTime())
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in gatherTextComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "gatherText"-------
    for thisComponent in gatherTextComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # let's store the final text string into the results finle...
    thisExp.addData('inputText', inputText)
    inputText=""
    # check responses
    if key_resp_type.keys in ['', [], None]:  # No response was made
        key_resp_type.keys=None
    trials_2.addData('key_resp_type.keys',key_resp_type.keys)
    if key_resp_type.keys != None:  # we had a response
        trials_2.addData('key_resp_type.rt', key_resp_type.rt)
    # the Routine "gatherText" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "end"-------
t = 0
endClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [text_end]
for thisComponent in endComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_end* updates
    if t >= 0.0 and text_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_end.tStart = t
        text_end.frameNStart = frameN  # exact frame index
        text_end.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_end.status == STARTED and t >= frameRemains:
        text_end.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
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
