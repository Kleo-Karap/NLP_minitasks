TxtToProcess='Οι erevniτές erevniτές, με επικεφαλής την επίκουρη καθηγήτρια Emily Smith της Σχολής Δημόσιας Υγείας του Πανεπιστημίου ' \
          'George Washington, που έκαναν τη σχετική δημοσίευση στο βρετανικό ιατρικό περιοδικό "BMJ Global Health",' \
          ' ανέλυσαν στοιχεία από 12 μελέτες που αφορούσαν συνολικά 13.136 έγκυες σε 12 χώρες του κόσμου.' \
          ' Η μελέτη παρέχει τα πιο εμπεριστατωμένα στοιχεία μέχρι σήμερα που δείχνουν ότι η Covid-19 συνιστά απειλή ' \
          'στη διάρκεια της εγκυμοσύνης. Τα ευρήματα μας αναδεικνύουν τη σημασία του εμβολιασμού κατά της Covid-19 για όλες' \
          ' τις γυναίκες σε αναπαραγωγική ηλικία", επεσήμανε η Dr. Smith . Τόνισε ότι δυστυχώς, χωρίς βάσιμη αιτία, ακόμη και' \
          ' μερικοί γιατροί διστάζουν να χορηγήσουν το εμβόλιο στις έγκυες. Η ανάλυση έδειξε ότι οι έγκυες που μολύνονται από τον' \
          ' κορονοϊό, έχουν επτά φορές μεγαλύτερη πιθανότητα να πεθάνουν σε σχέση με όσες δεν έχουν λοίμωξη Covid-19. ' \
          'Επίσης οι πρώτες είναι σχεδόν τέσσερις φορές πιθανότερο να χρειαστούν εισαγωγή σε μονάδα εντατικής θεραπείας (ΜΕΘ) ' \
          'και 15 φορές πιθανότερο να έχουν ανάγκη διασωλήνωσης. Ακόμη έχουν 23 φορές μεγαλύτερη πιθανότητα να διαγνωσθούν με ' \
          'πνευμονία και είναι πέντε φορές πιθανότερο να εμφανίσουν σοβαρές θρομβώσεις στο αίμα.'

#Keep the format of the TxtProc function and declare the variable TxtToProcess as global inside the function, so that the function has access to it.
def TxtProc2(detailedOutput = False):
  global TxtToProcess
  punctuation='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
  conj_word_freq={}
  non_greek_lst=[]
  greek_list=[]
  temp=[]
  conjuction_list=['και','κι','είτε','ή','δηλαδή','πως','που','ότι']
  lowercase= TxtToProcess.lower()
  list=lowercase.split()

  for i in range(0,len(list)):
    list[i]=list[i].strip(punctuation)


  for word in list:
    count=0
    for char in word:
      if char not in 'αβγδεζηιθικλμνξοπρσςτυφχψωάέήίόύώϊϋΐ':
        count +=1
    if count==0:
      greek_list.append(word)
    else:
      if word not in temp:
        non_greek_lst.append(word)
        temp.append(word)

  #For each link in the list of targeted links, count how many times it appears in the list of cleaned Greek words       
  #If the link is not found 0 times in the list, add it to the conj_word_freq dictionary with key the link itself and value the frequency of its occurrence in the list.
  for conj in conjuction_list:
    appeared_conj=greek_list.count(conj)
    if appeared_conj !=0:
      conj_word_freq[conj]=appeared_conj

  length=len(greek_list)
  sum_conj_word_freq=sum(conj_word_freq.values())
  conj_word_freq_percentage=(100* sum_conj_word_freq)/length
  round_conj_word_freq_percentage=round(conj_word_freq_percentage,2)

#If the value of the function's argument is True:        
#1. Using the sorted function, I simultaneously sort keys and values of the conj_word_freq dictionary with the .items() method
  # I set the optional key argument as the value of an anonymous function that returns the dictionary item by which to sort. The anonymous function is indexed by Indexing 
  #the values of the dictionary.
  #Set the optional argument Reverse=True to achieve the sorting of the dictionary items based on the descending order of their values.
  #Because the sorted method returns a list of the sorted items, I use the dict method to convert it to a list
#2. The function will return a list of elements with the requested information of the utterance
#If the value of the function's argument is False:
  # the function returns a list of the requested information of the utterance
  if detailedOutput == True:
    sorted_conjuctions_by_freq=sorted(conj_word_freq.items(),key=lambda v:v[1],reverse=True)
    conj_word_freq=dict(sorted_conjuctions_by_freq)
    return [round_conj_word_freq_percentage, non_greek_lst,length,sum_conj_word_freq,conj_word_freq]
  else:
    return [round_conj_word_freq_percentage, non_greek_lst]

#Call the function for each Boolean value of the detailedOutput argument separately, assigning it to a variable l.        
#Type the text by calling the global variable TxtToProcess
#Type the text of each output and since the function returns a list, I can use list indexing to access the requested information.

l=TxtProc2()
print("Input text processed = ", TxtToProcess)
print("Percentage of conjuctions-to-search in text entered after cleaning = ",l[0], "%")
print("Non GR tokens found = " ,l[1])
print()
l=TxtProc2(True)
print("Input text processed = ", TxtToProcess)
print("Word Count in cleaned text= ",l[2])
print("Conjuctions Count in cleaned text= ",l[3])
print("Percentage of conjuctions-to-search in text entered after cleaning = ",l[0], "%")
print("Conjuctions-Occurrence pairs in text entered after cleaning = ", l[4])
print("Non GR tokens found = ", l[1])

