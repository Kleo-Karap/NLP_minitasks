#Set the constants of the function
  #1. The set of special characters I want to remove from my string
  #2.The empty dictionary to which I will add the frequencies of the requested links
  #3.The empty list, to which I will add the cleaned words containing only Greek characters
  #4.The empty list, to which I will add the cleaned words that do not contain only Greek characters
  #5.The auxiliary list, which will avoid duplicates in the non-greek list
  #6.The list with the requested links as elements
  #7.The Lowercase variable, with which I convert the string of the mandatory function definition to lowercase
  #8. I create the list list, which has as its elements the characters of the lowercase string, separated by the space character
def TxtProc(text):
  punctuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
  conj_word_freq={}
  greek_list=[]
  non_greek_lst=[]
  temp=[]
  conjuction_list=['και','κι','είτε','ή','δηλαδή','πως','που','ότι']
  lowercase= text.lower()
  list=lowercase.split()

 # for each word in the list from the beginning to the end, remove from the ends of each word the characters of the Punctuation variable, so that each item in the list has been cleared of possible punctuation
  for i in range(0,len(list)):
    list[i]=list[i].strip(punctuation)

  #For each word in the list of microprinted words the counter is initialized with 0   #For each character in the word, if that character is not one of the lowercase Greek characters, increase the counter by 1.
  #If after the first iteration structure and the flow check within the word, a word is found that has no non-Greek characters at all, it means that it is Greek , so add it to the greek_list.
  #Otherwise, if 1) it contains non-Greek characters and 2)it is not in the temp list temp,
    #add it to both the temp and non-greek list.
  for word in list:
    count=0    #For each word the counter is initialised wih 0
    for char in word:
      if char not in 'αβγδεζηιθικλμνξοπρσςτυφχψωάέήίόύώϊϋΐ':
        count +=1   #add 1 to the counter
    if count==0:
      greek_list.append(word)
    else:
      if word not in temp:
        non_greek_lst.append(word)
        temp.append(word)

  # for each link in the list of links, fill the empty dictionary conj_word_freq with each link as a key and give each key the number of occurrences of each link in the list of Greek words  for conj in conjuction_list:
    conj_word_freq[conj]=greek_list.count(conj)
  #Set the variable length to the total number of words of the cleaned Greek text     
  #Set the variable sum_conj_word_freq to the sum of the dictionary values
  #Calculate the percentage of occurrence of the links in the list in the input cleaned text
  #Round the resulting percentage by 2 decimal places
  #The function returns a list with the rounded percentage of occurrence of links in the Greek text and the second is the list of non-Greek words
  
  length=len(greek_list)
  sum_conj_word_freq=sum(conj_word_freq.values())
  conj_word_freq_percentage=(100* sum_conj_word_freq)/length
  round_conj_word_freq_percentage=round(conj_word_freq_percentage,2)
  return [round_conj_word_freq_percentage, non_greek_lst]

#I assign to the variables sentence 1 and sentence 2 two texts respectively.     
#I call the function for each text separately, assigning it to a variable l.
#Type the text of the utterance and since the function returns a list, I can use list indexing to access the requested information.

sentence1='Οι ereνητές, με επικεφαλής την επίκουρη καθηγήτρια Emily Smith της Σχολής Δημόσιας Υγείας του Πανεπιστημίου George Washington, που έκαναν τη σχετική δημοσίευση στο βρετανικό ιατρικό περιοδικό "BMJ Global Health", ανέλυσαν στοιχεία από 12 μελέτες που αφορούσαν συνολικά 13.136 έγκυες σε 12 χώρες του κόσμου.'
sentence2="Ο Lane δήλωσε επίσης πως οι κυβερνήσεις της ευρωζώνης, οι οποίες ξοδεύουν τώρα υπερβολικά πολλά σε επιδόματα, θα πρέπει να αναλάβουν ένα μεγαλύτερο ρόλο στην καταπολέμηση του πληθωρισμού. Ο πληθωρισμός θα μειωθεί γρήγορα φέτος, αλλά -το θέμα είναι πώς θα πας εγκαίρως από το 3,5% στο τέλος του 2023 στο στόχο του 2%-, δήλωσε ο Lane. (Εδώ θα είναι σημαντική η πολιτική των επιτοκίων, για να εξασφαλιστεί πώς θα διανυθεί το τελευταίο χιλιόμετρο της επιστροφής στο στόχο)."

l=TxtProc(sentence1)
print("Input text processed = ", sentence1)
print('Percentage of conjuctions-to-search in text entered after cleaning= ',l[0], "%")
print('Non GR Tokens found = ', l[1])
print()
l=TxtProc(sentence2)
print(f'Input text processed = ', sentence2)
print('Percentage of conjuctions-to-search in text entered after cleaning= ',l[0], "%")
print('Non GR Tokens found = ', l[1])


