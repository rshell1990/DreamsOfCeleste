############ Mother - image definitions ############
# Requires CHAR_OFFSET.MOTHER; source canvas: 821 x 1408.
############ mother expressions ############
image mother angry  = Composite((821, 1408), CHAR_OFFSET.MOTHER, "mother_body", CHAR_OFFSET.MOTHER, ConditionSwitch("worldChars['mother']['clothes'] == 'black_eye'", "images/characters/mother/black_eye/celine_mother_angry_black_eye.webp", "True", "images/characters/mother/normal/celine_mother_angry.webp"))
image mother crying = Composite((821, 1408), CHAR_OFFSET.MOTHER, "mother_body", CHAR_OFFSET.MOTHER, ConditionSwitch("worldChars['mother']['clothes'] == 'black_eye'", "images/characters/mother/black_eye/celine_mother_crying_black_eye.webp", "True", "images/characters/mother/normal/celine_mother_crying.webp"))
image mother happy  = Composite((821, 1408), CHAR_OFFSET.MOTHER, "mother_body", CHAR_OFFSET.MOTHER, ConditionSwitch("worldChars['mother']['clothes'] == 'black_eye'", "images/characters/mother/black_eye/celine_mother_happy_black_eye.webp", "True", "images/characters/mother/normal/celine_mother_happy.webp"))
image mother sad    = Composite((821, 1408), CHAR_OFFSET.MOTHER, "mother_body", CHAR_OFFSET.MOTHER, ConditionSwitch("worldChars['mother']['clothes'] == 'black_eye'", "images/characters/mother/black_eye/celine_mother_sad_black_eye.webp", "True", "images/characters/mother/normal/celine_mother_sad_.webp"))
image mother scared = Composite((821, 1408), CHAR_OFFSET.MOTHER, "mother_body", CHAR_OFFSET.MOTHER, ConditionSwitch("worldChars['mother']['clothes'] == 'black_eye'", "images/characters/mother/black_eye/celine_mother_scared_black_eye.webp", "True", "images/characters/mother/normal/celine_mother_scared.webp"))
############ mother expression aliases ############
image mother cry      = "mother crying"
image mother talk     = "mother"
image mother neutral  = "mother"
image mother normal   = "mother"
############ mother body ############
image mother = Composite((821, 1408), CHAR_OFFSET.MOTHER, "mother_body")
image mother_body = ConditionSwitch(
    "worldChars['mother']['clothes'] == 'baby'", "images/characters/mother/celine_mother_baby_neutral.webp",
    "worldChars['mother']['clothes'] == 'black_eye'", "images/characters/mother/celine_mother_neutral_black_eye.webp",
    "True", "images/characters/mother/celine_mother_neutral.webp",
)