label start:
    # save compat-related vars
    $ SaveGameWasNeverUpdated   = False
    $ GameStartedOnVersion      = config.version

    # difficulty
    scene black
    with dissolve

    $ HideUI(True)
    $ ShowDialogueHistoryButton = False

    $ PlayMusic("audio/music/8_ValleyofDeath.ogg")

    if not config.developer:
        call screen ok_popup(
            label = _("Disclaimer"), 
            text = _("Please be aware Dreams of Celeste is still in development. Enjoy."),
            timer = 1.5)

    call screen BattleDifficultySelection() with dissolve

    # intro picture
    scene expression Transform("images/cgs/intro_picture.png", size = (config.screen_width, config.screen_height), fit = "cover") with Dissolve(1.0)
    $ renpy.pause(3.0)
    scene black with Dissolve(1.0)

    # init vars
    $ Celeste.image_tag = "images/characters/celeste_young/celeste_10_yrs_neutral_face.png"

    # char creation
    scene black with dissolve

    # jump to actual narrative start
    jump qst_prologue_intro

label dev_quickstart:
    $ DEBUG_SupressNotifs(True)
    $ SaveGameWasNeverUpdated = False
    $ QstStart(QstPrologue, Silent = True)
    $ QstComplete(QstPrologue, Silent = True)
    $ QstStart(MadnessModuleModule)

    $ gui_parts["characters"] = True