hp = 50

print("You enter a creepy, dark, underground pathway. You look in front of you, to see two alternative pathways. Do you choose into the left pathway for the right one?")
pathway = input('> ')

if pathway == "Left" or "L":
    print("Down the left pathway, you start seeing creepy hallucinations of red eyes staring at you.")
    print("You see an evil witch casting a hallucenation spell on you. Do you #1. try to kill the witch or #2. get away from the witch?")

    witch = input('> ')

    if witch == "1":
        print("You approach the witch quietly with a stake to slay it. However, the witch senses your prescence and casts a ball spell which turns you into a ball, and then she throws you into her brew. Poor you....")

    elif witch == "2":
        print("You try to sneak past the witch, but her hallucinations take a toll on your body, which makes you fall down in unconsiousness. You don't know what happens to you after that.")

    else:
        print("The witch gets bored of you,and flies away on her magic broomstick. Great Job!")

elif pathway == "Right" or "R":
    print("You enter a big, wet room and a huge man-eating slug is seen approaching you. This slug also happens to be faster than a normal slug is. What do you do?")
    print("#1. Try to mount it to use it to escape.")
    print("#2. Trick it into charging towards you, into a wall.")
    print("#3. You attempt to become friends with it.")
    slug = input('> ')

    if slug == "1" or "2":
        print("You successfully slayed the slug, and now, you can escape.")

    else:
        print("Being friends with a man-eating slug? Yeah, no. It gobbles you up with one slurp and now, you're stuck in its digestive track.")

else:
    print("You took too long of a descicion and you find yourself being bitten by a bunch of poisonous spiders. What an anticlimatic ending.")

    
    
