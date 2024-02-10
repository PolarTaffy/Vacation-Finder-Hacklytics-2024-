import streamlit as st
prompt = ""

st.title("Tour Around the World!")
st.header("Let's talk about your trip details.")

numPeople = st.number_input("How many people are coming?", min_value=1)
budget = st.slider("What's your budget?", 100, 10000)





# methods
def returnOutput(prompt):
    
    prompt = "Plan an affordable vacation on a $" + str(budget) + ' for ' + str(numPeople) + ' people.'
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





