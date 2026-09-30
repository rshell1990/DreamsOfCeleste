############ Ursula - character definition ############
default URSULA = Character(_("Ursula"), image="ursula")
init python:
    CharDefs["ursula"] = BuildCharTemplate(CharID="ursula",
        name=_("Ursula"),
        portrait="images/characters/ursula/ursula_neutral_face.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["ursula"] = "characters"
    RelText["ursula"] = {}
    RelText["ursula"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.
    }
