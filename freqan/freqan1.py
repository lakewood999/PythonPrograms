'''
freqan is a module that performs frequency analysis.  This program simply
will run the program when the function is called.  There are no values returned; a program is simply
run.

Author: Steven S

Official Hosting Site: Find more information at lakewood999.github.io

The only function in this module is freqan(inputText), where x is a string.

Notes: This considers all cases as lowercase
'''

#test data:
#Left till here away at to whom past. Feelings laughing at no wondered repeated provided finished. It acceptance thoroughly my advantages everything as. Are projecting inquietude affronting preference saw who. Marry of am do avoid ample as. Old disposal followed she ignorant desirous two has. Called played entire roused though for one too. He into walk roof made tall cold he. Feelings way likewise addition wandered contempt bed indulged. 

#ROT-25 Caesar cipher @ http://planetcalc.com/1434/ :
#Kdes shkk gdqd zvzx zs sn vgnl ozrs. Eddkhmfr kztfghmf zs mn vnmcdqdc qdodzsdc oqnuhcdc ehmhrgdc. Hs zbbdoszmbd sgnqntfgkx lx zcuzmszfdr dudqxsghmf zr. Zqd oqnidbshmf hmpthdstcd zeeqnmshmf oqdedqdmbd rzv vgn. Lzqqx ne zl cn zunhc zlokd zr. Nkc chronrzk enkknvdc rgd hfmnqzms cdrhqntr svn gzr. Bzkkdc okzxdc dmshqd qntrdc sgntfg enq nmd snn. Gd hmsn vzkj qnne lzcd szkk bnkc gd. Eddkhmfr vzx khjdvhrd zcchshnm vzmcdqdc bnmsdlos adc hmctkfdc.

#####################################
# The Main Function                 #
#####################################
def freqan(inputText):
    
    #-----------------------------------#
    # Initialize Variables              #
    #-----------------------------------#
    
    #textLength = 0

    # Total characters
    numberCharacters = 0
    # Individual characters
    #numberCharacter = 0

    valueCharacters = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    percentageCharacters = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0, 'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
    # Official data from https://en.wikipedia.org/wiki/Letter_frequency       -first table with data
    listPercentagesOfficial = {'a':8.167, 'b':1.492, 'c':2.782, 'd':4.253, 'e':12.702, 'f':2.228, 'g':2.015, 'h':6.094, 'i':6.966, 'j':0.153, 'k':0.772, 'l':4.025, 'm':2.406, 'n':6.749, 'o':7.507, 'p':1.929, 'q':0.095, 'r':5.987, 's':6.327, 't':9.056, 'u':2.758, 'v':0.978, 'w':2.360, 'x':0.150, 'y':1.974, 'z':0.074}

    # For ordered versions
    valueCharactersSorted = {}
    percentageCharactersSorted = {}
    #listPecentagesOfficialSorted = {}
    
    # For printing the summary
    #numberPlace = 0
    
    #------------------------------------#
    # Converts the text to all lowercase #
    #------------------------------------#
    inputText = inputText.lower()
    
    #------------------------------------#
    # Finds the length of the text       #
    #------------------------------------#
    #textLength = len(inputText)

    #-------------------------------------------#
    # Finds number of times each letter appears #
    #-------------------------------------------#
    for character in inputText:
        if character in valueCharacters:
            valueCharacters[character] += 1

    #----------------------------------------------------#
    # Calculates the number of characters without spaces #
    #----------------------------------------------------#
    for character in inputText:
        if character.isalpha() == True:
            numberCharacters += 1

    #------------------------------------#
    # Calculates the percentages         #
    #------------------------------------#
    for key in valueCharacters:
        percentage = valueCharacters[key] / numberCharacters
        percentage = round(percentage * 100, 3)
        percentageCharacters[key] = percentage
        
    #------------------------------------#
    # Orders the dictionaries            #
    #------------------------------------#
    valueCharactersSorted = sorted(valueCharacters, key = valueCharacters.get, reverse = True)
    percentageCharactersSorted = sorted(percentageCharacters, key = valueCharacters.get, reverse = True)
    listPercentagesOfficialSorted = sorted(listPercentagesOfficial, key = valueCharacters.get, reverse = True)
    
    #------------------------------------#
    # Prints the results                 #
    #------------------------------------#
    print("The following data will be printed in the format of: first row = number of characters, second row = percentages, third row = theoretical data")
    print("Also, before the data mentioned above is printed, this text had", numberCharacters, "letters")
    print()
    
    # Row 1
    for item in valueCharactersSorted:
        print(str(item) + "|" + str(valueCharacters[item]), end = " ")
    print()
    print()
    
    # Row 2
    for item in percentageCharactersSorted:
        print(str(item) + "|" + str(percentageCharacters[item]), end = " ")
        #print(str(item) + "|" + str(percentageCharacters[item]), end = " ")
    print()
    print()
    
    # Row 3
    for item in listPercentagesOfficialSorted:
        print(str(item) + "|" + str(listPercentagesOfficial[item]), end = " ")
        #print(str(item) + "|" + str(listPercentagesOfficial[item]), end = " ")
    
    

            
