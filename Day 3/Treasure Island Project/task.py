

print('''
*******************************************************************************
!!!!!!    `?                   - "?h,   .  `!,`!!;\'  <>
!!!!>>     `h                `-`- . "r .,J,-'!>`>` !>,! !
`!!! \      3           ,ccc,,,.````,c$???$c`!!,`> ! !,'            ,r
 !!>        ?,          `$$$$$$$c$$$c,   ),$b`'` \ `:'        ,,cc$$"
  `!        `h         -.`$PF"$????$$$b,"'?$$$J$c `'  ,,ccc$$$$$$P"
             F       -```,nP c$$$,<,3$$$$$$$$$$$$$$$$Ccd$$c`??""
            ;F        ,nMM" $$$$$$ $$$$$$$$$$$$$$$$$$"  ,`$
            J'      ,MMMM  ,$$$$$'J$$$$$$$$$$$$$$$$$$ ,,,cc,,
            J      dMMMMf,d$$$$$',$$$$$$$$$$$$$$$$$$$ ?$????$$bc
           ,$     JMMMMM `$$$$P",$$$$$$$$$$$$$$$$$$$$b ?F<$hd$$P"
           JP    ,MMMMMM.."L,,=$$$$$$$$$$$$$F",;;,`"??h, $$$P"
           $F    `MMMMMMb`,`"?h,. ,$$$$$$$$$FF""`""""==?-`?$"
          ,$      4MMMMMMb`Tnx`?$$$$$$$$$$$$$?????"""""' .,,cc,            M
          J$F    ,`4MMMMMMMh;"?'$$$$$$PF"',cccd$$$$$$$$$$$$$$$$$,         JM
          ?",,cP,$h,`4MMMMMMMMM $$$$P",$$$$$$$$$$$$$$$$$$$$$$$$$$,     , ,MM
        ,cd$$$$ d$$$$c,`"4MMMMM,`$$$ J$$$$$$$$P".::::,$$$$$$$$$$$$ ,,r",nMMM
      z$$$$$$$F $$$$$$$$$cc,. "" `$$ $$$$$$$$":::`.:,$$$$$$$P".`$$ ,xnMMMMP
     d$$$$$$$$F $$$$$$$$$$$$$$$c   ">`$$$$$$$, ```,z$$$$$$$"::',$",MMMMMP"
     $?$$$$$$$F $$$$$$$$$$$$$$$$L :::.""??$$$$$$$$$$$$$$$$$c,,cP" TTTT"
    j"d$$$$$$$L $$$$$$$$$$$$$$$$$$,``,mn,_ .`"""???????????""" ,c
     d$$$$$$$$$ ?$$$$$$$$$$$$$$$$$$b,`"4MM,:::::..::::: ::: 3$c`"
   ,$$$$$$$$$$$c $$$$$$$$$$$$$$$$$$$$$c,.'  ::::::::::` ::::."?h,
,c$$$$$$$$$$ $$$c`$$$$$$$$$$$$$$$$$$$$$$$$$hcc,,,,.   ```..,,ccd$"
',c"?$$$$$$F,$$$$bd$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
<$$h`$$$$$",$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P'
`$$$c".?$F,$$$$$$$$$$$$$$$$??$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"
 `$$$c,." d$$$$$$$$$$$$$$$$$,?$$$$$$$$$$$$$$$$$$$$$$$$$$$$P"
  `$$$$$c``$$$$$$$$$$$$$c"$$$c"$$$$$$$$$$$$$$$$$$$$$$$$P"
   `?$$$$h,`$$$$$$$$$$$$$h,?$$h,"$$$$$$$$$$$$$$$$$$PF".
     "$$$$$h ?$$$$$$$$F$$$$$c`??$c,"?$$$$$$$$$$P"',c$"
     -,"?$$$$,"$$$$$$$b`$$$$$$hc,`""==    .,,,cd$$P",
      "$c,"??$h "$$$$$$c`"==- ,z$$$$$$$$$$c-`3$P",c$"
       `$$$c  ""- ?$$$$$ J$$$$$$$$$$$$$$$$$$ ",c$$P'
         ?$$       "$$$$ ???$$$$$$$$$$$$PF" z$$$P"
          `$        `$$"       ,,           $$$"
           $>        ?$        `$           4$'
          ,F         ?$         "P  ,       4F
        ???'         `$           4Mn`-     J(
                      $c                    $b,
                  ,- ???                    `,dn(+
                 ',dMM-                      `"??=
                  "'
*******************************************************************************
''')
print("Welcome to lion king.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? '
                 'Type "Left" or "Right".').lower()

if choice1 == "Left":
    choice2=input('You\'ve come to a lake. '
                  'There is an island in the middle of the lake. '
                  'Type "wait" to wait for a boat. '
                  'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "One yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over\n")
        elif choice3 == "yellow":
            print("You found the treasure. You win!\n")
        elif choice3 == "blue":
            print("You enter a room of beats. Game Over.\n")
        else:
            print("You chose a door that doesn't exit. Game Over.\n ")
else:
    print("You fell in to a hole. Game Over.\n")
