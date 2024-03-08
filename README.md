<div align="center">
    <h1><code>TelegramRestrictionChecker</code></h1>
    <p>CLI Tool that Checks Telegram Bots, Chats, Users for any Restrictions</p>
</div>

## 📦 Installation

1. Clone the repository

    ```shell
    git clone https://github.com/TimNekk/TelegramRestrictionChecker
    ```

2. Rename [config.json.dist](config.json.dist) to `config.json`

    ```shell
    cd TelegramRestrictionChecker
    cp config.json.dist .env
    ```

3. Configure `config.json`

    - Obtain the API key by following [Telegram’s instructions](https://core.telegram.org/api/obtaining_api_id)
    - Fill in `api_id` and `api_hash` with the obtained values
    - Fill in the `usernames` with the usernames of the bots, chats, or users you want to check

4. Install the dependencies

   ```shell
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the app

```shell
python app.py
```

## 👥 Contributing

**Contributions are welcome! Here's how you can help:**

1. Fork it
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
6. Get your code reviewed
7. Merge your code
8. Get a 🌟

## 📝 License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details
