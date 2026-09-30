############ Mother - character definition ############
default MOTHER = Character(_("Mother"), image="mother")
init python:
    CharDefs["mother"] = BuildCharTemplate(CharID="mother",
        name=_("Mother"),
        portrait="images/characters/mother/celine_mother_neutral.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["mother"] = "characters"
    RelText["mother"] = {}
    RelText["mother"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.