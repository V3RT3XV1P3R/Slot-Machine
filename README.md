# 🎰 Slot Machine

A slot machine game built with Python and [Streamlit](https://streamlit.io/). Deposit virtual funds, choose how many lines to bet on, spin the reels, and see whether you win.

> **Note:** This is a learning project. It uses virtual money only and has no real-money gambling.

## Features

- Wallet in the sidebar to deposit virtual funds
- Bet on 1 to 3 lines, with a bet range of $1 to $100 per line
- 3×3 reel grid with randomly generated symbols
- Winning lines highlighted in green
- Win/loss summary showing your net profit or loss for each spin
- Balance maintained across interactions using Streamlit session state

## How the Game Works

1. Deposit funds from the sidebar.
2. Choose the number of lines to bet on (1 to 3) and the bet amount per line.
3. Click **Spin**. The machine fills a 3×3 grid, where each column is a reel.
4. A line wins when all three symbols in that row match across the three reels.
5. Winnings for each winning line = symbol value × bet per line.

### Symbol Counts and Values

| Symbol | Count | Value |
|:---:|---:|---:|
| A | 5 | 4 |
| B | 3 | 6 |
| C | 2 | 7 |
| D | 8 | 3 |
| E | 4 | 5 |
| F | 9 | 2 |
| G | 4 | 5 |
| H | 11 | 1 |

## Getting Started

### Prerequisites

- Python 3.9 or newer
- pip

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/V3RT3XV1P3R/Slot-Machine.git
   cd Slot-Machine
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

   Activate it on Windows:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

### Run the App

Run the following command from the project directory:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local URL, usually http://localhost:8501, where you can play the game.

## Project Structure

```text
.
├── app.py
├── requirements.txt
└── README.md
```

- `app.py` — Streamlit slot machine application
- `requirements.txt` — Python package dependencies
- `README.md` — Project documentation

## Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)

## Possible Improvements

- Add spin animations
- Save high scores
- Add sound effects
- Allow players to customize symbols and payouts

## License

This project is intended for learning and personal use. No license has been specified yet.
