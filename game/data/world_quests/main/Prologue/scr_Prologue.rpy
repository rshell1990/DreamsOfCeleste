define Celeste = Character("Celeste", image="celeste_young")
define Nashar = Character("Nashar", image="nashar")
define Father = Character("Father", image="father")
define Mother = Character("Mother", image="mother")
define Boris = Character("Boris", image="boris")
define Kayanna = Character("Kayanna", image="kayanna")
define Knight = Character("Knight", image="knight")
define Guard = Character("Guard", image="guard")
define Guard2 = Character("Guard", image="guard2")
define Ursula = Character("Ursula", image="ursula")
define Hara = Character("Sister Hara", image="hara")
define sister1 = Character("Unfamiliar Nun A", image="sister1")
define sister2 = Character("Unfamiliar Nun B", image="sister2")
define Brad = Character("Brad (Goon A)")
define Danny = Character("Danny (Goon B)")
define nunA = Character("Unfamiliar Nun A")
define nunB = Character("Unfamiliar Nun B")
define Harlok = Character("Harlok", image="harlok")
define Bully_1 = Character("Bully 1", image="game/images/characters/harlok_goon_a/bully_1.webp")
define Bully_2 = Character("Bully 2", image="game/images/characters/harlok_goon_b/bully_2.webp")
image fatherandbrotherfight = Transform(
    "images/cgs/Brothervsfather.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
    zoom=0.35,
    xzoom=-1.0,
)
image brothersisterhug = Transform(
    "images/cgs/Brother_And_Celeste.webp",
    size=(config.screen_width, config.screen_height),
    fit="contain",
)
image black = Solid("#000")
image CG_NailedCrow = "images/cgs/crowhammered.webp"
image CG_NailedCrow_wing_left = Transform(
    "images/cgs/crowhammered.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
    zoom=2.2,
    xalign=0.25,
    yalign=0.0,
)
image CG_NailedCrow_wing_right = Transform(
    "images/cgs/crowhammered.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
    zoom=2.2,
    xalign=0.75,
    yalign=0.0,
)
image cgAngryFather = "images/cgs/celestedad_angry.webp"
image father:
    "images/characters/father/celeste_father_neutral.webp"
    zoom 0.68
image father angry:
    Composite(
        (821, 1408),
        (0, 0), "images/characters/father/celeste_father_neutral.webp",
        (0, 0), "images/characters/father/normal/celeste_father_angry.webp",
    )
    zoom 0.68
image father sad:
    Composite(
        (821, 1408),
        (0, 0), "images/characters/father/celeste_father_neutral.webp",
        (0, 0), "images/characters/father/normal/celeste_father_sad.webp",
    )
    zoom 0.68
image celeste_young:
    "images/characters/celeste_young/celeste_10_yrs_neutral_face.webp"
    zoom 0.68
image celeste_young_crying:
    Composite(
        (821, 1408),
        (0, 0), "images/characters/celeste_young/celeste_10_yrs_neutral_face.webp",
        (0, 0), "images/characters/celeste_young/normal/celeste_10_yrs_crying.webp",
    )
    zoom 0.68
image celeste_young_sad:
    Composite(
        (821, 1408),
        (0, 0), "images/characters/celeste_young/celeste_10_yrs_neutral_face.webp",
        (0, 0), "images/characters/celeste_young/normal/celeste_10_yrs_sad.webp",
    )
    zoom 0.68
image celeste_teen:
    "images/characters/celeste_teen/celeste_15_yrs_neutral_face.webp"
    zoom 0.68
image nashar:
    "images/characters/nashar/celeste_brother_neutral.webp"
    zoom 0.68
image nashar angry:
    Composite(
        (821, 1408),
        (0, 0), "images/characters/nashar/celeste_brother_neutral.webp",
        (0, 0), "images/characters/nashar/normal/celeste_brother_angry.webp",
    )
    zoom 0.68
image boris:
    "images/characters/boris/boris_neutral_face.webp"
    zoom 0.55
image mother:
    "images/characters/mother/celeste_mother_neutral.webp"
    zoom 0.68
image motherwithbaby:
    "images/characters/mother/celeste_mother_baby_neutral.webp"
    zoom 0.68
image mother blackeye:
    Composite(
        (821, 1408),
        (0, 0), "images/characters/mother/celeste_mother_neutral.webp",
        (0, 0), "images/characters/mother/black_eye/celeste_mother_angry_black_eye.webp",
    )
    zoom 0.68
image kayanna:
    "images/characters/kayanna/kayanna_sylvaris_neutral_face_clothed.webp"
    zoom 0.68
image thenextday = "game/images/cgs/cg_thenextday.webp"
image knight = Transform(
    "images/characters/knight/knight.webp",
    size=(int(config.screen_width * 0.32), int(config.screen_height * 0.8)),
    fit="contain",
)
image guard:
    "images/characters/guard/guard_neutral.webp"
    zoom 0.56
    yoffset 85
image guard2:
    "images/characters/guard/guard_neutral.webp"
    zoom 0.56
    yoffset 85
image ursula:
    "images/characters/ursula/ursula_neutral_face.webp"
    zoom 0.68
image hara:
    "images/characters/nuns/v1.webp"
    zoom 0.68
image sister1:
    "images/characters/nuns/v2.webp"
    zoom 0.68
image sister2:
    "images/characters/nuns/v3.webp"
    zoom 0.68
image nunA:
    "images/characters/nuns/v2.webp"
    zoom 0.68
image nunB:
    "images/characters/nuns/v3.webp"
    zoom 0.68
image harlok:
    "images/characters/harlok/harlok.webp"
    zoom 0.68
image harlokgoon:
    "images/characters/harlok_goon_a/bully_1.webp"
    zoom 0.68
image harlokgoon2:
    "images/characters/harlok_goon_b/bully_2.webp"
    zoom 0.68
image celestebreakingharloksfoot = Transform(
    "images/cgs/DOC_CG_Celeste_BreakingHarloksLeg_daylight.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image childhood_living_room_day = "data/world_locations/novaras/childhood_home/childhood_living_room_day.webp"
image childhood_living_room = "data/world_locations/novaras/childhood_home/childhood_living_room_day.webp"
image childhood_living_room_night = "data/world_locations/novaras/childhood_home/childhood_living_room_night.webp"
image parent_room = "data/world_locations/novaras/childhood_home/parent_room_day.webp"
image parent_room_night = "data/world_locations/novaras/childhood_home/parent_room_night.webp"
image childhood_attic_room = "data/world_locations/novaras/childhood_home/childhood_attic_room_day.webp"
image childhood_attic_room_night = "data/world_locations/novaras/childhood_home/childhood_attic_room_night.webp"
image childhood_home_outdoor = "data/world_locations/novaras/childhood_home/childhood_home_outdoor_day.webp"
image childhood_home_outdoor_night = "data/world_locations/novaras/childhood_home/childhood_home_outdoor_night.webp"
image childhood_home_outdoor_back = "data/world_locations/novaras/childhood_home/childhood_home_outdoor_back_day.webp"
image childhood_home_outdoor_back_night = "data/world_locations/novaras/childhood_home/childhood_home_outdoor_back_night.webp"
image childhood_barn = "data/world_locations/novaras/childhood_home/childhood_barn_day.webp"
image childhood_barn_night = "data/world_locations/novaras/childhood_home/childhood_barn_night.webp"
image lake = "data/world_locations/novaras/childhood_home/lake_day.webp"
image lake_night = "data/world_locations/novaras/childhood_home/lake_night.webp"
image forest_day = "images/world_bgs/travel_locations/bg_forest.webp"
image separation = "images/cgs/separation.webp"
image parentssleeping = "images/cgs/parents_sleeping.webp"
image funeral = "images/cgs/funeral.webp"
image novaras_graveyard_night = "images/world_bgs/novaras_city/church_graveyard/bg_graveyard_night.webp"
image nasharincoffin = "images/cgs/00006.webp"
image closerlook = "images/cgs/00007.webp"
image heldbynuns = Transform(
    "images/cgs/00010.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image ursulabargesin = Transform(
    "images/cgs/00012.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image haraontheground = Transform(
    "images/cgs/00013.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image wakeup = "images/cgs/00008.webp"
image purpleeyes = Transform(
    "images/cgs/00011.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image stunned = "images/cgs/00002.webp"
image stunned tinted purple = Transform("stunned", matrixcolor=TintMatrix("#8f6bb840"))
image forest_night = "game/images/world_bgs/travel_locations/bg_forest_night.webp"
image orphanage_office = "data/world_locations/novaras/orphanage/orphanage_office_day.webp"
image orphanage_hallway = "data/world_locations/novaras/orphanage/orphanage_corridor_day.webp"
image orphanage_hallway_night = "data/world_locations/novaras/orphanage/orphanage_corridor_night.webp"
image orphanage_courtyard = "data/world_locations/novaras/orphanage/outdoor_orphanage_day.webp"
image orphanage_courtyard_night = "data/world_locations/novaras/orphanage/outdoor_orphanage_night.webp"
image orphanage_girls_quarters = "data/world_locations/novaras/orphanage/inside_orphanage_day.webp"
image orphanage_girls_quarters_night = "data/world_locations/novaras/orphanage/inside_orphanage_night.webp"
image parentsinbedburning = "images/cgs/DoC_CG_CelesteParents_Burning1.webp"
image parentsinbedburning2 = "images/cgs/DoC_CG_CelesteParents_Burning2.webp"
image houseburning = "images/cgs/farmhome_fire_night.webp"
image cg_oneweeklater = "images/cgs/cg_oneweeklater.webp"
image celestewithbaby = "images/characters/celeste_young/celeste_10_yrs_baby_neutral_face.webp"
image celeneagainstnuns = Transform(
    "images/cgs/00010.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image nunwithknife = Transform(
    "images/cgs/DOC_CG_SisterKatherine_Knife.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image nunknifedeath = Transform(
    "images/cgs/DOC_CG_SisterKatherine_death.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
)
image nunsarounddeadnun = Transform(
    "images/cgs/00014.webp",
    size=(config.screen_width, config.screen_height),
    fit="cover",
    zoom=1.15,
)
image sixmonthslatertext = Text("Six months later", size=64)
image atlastyoureachthebottom = "game/images/cgs/atlastyoureachthebottom.webp"
image orphanage_cellar_night = "data/world_locations/novaras/orphanage/orphanage_cellar_night.webp"

init python:
    CharDefs["e_harlok"] = BuildCharTemplate(
        CharID="e_harlok",
        name=_("Harlok"),
        IsMob=True,
        BattleSkin="harlok_still",
        base_health=25,
        base_damage=0,
        base_energy=50,
        Strength=2,
        Endurance=2,
        Willpower=2,
        Agility=2,
        Dexterity=2,
        Luck=2,
        base_xp_value=20,
        auto_attr_allocation="fighter",
        CharSkills={"NeutralTeamUp": 1, "NeutralASmallBlessing": 1},
    )

    CharDefs["e_harlokgoon"] = BuildCharTemplate(
        CharID="e_harlokgoon",
        name=_("Bully 1"),
        IsMob=True,
        BattleSkin="harlok_goon_a_still",
        base_health=25,
        base_damage=0,
        base_energy=50,
        Strength=2,
        Endurance=2,
        Willpower=2,
        Agility=2,
        Dexterity=2,
        Luck=2,
        base_xp_value=20,
        auto_attr_allocation="fighter",
        CharSkills={"NeutralTeamUp": 1, "NeutralASmallBlessing": 1},
    )

    CharDefs["e_harlokgoon2"] = BuildCharTemplate(
        CharID="e_harlokgoon2",
        name=_("Bully 2"),
        IsMob=True,
        BattleSkin="harlok_goon_b_still",
        base_health=25,
        base_damage=0,
        base_energy=50,
        Strength=2,
        Endurance=2,
        Willpower=2,
        Agility=2,
        Dexterity=2,
        Luck=2,
        base_xp_value=20,
        auto_attr_allocation="fighter",
        CharSkills={"NeutralTeamUp": 1, "NeutralASmallBlessing": 1},
    )

    CharDefs["e_hara"] = BuildCharTemplate(
        CharID="e_hara",
        name=_("Sister Hara"),
        IsMob=True,
        BattleSkin="orphanage_hara_still",
        base_health=35,
        base_damage=5,
        base_energy=60,
        Strength=3,
        Endurance=3,
        Willpower=3,
        Agility=3,
        Dexterity=3,
        Luck=3,
        base_xp_value=25,
        auto_attr_allocation="fighter",
        CharSkills={"NeutralTeamUp": 1, "NeutralASmallBlessing": 1},
    )

    CharDefs["e_sister1"] = BuildCharTemplate(
        CharID="e_sister1",
        name=_("Unfamiliar Nun A"),
        IsMob=True,
        BattleSkin="orphanage_sister1_still",
        base_health=35,
        base_damage=5,
        base_energy=60,
        Strength=3,
        Endurance=3,
        Willpower=3,
        Agility=3,
        Dexterity=3,
        Luck=3,
        base_xp_value=25,
        auto_attr_allocation="fighter",
        CharSkills={"NeutralTeamUp": 1, "NeutralASmallBlessing": 1},
    )

    CharDefs["e_sister2"] = BuildCharTemplate(
        CharID="e_sister2",
        name=_("Unfamiliar Nun B"),
        IsMob=True,
        BattleSkin="orphanage_sister2_still",
        base_health=35,
        base_damage=5,
        base_energy=60,
        Strength=3,
        Endurance=3,
        Willpower=3,
        Agility=3,
        Dexterity=3,
        Luck=3,
        base_xp_value=25,
        auto_attr_allocation="fighter",
        CharSkills={"NeutralTeamUp": 1, "NeutralASmallBlessing": 1},
    )

    WorldLocation("house_livingroom", _("Childhood Home"), "childhood_living_room")
    WorldLocation("parents_bedroom", _("Parents' Bedroom"), "parent_room")
    WorldLocation("childhood_attic_room", _("Childhood Attic"), "childhood_attic_room")
    WorldLocation("childhood_home_outdoor", _("Farm Courtyard"), "childhood_home_outdoor_back")
    WorldLocation("childhood_barn", _("Barn"), "childhood_barn")
    WorldLocation("childhood_lake", _("Lake"), "lake")
    WorldLocation("orphanage_office", _("Orphanage Office"), "orphanage_office")
    WorldLocation("orphanage_hallway", _("Orphanage Hallway"), "orphanage_hallway")
    WorldLocation("orphanage_courtyard", _("Orphanage Courtyard"), "orphanage_courtyard")
    WorldLocation("orphanage_girls_quarters", _("Girls' Quarters"), "orphanage_girls_quarters")
    WorldLocation("orphanage_girls_hallway", _("Girls' Hallway"), "black")
    WorldLocation("orphanage_basement", _("Orphanage Basement"), "black")

    house_livingroom = wLocs["house_livingroom"]
    house_livingroom.withBtn("leave_childhood_room", BtnChangeLoc(STR_NAV.LEAVE, "childhood_home_outdoor"))
    house_livingroom.withBtn("childhood_to_parents_bedroom", BtnChangeLoc(STR_NAV.TO_BEDROOM, "parents_bedroom"))
    house_livingroom.withBtn("childhood_to_attic", BtnChangeLoc(_("Go to the attic"), "childhood_attic_room"))
    wLocs["parents_bedroom"].withBtn("parents_bedroom_to_livingroom", BtnChangeLoc(STR_NAV.TO_LIVING_ROOM, "house_livingroom"))
    wLocs["childhood_attic_room"].withBtn("attic_to_livingroom", BtnChangeLoc(STR_NAV.TO_LIVING_ROOM, "house_livingroom"))
    wLocs["childhood_home_outdoor"].withBtn("courtyard_to_livingroom", BtnChangeLoc(STR_NAV.TO_LIVING_ROOM, "house_livingroom"))
    wLocs["childhood_home_outdoor"].withBtn("courtyard_to_barn", BtnChangeLoc(_("Go towards the barn"), "childhood_barn"))
    wLocs["childhood_home_outdoor"].withBtn("courtyard_to_lake", BtnChangeLoc(_("Go to the lake"), "childhood_lake"))
    wLocs["childhood_home_outdoor"].withBtn("courtyard_talk_nashar", BtnJumpLabel(_("Talk to Nashar"), "courtyard_talk_nashar"))
    wLocs["childhood_barn"].withBtn("barn_grab_tools", BtnJumpLabel(_("Grab the farm tools"), "farming_equipment"))
    wLocs["childhood_barn"].withBtn("barn_to_courtyard", BtnChangeLoc(_("Return to the courtyard"), "childhood_home_outdoor"))
    wLocs["childhood_lake"].withBtn("lake_to_courtyard", BtnChangeLoc(_("Return to the courtyard"), "childhood_home_outdoor"))
    wLocs["childhood_lake"].withBtn("lake_talk_boris", BtnJumpLabel(_("Talk to Boris"), "boris_lake"))
    GotScythe = False

    # Orphanage navigation
    orphanage_hallway = wLocs["orphanage_hallway"]
    orphanage_hallway.withBtn("orphanage_hallway_to_office", BtnChangeLoc(STR_NAV.LEAVE, "orphanage_office"))
    orphanage_hallway.withBtn("orphanage_hallway_to_courtyard", BtnChangeLoc(_("Go to the courtyard"), "orphanage_courtyard"))
    orphanage_hallway.withBtn("orphanage_hallway_to_girls_quarters", BtnChangeLoc(_("Go to the girls' quarters"), "orphanage_girls_quarters"))
    orphanage_hallway.withBtn("orphanage_hallway_to_basement", BtnJumpLabel(_("Go to the basement"), "orphanage_basement_locked"))

    wLocs["orphanage_office"].withBtn("orphanage_office_to_hallway", BtnChangeLoc(STR_NAV.LEAVE, "orphanage_hallway"))
    wLocs["orphanage_courtyard"].withBtn("orphanage_courtyard_to_hallway", BtnChangeLoc(STR_NAV.LEAVE, "orphanage_hallway"))
    wLocs["orphanage_courtyard"].withBtn("orphanage_courtyard_do_chores", BtnJumpLabel(_("Do your chores"), "chores"))
    wLocs["orphanage_girls_quarters"].withBtn("orphanage_girls_quarters_to_hallway", BtnChangeLoc(STR_NAV.LEAVE, "orphanage_hallway"))

screen loc_house_livingroom():
    default locTag = "house_livingroom"
    use locBtn_sprite(locTag, "leave_childhood_room", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.9, 0.53)))
    use locBtn_sprite(locTag, "childhood_to_parents_bedroom", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.16, 0.52)))
    use locBtn_sprite(locTag, "childhood_to_attic", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.53, 0.28)))

screen loc_parents_bedroom():
    default locTag = "parents_bedroom"
    use locBtn_sprite(locTag, "parents_bedroom_to_livingroom", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.92, 0.53)))

screen loc_childhood_attic_room():
    default locTag = "childhood_attic_room"
    use locBtn_sprite(locTag, "attic_to_livingroom", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.92, 0.53)))

screen loc_childhood_home_outdoor():
    default locTag = "childhood_home_outdoor"
    use locBtn_sprite(locTag, "courtyard_to_livingroom", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.51, 0.68)))
    use locBtn_sprite(locTag, "courtyard_to_barn", "images/gui/buttons_loc/explore.webp", "images/gui/buttons_loc/explore.webp", Transform(pos=(0.86, 0.48)))
    use locBtn_sprite(locTag, "courtyard_to_lake", "images/gui/buttons_loc/travel.webp", "images/gui/buttons_loc/travel.webp", Transform(pos=(0.15, 0.53)))
    if not IsGoalComplete(QstPrologue, 0):
        use locBtn_Char(locTag, "courtyard_talk_nashar", "nashar", "nashar", Transform(anchor=(0.5, 1.0), pos=(0.7, 0.8), zoom=0.65))

screen loc_childhood_barn():
    default locTag = "childhood_barn"
    if not GotScythe:
        use locBtn_sprite(locTag, "barn_grab_tools", "images/gui/buttons_loc/explore.webp", "images/gui/buttons_loc/explore.webp", Transform(pos=(0.84, 0.82)))
    use locBtn_sprite(locTag, "barn_to_courtyard", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.16, 0.82)))

screen loc_childhood_lake():
    default locTag = "childhood_lake"
    if not IsGoalComplete(QstPrologue, 1):
        use locBtn_Char(locTag, "lake_talk_boris", "boris", "boris", Transform(anchor=(0.5, 1.0), pos=(0.58, 0.74), zoom=0.65))
    use locBtn_sprite(locTag, "lake_to_courtyard", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.9, 0.55)))

screen loc_orphanage_hallway():
    default locTag = "orphanage_hallway"
    use locBtn_sprite(locTag, "orphanage_hallway_to_office", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.08, 0.55)))
    use locBtn_sprite(locTag, "orphanage_hallway_to_courtyard", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.5, 0.55)))
    use locBtn_sprite(locTag, "orphanage_hallway_to_girls_quarters", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.92, 0.55)))
    use locBtn_sprite(locTag, "orphanage_hallway_to_basement", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.28, 0.85)))

screen loc_orphanage_courtyard():
    default locTag = "orphanage_courtyard"
    use locBtn_sprite(locTag, "orphanage_courtyard_to_hallway", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.9, 0.55)))
    if not IsGoalComplete(QstPrologue2, 0):
        use locBtn_sprite(locTag, "orphanage_courtyard_do_chores", "images/gui/buttons_loc/explore.webp", "images/gui/buttons_loc/explore.webp", Transform(pos=(0.5, 0.55)))

screen loc_orphanage_girls_quarters():
    default locTag = "orphanage_girls_quarters"
    use locBtn_sprite(locTag, "orphanage_girls_quarters_to_hallway", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.9, 0.55)))

screen loc_orphanage_office():
    default locTag = "orphanage_office"
    use locBtn_sprite(locTag, "orphanage_office_to_hallway", "images/gui/buttons_loc/door.webp", "images/gui/buttons_loc/door.webp", Transform(pos=(0.9, 0.55)))

screen loc_orphanage_girls_hallway():
    add Solid("#00000000")

label qst_prologue_primer:
    play sound "audio/cfx/crowcaw.ogg"
    scene CG_NailedCrow_wing_left with flash
    $ renpy.pause(1)
    play sound "audio/cfx/crowcaw.ogg"
    scene CG_NailedCrow_wing_right with flash
    $ renpy.pause(1)
    scene CG_NailedCrow with dissolve
    Father "Celeste!"
    "Father's hands drag and pull your small, frail body toward the front door as you frantically resist, to no avail."
    scene cgAngryFather
    Father "you've done it now, girl"
    Celeste "Let me go!"
    "Your protests fall on deaf ears, yet you still continue to scream and struggle against his grip."
    Celeste "I haven't done anything!"
    play sound "audio/cfx/crowcaw.ogg"
    scene CG_NailedCrow with dissolve
    "...Well, that was a lie, wasn't it?"
    Father "LIAR!"
    play sound "audio/cfx/door_slam.ogg"
    scene childhood_living_room_day
    "With a loud thud, he kicks the door open and swings your small body forward."
    "You crash onto the cold, dirty floor, grazing your knee as you try to stand back up."
    show celeste_young at left
    show father at right with easeinright
    "In his hands, Father grips the blood-stained stick --something you were all too familiar with by now."
    show father angry at right
    "It looks like it's going to get a fresh coat of red today."
    play sound "audio/cfx/running_steps.ogg"
    show nashar at center with slideright
    hide celeste_young
    "As he raises his hand to strike you, there's a rush of feet behind you as your brother moves forward, wrestling the stick from Father's hardened hands."
    show fatherandbrotherfight with dissolve
    Father "GET OFF ME, BOY!"
    Nashar "FATHER, STOP!"
    "He stands as a barrier between you and your father's wrath, managing to knock the stick away as it thuds and rolls across the floor."
    hide fatherandbrotherfight
    show father angry at right
    show nashar angry at center
    show celeste_young at left
    Nashar "What in the hells is going on?"
    Father "Again, I caught her torturing animals!"
    menu celestelieortruth:
        "He's lying I didn't do anything":
            Father "Calling your own father a liar? You shameless little cunt!"
            jump celesteintro_result
        "I was only putting it out of it's misery!":
            Father "BY NAILING IT'S WINGS TO A TREE?"
            Father "I don't know what devil's possessed you, girl, but I swear I'll beat it out of you!"
            jump celesteintro_result
        "If the bird didn't want to die, it should've fought back harder!":
            Father "...By the gods, girl."
            Father "What the fuck is wrong with you?"
            jump celesteintro_result

label celesteintro_result:
    Father "WHAT THE HELL IS WRONG WITH YOU, BOY?"
    Father "The girl needs a beating! It's the only way!"
    Nashar "She's sick! She needs help!"
    Father "The girl's possessed by demons!"
    Nashar "We brought her to a mage of Palam, and you know that's not true!"
    Nashar "It's her mind, it's this place, it's..."
    "He gestures widely."
    Nashar "Fucking all of this!"
    Father "You watch your tongue, boy!"
    Father "I won't spare you the rod either"
    Nashar "I'll get her help. There are people in Novaras"
    Nashar "High mages and men of science who can help her!"
    Father "With what coin, boy?"
    Father "I should just take her to the inquisitors and be done with it!"
    Nashar "They'll brand her the work of dark magecraft and KILL HER!"
    "Father scowls as he always does, cheeks flushed red from the half-empty bottle of mead."
    Father "And maybe we'd all be better for it!"
    "Your brother is furious, his teeth gnashing together as he moves closer toward your father."
    show nashar at cright with slideright
    "A familiar, common sight in the Gwenovair household."
    "Behind you, you hear the soft wailing of Maize, your baby sister."
    show celeste_young at center with dissolve
    "In a moment your mother appears, Maize in her arms as she scowls at all of you."
    show motherwithbaby at left with easeinleft
    Mother "What in the seven hells is going on in here?"
    Father "Ask the boy. He's the one who keeps trying to stop me from doing what needs to be done."
    Nashar "You've beaten her a hundred times before, and it hasn't fixed a damn thing!"
    Father "Bah! Enough of this, I'm heading to the damn tavern!"
    hide father
    hide father with moveoutright
    Mother "Dear!"
    Mother "DEAR!"
    show celeste_young at left with dissolve
    show motherwithbaby at center with dissolve
    Mother "Now look what you've both done!"
    Mother "He won't be back for hours now! Who's gonna finish the field?"
    Celeste "Father is always too drunk for it any--"
    show motherwithbaby at left
    show motherwithbaby at center
    show motherwithbaby at left
    play sound "audio/cfx/slap.ogg"
    "You feel the sting of a slap across your cheek."
    hide celeste_young
    show celeste_young_sad at center
    Mother "Why can't you just be normal, Celeste?"
    Mother "WHY MUST YOU MAKE EVERYTHING SO DIFFICULT?"
    hide motherwithbaby with slideleft
    hide celeste_young_sad
    show celeste_young at center
    "With your baby sister still wailing in her arms, your mother storms off."
    play sound "audio/cfx/running_steps.ogg"
    Celeste "..."
    Nashar "..What happened, Celeste?"
    Celeste "Nothing"
    Nashar "Celeste..."
    Celeste "I don't know."
    Nashar "... More dark thoughts?"
    Celeste "...Yes."
    Celeste "...I can't help it. It's like... this pressure builds inside of me."
    Celeste "It doesn't stop till I do bad things"
    Nashar "Celeste..."
    Nashar "You're not well, Celeste"
    Nashar "We've talked about this before."
    Nashar "You can't... act on those feelings, understand?"
    Celeste "I'm trying... {i}I don't want to let you down.{/i}"
    hide celeste_young
    hide nashar
    "He pulls you into a hug."
    #show brothersisterhug
    show celeste_young at left with dissolve
    show nashar at center with dissolve

    Nashar "I know... I know you're trying."
    Nashar "Listen, there's something I need to talk with you about later."
    Nashar "I need your help with some chores, alright?"
    Celeste "What do you need me to do?"
    Nashar "I'm going to need some help tending to the field."
    Celeste "But-"
    Nashar "You know as well as I do, when he goes off like that to get a drink, we don't see him again until after dark."
    Nashar "You're gonna have to help me a little, Celeste. I can't do it all."
    Celeste "*Sigh*"
    Celeste "Alright."
    Nashar "There's a spare scythe in the barn."
    Nashar "Go get it and meet me in the field."
    Celeste "Yes, Nashar"
    $ QstStart(QstPrologue)
    $ LocSet("house_livingroom")
    $ LocEnter()


label courtyard_talk_nashar:
    call qst_prologue_nashar
    $ LocEnter()

label qst_prologue_nashar:
    show nashar at right
    show celeste_young at left with moveinleft
    Nashar "Did you get the scythe, yet?"
    menu nasharfarming:
        "Yes, I got it.":
            if GotScythe:
                $ GoalComplete(QstPrologue, 0)
                Nashar "Alright, let's begin then..."
                "The day slips by as you spend your time toiling in the field with your brother."
                "It is tiring, hot work as the sun beats down on you both."
                "As last, you finally finish."
                jump qst_prologue_nashar_done
            else:
                Nashar "Stop fooling around, Celeste."
                Nashar "Come to me when you have it."
            jump qst_prologue_nashar
        "Not yet.":
            Nashar "Stop fooling around, Celeste."
            Nashar "Come to me when you have it."
    return

label farming_equipment:
    $ GotScythe = True
    "You gather the farm tools."
    $ LocEnter()

label qst_prologue_nashar_done:
    show nashar at center
    show celeste_young at left
    Nashar "*Yawn*"
    Nashar "Alright, Thanks for the help, Celeste"
    Nashar "Why don't you go play for a little while?"
    Nashar "Just be back before it gets dark."
    Celeste "Alright"
    Celeste "(Maybe Boris is free?)"
    Celeste "(He's usually over by the lake.)"
return

label boris_lake:
    show boris at left
    show celeste_young at cright
    Boris "C-Celeste"
    "The chubby boy stammers"
    "Boris is not a friend"
    "More of... an acquaintance who has latched onto you."
    "Fat and with a stutter, he is an easy target for other children to harass."
    "...At least he was, until you slashed one of the boy's eyes with a jagged piece of rock."
    "Another one of your little 'incidents.'"
    "Either way, since then, Boris has followed you around whenever he can."
    "You are fairly sure he might be in love with you."
    "Not that you've ever felt anything like that."
    "Really, you don't feel much for anyone other than Maize and your brother."
    Celeste "Caught anything good?"
    Boris "N-Not today."
    Boris "U-Uhh, you maybe want to join me?"
    "You take a seat beside Boris"
    Celeste "How's your mother, has she--"
    Boris "She's getting better."
    Boris "But she still hasn't left her bed yet."
    Boris "It's a real pain having to do all the work she normally does!"
    Boris "I don't know how to properly wash clothes!"
    Boris "*Sigh*"
    Celeste "Ah... I see."
    Celeste "..."
    Boris "..."
    Boris "...Is your mother and father still hitting you?"
    Celeste "You know I don't like talking about that."
    Boris "I know..."
    show boris at center
    "In all seriousness, Boris grabs both of your shoulders and forces you to look at him."
    Boris "One day, I'm gonna become the strongest boy in the village."
    Boris "And if your father hits you, I'll knock him out!"
    Celeste "... Hahahaha!"
    "You can't help but smile at his endearing need to protect you."
    "He might be an idiot, but..."
    "You lean forward, gently kissing him on the cheek."
    Celeste "Thank you, Boris."
    "Boris, now bright as a tomato, stutters out his answer."
    Boris "D-D-Don't distract me too much!"
    Boris "I g-gotta focus on the fish!"
    Celeste "Right..."
    "Time drifts by until, at last, it's time for you to go home."
    $ TimeAdvTo(TIME_LATEEVENING)
    Celeste "I'd best be heading back now, Boris."
    Boris "S-So soon?"
    Boris "Umm..."
    Boris "Can we play together tomorrow?"
    Celeste "Sure, Boris"
    Celeste "I'll meet you here tomorrow after I'm done with my chores."
    Boris "A-Alright..."
    hide celeste_young with moveoutright
    hide boris
    $ GoalComplete(QstPrologue, 1)
    $ GoalShow(QstPrologue, 2)
    $ LocSet("childhood_lake")
    $LocEnter()

label return_home:
    show mother at cleft
    show father at right
    Mother "I CAN SMELL HER ON YOU!"
    Mother "I CAN SMELL THAT FUCKING WHORE!"
    Father "Have you gone mad, woman?!"
    "Your mother hurls a saucepan at your father, barely missing him as it slams against the wall with a crash."
    play sound "audio/cfx/door_crash.ogg"
    show father at cleft with slideleft
    hide mother
    hide father
    "Angerly, he storms toward your mother, who keeps hitting and beating at him as he drags her by the hair into the bedroom, slamming the door shut."
    play sound "audio/cfx/door_slam.ogg"
    queue sound "audio/cfx/whip.ogg"
    queue sound "audio/cfx/female_short_scream.ogg"
    "You hear screaming, then the familiar *THUD* *THUD* *THUD* as your father beats her with his belt."
    queue sound "audio/cfx/whip.ogg"
    queue sound "audio/cfx/whip.ogg"
    queue sound "audio/cfx/whip.ogg"
    queue sound "audio/cfx/female_short_scream.ogg"
    "Neither of them even acknowledge you've returned home."
    show celeste_young at left
    "Why would they?"
    "After all..."
    "{i}You were used to this by now.{/i}"
    show nashar at right with moveinright
    Nashar "Celeste, what was that--"
    play sound "audio/cfx/whip.ogg"
    queue sound "audio/cfx/spank.ogg"
    queue sound "audio/cfx/female_short_scream.ogg"
    Celeste "Father and Mother are fighting again."
    "A horrified Nashar looks up toward their bedroom door, then at your completely disinterested face."
    Nashar "Come with me a second."
    "He reaches down to take your hand, pulling you into his room, where Maize is peacefully resting in a crib."
    hide celeste_young
    hide nashar
    scene childhood_attic_room
    "Down on his knees, Nashar meets you at eye level."
    show nashar at cright, nashar_bends_down with moveinright
    show celeste_young at cleft with moveinleft
    Nashar "I need you to listen to me, and not to panic, okay?"
    Nashar "But you don't have to face it alone."
    Nashar "...I'm joining a real big adventure party soon."
    show celeste_young_crying at cleft
    Celeste "You... you got into The Silver Dawn?"
    Nashar "Ha... Can you believe it?"
    Nashar "The greatest adventure party around, and I'm going to be in it!"
    Celeste "... Please don't leave me alone."
    Celeste "I don't have anyone else."
    Nashar "...I promise you, Celeste."
    Nashar "I'm gonna get you and your sister out of here."
    Nashar "I need to make enough coin."
    Nashar "I should have enough in a year, maybe even a little less."
    Celeste "...A whole year?"
    Celeste "Without you?"
    Nashar "I know it seems like a long time."
    Nashar "But I'll be back before you know it."
    Celeste "Why not sooner? Aren't they famous adventurers?"
    "Your brother's face strains slightly."
    Nashar "They are..."
    Nashar "But they're taking me under their wing as an apprentice."
    Nashar "I won't earn as much as I should for a while."
    Celeste "That's not fair..."
    Nashar "It's not always about what's fair, Celeste."
    "The thought of being separated from your brother for such a long time makes you anxious."
    "It was always us versus them."
    "You and your big brother."
    "Against the monsters of the world."
    "Against the bullies and the bandits."
    "Against your parents."
    "Now, with him gone, it would just be {i}you{/i} versus those things."
    "And {i}you{/i} versus them is a much terrifying thought."
    Celeste "Please..."
    Celeste "Let me come; I'll look after Maize and--"
    Nashar "I'm sorry, Celeste."
    Nashar "The adventurers' guild is no place for children."
    Celeste "Please."
    Nashar "Celeste--"
    Celeste "I don't want to be alone."
    Celeste "...I don't know if I'll be okay without you."
    "Your brother sighs, gently resting his hand on your head to stroke your hair softly."
    Nashar "...One day, Celeste."
    Nashar "You won't need me anymore."
    Celeste "That's not true. I'll always need you."
    "Your brother smiles and shakes his head."
    Nashar "You have an incredible gift, Celeste."
    Nashar "Magecraft unlike anything I've ever seen in someone so young."
    "His hands reach down to grab your small shoulders."
    Nashar "{i} I know that one day, you'll be the greatest adventurer who ever lived.{/i}"
    Celeste "...I don't wanna be the greatest adventurer."
    Celeste "I just want you to stay with me."
    "Your brother's soft smile fades as he rises from his knees."
    Nashar "When I return, Celeste, I'll never leave your side again."
    Nashar "But until then, I'm going to need you to look after Maize, understand?"
    Nashar "She's going to need her big sister to keep her safe while I'm gone."
    "You want to protest more, but you know it won't do any good."
    "You nod, your face a little puffy as you try to hold back the tears."
    Celeste "When will you be leaving?"
    Nashar "Tomorrow."
    "Your heart sinks."
    Celeste "So soon?"
    Nashar "I'm sorry, Celeste."
    Nashar "They're passing through tomorrow --- I have to go now or I'll miss my chance."
    Nashar "I promise I'll write home."
    Celeste "..."
    Nashar "I have to finish packing up."
    Nashar "We can talk more later."
    hide nashar with fade
    "You watch as your brother heads toward his quarters."
    "The though of leaving you and your little sister alone no doubt pains him."
    scene black
    "But as much as it pains him, its {i}you{/i} who is going to have to live without the only shield in your life..."
    "And so the rest of of the day limps on as your parents scream at each other throughout the night."
    $ TimeAdvTo(TIME_NIGHT)
    scene childhood_attic_room
    "Your brother reads you a bedtime story as he promised all the wonderful things he was going to do for you and Maize when he returned."
    "the great home just the three of you would live in."
    "Never going hungry again because someone was too drunk or angry to do the cooking."
    "And no more beatings anymore."
    "It all feels, strangely, like a dream within a dream."
jump the_next_day
label the_next_day:
    $ TimeAdvTo(TIME_MORNING)
    scene thenextday
    scene childhood_living_room_day
    "The ornate stagecoach arrives outside, a small convoy of wagons covered in cloth following behind as the rain hammers down."
    "Even Father, already drunk, notices and snaps for your mother's attention."
    show father at left
    show mother at cleft
    show celeste_young at center
    Father "She's here! Get the boy!"
    Mother "I thought she wouldn't arrive until after dark?"
    Father "Well, she's here now, so hurry."
    "Your mother sighs as she scurries off to go find your brother."
    hide mother with moveoutleft
    "The doors of the stagecoach open, and a figure inside, obscured by the rain, heads toward the door."
    "Your father's eyes glare down accusatorily at you."
    Father "Don't do anything stupid now, girl."
    Father "This is an important moment for this family."
    Father "Your brother's going to earn us a lot of coin."
    "You hate him."
    "You hate your father so much."
    play sound "audio/cfx/door_knock.ogg"
    "Your father moves forward to answer the door."
    play sound "audio/interactables/wooden_door_open_1.ogg"
    "The door swings open, creaking on its hinges, and {i}she{/i} enters slowly as your father takes a few nervous steps back."
    Father "W-welcome, Ms. Kayanna!"
    Father "You honor our home with your presence!"
    "You stare curiously at the beautiful, but cold creature now standing in your living room."
    "She radiates a naked, unseen magecraft -- overwelming to those who can percieve it."
    "Her clothes are unlike anything you've ever seen."
    "Do all rich adventurers dress like this?"
    "She carries herself less like an adventurer ready to brave the wilds and more like a nobel towering over the lives of everyone beneath her."
    "She looks slowly from left to right around the room."
    "As her daggerlike eyes fall on you, the two of you hold each other's gaze for a moment before she smiles softly."
    "Her voice is soft, yet eerie in it's command."
    Kayanna "you must be the sister."
    Celeste "... Hello."
    Kayanna "And your brother is where?"
    Father "T-The boys is just gathering up the last of his things."
    "Her eyes flicker toward your father for the briefest moment, but she says nothing."
    show kayanna at right_f with move
    "Instead, the woman kneels to meet you at eye level; her gaze seems to scan you over."
    Kayanna "Such magecraft potential in you."
    Kayanna "Celeste, isn't it?"
    Kayanna "I've heard so much about you from your brother already."
    Celeste "... Will you bring my brother back to me?"
    "The woman blinks, tilts her head, and the smile widens slightly."
    "She raises one talon-like finger and gently prods your nose with it."
    Kayanna "{i}I promise to give him back when I'm done.{/i}"
    show mother blackeye at cleft
    show nashar at cright
    "Your brother enters the room, huffing, and puffing as he forces an awkward smile."
    Nashar "S-Sorry for making you wait, Ms. Kayanna!"
    "The woman rises back to her feet."
    Kayanna "Not at all. Are you ready?"
    Nashar "Yes, all packed."
    Kayanna "Good. Load your bags onto one of the supply wagons."
    "Your brother nods and hurries past your silent father and mother. He turns, looks back toward you, and smiles."
    Nashar "Look after yourself, Celeste"
    Nashar "I'll be home before you know it!"
    "You don't answer your brother."
    "You want to tell him that you love him, but instead you simily stare and watch as he leaves out the door."
    hide nashar
    Mother "... H-He will be alright, won't he?"
    Kayanna "Of course."
    "From the open door, you see the other members of the Silver Dawn lingering outside."
    "One of them helps take your brother's bags, loading them onto a wagon."
    Kayanna "Most of his time will be acting as support."
    Kayanna "He probably won't see much, if any, actual fighting."
    Mother "O-Oh..."
    Mother "Thank the gods."
    "For a moment, your parents share a tender smile with each other."
    "You hated them."
    "But at least they loved your brother."
    "And that made you hate them slightly less."
    Kayanna "And as for {i}you{/i}, young lady."
    Kayanna "{i}I look forward to meeting you again, Celeste.{/i}"
    "The woman leaves, and you realize the hairs on your arms have been pricked this whole time."
    hide kayanna
    "There was something about her."
    "Birds of a father, or something your brother once said."
    "{i}Why did you feel like you were looking into a mirror?{/i}"
    hide celeste_young with moveoutleft
    show father at left with moveinleft
    "You give chase. Your father reaches out to stop you, but its too late."
    Father "CELESTE!"
    scene separation
    "The heavy rain pours down as, poorly dressed and barefoot, you run into the soaking mud."
    "The trail of wagons is already far ahead, but you try to run after them anyway."
    "You didn't want him to go."
    "Something terrible inside you knew he wouldn't come back."
    "You trip, falling into the mud as you look up."
    "From the farthest wagon at the back, your brother sees you, waving and smiling one last time before he vanishes from view behind the downpour."
    Celeste "COME BACK!"
    Celeste "DON'T GO!"
    Celeste "Please...!"
    "Please don't go."
    scene black with fade
    "The rain continues to pour, but you are left alone in the darkness, your heart aching for your brother."
    scene sixmonthslatertext with fade
    scene funeral
    "...Kayanna promised you she would return him when she was done."
    "And she did deliver---Your brother came home."
    "{i}... Too bad it was in a box.{/i}"
    "Your mother wails as your father tries to comfort her."
    "Few are gathered for the funeral; friends of your brother you have only a passing recollection of."
    "That pretty girl with the freckles and crooked nose wails louder then the others."
    "Inside, you feel empty."
    "But you don't cry."
    "The mage speaks about your brother's passing."
    "He tells a noble story of your brother's journey with the Silver Dawn."
    "One filled with adventure and hope, ended only in tragedy."
    "How, whilst scaling the snowy mountains of the far north, he managed to push one of the Silver Dawn to safety as an avalanche swept him away."
    "It's a wonderful, if sad, story."
    "...You fucking hate it."
    "You look down toward Maize, crying in your arms."
    Celeste "{i}Looks like it's just me and you now, Maize.{/i}"
    scene black with fade
    jump after_funeral
label after_funeral:
    $ TimeAdvTo(TIME_NIGHT)
    scene childhood_living_room_night
    "As the funeral comes to an end, your home is visited by a strange man later that evening."
    "Dismissed to your room, you watch from the crack in your door."
    show knight at left
    show mother at center
    show father at right
    Knight "The Silver Dawn sends its condolences for your son."
    Mother "Oh gods..."
    Knight "They hope that their generous contributions toward the funeral costs have helped ease this difficult time for you both."
    Mother "Y-Yes, the coin has helped, thank you."
    "Your father takes a step forward, drunk and angry as usual; he shoves your mother aside."
    Father "Why have I had inquistors sniffing around?"
    Father "They're askin' me a lot of bloody questions about my boy and what happened for something that was supposedly an accident!"
    Knight "Of course."
    Knight "The inquisition is just doing it's job with matters such as these."
    Knight "{i}...Though they are very...{/i}"
    Knight "Overzealous in their zeal."
    Father "Over what?"
    Father "I don't know what that means, but some of the things my boy was writing in his letters home..."
    Father "{i}I don't know... but he didn't sound right..."
    Father "So what in the hells are you and your lot hiding?"
    Knight "Sir... {i}No one's hiding anything.{/i}"
    Knight "Your son was simply struggling in the end; the life of an adventurer is difficult."
    Knight "Most people don't come back the same."
    show father sad at right
    Father "...But my boy isn't coming back, is he?"
    Father "He's buried in that fucking box out there!"
    Knight "I can't bring back your son."
    Knight "{i}But the Silver Dawn wants to help{/i}"
    Knight "They treasured your boy deeply in the end, I assure you---everyone is devastated by his loss."
    Mother "Help us?"
    Mother "How?"
    Knight "The inquisitors... they see dark magecraft everywhere they look, even where there is none."
    Knight "Unfortunately, inquisition investigations can last months upon months, with endless interrogations and paperwork."
    Knight "It's all very stressful, I assure you."
    Knight "...The Silver Dawn would very much like to avoid dragging out any kind of investigation."
    Knight "They simply don't want to waste your time or their own over a tragic accident."
    Father "What does the Silver Dawn want?"
    Knight "All you need to do is sign these documents and hand over any letters your son wrote to you."
    Mother "Documents?"
    Knight "Just as signature will do. I have some ink and a feather if needed."
    Father "What the hells are we signing?"
    Knight "Just a simple document that states you both firmly believe the events to be an accident."
    Knight "{i}...And that your son unfortunately suffered bouts of melancholy, leading him to sometimes act erractically."
    Mother "Melancholy? My son never---"
    "The Knight places a large back of coins onto the table."
    Mother "..."
    Father "..."
    Knight "There's a lot more I can give as well."
    Father "...How much?"
    Knight "Fifty thousand coins."
    "Your parents look at each other as they hear the astronomical figure."
    "They would perhaps earn that much between themselves in ten years or longer."
    "If it was life-changing money."
    Knight "So... do we have a deal?"
    "Your parents share another look; your mother reluctantly nods as your father nods toward the man."
    Father "...Aye, we do."
    scene black with flash
    "Your blood boils."
    "How... how could they do this?"
    "How could they betray your brother like this?"
    "You want to run out and scream at them."
    Knight "Good, then sign here."
    "As he slides the papers across the table, your parents sign the sheets."
    "The Knight inspects the signatures."
    "Satified, he nods."
    Knight "Good."
    Knight "And the letters?"
    show father at cleft with move
    show father at cright with move
    "Your father hands them over silently."
    Knight "Spend the coins wisely."
    "The Knight turns to leave, pausing briefly to add;"
    Knight "Oh... and make sure to keep everything said tonight just between us, am I clear?"
    "Your parents don't say anything, and he takes their silence as agreement."
    hide knight
    "Without another word, the Knight leaves, and your parents embrace."
    "{i}You want to kill them all.{/i}"
    "Your blood is simmering hot, but as you move to push open the door---to {i}punish{/i} your parents for betraying you and your brother---you hear the soft crying of Maize behind you."
    scene black
    $ TimeAdvTo(TIME_NIGHT)
    scene childhood_attic_room
    "You remember the promise to your brother, and hurry toward her, holding her in your arms as you sooth and rock her."
    hide mother
    hide father
    show celeste_young at center
    Celeste "Don't worry, Maize."
    Celeste "I'll keep you safe... I promise."
    "And you would keep her safe."
    "You would get the two of you out of here somehow, even if it killed you."
    "...But first, you need to know the truth."
    "You need to know what happened."
    "{i}You need to know what happened to your brother.{/i}"
    hide celeste_young
    scene black
    jump Prologue_Truth

label Prologue_Truth:
    $ TimeAdvTo(TIME_MORNING)
    scene forest_day
    show celeste_young at cright
    show boris at cleft
    Boris "C-Celeste."
    Boris "W-Why did you ask to meet so suddenly?"
    "The young boy stutters."
    Boris "I-I'm really sorry about what happened to your brohter."
    Celeste "I need your help with something"
    Boris "R-Really?"
    Celeste "Can you get a shovel?"
    Boris "H-Huh?"
    Boris "Why?"
    Celeste "{i}I want to dig up my brother's body.{/i}"
    hide celeste_young
    hide boris
    scene black
    play sound "audio/music/digging-with-shovel.ogg"
    "It took you and Boris more than two hours to dig up your brother's grave in the dead of night."
    $ TimeAdvTo(TIME_NIGHT)
    scene novaras_graveyard_night
    "The dim lantern you brought with you seems ready to go out at a moment's notice, and Boris looks particularly afraid, watching for anyone who might see what the two of you are doing."
    show celeste_young at cright
    show boris at cleft
    Boris "I can't believe you talked me into this!"
    Celeste "Enough complaining."
    play sound "audio/music/woodhit.ogg"
    "When the shovel finally hits the hard wood of the coffin, Boris looks toward you."
    Boris "I-It's here!"
    "You wedge and force the shovel between the lid and the coffin as Boris pleads."
    Boris "Celeste!"
    Celeste "..."
    Boris "D-Don't do this."
    Boris "This is your brother's rest..."
    Celeste "..."
    hide celeste_young
    hide boris
    scene nasharincoffin with fade
    "You ignore his words, tearing off the lid as you stare at your brother's lifeless, pale corpse."
    "Boris turns his head and begins to hurl as you inspect your brother's body closer."
    "You were used to inspecting dead things, like teh deer and other mammals you found."
    "You enjoyed figuring out how they died---in fact, you had studied and become quite good at it."
    "You look at your brother's corpse and notice how remarkably undamaged it is."
    "A fall from such heights to kill... and not the slightest broken bone."
    "You look closer, and there---you spot it."
    scene closerlook
    "Resonating from a black wound"
    "{i}Magecraft{/i}"
    "Like an arrow to the heart---some pungent, dark thing having drained him of his life."
    "{i}It smells exactly like the magecraft resonating from that woman, Kayanna.{/i}"
    Boris "Celeste... Urgh... Can we go now, please?"
    Boris "We're gonna get in so much trouble if we're caught!"
    scene nasharincoffin with flash
    "The rage boils inside you."
    "That woman... That bitch."
    "{i}She took your brother from you.{/i}"
    Boris "Celeste!"
    scene novaras_graveyard_night
    "You close the lid on your brother's coffin."
    Celeste "I've seen what I needed to."
    show celeste_young at cright
    show boris at cleft
    "The two of you climb out of the grave."
    Boris "D-Did you find what you were looking for?"
    Celeste "Yes."
    "You take teh first few steps toward home when Boris calls weakly behind you."
    Boris "W-What will you do now?"
    Celeste "...Go home, Boris."
    hide celeste_young with moveoutright
    "Saying nothing else, you make your way home with a burning fire in your heart."
    hide boris
    scene black with fade
    jump revengeonparents
label revengeonparents:
    $ TimeAdvTo(TIME_NIGHT)
    scene childhood_living_room_night
    play sound "audio/music/heartbeat.ogg"
    "...As you quietly enter through the still-unlocked front door, you realize your parents have gone to sleep"
    "Your father likely having drunk himself into another stupor."
    "You stop by to check on Maize, sleeping peacefully in her crib, and then,"
    $ renpy.pause(2.0)
    "{i}You make your way to your parent's room.{/i}"
    scene parentssleeping with fade
    "Asleep on the bed, with another half-drunk bottle in the cabinet beside your father, he snores as you watch the two of them sleep peacefully while your brother rots in the ground."
    "How... how could they betray him?"
    "Betray Maize?"
    scene parentssleeping with fade
    "Betray you."
    "What kind of monsters sell out their own son for a few coins?"
    "The rage builds, and with a trembling voice you speak."
    Celeste "{i}Murderers.{/i}"
    "Your mother's eyes hazily open, and as they do, she shakes your father awake."
    Mother "Celeste? What are you---"
    Celeste "{i}You cannot move.{/i}"
    scene stunned tinted purple
    "Your mother is pinned to the bed by some invisible force---"
    "Now she's awake all right, as her eyes widen with fear."
    Father "WHAT IN THE HELLS DO YOU THINK YOU'RE DOING, G-"
    "Your father moves to get up and stop you, but you turn your gaze to him."
    Celeste "STAY."
    scene stunned
    "Your father, too is now unable to move."
    "The two of them struggle against the invisible pressure exerted against them."
    "It's strange... for all their menace and venom, how helpless they seem to you right now."
    Father "C-Celeste!"
    Father "What do you think you're doing?"
    scene stunned
    Celeste "How could you?"
    Celeste "How could you let them get away with it?"
    Mother "C-Celeste, dear... What are you---"
    Celeste "SILENCE!"
    scene stunned tinted purple with fade
    Father "..."
    Mother "..."
    Celeste "He was the only one who truly loved me in this family."
    Celeste "{i}And you...{/i}"
    scene stunned
    Celeste "ALL IT TOOK WAS A FEW COINS TO BUY YOUR SILENCE?"
    Celeste "TO ABANDON YOUR ONLY SON?"
    scene stunned tinted purple with fade
    "Your parents do their best to squirm in the bed."
    "They're panicking now --- they realize something terrible is going to happen."
    "{i}... What fun.{/i}"
    scene stunned with fade
    Celeste "...Now it's my turn to abandon you both."
    "You raise your hand, setting the bed alight as they panic and squirm, still unable to do anything other then twitch."
    scene parentsinbedburning
    Celeste "Goodbye... Mother..."
    Celeste "Father."
    scene parentsinbedburning2
    "As the fire begins to consume the whole bed --- The flame crawling up your father's leg as he remains unable to break free from your power --- your turn to leave."
    play sound "audio/cfx/fire_burning.ogg"
    scene black with fade
    "Heading quickly into Maize's room, you qently pick up your baby sister before heading out of the house."
    scene houseburning
    play sound "audio/cfx/fire_burning.ogg"
    Guard "Get some more buckets, damn it!"
    show celestewithbaby at center
    Guard "Girl is there anyone still inside?"
    scene parentsinbedburning with flash
    scene houseburning
    Celeste "...No one worth saving."
    "The guard pulls back --- you cannot tell beneath the helmet his expression, but it must be one of confusion and shock."
    "He decides to ignore you, rushing over to try and help the others put out the fire."
    "You lean closer to Maize, gently soothing your crying little sister."
    "The sounds of the fire and the chaos outside fade into the background as you focus on her."
    "For the first time in what feels like forever, there is a moment of peace."
    Celeste "Don't worry, Maize, I won't let anyone hurt you ever again."
    jump oneweeklater
label oneweeklater:
    $ LocSet("orphanage_office")
    $ TimeAdvTo(TIME_MORNING)
    scene cg_oneweeklater with fade
    scene orphanage_office
    $ LocSet("orphanage_office")
    show guard2 at left
    show ursula at right_f
    Guard2 "...You can come in now, girl"
    show celeste_young at center
    "You enter the run-down office as a kind sister in red smiles at you with her hands clasped together."
    Ursula "Hello."
    Ursula "I am Sister Ursula."
    Ursula "You must be Celeste."
    jump firsttimeatofficemenu
label firsttimeatofficemenu:
    menu:
        "What is this place?":
            Ursula "This is the goddess Bellefrom's orphanage."
            Ursula "The Sisters of Bellefrom look after children like yourself who have no other family."
            jump firsttimeatofficemenu
        "Where is my sister--- Where's Maize?":
            Ursula "Maize is being cared for by the other sisters."
            Ursula "Don't worry, she's safe."
            Celeste "I want to see her."
            Ursula "In time, Celeste."
            jump firsttimeatofficemenu
        "What happens now?":
            jump wantingtoleave
label wantingtoleave:
    $ LocSet("orphanage_office")
    Ursula "You'll be staying here for a while now"
    Ursula "At least, until you come of age."
    Ursula "Or, if a family chooses to adopt you"
    Celeste "I want to leave."
    Ursula "I'm sorry, child."
    Ursula "There's nowhere else for you to go."
    Ursula "You must stay here for now."
    Celeste "I WANT TO GO!"
    show guard2 at left with move
    "The guard smacks you on the back of the head from behind, causing you to stumble forward."
    Guard "Be silent, girl."
    "Sister Ursula rushes to your side, raising her hand toward the guard."
    show celeste_young at cleft with move
    show ursula at center_f with move
    Ursula "Guard!"
    Ursula "Please... That will be all."
    "The guard, who seemed ready to hit you again, pulls back."
    Guard "Very well, Sister."
    Guard "I shall leave this matter in your care."
    "With a slight bow, the guard turns to leave as Sister Ursula tends to you."
    hide guard2
    show ursula at right_f with move
    Ursula "Are you alright, child?"
    Celeste "I'm fine."
    Celeste "He hits like a girl anyway."
    "Sister Ursula smiles warmly toward you."
    Ursula "You're a strong girl, aren't you?"
    Ursula "But you don't need to be so strong."
    Ursula "{i}Especially after such a terrible tragedy.{/i}"
    Celeste "..."
    Ursula "Your parents were not the first drunkards I've seen die in such accidents, I'm afraid."
    Celeste "..."
    Ursula "...Come."
    "She holds out her hand for you to take."
    Ursula "Let me show you where you'll be sleeping."
    "Cautiously, you reach out to take the hand, following Sister Ursula as she pulls you along."
    Ursula "This is your new home now, Celeste"
    Ursula "Let's try to make the most of it, shall we?"
    Celeste "Yes, sister."
    hide ursula
    hide celeste_young
    jump years_later
label years_later:
    scene orphanage_girls_quarters
    show ursula at right_f
    show celeste_teen at left
    Ursula "Celeste!"
    "Your eyes open as you drowsily rise from your bed."
    Celeste "Urghhh... What?"
    Ursula "Don't {i}what{/i} me, young lady."
    Ursula "You were supposed to scrub the hallway floors the other night!"
    Ursula "So why did I find young Madison on her hands and knees in your stead?"
    Celeste "Madison owed me a favor."
    Ursula "You mean for beating up that boy the other week, Davis?"
    Celeste "...He shouldn't have taken her food."
    "Ursula's hand whooshes out to lightly slap you."
    "It's nothing like Father's heavy hands were, but it still stings enough to make a point."
    Ursula "I have told you before about shirking your duties, Celeste."
    Ursula "When you're asked to do something, you do it."
    Ursula "It's not an excuse to find ways around it."
    Celeste "Yes... Sister Ursula."
    Ursula "*Sigh*"
    Ursula "Take this bucket and cloth. Clearn some of the doors and windows outside."
    Celeste "Yes, Sister."
    Celeste "...When can I see Maize?"
    Ursula "Soon. Your sister is doing well. Leave her be, Celeste."
    $LocSet("orphanage_hallway")
    $QstStart(QstPrologue2)
    $LocEnter()
    # Show STAT Page
    # Tutorial TALENTS PAGE
label orphanage_basement_locked:
    "You place your hand on the heavy black door and give it a push."
    "...Locked."
    "Whatever the sisters keep down there, they don't want the children poking around."
    return

label courtyard:
    "As you step out into the main courtyard, you hear the usual chatter of the irritating younger children running around."
    "The older ones give uneasy, glancing looks toward you when they see you."
    "You don't have many friends."
    "Well, it would be better to say you have {i}no{/i} friends---only those who fear you enough not to cause problems."
    "Well, what now?"
return
label chores:
    "You grab a bucket and cloth, heading out to clean the doors and windows as instructed by Sister Ursula."
    menu startchoresmenu:
        "Start chores.":
            jump chores_task
        "Not yet.":
            return
label chores_task:
    $GoalComplete(QstPrologue2, 0)
    show celeste_teen at left
    "With your wet cloth soaked in the bucket's water, you begin to wipe the dirty windows as best as you can."
    "Going up on your tiptoes to reach the higher glass."
    "Suddenly, you feel the sharp sting of a small rock hitting your back"
    "You drop the cloth instantly, the bucket tipping over as you turn to look at the skinny, angry little shit with another rock in his hand."
    show harlok at center with movein
    show harlokgoon at cright with movein
    show harlokgoon2 at right with movein
    "His two little minions stand beside him."
    Harlok "Opps! Would you look at that."
    Harlok "Looks like you'll need to fetch yourself a fresh bucket."
    Harlok "Fucking freak."
    "His goons snicker."
    "Harlok never quite accepted why you turned down his advances; he's convinced it's because you're a prude."
    "Perhaps it had something to do with catching him pinning one of the other girls against a wall so he could {i}'have a feel'{/i}.--- which made him repulsive to you."
    "Lucky for him, rumor has it; he's the bastard child of sister Tera, a scandal scarcely discussed but she has no doubt pleaded on his behalf to protect him whenever he gets in trouble."
    Celeste "Leave me alone, Harlok."
    Harlok "Or what, you crazy bitch?"
    Celeste "{i}I won't ask again{/i}."
    menu fightoneorthreemenu:
        "If either of you two idiots help him, {i}I'll smother you in your sleep{/i}." (Req_Strength = 5):
            jump fight_harlok
        "...":
            jump fight_harlok

label fight_harlok:
    "Harlok's two goons stop laughing; they know you're serious."
    "Everyone has learned by now what you're capable of."
    hide harlokgoon
    hide harlokgoon2
    Harlok "What the fuck!"
    Harlok "Where are you guys going?!"
    Brad "Y-You know what she's like, Harlok!"
    Danny "S-Sorry, she's crazy bro!"
    Harlok "Shit..."
    show harlok at cleft with movein
    "Harlok marches toward you, ready to swing a punch!"
    "his two goons retreat, remembering your threat."
    hide celeste_teen
    hide harlok
    $ PartyAddChar(MC_ID, Silent=True)
    $ CharSetBattleSkinID(MC_ID, "mc_prologue")
    $ StartBattle(BattleData(BackgroundImage="orphanage_courtyard", CharIDList_Left=[MC_ID], CharIDList_Right=["e_harlok"], ContinueOnDefeat=False, GiveLoot=False))
    jump after_fight_harlok
label fight_harlokandgoons:
    $ StartBattle(BattleData(BackgroundImage="orphanage_courtyard", CharIDList_Left=[MC_ID], CharIDList_Right=["e_harlok", "e_harlokgoon", "e_harlokgoon2"], ContinueOnDefeat=False, GiveLoot=False))
    jump after_fight_harlok

label after_fight_harlok:
    scene celestebreakingharloksfoot
    "The others have gathered around to watch now, Harlok screams in agony as you bring your foot down onto his leg, the bone loudly breaking and crunching as you do so."
    "The other children and teens gasp, horrified, as a crying Harlok falls to the floor, screaming as tears scream down his cheeks."
    Harlok "AHHHHHHHHHHHHHHHH!"
    Harlok "MY LEG! MY FUCKING LEG!"
    Harlok "YOU CRAZY---"
    "You hear the whispers from behind you."
    "{i}She's possessed, she's a witch, she's a...{/i}"
    "{b}Freak.{b}"
    "You grab one of the nearby rocks, ready to bash the little shit's head in."
    "Before you can, a hand grabs your wrist."
    "It's Sister Ursula."
    scene orphanage_courtyard
    show ursula at cright_f
    show celeste_teen at cleft
    Ursula "Enough!"
    Ursula "Drop it... now!"
    "You drop the rock, and as you do, other sisters rush over to help the still-screaming Harlok."
    "Angrily, Ursula drags you toward her office."
    "You don't protest, but even you must admit..."
    "{i}Perhaps even you went a little too far this time.{/i}"
    hide ursula
    hide celeste_teen
    Ursula "Get in there!"
    "Sister Ursula shoves you forward, slamming the door behind her."
    show celeste_teen at cleft
    show ursula at cright_f with movein
    Ursula "What in the hells were you thinking?!"
    Celeste "He started it!"
    show ursula at center_f with movein
    "On her knees, Sister Ursula grabs your shoulders."
    Ursula "Celeste!"
    Ursula "You broke his leg!"
    Ursula "The bone was sticking out!"
    Ursula "Don't you understand?"
    Ursula "He may not be able to walk again!"
    Celeste "So what? I was just supposed to let him beat me up?!"
    Ursula "There's a difference between fending for yourself, girl, and scaring everyone to death!"
    Ursula "{i}Do you realize the other sisters think you might be possessed?{/i}"
    Celeste "YOU THINK I WANT THIS?!"
    Ursula "..."
    Celeste "You think I always feel like I need eyes in the back of my skull?"
    Celeste "You think I want everyone to hate me?"
    Celeste "...I just wanna take Maize and get away from this place."
    Celeste "Start somewhere new, far away!"
    Celeste "AND BE LEFT ALONE!"
    Ursula "...*Sigh*"
    "Sister Ursula rubs at her brow."
    Ursula "By the gods, girl, you're going to be the death of me."
    Celeste "...I hate it here."
    Ursula "I know you do."
    Ursula "And I promise you, Celeste---"
    Ursula "I will do wht I can for you and your sister."
    Ursula "But please..."
    Ursula "{i}Just try to be good?{/i}"
    Celeste "...Yes."
    Ursula "Alright, Celeste."
    Ursula "You are to return to the girls' quarters and stay there for now."
    Ursula "{i}I need to clear up this mess and speak to the other sisters about what has happened."
    Celeste "But---"
    Ursula "No arguing, Celeste."
    Ursula "Just do it!"
    hide celeste_teen with moveoutleft
    scene orphanage_hallway
    "You slam the door furiously behind you."
    hide ursula
    scene black with fade
    jump orphanage_girls_quarters
label orphanage_girls_quarters:
    $LocSet("orphanage_girls_quarters")
    show celeste_teen at center
    "What a wretched joke."
    "It was that little shit who started it!"
    "Why were you punished for simply defending yourself?"
    hide celeste_teen
    "You sigh and drop onto the bed, with little else to do, and bury your face into your pillow."
    scene lonelyfeeling #...Does no one else really feel the same as you do?
jump middleofthenight

label middleofthenight:
    $ TimeAdvTo(TIME_NIGHT)
    scene orphanage_girls_quarters_night
    Hara "Celeste."
    Hara "..."
    Hara "...CELESTE!"
    "The voice wakes you, and you dazedly see one of the sisters standing over your bed."
    Celeste "...Sister Hara?"
    show hara at center_f with movein
    Hara "You're to come with me, Celeste."
    "You rise from your bed."
    show celeste_teen at right
    Celeste "Where are we going?"
    Hara "We're going to see Maize."
    "Did the sister's voice just crack for a moment?"
    "You're not quite sure; you're still a little dazed from being woken after all."
    Celeste "{i}*Grumbles*{/i} What time is it?"
    Hara "Shh."
    Hara "The others are still asleep."
    "Sister Hara reaches for your hand as she almost drags you away."
    show hara at cright_f with movein
    hide hara with moveoutleft
    hide celeste_teen with moveoutleft
    "You didn't even have time to put your shoes on!"
    $LocSet("orphanage_girls_hallway")
    show celeste_teen at cright with movein
    show hara at center with movein
    Celeste "Sister!"
    Celeste "Where are we going?"
    Hara "I told you, Celeste---We're going to see your sister..."
    "Sister Hara pulls harder, her feet moving faster."
    "Her hands seem shaky---was she afraid?"
    "What was going on?"
    Celeste "...Sister Hara?"
    Hara "Stop talking, Celeste."
    scene black with fade
    "At last, you arrive at your destination: a black, heavy door, normally locked but now open, leading to a dimly lit stone staircase descending into darkness. Sister Hara's hard continues to tug you into the depths."
    "You don't feel afraid exactly; you've never felt fear before---"
    "At least, not in the same way other people do."
    scene Unsettledfeeling with fade #Your heart is calm... and yet, your hairs stand on end, as though something inside you is warning that something terrible is going to happen."
    jump Basement
label Basement:
    scene atlastyoureachthebottom with fade #at last, you reach the bottom floor.
    scene orphanage_cellar_night
    "An open, chamber, filled with sacks of wheat and other foods stored down here in the cold dark."
    "Standing there, each holding torches and a blade, are two other sisters."
    show sister1 at cright with movein
    show sister2 at right with movein
    show hara at left_f with movein
    show celeste_teen at center with movein
    Celeste "What's going on?"
    "You take a nervous step back to turn and leave, seeing Sister Hara block your path."
    Hara "Celeste"
    Hara "{i}There is a demon within you, child.{/i}"
    "Your eyes widen as you catch the glint of the blades they carry."
    Celeste "W-Wait..."
    Hara "Celeste, please!"
    Hara "We only want to help!"
    Celeste "W-What are you going to do to me?!"
    Hara "We need to let your blood out."
    Hara "It's an old ritual but it should let the demon out."
    Celeste "Stay back!"
    nunB "P-Perhaps we should stop, sisters."
    nunB "If the inquistors ever found out about this ritual..."
    nunA "Be silent sister!"
    nunA "It is the only way!"
    nunA "The child is cursed!"
    show hara at center with move
    show celeste_teen at left with move
    Celeste "STAY BACK!"
    "Now your heart is pounding. Like a cornered animal, you look for somewhere to run."
    #scene atlastyoureachthebottom with flash
    Hara "Celeste, please---"
    Celeste "GET AWAY FROM ME!"
    hide celeste_teen
    hide hara
    hide nunA
    hide nunB
    $ CharSetBattleSkinID(MC_ID, "mc_prologue")
    $StartBattle(BattleData(BackgroundImage="pbat_dungeon", CharIDList_Right=["e_hara", "e_sister1", "e_sister2"], ContinueOnDefeat=True))
    jump after_nunfight
label after_nunfight:
    scene black with fade
    scene heldbynuns
    nunA "By the gods, Sister Hara! Pin her Down! I'll make the cut!"
    "As Sister Hara reaches to grab and pin your arms from behind, you squirm and writhe, screaming for them to let you go."
    Hara "I'm sorry, Celeste! I'm sorry!"
    Hara "Please! It's for your own good!"
    "As the other sister closes in, grabbing one of your struggling arms to place the knife, you feel the surge of darkness swell within."
    "Something raw, something dangerous."
    "Something even you didn't know you could do."
    scene purpleeyes with vpunch
    Celeste "{i}Sister.{/i}"
    "The sister looks up toward you as your eyes glow purple, mana overflowing."
    Celeste "{i}Kill yourself{/i}"
    scene ursulabargesin
    Ursula "WHAT IN THE NAME OF AL'VAZAH IS GOING ON HERE?!"
    "Sister Hara releases you at once as the second sister retreats."
    "Sister Ursula storms over to grab you."
    Ursula "What is this madness?!"
    Ursula "Why have you taken Celeste down here?!"
    Hara "S-She's possessed, Sister Ursula!"
    Hara "You know it! We all do!"
    scene haraontheground
    "Sister Ursula backhands Sister Hara, knocking her to the floor."
    "Sister Ursula reaches down to shake you."
    Ursula "Celeste! CELESTE!"
    Ursula "Are you alright?"
    "You cannot peel your eyes away."
    "At last, Sister Ursula and the others realize what is happening."
    scene nunwithknife
    "The sister you commanded is standing, trembling"
    "Her eyes are wide with panic as, with a shaking hand, she begins to lift the knife."
    Ursula "S-Sister Katherine!"
    Ursula "What are you doing?!"
    "There are gutteral grunts as tears stream down her unblinking eyes"
    "It is as though she is trying to fight back against her own body, but it's hopeless."
    scene nunknifedeath
    "The blade plunges sharply into the side of her neck, and the sisters scream."
    "She pulls the knife out, plunging it in again and again..."
    "With the third strike, she drops lifelessly to the floor in a pool of her own blood as the sisters rush toward her."
    scene nunsarounddeadnun
    "You look at your hands, seeing the splash of blood on them."
    "{i}What... what have you done?{/i}"
    "END OF DEMO"
    $ renpy.full_restart()