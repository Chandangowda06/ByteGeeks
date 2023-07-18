from  nltk.chat.util import Chat, reflections
import nltk
from sys import version_info
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer


nltk.download('all')
pairs = [
    [
        r"hello chandu",
        ['Hi there you can get more details about chandu here https://www.aparichita.tech',]
    ],
    [
        r"What is your company name?",
        ['Our company is ByteGeeks.chandu a team leader who created me',]
    ],
    [
        r"help me",
        ['Hello! how can i help you',]
    ],
     [
        rpavana height will grow",
        ['Illa chanceye illa no way she is a limited height edition',]
    ],
    [
        r"why are you here?",
        ['Hi there! am here to assist you',]
    ],
    [
        r"What is your  name?",
        ['My name is chandu',]
    ],
    [
        r"ByteGeeks",
        ['ByteGeeks is our company name',]
    ],
    [
        r"what is meaning for ByteGeeks",
        ['Where "byte" symbolizes our mastery of system memory and "geeks" reflects our unwavering passion for all things computer-related. Together, we embody a team driven by technical prowess and an insatiable curiosity to explore the realms of technology.',]
    ],
    [
        r"information about your developers team",
        ['Our talented developers, led by Chandan, including Pavana, Ananya, and Gayathri, form a formidable team that consistently delivers exceptional results. Together, we leverage our expertise and passion to push the boundaries of innovation and achieve remarkable milestones in our projects.',]
    ],
    [
        r'what is your purpose job work',
        ["I'm here to make your shopping experience easier. Let me know if there's anything I can do to assist you",]
    ],
    [
    r'How many shops are there in this mall?',
    ['576 shops are avialble till now',]
    ],
    [
    r'Thank you',
    ["You're welcome! I'm glad I could assist you. If you have any more questions, feel free to ask.",]
    ],
    [
    r'What are the mall operating hours?',
    ['The mall is open from 9:00 am to 10:00 pm every day. ',]
    ],
    [
    r'Where can I find the parking area?',
    ['The parking area is located at ground floor of the mall move 200m straight then take down',]
    ],
    [
    r'Are there any ATMs in the mall?',
    ['Yes, we have ATMs located on 1st floor.',]
    ],
    [
    r'How many floors does the mall have?',
    ['The mall has 8 floors.',]
    ],
    [
    r'Are there any restrooms or washrooms in the mall?',
    ['Yes, we have restrooms located on each floor of the mall for your convenience.',]
    ],
]
def unique(list1):
    # intilize a null list
    unique_list = []
    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    return(unique_list)
lemmatiser = WordNetLemmatizer()

def preprocessing (sent) :
    rem_words = ['get', 'avail', 'who' , 'where', 'how' , 'what', 'why' , 'when', 'I', 'can']
    ##print(sent)
    # remove punctuation
    # convert to lower
    for p in list(punctuation):
        sent=sent.replace(p,'')


    sent=sent.lower().split()
    #remove stop words 
    stop_words = set(stopwords.words('english'))
    sent = [i for i in sent if not i in stop_words]
    sent = [i for i in sent if not i in rem_words]
    # lemmitise 
    #[item.upper() for item in mylis]
    sent = [lemmatiser.lemmatize(item, pos="v") for item  in sent ]
    return(unique(sent))
def tellme_bot(response):
    while(1):
        if response == 'q':
            break
        i=0
        chosen = len(pairs) 
        matches = 0
        list_response=preprocessing(response) 
        while (i<len(pairs)):
            loc_matches = 0 
            x=pairs[i][0] + "  ".join(pairs[i][1])
            list_pair=preprocessing(x)
            for word in list_pair:
                if word in list_response:
                    loc_matches=loc_matches+1
            if ( loc_matches > matches ):
                chosen = i 
                matches = loc_matches
            i = i + 1 
        if ( chosen <len(pairs) ) :
            ans=pairs[chosen][1]
            return (ans[0]) 
        else :
            return ("Unable to answer this question" ) 
