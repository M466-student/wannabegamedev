
define k = Character("Kazuya")
define v = Character("???")
define s = Character("Sensei")
define c = Character("Class")
define e = Character("Kaguya")
label start:
    play music "backsound.mp3" fadein 3.0 fadeout 3.0
    scene pic1
    pause
    "It was a sunny day. Kazuya and his friends are playing video games in his place everything is normal when suddenly everything went Black."
    scene pic2
    with fade
    k "I cant see anything,it felt like an hour passed by,just sitting there looking at the deep darkness surrounded me when a glimps of shadow appeared infront of me."
    k "Where am i?What are you?What do you want from me?"
    "The shadow just standed there and just stared at kazuya."
    "and then he jumped at him"
    with hpunch
    "kazuya freaked out until he woke up seeing he was only just dreaming"
    pause
    scene pic1
    with dissolve
    "he sighed of relief and saw the time and oh shit it was 8 a.m he was late to school."
    scene pic3
    "he jumped out of his bed and went to the closet to get his uniform."
    scene pic5
    "he rushed to school running as fast as he can.but even tho he ran like hell,he couldn’t make it in time.he arrived at class 25 minutes late,sweating like hell."
    scene pic6
    "the teacher got pissed at him and didn’t let him study in class but infront of the class.he sighed and said ok cause that’s normal for him.kazuya has no friends and didn’t care about anything,his grades,making friends,anything I guess."
    ".he went infront of the class and a girl he didn’t recognized passed by him and went to his same class"
    v "I’m sorry sensei i‘m late my mom forgot to wake me up"
    s "its ok just introduce yourself and sit down"
    k "(wtf,why am I here then)"
    c "who is that?she’s so pretty and kawai"
    v "hi my name is kaguya,hajimemashite!"
    c "kawaii,nee!"
    "Kazuya didn’t really care about the girl,he thought that she was just an ordinary student like anybody else(because he's gay)"
    "Kazuya finaly got in class just to find out beside him was not other than the new girl,the pretty girl."
    k "damn it why her by all the student"
    "He sat beside her and she looked at him and smiled"
    e "hi,my name is kaguya nice to meet you"
    menu:
        "What should i say?"

        "Nice to meet you to kaguya":
              jump friends
        "ignore her":
            e "Hey didn't you hear me Heyy"
            jump friends
        "fuck off":
             jump badending1

    label badending1:
        "kazuya got expelled because he cursed in the class loudly and make kaguya cried"
    return

    label friends:
        e "Lets be friends!"
        "Kazuya tried to ignore her until the school ended"
        scene pic5
        v "KAZUYA KAZUYA!"
        "Kazuya turned his head around to see that kaguya is calling him.Kazuya got the center of a attention cause a cute girl is calling him,a weirdo"
    menu:
        "What should i say?"

        "Yes i'm kazuya":
            jump dating
        "What do u want?":
            jump dating

    label dating:
        e "sensei said your house is close to mine,i was wondering that can we go home together"
        k "WAIT are you serious?I dont belive you lets go to sensei"
        e "oh cmon can we just go"
        k "o hell no,everyone will think were dating,cmon lets go"
        "Kazuya without hesitation grabed her hand and walked to sensei lounge.kaguya got embarrassed."
        e "what are you doing?let go off my hand!"
        "Kazuya realized what he has done and started to blush"
        k "I…im sorry"
        "Kazuya ran to his house embarrassed."


return

