############ Boris - character definition ############
default BORIS = Character(_("Boris"), image="boris")
init python:
    CharDefs["boris"] = BuildCharTemplate(CharID="boris",
        name=_("Boris"),
        portrait="images/characters/boris/boris_neutral_face.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["boris"] = "characters"
    RelText["boris"] = {}
    RelText["boris"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.
    }
