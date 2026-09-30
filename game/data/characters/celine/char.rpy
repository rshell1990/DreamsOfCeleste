default CELINE = Character(_("Celine"), image = "celine")
init python:
    CharDefs["celine"] = BuildCharTemplate(CharID = "celine",
        name = _("Celine"),
        portrait = "images/characters/celeste/portrait.webp",
        BattleSkin = "mc_prologue",
        RelTextIDs = {"initial"},
        ExtraData = {"clothes":"normal"})
    
    config.tag_layer["celine"] = "characters"
    config.tag_layer["cg_celine_return_party"] = "characters"
    config.tag_layer["cg_celine_return_kid"] = "characters"

    RelText["celine"] = {}
    RelText["celine"]["initial"] = {
        "order":0,
        "text":_("A living legend. Not since the death of Newheart has a hero with such potential and hope swept across Novaras. Her powerful abilities are only matched by her beauty.")}