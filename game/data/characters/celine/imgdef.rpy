############# celine expressions #############
image celine angry = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/angry.webp")
image celine blush = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/blush.webp")
image celine happy = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/happy.webp")
image celine laugh = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/laugh.webp")
image celine lewd  = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/lewd.webp")
image celine sad   = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/sad.webp")
image celine think = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/think.webp")
############# celine psycho expressions #######
image celine p_fury    = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/p_fury.webp")
image celine p_laugh   = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/p_laugh.webp")
image celine p_laugh2  = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/p_laugh2.webp")
image celine p_laugh3  = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/p_laugh3.webp")
image celine p_lewd    = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/p_lewd.webp")
image celine p_sad    = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body", CHAR_OFFSET.CELINE, "images/characters/celine/face/p_sad.webp")
image celine talk = "celine"
################################################
image celine = Composite((1118, 1270), CHAR_OFFSET.CELINE, "celine_body")
image celine_body = ConditionSwitch(
    "worldChars['celine']['clothes'] == 'sword'", "images/characters/celine/sword.webp",
    "worldChars['celine']['clothes'] == 'naked'", "images/characters/celine/naked.webp",
    "True", "images/characters/celine/normal.webp",
)



