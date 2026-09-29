define Celine = Character("Celine", image="celine_young")
define Nashar = Character("Nashar", image="nashar")
define Father = Character("Father", image="father")
define Mother = Character("Mother", image="motherwithbaby")
define Boris = Character("Boris", image="boris")
define fatherandbrotherfight = "images/cgs/Brothervsfather.png"
define brothersisterhug = "images/cgs/Brother_And_Celeste.png"

image black = Solid("#000")
image CG_NailedCrow = "images/cgs/crowhammered.png"
image cgAngryFather = "images/cgs/celestedad_angry.png"
image father = "images/characters/father/celeste_father_neutral.png"
image father_angry = "images/characters/father/normal/celeste_father_angry.png"
image celine_young = "images/characters/celeste_young/celeste_10_yrs_neutral_face.png"
image celine_young_crying = "images/characters/celeste_young/normal/celeste_10_yrs_crying.png"
image nashar = "images/characters/nashar/celeste_brother_neutral.png"
image nashar angry = "images/characters/nashar/normal/celeste_brother_angry.png"
image celine_young_sad = "images/characters/celeste_young/normal/celeste_10_yrs_sad.png"
image motherwithbaby = "images/characters/mother/celeste_mother_baby_neutral.png"
image boris = "images/characters/boris/celeste_boris_neutral.png"
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
    hide celine_young
    hide father
    hide nashar
    "As he raises his hand to strike you, there's a rush of feet behind you as your brother moves forward, wrestling the stick from Father's hardened hands."
    show fatherandbrotherfight with dissolve
    Father "GET OFF ME, BOY!"
    Nashar "FATHER, STOP!"
    "He stands as a barrier between you and your father's wrath, managing to knock the stick away as it thuds and rolls across the floor."
    show father_angry at right
    show nashar angry at center
    show celine_young at left
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
    hide celine_young
    hide nashar
    show brothersisterhug with dissolve
    show celine_young at left with dissolve
    show nashar at center with dissolve
    
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
    Nashar "Did you get the scythe, yet?"
    menu nasharfarming:
        "Yes, I got it.":
            if GotScythe:
                $ GoalComplete(0)
                Nashar "Alright, let's begin then..."
                "The day slips by as you spend your time toiling in the field with your brother."
                "It is tiring, hot work as the sun beats down on you both."
                "As last, you finally finish."
            jump qst_prologue_nashar
        "Not yet.":
            Nashar "Stop fooling around, Celine."
            Nashar "Come to me when you have it."
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
    show celine_young_crying at centerleft
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
    scene childhood_attic_room_night
    "Your brother reads you a bedtime story as he promised all the wonderful things he was going to do for you and Maize when he returned."
    "the great home just the three of you would live in."
    "Never going hungry again because someone was too drunk or angry to do the cooking."
    "And no more beatings anymore."
    "It all feels, strangely, like a dream within a dream."
jump to label the_next_day
label the_next_day:
    scene bg_TheNextDay with fade
    scene childhood_attic_room_day
    "The ornate stagecoach arrives outside, a small convoy of wagons covered in cloth following behind as the rain hammers down."
    "Even Father, already drunk, notices and snaps for your mother's attention."
    show father centerleft
    show mother left
    show celine_young at right
    Father "She's here! Get the boy!"
    Mother "I thought she wouldn't arrive until after dark?"
    Father "Well, she's here now, so hurry."
    "Your mother sighs as she scurries off to go find your brother."
    hide mother slidesoutleft with fade
    "The doors of the stagecoach open, and a figure inside, obscured by the rain, heads toward the door."
    "Your father's eyes glare down accusatorily at you."
    Father "Don't do anything stupid now, girl."
    Father "This is an important moment for this family."
    Father "Your brother's going to earn us a lot of coin."
    "You hate him."
    "You hate your father so much."
    sound "knock.ogg"
    "Your father moves forward to answer the door."
    sound "door.ogg"
    "The door swings open, creaking on its hinges, and {i}she{/i} enters slowly as your father takes a few nervous steps back."
    Father "W-welcome, Ms. Kayanna!"
    Father "You honor our home with your presence!"
    "You stare curiously at the beautiful, but cold creature now standing in your living room."
    "She radiates a naked, unseen magecraft -- overwelming to those who can percieve it."
    "Her clothes are unlike anything you've ever seen."
    "Do all rich adventurers dress like this?"
    "She carries herself less like an adventurer ready to brave the wilds and more like a nobel towering over the lives of everyone beneath her."
    "She looks slowly from left to right around the room."
    "As her daggerlike eyes fall on you, the two of you hold each other's gaze for a moment before she smiles softly."
    "Her voice is soft, yet eerie in it's command."
    Kayanna "you must be the sister."
    Celine "... Hello."
    Kayanna "And your brother is where?"
    Father "T-The boys is just gathering up the last of his things."
    "Her eyes flicker toward your father for the briefest moment, but she says nothing."
    slide right Kayana to rightcenter
    "Instead, the woman kneels to meet you at eye level; her gaze seems to scan you over."
    Kayanna "Such magecraft potential in you."
    Kayanna "Celine, isn't it?"
    Kayanna "I've heard so much about you from your brother already."
    Celine "... Will you bring my brother back to me?"
    "The woman blinks, tilts her head, and the smile widens slightly."
    "She raises one talon-like finger and gently prods your nose with it."
    Kayanna "{i}I promise to give him back when I'm done.{/i}"
    show celeste_mother_angry_black_eye at centerleft
    show nasar at left
    "Your brother enters the room, huffing, and puffing as he forces an awkward smile."
    Nashar "S-Sorry for making you wait, Ms. Kayanna!"
    "The woman rises back to her feet."
    Kayanna "Not at all. Are you ready?"
    Nashar "Yes, all packed."
    Kayanna "Good. Load your bags onto one of the supply wagons."
    "Your brother nods and hurries past your silent father and mother. He turns, looks back toward you, and smiles."
    Nashar "Look after yourself, Celine"
    Nashar "I'll be home before you know it!"
    "You don't answer your brother."
    "You want to tell him that you love him, but instead you simily stare and watch as he leaves out the door."
    hide nashar
    Mother "... H-He will be alright, won't he?"
    Kayanna "Of course."
    "From the open door, you see the other members of the Silver Dawn lingering outside."
    "One of them helps take your brother's bags, loading them onto a wagon."
    Kayanna "Most of his time will be acting as support."
    Kayanna "He probably won't see much, if any, actual fighting."
    Mother "O-Oh..."
    Mother "Thank the gods."
    "For a moment, your parents share a tender smile with each other."
    "You hated them."
    "But at least they loved your brother."
    "And that made you hate them slightly less."
    Kayanna "And as for {i}you{/i}, young lady."
    Kayanna "{i}I look forward to meeting you again, Celine.{/i}"
    "The woman leaves, and you realize the hairs on your arms have been pricked this whole time."
    hide kayanna
    "There was something about her."
    "Birds of a father, or something your brother once said."
    "{i}Why did you feel like you were looking into a mirror?{/i}"
    hide celine_young slideleft
    show father left slideleft
    "You give chase. Your father reaches out to stop you, but its too late."
    Father "CELINE!"
    scene chasingafteryourbrother
    "The heavy rain pours down as, poorly dressed and barefoot, you run into the soaking mud."
    "The trail of wagons is already far ahead, but you try to run after them anyway."
    "You didn't want him to go."
    "Something terrible inside you knew he wouldn't come back."
    "You trip, falling into the mud as you look up."
    "From the farthest wagon at the back, your brother sees you, waving and smiling one last time before he vanishes from view behind the downpour."
    Celine "COME BACK!"
    Celine "DON'T GO!"
    Celine "Please...!"
    "Please don't go."
    scene black with fade
    "The rain continues to pour, but you are left alone in the darkness, your heart aching for your brother."
    scene sixmonthslatertext with fade
    scene buryingbrother
    "...Kayanna promised you she would return him when she was done."
    "And she did deliver---Your brother came home."
    "{i}... Too bad it was in a box.{/i}"
    "Your mother wails as your father tries to comfort her."
    "Few are gathered for the funeral; friends of your brother you have only a passing recollection of."
    "That pretty girl with the freckles and crooked nose wails louder then the others."
    "Inside, you feel empty."
    "But you don't cry."
    "The mage speaks about your brother's passing."
    "He tells a noble story of your brother's journey with the Silver Dawn."
    "One filled with adventure and hope, ended only in tragedy."
    "How, whilst scaling the snowy mountains of the far north, he managed to push one of the Silver Dawn to safety as an avalanche swept him away."
    "It's a wonderful, if sad, story."
    "...You fucking hate it."
    "You look down toward Maize, crying in your arms."
    Celine "{i}Looks like it's just me and you now, Maize.{/i}"
    scene black with fade
    jump label after_funeral
label after_funeral:
    scene childhood_attic_room_night
    "As the funeral comes to an end, your home is visited by a strange man later that evening."
    "Dismissed to your room, you watch from the crack in your door."
    show knight at left
    show mother at right
    show father at rightcenter
    Knight "The Silver Dawn sends its condolences for your son."
    Mother "Oh gods..."
    Knight "They hope that their generous contributions toward the funeral costs have helped ease this difficult time for you both."
    Mother "Y-Yes, the coin has helped, thank you."
    "Your father takes a step forward, drunk and angry as usual; he shoves your mother aside."
    Father "Why have I had inquistors sniffing around?"
    Father "They're askin' me a lot of bloody questions about my boy and what happened for something that was supposedly an accident!"
    Knight "Of course."
    Knight "The inquisition is just doing it's job with matters such as these."
    Knight "{i}...Though they are very...{/i}"
    Knight "Overzealous in their zeal."
    Father "Over what?"
    Father "I don't know what that means, but some of the things my boy was writing in his letters home..."
    Father "{i}I don't know... but he didn't sound right..."
    Father "So what in the hells are you and your lot hiding?"
    Knight "Sir... {i}No one's hiding anything.{/i}"
    Knight "Your son was simply struggling in the end; the life of an adventurer is difficult."
    Knight "Most people don't come back the same."
    show father_sad at rightcenter
    Father "...But my boy isn't coming back, is he?"
    Father "He's buried in that fucking box out there!"
    Knight "I can't bring back your son."
    Knight "{i}But the Silver Dawn wants to help{/i}"
    Knight "They treasured your boy deeply in the end, I assure you---everyone is devastated by his loss."
    Mother "Help us?"
    Mother "How?"
    Knight "The inquisitors... they see dark magecraft everywhere they look, even where there is none."
    Knight "Unfortunately, inquisition investigations can last months upon months, with endless interrogations and paperwork."
    Knight "It's all very stressful, I assure you."
    Knight "...The Silver Dawn would very much like to avoid dragging out any kind of investigation."
    Knight "They simply don't want to waste your time or their own over a tragic accident."
    Father "What does the Silver Dawn want?"
    Knight "All you need to do is sign these documents and hand over any letters your son wrote to you."
    Mother "Documents?"
    Knight "Just as signature will do. I have some ink and a feather if needed."
    Father "What the hells are we signing?"
    Knight "Just a simple document that states you both firmly believe the events to be an accident."
    Knight "{i}...And that your son unfortunately suffered bouts of melancholy, leading him to sometimes act erractically."
    Mother "Melancholy? My son never---"
    "The Knight places a large back of coins onto the table."
    Mother "..."
    Father "..."
    Knight "There's a lot more I can give as well."
    Father "...How much?"
    Knight "Fifty thousand coins."
    "Your parents look at each other as they hear the astronomical figure."
    "They would perhaps earn that much between themselves in ten years or longer."
    "If it was life-changing money."
    Knight "So... do we have a deal?"
    "Your parents share another look; your mother reluctantly nods as your father nods toward the man."
    Father "...Aye, we do."
    scene flicks in and out red
    "Your blood boils."
    "How... how could they do this?"
    "How could they betray your brother like this?"
    "You want to run out and scream at them."
    Knight "Good, then sign here."
    "As he slides the papers across the table, your parents sign the sheets."
    "The Knight inspects the signatures."
    "Satified, he nods."
    Knight "Good."
    Knight "And the letters?"
    father slidesleft to centerleft
    father slidesright to centerright
    "Your father hands them over silently."
    Knight "Spend the coins wisely."
    "The Knight turns to leave, pausing briefly to add;"
    Knight "Oh... and make sure to keep everything said tonight just between us, am I clear?"
    "Your parents don't say anything, and he takes their silence as agreement."
    hide knight
    "Without another word, the Knight leaves, and your parents embrace."
    "{i}You want to kill them all.{/i}"
    "Your blood is simmering hot, but as you move to push open the door---to {i}punish{/i} your parents for betraying you and your brother---you hear the soft crying of Maize behind you."
    scene black
    scene childhood_attic_room_night
    "You remember the promise to your brother, and hurry toward her, holding her in your arms as you sooth and rock her."
    hide mother
    hide father
    show celine_young at center
    Celine "Don't worry, Maize."
    Celine "I'll keep you safe... I promise."
    "And you would keep her safe."
    "You would get the two of you out of here somehow, een if it killed you."
    "...But first, you need to know the truth."
    "You need to know what happened."
    "{i}You need to know what happened to your brother.{/i}"
    hide celine_young
    scene black
    jump label Prologue_Truth

label Prologue_Truth:
    scene forest_day
    show celine_young at centerright
    show boris at centerleft
    Boris "C-Celine."
    Boris "W-Why did you ask to meet so suddenly?"
    "The young boy stutters."
    Boris "I-I'm really sorry about what happened to your brohter."
    Celine "I need your help with something"
    Boris "R-Really?"
    Celine "Can you get a shovel?"
    Boris "H-Huh?"
    Boris "Why?"
    Celine "{i}I want to dig up my brother's body.{/i}"
    hide celine_young
    hide boris
    scene black
    sound digging_shovel_loop
    "It took you and Boris more than two hours to dig up your brother's grave in the dead of night."
    scene cemetery_night
    "The dim lantern you brought with you seems ready to go out at a moment's notice, and Boris looks particularly afraid, watching for anyone who might see what the two of you are doing."
    show celine_young at centerright
    show boris at centerleft
    Boris "I can't believe you talked me into this!"
    Celine "Enough complaining."
    sound shovelhittingwood
    "When the shovel finally hits the hard wood of the coffin, Boris looks toward you."
    Boris "I-It's here!"
    "You wedge and force the shovel between the lid and the coffin as Boris pleads."
    Boris "Celine!"
    Celine "..."
    Boris "D-Don't do this."
    Boris "This is your brother's rest..."
    Celine "..."
    hide celine_young
    hide boris
    scene nasharincoffin with fade
    "You ignore his words, tearing off the lid as you stare at your brother's lifeless, pale corpse."
    "Boris turns his head and begins to hurl as you inspect your brother's body closer."
    "You were used to inspecting dead things, like teh deer and other mammals you found."
    "You enjoyed figuring out how they died---in fact, you had studied and become quite good at it."
    "You look at your brother's corpse and notice how remarkably undamaged it is."
    "A fall from such heights to kill... and not the slightest broken bone."
    "You look closer, and there---you spot it."
    "Resonating from a black wound"
    "{i}Magecraft{/i}"
    "Like an arrow to the heart---some pungent, dark thing having drained him of his life."
    "{i}It smells exactly like the magecraft resonating from that woman, Kayanna.{/i}"
    Boris "Celine... Urgh... Can we go now, please?"
    Boris "We're gonna get in so much trouble if we're caught!"
    Screen flickers red
    "The rage boils inside you."
    "That woman... That bitch."
    "{i}She took your brother from you.{/i}"
    Boris "Celine!"
    scene cemetery_night
    "You close the lid on your brother's coffin."
    Celine "I've seen what I needed to."
    show celine_young at centerright
    show boris at centerleft
    "The two of you climb out of the grave."
    Boris "D-Did you find what you were looking for?"
    Celine "Yes."
    "You take teh first few steps toward home when Boris calls weakly behind you."
    Boris "W-What will you do now?"
    Celine "...Go home, Boris."
    hide celine_young slideright
    "Saying nothing else, you make your way home with a burning fire in your heart."
    hide boris
    scene black with fade
    jump label revengeonparents
label revengeonparents:
    scene childhood_attic_room_night throbbing purple slowly
    sound heartbeat
    "...As you quietly enter through the still-unlocked front door, you realize your parents have gone to sleep"
    "Your father likely having drunk himself into another stupor."
    "You stop by to check on Maize, sleeping peacefully in her crib, and then," Pause 2 seconds
    "{i}You make your way to your parent's room.{/i}"
    scene parentssleeping with fade throbbing purple slowly
    "Asleep on the bed, with another half-drunk bottle in the cabinet beside your father, he snores as you watch the two of them sleep peacefully while your brother rots in the ground."
    "How... how could they betray him?"
    "Betray Maize?"
    scene parentssleeping with fade throbbing purple
    "Betray you."
    "What kind of monsters sell out their own son for a few coins?"
    "The rage builds, and with a trembling voice you speak."
    Celine "{i}Murderers.{/i}"
    "Your mother's eyes hazily open, and as they do, she shakes your father awake."
    Mother "Celine? What are you---"
    Celine "{i}You cannot move.{/i}"
    scene celineparentsroomnormal fade celineparentsroompurpleeyes
    "Your mother is pinned to the bed by some invisible force---"
    "Now she's awake all right, as her eyes widen with fear."
    Father "WHAT IN THE HELLS DO YOU THINK YOU'RE DOING, G-"
    "Your father moves to get up and stop you, but you turn your gaze to him."
    Celine "STAY."
    scene parentsinbedstunned with fade throbbing purple slowly
    "Your father, too is now unable to move."
    "The two of them struggle against the invisible pressure exerted against them."
    "It's strange... for all their menace and venom, how helpless they seem to you right now."
    Father "C-Celine!"
    Father "What do you think you're doing?"
    scene celineparentsroompurpleeyes
    Celine "How could you?"
    Celine "How could you let them get away with it?"
    Mother "C-Celine, dear... What are you---"
    Celine "SILENCE!"
    scene celineparentsroompurpleeyes tinted purple
    Father "..."
    Mother "..."
    Celine "He was the only one who truly loved me in this family."
    Celine "{i}And you...{/i}"
    scene celineparentsroompurpleeyes tinted purple shake
    Celine "ALL IT TOOK WAS A FEW COINS TO BUY YOUR SILENCE?"
    Celine "TO ABANDON YOUR ONLY SON?"
    scene parentsinbedstunned
    "Your parents do their best to squirm in the bed."
    "They're panicking now --- they realize something terrible is going to happen."
    "{i}... What fun.{/i}"
    scene celineparentsroompurpleeyes tinted purple
    Celine "...Now it's my turn to abandon you both."
    "You raise your hand, setting the bed alight as they panic and squirm, still unable to do anything other then twitch."
    scene parentsinbedburning
    Celine "Goodbye... Mother..."
    Celine "Father."
    "As the fire begins to consume the whole bed --- The flame crawling up your father's leg as he remains unable to break free from your power --- your turn to leave."
    scene black with fade
    "Heading quickly into Maize's room, you qently pick up your baby sister before heading out of the house."
    scene houseburning
    sound firecrackling
    Guard "Get some more buckets, damn it!"
    show celinewithbaby at center
    Guard "Girl is there anyone still inside?"
    scene parentsinbedburning with flash then back to houseburning
    Celine "...No one worth saving."
    "The guard pulls back --- you cannot tell beneath the helmet his expression, but it must be one of confusion and shock."
    "He decides to ignore you, rushing over to try and help the others put out the fire."
    "You lean closer to Maize, gently soothing your crying little sister."
    "The sounds of the fire and the chaos outside fade into the background as you focus on her."
    "For the first time in what feels like forever, there is a moment of peace."
    Celine "Don't worry, Maize, I won't let anyone hurt you ever again."
    jump label oneweeklater
label oneweeklater:
    scene cg_oneweeklater fade to 
    show guard at left
    show Ursula at right
    Guard "...You can come in now, girl"
    show celine_young at center
    "You enter the run-down office as a kind sister in red smiles at you with her hands clasped together."
    Ursula "Hello."
    Ursula "I am Sister Ursula."
    Ursula "You must be Celine."
    menu firsttimeatofficemenu:
        "What is this place?":
            Ursula "This is the goddess Bellefrom's orphanage."
            Ursula "The Sisters of Bellefrom look after children like yourself who have no other family."
            jump firstimeatofficemenu
        "Where is my sister--- Where's Maize?":
            Ursula "Maize is being cared for by the other sisters."
            Ursula "Don't worry, she's safe."
            Celine "I want to see her."
            Ursula "In time, Celine."
            jump firstimeatofficemenu
        "What happens now?":
            Ursula "You'll be staying here for a while now"
            Ursula "At least, until you come of age."
            Ursula "Or, if a family chooses to adopt you"
            Celine "I want to leave."
            Ursula "I'm sorry, child."
            Ursula "There's nowhere else for you to go."
            Ursula "You must stay here for now."
            Celine "I WANT TO GO!"
            jump wantingtoleave
label wantingtoleave:
    Ursula "You'll be staying here for a while now"
    Ursula "At least, until you come of age."
    Ursula "Or, if a family chooses to adopt you"
    Celine "I want to leave."
    Ursula "I'm sorry, child."
    Ursula "There's nowhere else for you to go."
    Ursula "You must stay here for now."
    Celine "I WANT TO GO!"
    slide the guard to center with move
    slide the guard to left with move
    "The guard smacks you on the back of the head from behind, causing you to stumble forward."
    Guard "Be silent, girl."
    "Sister Ursula rushes to your side, raising her hand toward the guard."
    slide ursula to center with move
    Ursula "Guard!"
    Ursula "Please... That will be all."
    "The guard, who seemed ready to hit you again, pulls back."
    Guard "Very well, Sister."
    Guard "I shall leave this matter in your care."
    "With a slight bow, the guard turns to leave as Sister Ursula tends to you."
    hide guard
    slide ursula to right with move
    Ursula "Are you alright, child?"
    Celine "I'm fine."
    Celine "He hits like a girl anyway."
    "Sister Ursula smiles warmly toward you."
    Ursula "You're a strong girl, aren't you?"
    Ursula "But you don't need to be so strong."
    Ursula "{i}Especially after such a terrible tragedy.{/i}"
    Celine "..."
    Ursula "Your parents were not the first drunkards I've seen die in such accidents, I'm afraid."
    Celine "..."
    Ursula "...Come."
    "She holds out her hand for you to take."
    Ursula "Let me show you where you'll be sleeping."
    "Cautiously, you reach out to take the hand, following Sister Ursula as she pulls you along."
    Ursula "This is your new home now, Celine"
    Ursula "Let's try to make the most of it, shall we?"
    Celine "Yes, sister."
    jump years_later
label years_later:
    show ursula at right
    show celine_teen at left
    Ursula "Celine!"
    "Your eyes open as you drowsily rise from your bed."
    Celine "Urghhh... What?"
    Ursula "Don't {i}what{/i} me, young lady."
    Ursula "You were supposed to scrub the hallway floors the other night!"
    Ursula "So why did I find young Madison on her hands and knees in your stead?"
    Celine "Madison owed me a favor."
    Ursula "You mean for beating up that boy the other week, Davis?"
    Celine "...He shouldn't have taken her food."
    "Ursula's hand whooshes out to lightly slap you."
    "It's nothing like Father's heavy hands were, but it still stings enough to make a point."
    Ursula "I have told you before about shirking your duties, Celine."
    Ursula "When you're asked to do something, you do it."
    Ursula "It's not an excuse to find ways around it."
    Celine "Yes... Sister Ursula."
    Ursula "*Sigh*"
    Ursula "Take this bucket and cloth. Clearn some of the doors and windows outside."
    Celine "Yes, Sister."
    Celine "...When can I see Maize?"
    Ursula "Soon. Your sister is doing well. Leave her be, Celine."
    $LocSet(Orphanage_Hallway)
    $QstStart(Prologue2)
    $GoalShow(Prologue2, 1)
TUTORIAL STAT Page
Tutorial TALENTS PAGE
label courtyard
    "As you step out into the main courtyard, you hear the usual chatter of the irritating younger children running around."
    "The older ones give uneasy, glancing looks toward you when they see you."
    "You don't have many friends."
    "Well, it would be better to say you have {i}no{/i} friends---only those who fear you enough not to cause problems."
    "Well, what now?"
return
label chores:
    "You grab a bucket and cloth, heading out to clean the doors and windows as instructed by Sister Ursula."
    menu startchoresmenu:
        "Start chores."
            jump chores_task
        "Not yet."
            return
label chores_task:
    $GoalComplete(Prologue2, 1)
    show celine_teen at left
    "With your wet cloth soaked in the bucket's water, you begin to wipe the dirty windows as best as you can."
    "Going up on your tiptoes to reach the higher glass."
    "Suddenly, you feel the sharp sting of a small rock hitting your back"
    "You drop the cloth instantly, the bucket tipping over as you turn to look at the skinny, angry little shit with another rock in his hand."
    show harlok at center with movein
    show harlokgoon at rightcenter with movein
    show harlokgoon2 at right with movein
    "His two little minions stand beside him."
    Harlok "Opps! Would you look at that."
    Harlok "Looks like you'll need to fetch yourself a fresh bucket."
    Harlok "Fucking freak."
    "His goons snicker."
    "Harlok never quite accepted why you turned down his advances; he's convinced it's because you're a prude."
    "Perhaps it had something to do with catching him pinning one of the other girls against a wall so he could {i}'have a feel'{/i}.--- which made him repulsive to you."
    "Lucky for him, rumor has it; he's the bastard child of sister Tera, a scandal scarcely discussed but she has no doubt pleaded on his behalf to protect him whenever he gets in trouble."
    Celine "Leave me alone, Harlok."
    Harlok "Or what, you crazy bitch?"
    Celine "{i}I won't ask again{/i}."
    menu fightoneorthreemenu:
        "If either of you two idiots help him, {i}I'll smother you in your sleep{/i}." requiredstat STR 5
            jump fight_harlok
        "..."
            jump fightharlokandgoons

label fight_harlok:
    "Harlok's two goons stop laughing; they know you're serious."
    "Everyone has learned by now what you're capable of."
    hide harlokgoon
    hide harlokgoon2
    Harlok "What the fuck!"
    Harlok "Where are you guys going?!"
    Brad (Goon A) "Y-You know what she's like, Harlok!"
    Danny (Goon B) "S-Sorry, she's crazy bro!"
    Harlok "Shit..."
    show harlok at centerleft with movein
    "Harlok marches toward you, ready to swing a punch!"
    "his two goons retreat, remembering your threat."
    hide celine_teen
    hide harlok
    $BattleStart("harlok")
    jump after_fight_harlok

label after_fight_harlok:
    scene celinebreakingharloksfoot
    "The others have gathered around to watch now, Harlok screams in agony as you bring your foot down onto his leg, the bone loudly breaking and crunching as you do so."
    "The other children and teens gasp, horrified, as a crying Harlok falls to the floor, screaming as tears scream down his cheeks."
    Harlok "AHHHHHHHHHHHHHHHH!"
    Harlok "MY LEG! MY FUCKING LEG!"
    Harlok "YOU CRAZY---"
    "You hear the whispers from behind you."
    "{i}She's possessed, she's a witch, she's a...{/i}"
    "{b}Freak.{b}"
    "You grab one of the nearby rocks, ready to bash the little shit's head in."
    "Before you can, a hand grabs your wrist."
    "It's Sister Ursula."
    Ursula "Enough!"
    Ursula "Drop it... now!"
    "You drop the rock, and as you do, other sisters rush over to help the still-screaming Harlok."
    "Angrily, Ursula drags you toward her office."
    "You don't protest, but even you must admit..."
    "{i}Perhaps even you went a little too far this time.{/i}"
    Ursula "Get in there!"
    "Sister Ursula shoves you forward, slamming the door behind her."
    show celine_teen @smug at leftcenter
    show ursula at centerright with movein
    Ursula "What in the hells were you thinking?!"
    Celine "He started it!"
    show ursula at center with movein
    "On her knees, Sister Ursula grabs your shoulders."
    Ursula "Celine!"
    Ursula "You broke his leg!"
    Ursula "The bone was sticking out!"
    Ursula "Don't you understand?"
    Ursula "He may not be able to walk again!"
    Celine "So what? I was just supposed to let him beat me up?!"
    Ursula "There's a difference between fending for yourself, girl, and scaring everyone to death!"
    Ursula "{i}Do you realize the other sisters think you might be possessed?{/i}" 
    Celine "YOU THINK I WANT THIS?!"
    Ursula "..."
    Celine "You think I always feel like I need eyes in the back of my skull?"
    Celine "You think I want everyone to hate me?"
    Celine "...I just wanna take Maize and get away from this place."
    Celine "Start somewhere new, far away!"
    Celine "AND BE LEFT ALONE!"
    Ursula "...*Sigh*"
    "Sister Ursula rubs at her brow."
    Ursula "By the gods, girl, you're going to be the death of me."
    Celine "...I hate it here."
    Ursula "I know you do."
    Ursula "And I promise you, Celine---"
    Ursula "I will do wht I can for you and your sister."
    Ursula "But please..."
    Ursula "{i}Just try to be good?{/i}"
    Celine "...Yes."
    Ursula "Alright, Celine."
    Ursula "You are to return to the girls' quarters and stay there for now."
    Ursula "{i}I need to clear up this mess and speak to the other sisters about what has happened."
    Celine "But---"
    Ursula "No arguing, Celine."
    Ursula "Just do it!"
    hide celine_teen with moveoutleft
    "You slam the door furiously behind you."
    hide ursula
    scene black with fade
    jump orphanage_girls_quarters
label orphanage_girls_quarters:
    $locset = "orphanage_girls_quarters"
    show celine_teen at center
    "What a wretched joke."
    "It was that little shit who started it!"
    "Why were you punished for simplyd defending yourself?"
    hide celine_teen
    "You sigh and drop onto the bed, with little esle to do, and bury your face into your pillow."
    scene lonelyfeeling #...Does no one else really feel the same as you do?
jump middleofthenight

label middleofthenight:
    set time of day to "night"
    Hara(???) "Celine."
    Hara(???) "..."
    Hara(???) "...CELINE!"
    "The voice wakes you, and you dazedly see one of the sisters standing over your bed."
    Celine "...Sister Hara?"
    show hara at center with movein
    Hara (Sister Hara) "You're to come with me, Celine."
    "You rise from your bed."
    show celine_teen at right
    Celine "Where are we going?"
    Hara (Sister Hara) "We're going to see Maize."
    "Did the sister's voice just crack for a moment?"
    "You're not quite sure; you're still a little dazed from being woken after all."
    Celine "{i}*Grumbles*{/i} What time is it?"
    Hara (Sister Hara) "Shh."
    Hara (Sister Hara) "The others are still asleep."
    "Sister Hara reaches for your hand as she almost drags you away."
    show hara at centerright with movein
    hide hara with moveoutleft && hide celine_teen with moveoutleft
    "You didn't even have time to put your shoes on!"
    $locset = "orphanage_girls_hallway"
    show celine_teen at centerright with movein
    show hara at center with movein
    Celine "Sister!"
    Celine "Where are we going?"
    Hara (Sister Hara) "I told you, Celine---We're going to see your sister..."
    "Sister Hara pulls harder, her feet moving faster."
    "Her hands seem shaky---was she afraid?"
    "What was going on?"
    Celine "...Sister Hara?"
    Hara (Sister Hara) "Stop talking, Celine."
    scene black with fade
    "At last, you arrive at your destination: a black, heavy door, normally locked but now open, leading to a dimly lit stone staircase descending into darkness. Sister Hara's hard continues to tug you into the depths."
    "You don't feel afraid exactly; you've never felt fear before---"
    "At least, not in the same way other people do."
    scene Unsettledfeeling with fade #Your heart is calm... and yet, your hairs stand on end, as though something inside you is warning that something terrible is going to happen."
    jump Basement
label Basement:
    scene atlastyoureachthebottom with fade #at last, you reach the bottom floor.
    "An open, chamber, filled with sacks of wheat and other foods stored down here in the cold dark."
    "Standing there, each holding torches and a blade, are two other sisters."
    show sister1 at rightc with movein
    show sister2 at right with movein
    show sisterhara at left with movein
    show celine_teen @shocked at center with movein
    Celine "What's going on?
    "You take a nervous step back to turn and leave, seeing Sister Hara block your path.
    Hara (Sister Hara) "Celine"
    Hara (Sister Hara) "{i}There is a demon within you, child.{/i}"
    "Your eyes widen as you catch the glint of the blades they carry."
    Celine "W-Wait..."
    Hara (Sister Hara) "Celine, please!"
    Hara (Sister Hara) "We only want to help!"
    Celine "W-What are you going to do to me?!"
    Hara (Sister Hara) "We need to let your blood out."
    Hara (Sister Hara) "It's an old ritual but it should let the demon out."
    Celine "Stay back!"
    nunB (Unfamiliar Nun B) "P-Perhaps we should stop, sisters."
    nunB (Unfamiliar Nun B) "If the inquistors ever found out about this ritual..."
    nunA (Unfamiliar Nun A) "Be silent sister!"
    nunA (Unfamiliar Nun A) "It is the only way!"
    nunA (Unfamiliar Nun A) "The child is cursed!"
    show hara at center with move
    show celine_teen at left with move
    Celine "STAY BACK!"
    "Now your heart is pounding. Like a cornered animal, you look for somewhere to run."
    change background with purple shader then back to normal
    Hara (Sister Hara) "Celine, please---"
    Celine "GET AWAY FROM ME!"
    hide celine_teen && hide hara && hide nunA && hide nunB
    $BattleStart("Sister Hara, nunA, nunB")
    jump after_nunfight
label after_nunfight:
    scene black with fade
    scene bg_celenewithnuns
    nunA (Unfamiliar Nun A) "By the gods, Sister Hara! Pin her Down! I'll make the cut!"
    "As Sister Hara reaches to grab and pin your arms from behind, you squirm and writhe, screaming for them to let you go."
    Hara (Sister Hara) "I'm sorry, Celine! I'm sorry!"
    Hara (Sister Hara) "Please! It's for your own good!"
    "As the other sister closes in, grabbing one of your struggling arms to place the knife, you feel the surge of darkness swell within."
    "Something raw, something dangerous."
    "Something even you didn't know you could do."
    tint bg_celenewithnuns with purple shader
    Celine "{i}Sister.{/i}"
    "The sister looks up toward you as your eyes glow purple, mana overflowing."
    Celine "{i}Kill yourself{/i}"
    scene bg_ursulabargesin
    Ursula "WHAT IN THE NAME OF AL'VAZAH IS GOING ON HERE?!"
    "Sister Hara releases you at once as the second sister retreats."
    "Sister Ursula storms over to grab you."
    Ursula "What is this madness?!"
    Ursula "Why have you taken Celine down here?!"
    Hara (Sister Hara) "S-She's possessed, Sister Ursula!"
    Hara (Sister Hara) "You know it! We all do!"
    scene haraontheground
    "Sister Ursula backhands Sister Hara, knocking her to the floor."
    "Sister Ursula reaches down to shake you."
    Ursula "Celine! CELINE!"
    Ursula "Are you alright?"
    "You cannot peel your eyes away."
    "At last, Sister Ursula and the others realize what is happening."
    scene nunwithknife
    "The sister you commanded is standing, trembling"
    "Her eyes are wide with panic as, with a shaking hand, she begins to lift the knife."
    Ursula "S-Sister Katherine!"
    Ursula "What are you doing?!"
    "There are gutteral grunts as tears stream down her unblinking eyes"
    "It is as though she is trying to fight back against her own body, but it's hopeless."
    scene nunknifedeath
    "The blade plunges sharply into the side of her neck, and the sisters scream."
    "She pulls the knife out, plunging it in again and again..."
    "With the third strike, she drops lifelessly to the floor in a pool of her own blood as the sisters rush toward her."
    scene nunsarounddeadnun
    "You look at your hands, seeing the splash of blood on them."
    "{i}What... what have you done?{/i}"
    GoalComplete