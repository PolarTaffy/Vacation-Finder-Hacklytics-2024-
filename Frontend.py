import streamlit as st
import re
import time
import languagemodels as lm
lm.config["max_ram"] = "4gb"



prompt = ""

def welcomeText():   
    st.title("Tour Around the World!")
    st.header("Let's talk about your trip details.")
    st.subheader("Fill out this form to generate a dream vacation for you!")

welcomeText()


def runModel(prompt):
    formatted_prompt = (
    f"A chat between a client looking for ONE vacation spot for an upcoming trip and an artificial intelligence assistant."
    f"The assistant gives a helpful and detailed travel itinerary for a random location that fits the client's specifications. It should include specific activities one can do in the location and the activities should be cost-appropriate for the budget. The response should not be cut off. After each day, put the rest of your response on a new line.\n"
    f"### Human: {prompt} ### Assistant:")
    return lm.do(formatted_prompt)

def dayList(prompt):
    paragraph = runModel(prompt)
    paraList = re.split(r'(?=\bDay\b)', paragraph)

    return paraList
    




#THE USER INPUTS
# TODO Add day count, split up responses into paragraphs, make region list functional, ADD NAMES 
#number inputs
numPeople = st.number_input("How many people are coming?", min_value=1)  #number of people going 
dayCount = st.number_input("How long do you want to be away?", min_value=1) #days staying there 
    
    
budget = st.slider("What's your budget?", 100, 10000)  #the budget starting from 100 to 10000
urbanRural = st.slider("How urban/rural do you prefer your destination to be? 0 being very urban and 100 to being very rural.", 0, 100) # degree of rural/urban
urbRur = ""
if urbanRural >= 80:
    urbRur = "very rural"
elif urbanRural >= 60:
    urbRur = "rural"
elif urbanRural >= 40:
    urbRur = "a balance between urban and rural"
elif urbanRural >= 20:
    urbRur = "urban"
else:
    urbRur = "very urban"

isNightlife = st.checkbox("Nightlife?")  #yes or no on nightlift 
nightlife = ""
if isNightlife:
    nightlife = "I want a nightlife."
else:
    nightlift = "Nightlift is not necessary for me."

familyFriendly = st.checkbox("Family Friendly?") # yes or no on family friendly
family = ""
if familyFriendly:
    family = "I want the location to be family friendly."
else:
    family = "The location does not have to family friendly."

cultureConnect = st.checkbox("Would you like to learn and experience the culture of the region?")
if cultureConnect:
    cultureSlider = st.slider("How cultural would you like the region to be? 0 being a little and 100 being a lot.", 0, 100)


regions = ["North America", "South America", "Australia", "Asia", "Africa", "Europe"]
desiredRegions = st.multiselect("What region of the world would you prefer?", regions) #can select multiple regions in which they can travel to
st.write('You selected:', desiredRegions)
regionStr = ""
for i in range(desiredRegions):
    regionStr += desiredRegions[i]
    if i != (len(desiredRegions) + 1):
        regionStr += " ,"




# methods
def returnOutput(prompt):
    
    prompt = "Plan an affordable vacation on a $" + str(budget) + ' for ' + str(numPeople) + ' people that lasts for ' + str(dayCount) + '. I want a ' + urbRur + ' place and ' + nightlife + " " + family + " These are the regions I prefer: " + regionStr + "."

    st.header("Prompt (Debug Purposes)")
    st.write(prompt)

    st.header("AI Response")
    placeholder = st.empty()
    placeholder.text("Generating...")
    
    daysActivity = dayList(prompt)
    
    placeholder.text("Here is your dream vacation!")
    time.sleep(2)
    placeholder.empty()

    for i in range(daysActivity):
        if i == 0:
            st.write(daysActivity[i])
            continue
        st.write("- " + daysActivity[i])

        


st.divider()
if st.button("Plan my vacation!"):
    returnOutput("")

# feed the promp into



#side bar links PUT YOUR INFO
def links_section():
    st.sidebar.header("Links")


    st.sidebar.text("Connect with us on Linkedin")
    linkedin_link = f'<a href="{"https://www.linkedin.com/in/william-li-b0142b290/"}"><img src = "{"https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"}" alt = "LinkedIn" width = "75" height = "75">'
    st.sidebar.markdown(linkedin_link, unsafe_allow_html=True)

    linkedin_link1 = f'<a href="{"https://www.linkedin.com/in/evan-thomas-68b93a247/"}"><img src = "{"https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg"}" alt = "LinkedIn" width = "75" height = "75">'
    st.sidebar.markdown(linkedin_link1, unsafe_allow_html=True)


    st.sidebar.text("Checkout our work")
    github_link = f'<a href="{"https://github.gatech.edu/williamli12"}"><img src = "{"https://cdn-icons-png.flaticon.com/256/25/25231.png"}" alt = "Github" width = "65" height = "65">'
    st.sidebar.markdown(github_link, unsafe_allow_html=True)

    github_link1 = f'<a href="{"https://github.com/PolarTaffy"}"><img src = "{"https://cdn-icons-png.flaticon.com/256/25/25231.png"}" alt = "Github" width = "65" height = "65">'
    st.sidebar.markdown(github_link1, unsafe_allow_html=True)


    st.sidebar.text("Or email us!")
    email_html = f'<a href="{"liwilliam12@gmail.com"}"><img src = "{"https://logowik.com/content/uploads/images/513_email.jpg"}" alt = "Email" width = "75" height = "75">'
    st.sidebar.markdown(email_html, unsafe_allow_html=True)

    email_html1 = f'<a href="{"thomasevan1248@gmail.com"}"><img src = "{"https://logowik.com/content/uploads/images/513_email.jpg"}" alt = "Email" width = "75" height = "75">'
    st.sidebar.markdown(email_html1, unsafe_allow_html=True)

    
links_section()




