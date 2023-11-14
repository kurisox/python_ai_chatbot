# chatbot

[Chatbot-Doku](https://www.youtube.com/watch?v=PMFf9FwPN70&t=1777s)

Docker-Version is work in progress

# Project-Start
## Requierements
- python 3:11

## Start-Up

1. [Create a discord bot](https://discordpy.readthedocs.io/en/stable/discord.html) 
2. create .env file in chatbot with following entries:
   - DBUSER: username for the db
   - PASSWORD: password for the db
   - DATABASE: database name
   - PORT: port of the db
3. chatbot(terminal): "docker-compose -f database.yaml up -d" to start the database. "docker-compose -f database.yaml down" to stop the database
4. chatbot(terminal): pip install virtualenv
5. chatbot(terminal): virtualenv venv
6. chatbot(terminal): source venv/bin/activate
7. chatbot(terminal): pip install -r requirements.txt
8. create .env file in chatbot/llama-api/scripts with following entries:
   - DOWNLOAD_URL=link to language model (model.gguf file. for example https://huggingface.co/TheBloke/WizardLM-13B-V1.2-GGUF/resolve/main/wizardlm-13b-v1.2.Q2_K.gguf?download=true)
   - DESTINATION_PATH=../language_model/
   - FILE_LOCATION=../language_model/language model file.gguf
9. chatbot(terminal); ./llama-api/scripts/download_language_model.py
10. chatbot(terminal); python3 -m llama_cpp.server --model ./llama-api/language_model/wizardlm-13b-v1.2.Q2_K.gguf
11. create .env file in chatbot/discordbot/scripts with following entries (only API_URL for console-bot):
    - API_URL=http://localhost:8000/v1/chat/completions
    - DISCORD_TOKEN=Token of the bot
    - HOST: hostname of the database (localhost in this example)
    - DBUSER: same username as in the docker-compose .env file
    - PASSWORD: same password as in the docker-compose .env file
    - DATABASE: same name as in the docker-compose .env file
    - PORT: same name as in the docker-compose .env file
12. chatbot(new terminal): python3 discordbot/scripts/discord_bot.py