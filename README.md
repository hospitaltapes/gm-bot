# FWB GM Bot
This is a simple Discord bot that monitors a specific channel and reacts with a sun emoji to any message that starts with "gm".

## Installation

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Create a new Discord bot and add it to your server. You can follow the instructions [here](https://discordpy.readthedocs.io/en/stable/discord.html).
4. Rename `config.example.py` to `config.py` and fill in the required fields.
5. Run the bot using `python main.py`.

## Configuration

The `config.py` file contains the following fields:

- `TOKEN`: The Discord bot token.
- `CHANNEL_ID`: The ID of the channel that the bot should monitor.

## Usage

Once the bot is running, it will monitor the specified channel and react with a sun emoji to any message that starts with "gm" or "Gm". 

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
