screen BattleDifficultySelection():
    default HoveredButton = 0
    add "cg_celeste_normal" fit "cover":
        if HoveredButton == 0:
            at DifficultyScreenBackground
        else:
            at DifficultyScreenBackgroundHide
    add Transform("cg_celeste_normal", matrixcolor=TintMatrix("#9973CC")) fit "cover":
        if HoveredButton == 1:
            at DifficultyScreenBackground
        else:
            at DifficultyScreenBackgroundHide
    add Transform("cg_celeste_normal", matrixcolor=BrightnessMatrix(-0.5)) fit "cover":
        if HoveredButton == 2:
            at DifficultyScreenBackground
        else:
            at DifficultyScreenBackgroundHide
    vbox:
        align (0.02, 0.4)
        vbox:
            text _("Game difficulty") size 60
            text _("{i}You can change it anytime during your adventure...{/i}") size 20
        null height 10
        vbox:
            for idx, name in DIFFICULTY.NAMES.items():
                hbox:
                    spacing 10
                    $ numKey = "%d" % (idx + 1)
                    label "%s" % str(idx + 1):
                        style "choice_label"
                        anchor (0.33335, 0.5)
                        pos (0.5, 0.5)
                    textbutton tra(name):
                        style "choice_button"
                        yminimum 35
                        xminimum 480
                        keysym str(idx + 1)

                        if idx == 2:
                            action NullAction()
                        else:
                            action [TooltipClearUI(), SetVariable("CurrentDifficulty", idx), Return()]

                        hovered [TooltipSetUI("{i}" + tra(CurrentDifficultyDesc[idx]) + "{/i}"), SetScreenVariable("HoveredButton", idx)]
                        unhovered [TooltipClearUI(), SetVariable("currentBDBG", None)]

transform DifficultyScreenBackground:
    alpha 0.0
    ease 0.25 alpha 1.0

transform DifficultyScreenBackgroundHide:
    ease 0.75 alpha 0.0
