# -------- Slot Machine -------- #

import random
import streamlit as st

# -------- Page Layout -------- #

st.set_page_config(
    page_title="Slot Machine",
    page_icon="🎰",
    layout="wide",
    initial_sidebar_state="auto",
)

MAX_BET = 100
MIN_BET = 1
ROWS = 3  # items in each reel
COLS = 3  # number of reels

symbols_count = {"A": 5, "B": 3, "C": 2, "D": 8, "E": 4, "F": 9, "G": 4, "H": 11}

# The rarer the symbol, the higher its value
symbols_value = {"A": 4, "B": 6, "C": 7, "D": 3, "E": 5, "F": 2, "G": 5, "H": 1}

# -------- Session state -------- #
    # Streamlit forgets variable on every rerun
    # This sets default value in the session value the first time the app loads, so they survive rerun
if "balance" not in st.session_state:
    st.session_state.balance = 0
    st.session_state.last = None #Result of last rerun


# -------- Callback -------- #
    # Executes when a add fund button is clicked
def add_funds(deposit_amount):
    st.session_state.balance+=deposit_amount

# -------- Set up reel Symbols -------- #
def reel_value():
    temp_list=[]
    for symbol,freq in symbols_count.items():
        for _ in range(freq):
            temp_list.append(symbol)


    reels=[]
    for _ in range(COLS):
        t_list = temp_list[:]
        reel=[]
        for _ in range(ROWS):
            value = random.choice(t_list)
            t_list.remove(value)
            reel.append(value)

        reels.append(reel)

    # reels is a list of lists: one inner list per reel (column).
    # Each inner list holds the symbols visible on that reel, top to bottom.
    #
    # Example with COLS = 3 and ROWS = 3:
    # reels = [
    #     ["A", "A", "B"],   # reel 1
    #     ["B", "C", "C"],   # reel 2
    #     ["F", "H", "D"],   # reel 3
    # ]

    return reels
# -------- Winning Logic ------- #
def check_winning(reels,lines,bet):
    winning=0
    winning_line=[]
    for line in range(lines):
        symbol=reels[0][line]
        for reel in reels:
            symbol_to_check=reel[line]
            if symbol!=symbol_to_check:
                break
        else:
            winning=winning+symbols_value[symbol]*bet
            winning_line.append(line+1)

    return winning,winning_line
# -------- Spin -------- #
def spin():
    lines=st.session_state.lines
    bet=st.session_state.bet

    total_bet=lines*bet

    reels=reel_value()
    winning,winning_lines=check_winning(reels,lines,bet)

    st.session_state.balance+=winning-total_bet

    st.session_state.last={
        "reels":reels,
        "winning":winning,
        "winning_lines":winning_lines,
        "total_bet":total_bet,
    }


st.title("Text Based Slot Machine",icon="🎰")

# -------- Sidebar -------- #
with st.sidebar:
    st.title("Wallet")
    st.metric("Balance", f"${st.session_state.balance}",icon="💸")
    amount_deposit=st.number_input("Deposit Amount $",min_value=0,step=10,value=100)
    st.button("Add funds",on_click=add_funds,args=[amount_deposit])


# -------- Betting Control -------- #
col1,col2=st.columns(2)
with col1:
    col1.radio(
        "Lines to bet on:",
        [1,2,3],
        index=None,
        key="lines"
    )

col2.number_input(
    f"Bet per line ($) [{MIN_BET} - {MAX_BET}]",
    min_value=MIN_BET,
    max_value=MAX_BET,
    step=5,
    value=10,
    key="bet",
)

col2.caption(f"Bet per line: ${st.session_state.bet}")

if st.session_state.lines is None:
    st.info("Please select the number of lines to bet on:")
    total_bet=0
else:
    total_bet=st.session_state.lines*st.session_state.bet

st.write(f"**Total Bet:**${total_bet}")

can_spin=(
        st.session_state.lines is not None and
        st.session_state.balance>=total_bet
)

if st.session_state.balance == 0:
    st.info("Deposit some money in the sidebar to start playing.")
elif st.session_state.lines is None:
    st.info("Please select the number of lines to bet on.")
elif not can_spin:
    st.warning(f"Not enough balance. Your balance is ${st.session_state.balance}.")

st.button("🎰 Spin", on_click=spin, disabled=not can_spin, type="primary")


# -------- Result of Last Spin -------- #
last=st.session_state.last
if last:
    reel_col=st.columns(COLS)

    for col,reel in zip(reel_col,last["reels"]):
        for row,sym in enumerate(reel):
            won=(row+1) in last["winning_lines"]
            if won:
                color="green"
            else:
                color="inherit"
            col.markdown(
                f"<h1 style='text-align:center; color:{color};'>{sym}</h1>",
                unsafe_allow_html=True,
            )


    net=last["winning"]-last["total_bet"]
    if last["winning"] > 0:
        lines_won = ", ".join(str(n) for n in last["winning_lines"])
        st.success(f"You won ${last['winning']} on line(s): {lines_won} (net {net:+d})")
    else:
        st.error(f"No win this time. You lost ${last['total_bet']}.")