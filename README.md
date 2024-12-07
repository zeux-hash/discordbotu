# Discord Bot - Features and Setup

## Overview

This is a simple Discord bot built using **Python** and **discord.py**. It offers several useful features such as math operations, image sharing, and fun commands for user interaction. The bot is easy to set up and can be customized to suit your server's needs.

---

## Features

### 1. **Greetings**
- **`$hello`**: Greets the user with a friendly message.

### 2. **Math Commands**
- **`$add <number1> <number2>`**: Adds two numbers together and returns the result.
  
### 3. **Recycling Helper**
- **`$cop <item>`**: Suggests the correct recycling bin for items like plastic bottles, paper, or metal objects.

### 4. **Random Image Commands**
- **`$mem`**: Sends a random image from a predefined directory of meme images.
- **`$animal`**: Sends a random image of an animal from a predefined directory of animal images.
- **`$duck`**: Fetches and shares a random duck image from the Random-D UK API.

### 5. **Randomization Commands**
- **`$roll <NdN>`**: Rolls a dice in the format `NdN` (e.g., `2d6` for two 6-sided dice).
- **`$choose <choice1> <choice2> ...`**: Chooses randomly between multiple choices provided by the user.
- **`$repeat <times> <message>`**: Repeats a message a specified number of times.
- **`$heh <count>`**: Sends a "he" repeated `count` times. (Default count is 5)

### 6. **User Information**
- **`$joined <member>`**: Tells you when a member joined the server.

---

## Prerequisites

Before running the bot, make sure you have the following installed:

- **Python 3.8+**: Download and install Python from the [official website](https://www.python.org/downloads/).
- **discord.py library**: Install the library by running:
  ```bash
  pip install discord.py
