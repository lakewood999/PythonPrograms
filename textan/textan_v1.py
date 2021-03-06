'''
textan is a module that performs text analysis.  This program simply
will run the program when the function is called.  There are no values returned; the programs print out a thing

Author: Steven S

Official Hosting Site: Find more information at lakewood999.github.io

The functions in this module are freqan(inputText), and wordCount(inputText), where inputText is a string.

Notes: This considers all cases as lowercase
'''

#test data:
#Left till here away at to whom past. Feelings laughing at no wondered repeated provided finished. It acceptance thoroughly my advantages everything as. Are projecting inquietude affronting preference saw who. Marry of am do avoid ample as. Old disposal followed she ignorant desirous two has. Called played entire roused though for one too. He into walk roof made tall cold he. Feelings way likewise addition wandered contempt bed indulged. 

#ROT-25 Caesar cipher @ http://planetcalc.com/1434/ :
#Kdes shkk gdqd zvzx zs sn vgnl ozrs. Eddkhmfr kztfghmf zs mn vnmcdqdc qdodzsdc oqnuhcdc ehmhrgdc. Hs zbbdoszmbd sgnqntfgkx lx zcuzmszfdr dudqxsghmf zr. Zqd oqnidbshmf hmpthdstcd zeeqnmshmf oqdedqdmbd rzv vgn. Lzqqx ne zl cn zunhc zlokd zr. Nkc chronrzk enkknvdc rgd hfmnqzms cdrhqntr svn gzr. Bzkkdc okzxdc dmshqd qntrdc sgntfg enq nmd snn. Gd hmsn vzkj qnne lzcd szkk bnkc gd. Eddkhmfr vzx khjdvhrd zcchshnm vzmcdqdc bnmsdlos adc hmctkfdc.

#Sussex result matter any end see. It speedily me addition weddings vicinity in pleasure. Happiness commanded an conveying breakfast in. Regard her say warmly elinor. Him these are visit front end for seven walls. Money eat scale now ask law learn. Side its they just any upon see last. He prepared no shutters perceive do greatest. Ye at unpleasant solicitude in companions interested. Her companions instrument set estimating sex remarkably solicitude motionless. Property men the why smallest graceful day insisted required. Inquiry justice country old placing sitting any ten age. Looking venture justice in evident in totally he do ability. Be is lose girl long of up give. Trifling wondered unpacked ye at he. In household certainty an on tolerably smallness difficult. Many no each like up be is next neat. Put not enjoyment behaviour her supposing. At he pulled object others. Dashwood contempt on mr unlocked resolved provided of of. Stanhill wondered it it welcomed oh.Hundred no prudent he however smiling at an offence. If earnestly extremity he he propriety something admitting convinced ye. Pleasant in to although as if differed horrible. Mirth his quick its set front enjoy hoped had there. Who connection imprudence middletons too but increasing celebrated principles joy. Herself too improve gay winding ask expense are compact. New all paid few hard pure she. His exquisite sincerity education shameless ten earnestly breakfast add. So we me unknown as improve hastily sitting forming. Especially favourable compliment but thoroughly unreserved saw she themselves. Sufficient impossible him may ten insensible put continuing. Oppose exeter income simple few joy cousin but twenty. Scale began quiet up short wrong in in. Sportsmen shy forfeited engrossed may can
# wordCount("this is a test keyboarding is a neccessary skill my spelling is not good I do not type very well this has no white space except for single spaces I must be able to type faster python is a good programming language most of this is in lowercase there is no punctuation in this passage i am done writing test paragraph")

#####################################
# Freqan                            #
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
#####################################
# wordCount                         #
#####################################
def wordCount(inputText):
  #-----------------------------------#
  # Import modules                    #
  #-----------------------------------#
  import string
  
  #-----------------------------------#
  # Initialize Variables              #
  #-----------------------------------#
  wordDictionary = {}
  wordList = [] # For analysis of words
  wordSorted = []
  
  #-----------------------------------------------------------#
  # Makes text ready for analysis and splits the string       #
  #-----------------------------------------------------------#
  inputText = inputText.lower()
  inputText = inputText.replace("  ", " ")
  # Strips punctuation
  for character in range(len(string.punctuation)):
    inputText = inputText.replace(string.punctuation[character], "")
  wordList = inputText.split()
  
  #-----------------------------------#
  # Performs Analysis                 #
  #-----------------------------------#
  for word in wordList:
    if word in wordDictionary:
      wordDictionary[word] = wordDictionary[word] + 1
    else:
      wordDictionary[word] = 1
      
  # Test ordering - Will keep if works
  # wordSorted = sorted(wordDictionary)
  
  #-----------------------------------#
  # Prints results                    #
  #-----------------------------------#
  print("%-20s%-20s" % ("Word", "Word Count"))
  print(40 * "-")
  for key in wordDictionary:
    print("%-20s%-20s" % (key, str(wordDictionary[key])))
  
  
  
    
    

            
