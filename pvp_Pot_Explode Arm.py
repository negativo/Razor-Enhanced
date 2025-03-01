# Explode pot 1 key executer.
# hit once to arm
# hit again to toss at last target

# true to cancel target after arming
cancelTarget = False

msgcolor = 53
fakeTarget = 0x00000
lastTarget = Target.GetLast()

import sys
            
def potArmOrThrow():
    # tosses pot if has been charging
    if Timer.Check( 'ex' + Player.Name ) == True:
        Player.HeadMessage( msgcolor, 'Tossing' )
        usePot()
        Target.WaitForTarget(1500)
        Target.TargetExecute(lastTarget)
        Timer.Create( 'ex' + Player.Name , 1)

    # starts charging pot 
    else:
        usePot()
        Misc.Pause(120)
        if Journal.Search('You should throw it now!'):
            Player.HeadMessage(msgcolor,'Exp Pot Armed')
            Timer.Create( 'ex' + Player.Name , 4500)
            if cancelTarget:
                Target.TargetExecute(fakeTarget)
                Misc.Pause(100)
                Target.SetLast(lastTarget)
    
def usePot():
    Player.ChatSay(msgcolor, '[drink GreaterExplosionPotion')
    Misc.Pause(120)
    if Journal.Search( 'You do not have any of those potions.'):
        Player.HeadMessage(msgcolor, 'Out of Exp Pots')
        sys.exit()
    elif Journal.Search('You must wait a moment before using another explosion potion'):
        Misc.NoOperation()

Journal.Clear()
potArmOrThrow()
