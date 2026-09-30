############ Boris - image definitions ############
# Requires CHAR_OFFSET.BORIS; source canvas: 821 x 1408.
############ boris expressions ############
image boris angry   = Composite((821, 1408), CHAR_OFFSET.BORIS, "boris_body", CHAR_OFFSET.BORIS, "images/characters/boris/normal/boris_angry.webp")
image boris happy   = Composite((821, 1408), CHAR_OFFSET.BORIS, "boris_body", CHAR_OFFSET.BORIS, "images/characters/boris/normal/boris_happy.webp")
image boris sad     = Composite((821, 1408), CHAR_OFFSET.BORIS, "boris_body", CHAR_OFFSET.BORIS, "images/characters/boris/normal/boris_sad.webp")
image boris shocked = Composite((821, 1408), CHAR_OFFSET.BORIS, "boris_body", CHAR_OFFSET.BORIS, "images/characters/boris/normal/boris_shoked.webp")
image boris shy     = Composite((821, 1408), CHAR_OFFSET.BORIS, "boris_body", CHAR_OFFSET.BORIS, "images/characters/boris/normal/boris_shy.webp")
############ boris expression aliases ############
image boris shock    = "boris shocked"
image boris shoked   = "boris shocked"
image boris talk     = "boris"
image boris neutral  = "boris"
image boris normal   = "boris"
############ boris body ############
image boris = Composite((821, 1408), CHAR_OFFSET.BORIS, "boris_body")
image boris_body = "images/characters/boris/boris_neutral_face.webp"