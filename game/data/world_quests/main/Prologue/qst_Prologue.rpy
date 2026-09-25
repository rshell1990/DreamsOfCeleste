init python:
    @AppendToAllQuests
    class QstPrologue(BaseQuest):
        GOALS = {
            0: QuestStage(_("Help with the farm"),     
                ## trackTag = "btn_brother",
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

        def onEnter(self):  
            if GetLocID() == "house_livingroom":
                if self.progress == 1:
                    return TriggeredEvent("qst_prologue_gohome")

        def onComplete(self):
            store.ShowLevelUpFloatingText = True

            AutoTimeFreeze(False)