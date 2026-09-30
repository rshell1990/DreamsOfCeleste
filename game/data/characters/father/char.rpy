############ Father - character definition ############
default FATHER = Character(_("Father"), image="father")
init python:
    CharDefs["father"] = BuildCharTemplate(CharID="father",
        name=_("Father"),
        # Temporary full-body portrait reference; replace when the portrait is supplied.
        portrait="images/characters/father/celine_father_neutral.webp",
        # BattleSkin and combat stats are deliberately not assigned here.
        RelTextIDs={"initial"},
        # Visual variants: normal.
        ExtraData={"clothes": "normal"})
    config.tag_layer["father"] = "characters"
    RelText["father"] = {}
    RelText["father"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.
    }
