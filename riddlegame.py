user_name = str(input("What's your name? \n"))
# Ask for a input Name
print('Hi! '+ user_name +', nice to meet you!')
# Print a response to the user
keep_name = str(input("Would you like to use these name? \n"))
if keep_name =='no' or keep_name == 'No' or keep_name == 'N' or keep_name == 'n':
  user_name = str(input("Chose a Nikname: "))
  print('Great ' + user_name + '!')
else:
  print('Great '+ user_name + '!')
print("Now that you have a user name let's get you started!")
print("Welcome to Level 1 " + user_name + "! \n Every level consists in 3 Riddles and you gotta find the right guess otherwise you'll have to start from the beginning ")
while True:
    q1_l1 = str(input('1. What has to be broken before you can use it? \n'))
    if q1_l1 == 'egg' or q1_l1 == 'an egg' or q1_l1 == 'Egg' or q1_l1 == 'An egg':
        print('You got it!')
        q2_l1 = str(input('2. What is full of holes but still holds water? \n'))
        if q2_l1 == 'sponge' or q2_l1 == 'a sponge' or q2_l1 == 'Sponge' or q2_l1 == 'A sponge':
            print('You got it!')
            q3_l1 = str(input('3. What can you break, even if you never pick it up or touch it? \n'))
            if q3_l1 == 'promise' or q3_l1 == 'a promise' or q3_l1 == 'Promise' or q3_l1 == 'A promise':
                print('You got it!\n')
                print("Congratulation " + user_name + " you passed Level 1!\n")
                print("Welcome to Level 2 " + user_name + "!")
                q1_l2 = str(input("1. I'm found in socks, scarves and mittens. I'm found in the paws of playful kittens. What am I? \n"))
                if q1_l2 == 'Yarn' or q1_l2 == 'yarn':
                    print('You got it!')
                    q2_l2 = str(input("2. Tool of thief, toy of queen. Always used to be unseen. Sign of joy, sign of sorrow. Giving all likeness borrowed. What am I? \n"))
                    if q2_l2 == 'a mask' or q2_l2 == 'A mask' or q2_l2 == 'mask' or q2_l2 == 'Mask':
                        print('You got it!')
                        q3_l2 = str(input("3. Who makes it, has no need of it. Who buys it, has no use for it. Who uses it can neither see nor feel it. What is it? \n"))
                        if q3_l2 == 'a coffin' or q3_l2 == 'A coffin' or q3_l2 == 'coffin' or q3_l2 == 'Coffin':
                            print('You got it!')
                            print("Congratulation " + user_name + " you passed Level 2!\n")
                            print("Welcome to Level 3 " + user_name + "!")
                            q1_l3 = str(input("1. Poor people have it. Rich people need it. If you eat it you die. What is it? \n"))
                            if q1_l3 == 'Nothing' or q1_l3 == 'nothing':
                                print('You got it!')
                                q2_l3 = str(input("2. When you stop to look, you can always see me. But if you try to touch me, you can never feel me. Although you walk towards me, I remain the same distance from you. What am I? \n"))
                                if q2_l3 == 'The horizon' or q2_l3 == 'the horizon' or q2_l3 == 'horizon' or q2_l3 == 'Horizon':
                                    print('You got it!')
                                    q3_l3 = str(input("3. I may be simple, I may be complex; I may have a name, but no gender or sex; I am often a question, or statements as a setup; I tend to have an answer, 'til you find it I won't let up. What am I? \n"))
                                    if q3_l3 == 'A riddle' or q3_l3 == 'a riddle' or q3_l3 == 'riddle' or q3_l3 == 'Riddle':
                                        print('You got it!')
                                        print("Good job " + user_name + " you WON!! ")
                                        break
                                    else:
                                        print("Nope!That's wrong.... try again.")
                                else:
                                    print("Nope!That's wrong.... try again.")
                            else:
                                print("Nope!That's wrong.... try again.")
                        else:
                            print("Nope!That's wrong.... try again.")
                    else:
                        print("Nope!That's wrong.... try again.")
                else:
                    print("Nope!That's wrong.... try again.")
            else:
                print("Nope!That's wrong.... try again.")
        else:
            print("Nope!That's wrong.... try again.")
    else:
        print("Nope!That's wrong.... try again.")
else:
    print("Nope!That's wrong.... try again")
