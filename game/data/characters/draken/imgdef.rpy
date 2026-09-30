############ Draken - image definitions ############
# Requires CHAR_OFFSET.DRAKEN; source canvas: 1680 x 2640.
init python:
    def doc_draken_aligned_face(image_path):
        return Composite((1680, 2640), (777, 808),
            Transform(Crop((367, 203, 103, 116), image_path), xysize=(146, 165)))
############ draken expressions ############
image draken angry   = Composite((1680, 2640), CHAR_OFFSET.DRAKEN, "draken_body", CHAR_OFFSET.DRAKEN, doc_draken_aligned_face("images/characters/draken/normal/draken_angry.webp"))
image draken blush   = Composite((1680, 2640), CHAR_OFFSET.DRAKEN, "draken_body", CHAR_OFFSET.DRAKEN, doc_draken_aligned_face("images/characters/draken/normal/draken_blushing.webp"))
image draken happy   = Composite((1680, 2640), CHAR_OFFSET.DRAKEN, "draken_body", CHAR_OFFSET.DRAKEN, doc_draken_aligned_face("images/characters/draken/normal/draken_happy.webp"))
image draken sad     = Composite((1680, 2640), CHAR_OFFSET.DRAKEN, "draken_body", CHAR_OFFSET.DRAKEN, doc_draken_aligned_face("images/characters/draken/normal/draken_sad.webp"))
image draken shocked = Composite((1680, 2640), CHAR_OFFSET.DRAKEN, "draken_body", CHAR_OFFSET.DRAKEN, doc_draken_aligned_face("images/characters/draken/normal/draken_shocked.webp"))
############ draken expression aliases ############
image draken blushing = "draken blush"
image draken shock    = "draken shocked"
image draken talk     = "draken"
image draken neutral  = "draken"
image draken normal   = "draken"
############ draken body ############
image draken = Composite((1680, 2640), CHAR_OFFSET.DRAKEN, "draken_body")
image draken_body = ConditionSwitch(
    "worldChars['draken']['clothes'] in ('naked', 'base')", "images/characters/draken/Draken_base.webp",
    "worldChars['draken']['clothes'] in ('hood', 'clothed_hood')", "images/characters/draken/Draken_clothed_hood.webp",
    "True", "images/characters/draken/Draken_clothed.webp",
)
