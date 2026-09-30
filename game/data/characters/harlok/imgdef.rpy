############ Draegor - image definitions ############
# Requires CHAR_OFFSET.DRAEGOR; source canvas: 821 x 1408.
############ draegor expressions ############
image draegor angry   = Composite((821, 1408), CHAR_OFFSET.DRAEGOR, "draegor_body", CHAR_OFFSET.DRAEGOR, "images/characters/draegor/normal/angry.webp")
image draegor happy   = Composite((821, 1408), CHAR_OFFSET.DRAEGOR, "draegor_body", CHAR_OFFSET.DRAEGOR, "images/characters/draegor/normal/happy.webp")
image draegor lewd    = Composite((821, 1408), CHAR_OFFSET.DRAEGOR, "draegor_body", CHAR_OFFSET.DRAEGOR, "images/characters/draegor/normal/lewd.webp")
image draegor sad     = Composite((821, 1408), CHAR_OFFSET.DRAEGOR, "draegor_body", CHAR_OFFSET.DRAEGOR, "images/characters/draegor/normal/sad.webp")
image draegor shocked = Composite((821, 1408), CHAR_OFFSET.DRAEGOR, "draegor_body", CHAR_OFFSET.DRAEGOR, "images/characters/draegor/normal/shoked.webp")
############ draegor expression aliases ############
image draegor shock    = "draegor shocked"
image draegor shoked   = "draegor shocked"
image draegor talk     = "draegor"
image draegor neutral  = "draegor"
image draegor normal   = "draegor"
############ draegor body ############
image draegor = Composite((821, 1408), CHAR_OFFSET.DRAEGOR, "draegor_body")
image draegor_body = "images/characters/draegor/draegor.webp"