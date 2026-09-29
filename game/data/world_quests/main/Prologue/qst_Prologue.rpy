init python:
    @AppendToAllQuests
    class QstPrologue(LogicModule):
        GOALS = {
            0: QuestStage(_("Help with the farm"),     
                ## trackTag = "btn_nashar",
                hintTxt = _("I need to help with the farm.")),
            1: QuestStage(_("Meet Brody at the lake"),
                ## trackTag = "btn_lake",    
                hintTxt = _("I need to meet Brody at the lake.")),
            2: QuestStage(_("Go Home its starting to get late"), 
                ## trackTag = "btn_home_frontdoor", 
                hintTxt = _("It's getting late, I should head home.")),
        }
        TITLE = _("Prologue")
        DESCRIPTION = _("Help my brother")

        def __init__(self):
            super().__init__()
    
            self.XpReward = 50
            self.GotScythe = False
            self.FarmTended = False
            self.MetBrody = False
            self.GoHome = False

        def locationMod(self):
            return LocButtonMod()

        def onEnter(self):  
            if GetLocID() == "house_livingroom" and IsGoalComplete(QstPrologue, 1):
                return TriggeredEvent("return_home")

        def onComplete(self):
            store.ShowLevelUpFloatingText = True

            AutoTimeFreeze(False)

    @AppendToAllQuests
    class QstPrologue2(LogicModule):
        GOALS = {
            0: QuestStage(_("Clean windows and doors"),
                ## trackTag = "btn_do_chores",
                hintTxt = _("Do your chores in the courtyard.")),
        }
        TITLE = _("Prologue-Teenage Years")
        DESCRIPTION = _("Do your chores in the courtyard.")

        def __init__(self):
            super().__init__()
            self.XpReward = 50
            self.DoChores = False

        def locationMod(self):
            return LocButtonMod()

        def onEnter(self):  
            if GetLocID() == "orphanage_courtyard":
                if self.DoChores:
                    return TriggeredEvent("qst_prologue2_dochores")

        def onComplete(self):
            store.ShowLevelUpFloatingText = True

            AutoTimeFreeze(False)