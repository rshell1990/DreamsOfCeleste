# these are for development
# !!! all these should be false in public builds
define DEBUG_SkipSaveUpdate         = False # on: save update will be skipped
define DEBUG_ForceSaveUpdate        = False # on: save update will happen regardless of version
define DEBUG_ShowSaveUpdateMessages = False # on: debug 'say' messages will be spammed around
define DEBUG_BypassDevFixup         = False # on: will bypass dev-only fixup-part
define DEBUG_ShowCheatMenu          = False # on: will show cheat menu regardless of whether cheat was entered
define DEBUG_AllowRollbackAfterLoad = (True if config.developer else False) # on: rollback after load will be allowed


default SaveGameVersion = config.version
# for pre-0.162 saves mostly, tells if the save went thru the update cycle at least once
default SaveGameWasNeverUpdated = True
default GameStartedOnVersion = "0.001"

label save_state_update_shared:
    ### WARNING: order here kinda matters, be wary swapping shit around (chars vs items mostly)
    $ SAVEFIX_InitializeMissingWorldChars()
    $ SAVEFIX_UpdateCharTemplateRefAndDeleteObsoleteChars()
    $ SAVEFIX_AddMissingCharPropsFromTemplate()
    $ SAVEFIX_UnequipAllItemsForAwayCompanions()
    $ SAVEFIX_RecalcAttrSkillPointsForPartyChars()
    $ SAVEFIX_QstDeleteObsolete()
    $ SAVEFIX_QstCreateMissing()
    #### items
    $ BuildAllItemContainers()          # creates all the variables like "house chest" or "hamun store"
    $ SAVEFIX_UpdateAllLogicModuleFields()
    return

label after_load:
    if not DEBUG_SkipSaveUpdate:
        if DEBUG_ForceSaveUpdate or SaveGameWasNeverUpdated or SaveGameVersion != config.version:
            call save_state_update_shared
            $ SaveGameVersion = config.version
            $ SaveGameWasNeverUpdated = False
    return

init python:
    # for that rare case where people had galleyUnlocks as different type
    if not isinstance(persistent.galleryUnlocks, dict):
        persistent.galleryUnlocks = dict()

    # to find fucked up (in rel. screen sense) world chars on old saves
    def DEBUG_PrintCharsThatHaveMCFaceAsPortrait():
        for CharID, CharData in worldChars.items():
            if CharID == MC_ID:
                continue
            if CharData["portrait"] == "characters/mc/portrait.webp":
                print("DEBUG: world char %s has mc face as portrait" % CharID)
        return

###############################################
    def SAVEFIX_AddFinishOrderFieldToAllQuests():
        for Quest in GetAllQuests():
            if not hasattr(Quest, "FinishOrder"):
                setattr(Quest, "FinishOrder", 0)
        return

    def SAVEFIX_AddQuestOverShowInHistoryToAllQuests():
        for Quest in GetAllQuests():
            Quest.QuestOverShowInHistory = True

    def SAVEFIX_QstDeleteObsolete():
        ## delete obso
        QuestNamesToDelete = []
        for QuestClassName, QuestObj in questObjs.items():
            if QuestObj.__class__ not in allQuests:
                QuestNamesToDelete.append(QuestClassName)
        
        for QstName in QuestNamesToDelete:
            questObjs.pop(QstName)

    def SAVEFIX_QstCreateMissing():
        ## new instances
        for QuestClass in allQuests:
            QuestName = QuestClass.__name__
            if QuestName not in questObjs:
                questObjs[QuestName] = QuestClass()
            elif questObjs[QuestName].__class__ is not QuestClass:
                questObjs[QuestName].__class__ = QuestClass
        return

    def SAVEFIX_InitializeMissingWorldChars():
        # #1 is "kind" (for variables) #2 is message.
        # inside it should do
        # funcname = sys._getframe().f_code.co_name
        # DEBUG_ConsLog("savefix", "save update: doing a missing world chars pass (SAVEFIX_InitializeMissingWorldChars)")
        CharsRebuilt = 0
        for CharID in CharDefs:
            if CharDefs[CharID]["IsMob"] == False:
                if CharID not in store.worldChars:
                    # print("save update: initializing missing char %s" % CharID)
                    CreateWorldCharFromID(CharID)
                    CharsRebuilt += 1
        # if CharsRebuilt != 0:
            # if DEBUG_ConsoleOutput_Savefix_General:
                # print("save update: initialized %s missing characters (SAVEFIX_InitializeMissingWorldChars)" % CharsRebuilt)
        return

    def SAVEFIX_UpdateCharTemplateRefAndDeleteObsoleteChars():
        VerboseLog_General = False
        # when save is loaded, TemplateRefs in characters are actually copies
        # theres some other crap goin on there too, 
        # tl;dr is this will make templateRef point to actual CharDef not the shadow-copy
        ObsoleteWorldCharIDs = []
        for CharID, CharData in worldChars.items():
            if CharID in CharDefs:
                worldChars[CharID].TemplateRef = CharDefs[CharID]
            else:
                ObsoleteWorldCharIDs.append(CharID)

        # also remove obsolete chars
        for CharID in ObsoleteWorldCharIDs:
            worldChars.pop(CharID)
            if VerboseLog_General: 
                print("save update: deleted obsolete character %s from worldChars" % CharID)
        return

    def SAVEFIX_AddMissingCharPropsFromTemplate():
        ### update props
        for CharID in worldChars:
            worldChars[CharID].AddMissingPropsFromTemplate()
        return

    def SAVEFIX_UnequipAllItemsForAwayCompanions():
        for CharID in worldChars:
            if not CharInParty(CharID):
                for SlotID in EQP_SLOTS.ALL:
                    UnequipItem_CharID(CharID, SlotID)

    # recalc/unfuck attribute/skill points
    def SAVEFIX_RecalcAttrSkillPointsForPartyChars():
        for CharID in player_party:
            RecalcSkillAndAttrPoints(CharID)
        return

    def SAVEFIX_UpdateAllLogicModuleFields():
        VerboseLog_General = False
        for LMClass in store.allQuests:

            LMTemporaryNewInstance = LMClass.__new__(LMClass)
            LMTemporaryNewInstance.__init__()

            LMActualObject = LMClass()
            for Var, Value in vars(LMTemporaryNewInstance).items():
                if not hasattr(LMActualObject, Var):
                    setattr(LMActualObject, Var, copy.deepcopy(Value))
                    if config.developer:
                        if VerboseLog_General:
                            print("save update: added missing field  %s  to logic module  %s" % (Var, LMClass.__name__))
            for GoalID, GoalContent in LMClass.GOALS.items():
                if GoalID not in LMActualObject.GoalStates:
                    LMActualObject.GoalStates[GoalID] = GoalState.HIDDEN
            # remove obsolete goalstates
            for GoalID in list(LMActualObject.GoalStates):
                if GoalID not in LMActualObject.GOALS:
                    LMActualObject.GoalStates.pop(GoalID)

                
    def SAVEFIX_UpdateCharPregModules0176():
        VerboseLog_General = False

        PregClassList = [
            PregJackalGirl,
            PregLizardRed,
            PregLizardGreen,
            PregLizardBlue,
            PregVizura,
            PregDivine,
            PregMika,
            PregWinward,
            PregMyu,
            PregNijah,
        ]
        
        for PregClass in PregClassList:
            PregClassTempNewInstance = PregClass.__new__(PregClass)
            PregClassTempNewInstance.__init__()

            PregClassObj = PregClass()
            for Var, Value in vars(PregClassTempNewInstance).items():
                if not hasattr(PregClassObj, Var):
                    setattr(PregClassObj, Var, copy.deepcopy(Value))
                    if config.developer:
                        if VerboseLog_General:
                            print("save update: added missing field  %s  to preg module  %s" % (Var, PregClass.__name__))

            if QstIsActive(PregClass):
                if PregClass().progress == 1:
                    PregClass().NumImpregs += 1
                    PregClass().IsInPregMode = True
                    PregClass().IsPreg = True
                    if CharGetPreg(PregClass().CharID) == 4:
                        PregClass().IsPreg = False
        for PregClass in PregClassList:
            if QstIsActive(PregClass):
                PregClass().onMidnight()
        return

    # bruteforce gal unlocks fix for some old ass versions (ON STARTUP)
    if not isinstance(persistent.galleryUnlocks, dict):
        persistent.galleryUnlocks = dict()

    def SAVEFIX_ConvertItemsFromIndexesToIDs():
        IdxIDMap = {} # <- for laters, to replace equipment with ids
        for ContainerID, ContainerItems in AllContainers.items():
            for ItemIndex in list(ContainerItems):
                # this check because logic modules with shops with IDs might have already been initialized (yea fucked but WHAT YOU GOONNA DOO HUH)
                if isinstance(ItemIndex, str):
                    continue
                else:
                    ItemID = world_items[ItemIndex]["template_ID"]
                    IdxIDMap[ItemIndex] = ItemID
                    ContainerItems[ItemID] = ContainerItems[ItemIndex]
                    ContainerItems.pop(ItemIndex)

        for CharID, CharData in worldChars.items():
            for SlotID in EQP_SLOTS.ALL:
                if CharData[SlotID] in IdxIDMap:
                    CharData[SlotID] = IdxIDMap[CharData[SlotID]]
