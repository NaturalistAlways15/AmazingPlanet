# Declare characters used by this game.
define t = Character(_("Teacher"), color="#c8ffc8")
define m = Character(_("[mc]"), color="#c8c8ff")
define score = 0

# This is a variable that is True if you've compared a VN to a book, and False
# otherwise.

# The game starts here.
label start:

    # Start by playing some music.
    
    scene bg schoolbus
    with fade
    
    python:
        mc = renpy.input("Today is your final day of school field trip! You're going to have a blast. But who are you?", length=32)
        mc = mc.strip()
    
        if not mc:
             mc = "MC"
    
    m "I'm [mc]!"

    show teacher idle
    t "Hi class today were going on a field trip!!!!!. we’re not going to talk about school today, everything is about have \“fun\”"

    t "Don't worry about waiting, because we're \"Hot\" on it's trail!"
    menu:

        "[mc]! You don't look like you're paying attention. Where are we going today?"

        "Terrestrial biome":
            show bg schoolbus terrestrial
            #jump terrestrial

        "Aquatic biome":
            show bg schoolbus aquatic
            #jump aquatic

        "Both":
            show bg schoolbus both
            #jump both

label Q1:

    t "That was a trick question. None are correct."
    t "We're going to 30 degrees south of the equator, where there's only two seasons."

    menu:

        "[mc]! Guess it right, or I'm cancelling the class trip."

        "Tundra":
            jump incorrect

        "Chaparral":

            jump incorrect

        "Savannah":
            $ score += 1
            show bg schoolbus savannah 

    t "Impressive. "
    t "Yes, we are going to the savannah. In fact, we are already there!"
    t "Let us get off the bus."

    show bg savannah low

    t "Please take a look at all these gazelles in their natural habitat."

    t "Uagh!!!! ugahH!!! i'm turning into a squirrel!"

    hide teacher idle
    with dissolve
    show squirrel idle
    with dissolve

label Q2:

    t "Squeak squeak squeak!!" 
    t "(turn me back by calcualating the speed of the airbus when it is travelling 7m in 6 seconds to pick up this magical sandwhich)"
    
    menu:
        t "(If you get it wrong, I'm cancelling the trip)"

        "1.1666":
            $ score += 1

        "0.8571":

            jump incorrect

        "42":
            jump incorrect

        "420":
            jump incorrect

    t "Good job!" 
    t "..." 
    t "... I think turning me back is virtually impossible." 

label Q3:
    show bg savannah high
    t "Ah! more gazelles have come. This reminds me.. "
    t "What problems might arise to a population that's density dependent?" 
    
    menu:
        "non-bottleneck": 
            t "nope, points off for you"
            $ score -= 1 

        "Diseases arise, and the population is not able to adapt to the diseases as quickly":
            t "Satisfactory"

        "A flood will wash all the plants away so grazelles starve.":
            hide squirrel idle
            show squirrel angry
            t "the flood probably flushed your brains out."
            t "I'm cancelling the trip."

            jump incorrect

        "predator population increase, and suppresses the grazelle population":
            t "Satisfactory"
    
label Q4:
    t "Now, for the fourth question:" 
    t "You see a piece of foil on the ground, if you want to pick it up, solve the equation: 2x+3x^7-5=9. If you don't, solve the equation: 3x^2-3=0." 

    menu:
        "x = 1.21274":
            jump do
        "x = 1":
            jump ignore

        "x = -1":
            jump ignore

        "...I'd rather not":
            jump ignore

label do:
    show squirrel happy
    t "Excellent work. Now the gazelles will not feast on the foil and get sick."

    jump Q5
    

label ignore:
    hide squirrel happy
    show squirrel angry
    "You seem to be in a pickle.."
    "Why is your teacher angry at you for not picking up the trash?"

    menu: 
        "Picking up the foil will result in a positive feedback loop in which more foil is found on the ground to be picked up.":
            t "goodbye (volcano)"
            jump incorrect

        "Nature is polluted enough":
            t "goodbye (volcano)"
            jump incorrect

        "The Savannah is an important exosystem that house their own biodivsersity; pollutants should be removed.":
            hide squirrel angry
            show squirrel happy
            t "Yes, Yes, Yes!" 
            $ score += 1

            hide squirrel happy
            show squirrel idle
            t "But it is also important to understand a suituation's benefits to ensure that we implement them when addressing the problems."

            menu: 
                t "What positive does the presence of Foil provide for this location?"

                "The Sun's rays are sent out into space through albedo, preventing the Earth's atmosphere from capturing dangerous rays.":
                    hide squirrel idle
                    show squirrel happy
                    t "Yes, Yes, Yes!" 
                    $ score += 1

                "Over time, the Foil will decompose, providing nutrients for the sand.":
                    hide squirrel happy
                    show squirrel angry
                    t "Wrong. Very wrong, even." 
                    t "I'm cancelling the trip."
                    jump incorrect
                
                "Nice aesthetic.":
                    t "You don't look interested..."
                    t "Perhaps I should change the subject." 

        "Squirrels rely on the presence of Foil for their source of Vitamin D":
            show squirrel angry
            t "Get lost"
            jump incorrect

    jump Q5

label Q5:
    show squirrel idle
    #broken bus sound. 
    t "..??"
    t "Ahh!! It seems that caused the airbus stop working. It's getting really hot..."
    menu: 
        t "What bus part do you persume stopped functioning due to the large exposure to heat?"
        "Engine":
            $ score += 1
            t "I think so too.."
        "Wheels":
            $ score -= 1
            t "I'll go easy on you, but that's not the right answer."
        "Digital Clock":
            $ score -= 1
            t "I'll go easy on you, but that's not the right answer."
        "Front Lights":
            $ score -= 1
            t "I'll go easy on you, but that's not the right answer."
    
    jump Q6

label Q6:
    hide squirrel idle 
    "Your teacher tries to fix the airbus.."
    "..but it doesn't work"
    show squirrel idle 
    t "[mc]! I'm a squirrel! I can't program!"
    "Because your teacher can't get it to work, you decide to do it yourself. "
    "In order to fix the airbus, you decide to hack into your teacher's computer to access the engine and execute the completely realistic advanced cooling mechanism."
    "You have to find the password by coding an algorithm trying out all the possible combinations of 4 numbers. You have a total of 1,000,000 tries"
    menu: 
        "you need to crack the computer before the sun sets off a wildfire, what method do you use?"
        "rescrusion();":
            $ score -= 1
            "You barely managed to complete the problem in time.."
        "iteration();":
            $ score += 1
            "Success! You managed to well before any heat issues."
        "arrayList();":
            $ score -= 1
            "You barely managed to complete the problem in time.."

        "probability();":
            "There's no way you're going to complete it in time.."
            jump incorrect
    
    jump Q7

label Q7:
    #broken bus sound. 
    "As you finish fixing the airbus' engine to get back to school, you catch one of the gazelles eating the battery. Uh Oh..."
    t "Geez.. It seems that we need to hitch another ride back home.."
    t "Fourtunately! Thanks to my science degree, I have unlimited access to the Coriolis effect."
    t "[mc]! You've been a good student so far. As you remember, this savannah was south of where we came."

    menu: 
        t "Which circulation cell must we riding on our current latitude?"
        "hadley cell":
            t "Muahahahaha! You are a fantastic student. Enjoy going back."
        "ferrell cell":
            t "No. There is too much coriolis force here, but I'll let you off the hook for now."
            $ score -= 1
        "polar cell":
            show squirrel angry
            t "That is extremely incorrect."
            t "If you're going to fail the test, I'd rather you stay here with the gazelles"
            jump incorrect
        "trade winds":
            t "Trade winds have nothing to do with the Coriolis effect."
            $ score -= 1

    jump Q8


label Q8:
    #broken bus sound. 
    t "Good, good.."
    t "We have a ride home after fixing the airbus' broken engine.."
    t "..."
    t "[mc].. How do we get the airbus on the air?" 
    "It turns out that the airbus needs to get high enough to for trade winds to work." 
    "You decide to build a solar panel." 
    menu: 
        "What is a method you can use to build this solar panel?"
        "Clear out a large area of the savannah to put the panels":
            t "Yes, we can do that.."
        "Find a bunch of photovoltaic solar cell":
            t "Yes, we can do that.."
        "First create passive solar energy collection device":
            t "..."
            t "[mc]... I think we're stranded for good"
            jump incorrect
        "Find convertor from direct current to alternating current":
            t "Yes, we can do that.."


    show squirrel happy
    t "This.."
    t "This is good! Congradulations, [mc]! We are able to go home now."

    hide squirrel happy
    "As soon as your solar panels were built, it started to rain." 
    "the heavy rain caused a huge flooding, which washes you and your teacher straight back to school"

    jump end



label end:
    hide squirrel idle
    show bg uni
    with ease

    "..."
    "Well, it seems like we don't have to worry about being home anymore.."

    pause

    "Ahh... This trip was so exhausting... "
    show teacher idle
    t "[mc]! It looks like leaving the savannah fixed the squirrel suituation!"
    t "How wonderful."
    t "Okay kids, now that your \"fun time\"'s over, let's get to your exam."
    t "---- what??"
    with vpunch 
    t "WHO LEFT THE BUNSEN BURNER OPE--"

    hide teacher idle
    show explosion normal

    pause

    hide explosion normal
    show bg darkscreen
    "[mc].."
    "This game tells us the moral: no matter how many questions you get right, you still have to study for your REAL LIFE exam."
    "I hope you learned something new from an unfamiliar societal sector."
    "Enough with the general learning, get out and study what you're supposed to be studying!!"

    "END GAME
    SCORE: [score]"

    return
    

label incorrect:
    show bg darkscreen
    hide teacher idle
    hide squirrel idle

    "SCORE: [score]"
    "I got the question wrong... should I try again?"
    menu:

        "Try Again":
            jump start

        "Quit":
            return