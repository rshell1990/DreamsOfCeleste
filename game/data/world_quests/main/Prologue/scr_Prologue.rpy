define Celine = Character("Celine", image="celine_young")
define Nashar = Character("Nashar", image="nashar")
define Father = Character("Father", image="father")
define Mother = Character("Mother", image="motherwithbaby")

image black = Solid("#000")
image CG_NailedCrow = "images/cgs/crowhammered.png"
image cgAngryFather = "images/cgs/celestedad_angry.png"
image father = "images/characters/father/celeste_father_neutral.png"
image father_angry = "images/characters/father/normal/celeste_father_angry.png"
image celine_young = "images/characters/celeste_young/celeste_10_yrs_neutral_face.png"
image nashar = "images/characters/nashar/celeste_brother_neutral.png"
image nashar angry = "images/characters/nashar/normal/celeste_brother_angry.png"
image celine_young_sad = "images/characters/celeste_young/normal/celeste_10_yrs_sad.png"
image motherwithbaby = "images/characters/mother/celeste_mother_baby_neutral.png"
image childhood_living_room_day = "data/world_locations/novaras/childhood_home/childhood_living_room_day.png"

init python:
    WorldLocation("house_livingroom", _("Childhood Home"), "childhood_living_room_day")

label qst_prologue_primer:
    scene CG_NailedCrow with flash
    $ renpy.pause(0.5)
    scene black with flash
    play sound "audio/cfx/flock_of_crows.ogg"
    Father "Celine!"
    scene CG_NailedCrow with flash
    $ renpy.pause(0.5)
    scene black
    play sound "audio/cfx/flock_of_crows.ogg"
    "Father's hands drag and pull your small, frail body toward the front door as you frantically resist, to no avail."
    scene cgAngryFather
    Father "you've done it now, girl"
    Celine "Let me go!"
    "Your protests fall on deaf ears, yet you still continue to scream and struggle against his grip."
    Celine "I haven't done anything!"
    scene CG_NailedCrow with dissolve
    "...Well, that was a lie, wasn't it?"
    Father "LIAR!"
    scene childhood_living_room_day
    "With a loud thud, he kicks the door open and swings your small body forward."
    "You crash onto the cold, dirty floor, grazing your knee as you try to stand back up."
    show celine_young at left
    "In his hands, Father grips the blood-stained stick --something you were all too familiar with by now."
    show father at right with easeinright
    show father_angry at right
    "It looks like it's going to get a fresh coat of red today."
    play sound "audio/cfx/running_steps.ogg"
    show nashar at right with slideright
    "As he raises his hand to strike you, there's a rush of feet behind you as your brother moves forward, wrestling the stick from Father's hardened hands."
    Father "GET OFF ME, BOY!"
    Nashar "FATHER, STOP!"
    "He stands as a barrier between you and your father's wrath, managing to knock the stick away as it thuds and rolls across the floor."
    show nashar angry at center
    Nashar "What in the hells is going on?"
    Father "Again, I caught her torturing animals!"
    menu celinelieortruth:
        "He's lying I didn't do anything":
            Father "Calling your own father a liar? You shameless little cunt!"
            jump celineintro_result
        "I was only putting it out of it's misery!":
            Father "BY NAILING IT'S WINGS TO A TREE?"
            Father "I don't know what devil's possessed you, girl, but I swear I'll beat it out of you!"
            jump celineintro_result
        "If the bird didn't want to die, it should've fought back harder!":
            Father "...By the gods, girl."
            Father "What the fuck is wrong with you?"
            jump celineintro_result

label celineintro_result:
    "Father raises his hand to strike you once more, as he had done countless times before."
    "Before the blow can connect, your older brother intercedes on your behalf, wrestling him down before he can strike."
    Nashar "Father, No!"
    Father "WHAT THE HELL IS WRONG WITH YOU, BOY?"
    Father "The girl needs a beating! It's the only way!"
    Nashar "She's sick! She needs help!"
    Father "The girl's possessed by demons!"
    Nashar "We brought her to a mage of Palam, and you know that's not true!"
    Nashar "It's her mind, it's this place, it's..."
    "He gestures widely."
    Nashar "Fucking all of this!"
    Father "You watch your tongue, boy!"
    Father "I won't spare you the rod either"
    Nashar "I'll get her help. There are people in Novaras"
    Nashar "High mages and men of science who can help her!"
    Father "With what coin, boy?"
    Father "I should just take her to the inquisitors and be done with it!"
    Nashar "They'll brand her the work of dark magecraft and KILL HER!"
    "Father scowls as he always does, cheeks flushed red from the half-empty bottle of mead."
    Father "And maybe we'd all be better for it!"
    "Your brother is furious, his teeth gnashing together as he moves closer toward your father."
    show nashar at cright with slideright
    "A familiar, common sight in the Gwenovair household."
    "Behind you, you hear the soft wailing of Maize, your baby sister."
    show celine_young at center with dissolve
    "In a moment your mother appears, Maize in her arms as she scowls at all of you."
    show motherwithbaby at left with easeinleft
    Mother "What in the seven hells is going on in here?"
    Father "Ask the boy. He's the one who keeps trying to stop me from doing what needs to be done."
    Nashar "You've beaten her a hundred times before, and it hasn't fixed a damn thing!"
    Father "Bah! Enough of this, I'm heading to the damn tavern!"
    hide father_angry
    hide father with moveoutright
    Mother "Dear!"
    Mother "DEAR!"
    show celine_young at left with dissolve
    show motherwithbaby at center with dissolve
    Mother "Now look what you've both done!"
    Mother "He won't be back for hours now! Who's gonna finish the field?"
    Celine "Father is always too drunk for it any--"
    show motherwithbaby at left
    show motherwithbaby at center
    show motherwithbaby at left
    play sound "audio/cfx/slap.ogg"
    "You feel the sting of a slap across your cheek."
    hide celine_young
    show celine_young_sad
    Mother "Why can't you just be normal, Celine?"
    Mother "WHY MUST YOU MAKE EVERYTHING SO DIFFICULT?"
    hide motherwithbaby with slideleft
    hide celine_young_sad
    show celine_young
    "With your baby sister still wailing in her arms, your mother storms off."
    play sound "audio/cfx/running_steps.ogg"
    Celine "..."
    Nashar "..What happened, Celine?"
    Celine "Nothing"
    Nashar "Celine..."
    Celine "I don't know."
    Nashar "... More dark thoughts?"
    Celine "...Yes."
    Celine "...I can't help it. It's like... this pressure builds inside of me."
    Celine "It doesn't stop till I do bad things"
    Nashar "Celine..."
    Nashar "You're not well, Celine"
    Nashar "We've talked about this before."
    Nashar "You can't... act on those feelings, understand?"
    Celine "I'm trying... {i}I don't want to let you down.{/i}"
    "He pulls you into a hug."
    Nashar "I know... I know you're trying."
    Nashar "Listen, there's something I need to talk with you about later."
    Nashar "I need your help with some chores, alright?"
    Celine "What do you need me to do?"
    Nashar "I'm going to need some help tending to the field."
    Celine "But-"
    Nashar "You know as well as I do, when he goes off like that to get a drink, we don't see him again until after dark."
    Nashar "You're gonna have to help me a little, Celine. I can't do it all."
    Celine "*Sigh*"
    Celine "Alright."
    Nashar "There's a spare scythe in the barn."
    Nashar "Go get it and meet me in the field."
    Celine "Yes, Nashar"
    $ QstStart(QstPrologue)
    $ LocSet("house_livingroom")

label qst_prologue_nashar:
    nashar "Did you get the scythe, yet?"
    menu nasharfarming:
        "Yes, I got it.":
            if GotScythe:
                $ GoalComplete(0)
                nashar "Alright, let's begin then..."
                "The day slips by as you spend your time toiling in the field with your brother."
                "It is tiring, hot work as the sun beats down on you both."
                "As last, you finally finish."
            jump qst_prologue_nashar
        "Not yet.":
            nashar "Stop fooling around, Celine."
            nashar "Come to me when you have it."
    return

label farming_equipment:
    "You approach the farming equipment."
    menu farming_equipment:
        "Take the scythe.":
            $ GotScythe = True
            "You take the scythe."
            "Now your brother will be waiting for you in the field"
        "Leave it.":
            "You decide to leave the scythe for now."
    return

label qst_prologue_nashar:
    Nashar "*Yawn*"
    Nashar "Alright, Thanks for the help, Celine"
    Nashar "Why don't you go play for a little while?"
    Nashar "Just be back before it gets dark."
    Celine "Alright"
    Celine "(Maybe Boris is free?)"
    Celine "(He's usually over by the lake.)"

label boris_lake:
    show boris center_left
    show celine center_right
    Boris "C-Celine"
    "The chubby boy stammers"
    "Boris is not a friend"
    "More of... an acquaintance who has latched onto you."
    "Fat and with a stutter, he is an easy target for other children to harass."
    "...At least he was, until you slashed one of the boy's eyes with a jagged piece of rock."
    "Another one of your little 'incidents.'"
    "Either way, since then, Boris has followed you around whenever he can."
    "You are fairly sure he might be in love with you."
    "Not that you've ever felt anything like that."
    "Really, you don't feel much for anyone other than Maize and your brother."
    Celine "Caught anything good?"
    Boris "N-Not today."
    Boris "U-Uhh, you maybe want to join me?"
    "You take a seat beside Boris"
    Celine "How's your mother, has she--"
    Boris "She's getting better."
    Boris "But she still hasn't left her bed yet."
    Boris "It's a real pain having to do all the work she normally does!"
    Boris "I don't know how to properly wash clothes!"
    Boris "*Sigh*"
    Celine "Ah... I see."
    Celine "..."
    Boris "..."
    Boris "...Is your mother and father still hitting you?"
    Celine "You know I don't like talking about that."
    Boris "I know..."
    show boris at center
    "In all seriousness, Boris grabs both of your shoulders and forces you to look at him."
    Boris "One day, I'm gonna become the strongest boy in the village."
    Boris "And if your father hits you, I'll knock him out!"
    Celine "... Hahahaha!"
    "You can't help but smile at his endearing need to protect you."
    "He might be an idiot, but..."
    "You lean forward, gently kissing him on the cheek."
    Celine "Thank you, Boris."
    "Boris, now bright as a tomato, stutters out his answer."
    Boris "D-D-Don't distract me too much!"
    Boris "I g-gotta focus on the fish!"
    Celine "Right..."
    "Time drifts by until, at last, it's time for you to go home."
    advance time to evening
    Celine "I'd best be heading back now, Boris."
    Boris "S-So soon?"
    Boris "Umm..."
    Boris "Can we play together tomorrow?"
    Celine "Sure, Boris"
    Celine "I'll meet you here tomorrow after I'm done with my chores."
    Boris "A-Alright..."

label return_home:
    show mother at centerleft
    show father at right
    Mother "I CAN SMELL HER ON YOU!"
    Mother "I CAN SMELL THAT FUCKING WHORE!"
    Father "Have you gone mad, woman?!"
    "Your mother hurls a saucepan at your father, barely missing him as it slams against the wall with a crash."
    sound "sfx/saucepan_crash.ogg"
    father to centerleft with slideleft
    hide mother
    hide father
    "Angerly, he storms toward your mother, who keeps hitting and beating at him as he drags her by the hair into the bedroom, slamming the door shut."
    sound "sfx/door_slam.ogg"
    sound "sfx/belt_whip.ogg"
    sound "sfx/woman_screaming.ogg"
    "You hear screaming, then the familiar *THUD* *THUD* *THUD* as your father beats her with his belt."
    sound "sfx/belt_whip.ogg"
    sound "sfx/woman_screaming.ogg"
    sound "sfx/belt_whip.ogg"
    sound "sfx/woman_screaming.ogg"
    sound "sfx/belt_whip.ogg"
    sound "sfx/woman_screaming.ogg"
    "Neither of them even acknowledge you've returned home."
    show celine_young at left
    "Why would they?"
    "After all..."
    "{i}You were used to this by now.{/i}"
    show nashar at right with slidein
    Nashar "Celine, what was that--"
    sound "sfx/belt_whip.ogg"
    sound "sfx/woman_screaming.ogg"
    sound "sfx/belt_whip.ogg"
    sound "sfx/woman_screaming.ogg"
    Celine "Father and Mother are fighting again."
    "A horrified Nashar looks up toward their bedroom door, then at your completely disinterested face."
    Nashar "Come with me a second."
    "He reaches down to take your hand, pulling you into his room, where Maize is peacefully resting in a crib."
    hide celine_young
    hide nashar
    $LocSet("childhood_attic_room_night")
    "Down on his knees, Nashar meets you at eye level."
    show nashar at centerright with slidein
    show celine_young at centerleft with slidein
    Nashar "I need you to listen to me, and not to panic, okay?"
    Nashar "But you don't have to face it alone."
    Nashar "...I'm joining a real big adventure party soon."
    show celine_young_worried at centerleft
    Celine "You... you got into The Silver Dawn?"
    Nashar "Ha... Can you believe it?"
    Nashar "The greatest adventure party around, and I'm going to be in it!"
    Celine "... Please don't leave me alone."
    Celine "I don't have anyone else."
    Nashar "...I promise you, Celine."
    Nashar "I'm gonna get you and your sister out of here."
    Nashar "I need to make enough coin."
    Nashar "I should have enough in a year, maybe even a little less."
    Celine "...A whole year?"
    Celine "Without you?"
    Nashar "I know it seems like a long time."
    Nashar "But I'll be back before you know it."
    Celine "Why not sooner? Aren't they famous adventurers?"
    "Your brother's face strains slightly."
    Nashar "They are..."
    Nashar "But they're taking me under their wing as an apprentice."
    Nashar "I won't earn as much as I should for a while."
    Celine "That's not fair..."
    Nashar "It's not always about what's fair, Celine."
    "The thought of being separated from your brother for such a long time makes you anxious."
    "It was always us versus them."
    "You and your big brother."
    "Against the monsters of the world."
    "Against the bullies and the bandits."
    "Against your parents."
    "Now, with him gone, it would just be {i}you{/i} versus those things."
    "And {i}you{/i} versus them is a much terrifying thought."
    Celine "Please..."
    Celine "Let me come; I'll look after Maize and--"
    Nashar "I'm sorry, Celine."
    Nashar "The adventurers' guild is no place for children."
    Celine "Please."
    Nashar "Celine--"
    Celine "I don't want to be alone."
    Celine "...I don't know if I'll be okay without you."
    "Your brother sighs, gently resting his hand on your head to stroke your hair softly."
    Nashar "...One day, Celine."
    Nashar "You won't need me anymore."
    Celine "That's not true. I'll always need you."
    "Your brother smiles and shakes his head."
    Nashar "You have an incredible gift, Celine."
    Nashar "Magecraft unlike anything I've ever seen in someone so young."
    "His hands reach down to grab your small shoulders."
    Nashar "{i} I know that one day, you'll be the greatest adventurer who ever lived.{/i}"
    Celine "...I don't wanna be the greatest adventurer."
    Celine "I just want you to stay with me."
    "Your brother's soft smile fades as he rises from his knees."
    Nashar "When I return, Celine, I'll never leave your side again."
    Nashar "But until then, I'm going to need you to look after Maize, understand?"
    Nashar "She's going to need her big sister to keep her safe while I'm gone."
    "You want to protest more, but you know it won't do any good."
    "You nod, your face a little puffy as you try to hold back the tears."
    Celine "When will you be leaving?"
    Nashar "Tomorrow."
    "Your heart sinks."
    Celine "So soon?"
    Nashar "I'm sorry, Celine."
    Nashar "They're passing through tomorrow --- I have to go now or I'll miss my chance."
    Nashar "I promise I'll write home."
    Celine "..."
    Nashar "I have to finish packing up."
    Nashar "We can talk more later."
    hide nashar with fade
    "You watch as your brother heads toward his quarters."
    "The though of leaving you and your little sister alone no doubt pains him."
    scene black with fade
    "But as much as it pains him, its {i}you{/i} who is going to have to live without the only shield in your life..."
    "And so the rest of of the day limps on as your parents scream at each other throughout the night."
    scene black with fade
