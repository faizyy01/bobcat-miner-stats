# bobcat miner statistics 

Discord bot to display Helium bobcat miner statistics. 


<img src="https://github.com/Sleepingpirates/bobcat-miner-stats/blob/main/screenshot.png?raw=true">

Commands: 

```
!stats (takes upto 10 seconds to respond.)
Display bobcat miners statistics 
```

# Setup 

**1. Enter discord bot token and miner ip in bot.env**

**2. Install requirements**

```
pip3 install -r requirements.txt 
```
**3. Start the bot**
```
python3 run.py
```

# Docker Setup & Start

1. First pull the image 
```
docker pull piratify/helium:latest
```
2. Make the container 
```
docker run -d --restart unless-stopped --name helium -e "discord_bot_token=YOUR_DISCORD_TOKEN_HERE" -e "miner_ip=miners_ip_here" piratify/helium:latest
```
