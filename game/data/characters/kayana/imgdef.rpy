############ Kayana - image definitions ############
# Requires CHAR_OFFSET.KAYANA; source canvas: 1680 x 2640.
############ kayana expressions ############
image kayana angry  = Composite((1680, 2640), CHAR_OFFSET.KAYANA, "kayana_body", CHAR_OFFSET.KAYANA, "images/characters/kayana/kayana_sylvaris_angry.webp")
image kayana blush  = Composite((1680, 2640), CHAR_OFFSET.KAYANA, "kayana_body", CHAR_OFFSET.KAYANA, "images/characters/kayana/kayana_sylvaris_blushing.webp")
image kayana happy  = Composite((1680, 2640), CHAR_OFFSET.KAYANA, "kayana_body", CHAR_OFFSET.KAYANA, "images/characters/kayana/kayana_sylvaris_happy.webp")
image kayana lewd   = Composite((1680, 2640), CHAR_OFFSET.KAYANA, "kayana_body", CHAR_OFFSET.KAYANA, "images/characters/kayana/kayana_sylvaris_lewd.webp")
image kayana sad    = Composite((1680, 2640), CHAR_OFFSET.KAYANA, "kayana_body", CHAR_OFFSET.KAYANA, "images/characters/kayana/kayana_sylvaris_sad.webp")
image kayana scared = Composite((1680, 2640), CHAR_OFFSET.KAYANA, "kayana_body", CHAR_OFFSET.KAYANA, "images/characters/kayana/kayana_sylvaris_scared.webp")
############ kayana expression aliases ############
image kayana blushing = "kayana blush"
image kayana talk     = "kayana"
image kayana neutral  = "kayana"
image kayana normal   = "kayana"
############ kayana body ############
image kayana = Composite((1680, 2640), CHAR_OFFSET.KAYANA, "kayana_body")
image kayana_body = ConditionSwitch(
    "worldChars['kayana']['clothes'] in ('naked', 'base')", "images/characters/kayana/kayana_sylvaris_base.webp",
    "True", "images/characters/kayana/kayana_sylvaris_clothed.webp",
)
