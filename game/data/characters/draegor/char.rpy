############ Draegor - character definition ############
default DRAEGOR = Character(_("Draegor"), image="draegor")
init python:
    CharDefs["draegor"] = BuildCharTemplate(CharID="draegor",
        name=_("Draegor"),
        portrait="images/characters/draegor/draegor.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["draegor"] = "characters"
    RelText["draegor"] = {}
    RelText["draegor"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.