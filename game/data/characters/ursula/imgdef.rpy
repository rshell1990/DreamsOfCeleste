############ Ursula - image definitions ############
# Requires CHAR_OFFSET.URSULA; source canvas: 1680 x 2640.
############ ursula expressions ############
image ursula angry  = Composite((1680, 2640), CHAR_OFFSET.URSULA, "ursula_body", CHAR_OFFSET.URSULA, "images/characters/ursula/normal/ursula_sister_angry.webp")
image ursula happy  = Composite((1680, 2640), CHAR_OFFSET.URSULA, "ursula_body", CHAR_OFFSET.URSULA, "images/characters/ursula/normal/ursula_sister_happy.webp")
image ursula sad    = Composite((1680, 2640), CHAR_OFFSET.URSULA, "ursula_body", CHAR_OFFSET.URSULA, "images/characters/ursula/normal/ursula_sister_sad.webp")
image ursula scared = Composite((1680, 2640), CHAR_OFFSET.URSULA, "ursula_body", CHAR_OFFSET.URSULA, "images/characters/ursula/normal/ursula_sister_scared.webp")
############ ursula expression aliases ############
image ursula talk     = "ursula"
image ursula neutral  = "ursula"
image ursula normal   = "ursula"
############ ursula body ############
image ursula = Composite((1680, 2640), CHAR_OFFSET.URSULA, "ursula_body")
image ursula_body = "images/characters/ursula/ursula_neutral_face.webp"
