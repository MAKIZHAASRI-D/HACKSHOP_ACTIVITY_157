import random
import streamlit as st



def user_guessing():

    min_range = st.number_input("Enter the minimum range:", key="min_range", step=1)
    max_range = st.number_input("Enter the maximum range:", key="max_range", step=1)


    if min_range >= max_range:
        st.error("Minimum range must be less than maximum range.")
    else:
        if 'random_number' not in st.session_state:
            st.session_state.random_number = random.randint(min_range, max_range)


    no_of_attempts = st.number_input("Enter the number of attempts you want:", step=1,value=0)
    def game():
        if st.button("Check"):
                st.session_state.attempted += 1
                if guessing_number ==  st.session_state.random_number:
                    st.write(f"the number that should be guessed is { st.session_state.random_number}")
                    st.success("You have won!")
                else:
                    remaining_attempts = no_of_attempts - st.session_state.attempted
                    if remaining_attempts > 0:
                        st.warning(f"Wrong guess! You have {remaining_attempts} attempts left.")
                    else:
                        st.error(f"You've used all your attempts! The correct number was {st.session_state.random_number}.")
                        st.session_state.attempted = 0
                        st.write("Game over! Please refresh to play again.")

    


    if 'attempted' not in st.session_state:
        st.session_state.attempted = 0
    if st.session_state.attempted < no_of_attempts:
        guessing_number = st.number_input(f"Enter your guess between {min_range} and {max_range}:", key="guess_input", value=0)
        if guessing_number<=max_range and guessing_number>=min_range:
            game()
        else:
            st.warning(f"enter the number which is within the range {min_range} and {max_range}")

            
               
        
           

def computer_guessing():
    st.write("set a range between 0 to 3000")
    user_input=st.number_input("enter the target number:",step=1,value=0,key="user_input")
    min_range=st.number_input("enter the minimum value:",step=1,value=0)
    max_range=st.number_input("enter the maximum value:",step=1,value=0)
    no_of_attempts=1
    if min_range >= max_range:
        st.error("Minimum range must be less than maximum range.")
    
    if 'guess' not in st.session_state:
        st.session_state.guess = random.randint(min_range, max_range)
    if no_of_attempts==1:
        st.write(f"my guess is{st.session_state.guess}")
        if st.button("reveal answer"):
            if st.session_state.guess==user_input:
                st.write(" i have won")
            else:
                st.write(f"my target is {user_input}")
                st.write("you have won")

#    if no_of_attempts>1:
#        if 'attempts,random' not in st.session_state:
#            st.session_state.attempts = 0
#            st.session_state.random=random.randint(min_range,max_range)
#    while st.session_state.attempts < no_of_attempts:
#        if st.button(f"attempt :{ st.session_state.attempts}",key=f"{ st.session_state.attempts}"):
#            mid_point=(min_range+max_range)//2
#            st.write(f"my guess is {mid_point}")
#            user_response = st.text_input("enter high--if the guess is high\n low--if guess is low\nequal--if guess is equal",key=f"user_response {st.session_state.random}")
#            st.session_state.attempts+=1
#            if user_response.lower()=="high":
#                max_range=mid_point-1
#            elif user_response.lower()=="low":
#                min_range=mid_point+1
#            elif user_response.lower()=="equal":
#                st.write(f"my guess is {mid_point}")
#                if st.button("reveal answer"):
#                    st.write(f"your target is {user_input}")
#                    st.write("i won")
            



computer_guessing()
st.markdown("[project](C:\\Users\\L E N O V O\\Desktop\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157-1\\ACITVITY.PY)")

st.markdown('<a href="C:\\Users\\L E N O V O\\Desktop\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157-1\\ACITVITY.PY" >Project</a>', unsafe_allow_html=True)


# Assuming ACTIVITY.py is in the same directory as your Streamlit app
with open("C:\\Users\\L E N O V O\\Desktop\\HACKSHOP_ACTIVITY_157\\HACKSHOP_ACTIVITY_157-1\\ACITVITY.PY", "rb") as file:
    st.download_button(
        label="Download Project",
        data=file,
        file_name="ACTIVITY.py",
        mime="text/x-python"
    )
