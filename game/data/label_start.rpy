transform intro_smoke_drift:
    subpixel True
    xalign 0.5
    yalign 0.5
    alpha 0.5
    zoom 1.5
    ease 5.0 xoffset -100
    ease 10.0 xoffset 100
    ease 5.0 xoffset 0
    repeat

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
    scene black with Dissolve(1.0)
    scene expression Transform("images/cgs/intro_picture.png", size = (config.screen_width, config.screen_height), fit = "cover") with Dissolve(1.0)
    show expression Transform("images/vfx_sprites/vfx_light_haze.webp", size = (config.screen_width, config.screen_height), fit = "cover") as intro_smoke at intro_smoke_drift
    $ renpy.pause(3.0)
    scene black with Dissolve(1.0)

    # init vars
    $ CELESTE.image_tag = "images/characters/celeste_young/celeste_10_yrs_neutral_face.png"

    # char creation
    scene black with dissolve

    # jump to actual narrative start
    jump qst_prologue_primer

label dev_quickstart:
    $ DEBUG_SupressNotifs(True)
    $ SaveGameWasNeverUpdated = False
    $ QstStart(PrimerPrologue, Silent = True)
    $ QstComplete(PrimerPrologue, Silent = True)
    $ QstStart(MadnessModuleModule)

    $ gui_parts["characters"] = True