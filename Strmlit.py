import streamlit as st


prompt = ""

def welcomeText():
    
    st.title("Tour Around the World!")
    st.header("Let's talk about your trip details.")

welcomeText()


#THE USER INPUTS

numPeople = st.number_input("How many people are coming?", min_value=1)  #number of people going 
    
    
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



    



                              





# methods
def returnOutput(prompt):
    
    prompt = "Plan an affordable vacation on a $" + str(budget) + ' for ' + str(numPeople) + ' people. I want a ' + urbRur + ' place and ' + nightlife + " " + family
    aiResponse = "Not yet implemented"

    st.header("Prompt (Debug Purposes)")
    st.write(prompt)

    st.header("AI Response")
    st.write('Generating...')
    st.write(aiResponse)


st.divider()
if st.button("Plan my vacation!"):
    returnOutput("")

# feed the promp into





