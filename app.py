import streamlit as st

st.title("🌟 Dost-e-bot for Starcool Industries 🌟")
st.write("Namaste, Satshri Akal, Khama Ghani, Ram Ram, Adab! 🤗")
st.write("You can ask me basic questions. Type 'bye' to exit.\n")

# chatbot memory (dictionary of responses)
it_ResponseAs = {
    "hello": "Hi, you are welcome. How did you come here today?",
    "hi": "Hi, you are welcome. How did you come here today?",
    "how are you": "I am good, thank you.",
    "who are you": "I am a smart chatbot for Starcool Industries.",

    "what work is available in starcool industries":
        "We work in kitchen equipment like ovens, refrigerators, coffee machines, bakery and display counters, popcorn machines and many more items.",
    "what actually you are":
        "We are manufacturers, wholesalers, retailers and exporters of kitchen equipment.",

    "tell more about the company":
        "STAR COOL Industry is a trusted and well-established name in the commercial kitchen equipment sector. The company was founded 25 years ago by Mr. Kapil Sharma, who is also the current CEO of Balaji Cool. With decades of innovation, STAR COOL Industry provides premium-grade Stainless Steel 304 commercial kitchen equipment and is ISO certified. We specialize in water cooler manufacturing and supply to hotels, restaurants, offices, schools, hospitals, and industrial kitchens across India.",

    "contact number": "You can contact us on this number: 9414089765.",
    "contact details": "For more contact details, you can contact us on this number: 7696969620.",
    "address": "You can visit us at- 88, Bapu Nagar, Tiny Tots Road"
}

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in it_ResponseAs:
        if eachKey in userQuestion:
            return it_ResponseAs[eachKey]
    return "I am not aware about it yet. Please ask something else."

# chat UI
user_input = st.text_input("Ask your question:")

if user_input:
    if "bye" in user_input.lower():
        st.success("Bye! Thank you for visiting Starcool Industries.")
    else:
        reply = getResponseOfBot(user_input)
        st.write("### Bot Response:")
        st.info(reply)
