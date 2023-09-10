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

#Κρατάω τον σκελετό της συνάρτησης TxtProc και δηλώνω τη μεταβλητη TxtToProcess ως global μέσα στη συνάρτηση, ώστε η συνάρτηση να έχει
#πρόσβαση σε αυτήν.
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

  #Για κάθε σύνδεσμο στη λίστα των στοχευόμενων συνδέσμων, μέτρα πόσες φορές αυτός εμφανίζεται στη λίστα με τις καθαρισμένες ελληνικές λέξεις
  #Αν ο σύνδεσμος δεν βρεθεί 0 φορές στη λίστα, πρόσθεσέ τον στο λεξικό conj_word_freq με key τον ίδιο τον σύνδεσμο και value την συχνότητα εμφάνισής του στη λίστα.
  for conj in conjuction_list:
    appeared_conj=greek_list.count(conj)
    if appeared_conj !=0:
      conj_word_freq[conj]=appeared_conj

  length=len(greek_list)
  sum_conj_word_freq=sum(conj_word_freq.values())
  conj_word_freq_percentage=(100* sum_conj_word_freq)/length
  round_conj_word_freq_percentage=round(conj_word_freq_percentage,2)

#Αν η τιμή του ορίσματος της συνάρτησης είναι True
 #1. Χρησιμοποιώ τη συνάρτηση sorted, διατρέχω ταυτόχρονα κλειδιά και τιμές του λεξικού conj_word_freq με τη μέθοδο .items()
  # Θέτω στο optional όρισμα key ως τιμή μια ανώνυμη συνάρτηση που επιστρέφει το στοιχείο του λεξικού με βάση το οποίο θα γίνει η ταξινόμηση. Η ανώνυμη συνάρτηση επστρέφει μέσω Indexing 
  #τις τιμές του λεξικού.
  #Θέτω το optional όρισμα Reverse=True για να πετύχω την ταξινόμηση των στοιχείων του λεξικού με βάση την φθίνουσα σειρά των τιμών του.
  #Επειδή η μέθοδος sorted επιστρέφει λίστα των ταξινομημένων στοιχείων, με τη μέθοδο dict την μετατρέπω σε λίστα
  #2. Η συνάρτηση θα επιστρέφει μια λίστα με στοιχεία της τις ζητούμενες πληροφορίες της εκφώνησης
#Αν η τιμή του ορίσματος της συνάρτησης είναι False:
  # η συνάρτηση επιστρέφει μια λίστα με τις ζητούμενες πληροφορές της εκφώνησης
  if detailedOutput == True:
    sorted_conjuctions_by_freq=sorted(conj_word_freq.items(),key=lambda v:v[1],reverse=True)
    conj_word_freq=dict(sorted_conjuctions_by_freq)
    return [round_conj_word_freq_percentage, non_greek_lst,length,sum_conj_word_freq,conj_word_freq]
  else:
    return [round_conj_word_freq_percentage, non_greek_lst]

#Καλώ τη συνάρτηση για κάθε Boolean τιμή του ορίσματος detailedOutput ξεχωριστά, αναθέτοντας την σε μια μεταβλητή l.
#Τυπώνω το κείμενο καλώντας την global μεταβλητή TxtToProcess
#Τυπώνω το κείμενο της κάθε εκφώνησης και εφόσον η συνάρτηση επιστρέφει λίστα, μπορώ μέσω list indexing να έχω πρόσβαση στην ζητούμενη πληροφορία.
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

