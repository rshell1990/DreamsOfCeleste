############ Harlok - character definition ############
default HARLOK = Character(_("Harlok"), image="harlok")
init python:
    CharDefs["harlok"] = BuildCharTemplate(CharID="harlok",
        name=_("Harlok"),
        portrait="images/characters/harlok/harlok_portrait.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["harlok"] = "characters"
    RelText["harlok"] = {}
    RelText["harlok"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.
    }
