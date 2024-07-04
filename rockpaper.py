import streamlit as st
import random

def main():
    st.title("Rock Paper Scissor")
    
    st.write("Welcome to the rock paper scissor game")
    st.write("Choose your move against the computer")
    
    player_choice = st.radio("select your move:",('Rock','Paper','Scissor'))
    
    moves=['Rock','Paper','Scissor']
    computer_choice = random.choice(moves)
    
    winner = determine_winner(player_choice,computer_choice)
    
    st.write(f"you chose : {player_choice}")
    st.write(f"Computer chose: {computer_choice}")
    if winner == 'Player':
        st.success("You win")
    elif winner == 'Computer':
        st.error("Computer wins")
    else:
        st.info("It's A draw")
        
def determine_winner(player_choice, computer_choice):
    # Rock beats Scissors, Scissors beats Paper, Paper beats Rock
    if player_choice == computer_choice:
        return 'Draw'
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper') or \
         (player_choice == 'Paper' and computer_choice == 'Rock'):
        return 'Player'
    else:
        return 'Computer'

if __name__ == "__main__":
    main()
        
    