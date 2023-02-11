
wrod_2 = "****"
word = "yasah"
lives = 8
while lives != 0:
    print(f"Your word is : {wrod_2}")
    print(f"Your lives left are : {lives}")
    lol = input("enter : ")

    if len(lol) != 1:

        print("FUCK YOU")
        lives = lives - 1
        continue



    if lol in word:

        wrod_2 = ""

        for i in range(0,len(word)):

            if lol == word[i]:
                wrod_2 = wrod_2 + lol
            else:
                wrod_2 = wrod_2+"*"


        continue

    lives = lives - 1

