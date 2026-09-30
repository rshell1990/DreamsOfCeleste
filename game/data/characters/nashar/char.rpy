############ Nashar - character definition ############
default NASHAR = Character(_("Nashar"), image="nashar")
init python:
    CharDefs["nashar"] = BuildCharTemplate(CharID="nashar",
        name=_("Nashar"),
        portrait="images/characters/nashar/celine_brother_neutral.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["nashar"] = "characters"
    RelText["nashar"] = {}
    RelText["nashar"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.
    }