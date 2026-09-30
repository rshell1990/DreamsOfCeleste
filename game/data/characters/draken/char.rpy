############ Draken - character definition ############
default DRAKEN = Character(_("Draken"), image="draken")
init python:
    CharDefs["draken"] = BuildCharTemplate(CharID="draken",
        name=_("Draken"),
        portrait="images/characters/draken/Draken_clothed.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["draken"] = "characters"
    RelText["draken"] = {}
    RelText["draken"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.
    }