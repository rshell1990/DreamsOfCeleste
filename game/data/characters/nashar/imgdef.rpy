############ Nashar - image definitions ############
# Requires CHAR_OFFSET.NASHAR; source canvas: 821 x 1408.
image nashar angry   = Composite((821, 1408), CHAR_OFFSET.NASHAR, "nashar_body", CHAR_OFFSET.NASHAR, ConditionSwitch("worldChars['nashar']['clothes'] in ('corpse_1', 'corpse_2')", Null(), "True", "images/characters/nashar/normal/celine_brother_angry.webp"))
image nashar blush   = Composite((821, 1408), CHAR_OFFSET.NASHAR, "nashar_body", CHAR_OFFSET.NASHAR, ConditionSwitch("worldChars['nashar']['clothes'] in ('corpse_1', 'corpse_2')", Null(), "True", "images/characters/nashar/normal/celine_brother_blushing.webp"))
image nashar happy   = Composite((821, 1408), CHAR_OFFSET.NASHAR, "nashar_body", CHAR_OFFSET.NASHAR, ConditionSwitch("worldChars['nashar']['clothes'] in ('corpse_1', 'corpse_2')", Null(), "True", "images/characters/nashar/normal/celine_brother_happy.webp"))
image nashar sad     = Composite((821, 1408), CHAR_OFFSET.NASHAR, "nashar_body", CHAR_OFFSET.NASHAR, ConditionSwitch("worldChars['nashar']['clothes'] in ('corpse_1', 'corpse_2')", Null(), "True", "images/characters/nashar/normal/celine_brother_sad.webp"))
image nashar shocked = Composite((821, 1408), CHAR_OFFSET.NASHAR, "nashar_body", CHAR_OFFSET.NASHAR, ConditionSwitch("worldChars['nashar']['clothes'] in ('corpse_1', 'corpse_2')", Null(), "True", "images/characters/nashar/normal/celine_brother_shoked.webp"))
############ nashar expression aliases ############
image nashar blushing = "nashar blush"
image nashar shock    = "nashar shocked"
image nashar shoked   = "nashar shocked"
image nashar talk     = "nashar"
image nashar neutral  = "nashar"
image nashar normal   = "nashar"
############ nashar body ############
image nashar = Composite((821, 1408), CHAR_OFFSET.NASHAR, "nashar_body")
image nashar_body = ConditionSwitch(
    "worldChars['nashar']['clothes'] == 'corpse_1'", "images/characters/nashar/celine_brother_corpse_1.webp",
    "worldChars['nashar']['clothes'] == 'corpse_2'", "images/characters/nashar/celine_brother_corpse_2.webp",
    "True", "images/characters/nashar/celine_brother_neutral.webp",
)
