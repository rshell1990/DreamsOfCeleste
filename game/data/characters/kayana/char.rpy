############ Kayana - character definition ############
default KAYANA = Character(_("Kayana"), image="kayana")
init python:
    CharDefs["kayana"] = BuildCharTemplate(CharID="kayana",
        name=_("Kayana"),
        portrait="images/characters/kayana/kayana_sylvaris_clothed.webp",
        RelTextIDs={"initial"},
        ExtraData={"clothes": "normal"})
    config.tag_layer["kayana"] = "characters"
    RelText["kayana"] = {}
    RelText["kayana"]["initial"] = {
        "order": 0,
        "text": _(""),  # TODO: Add the authored character description.
    }