const Discord = require('discord.js');
const client = new Discord.Client();

client.on('ready', () => {
    console.log('Jsem připraven');
});

client.on('message', message => {
    if (message.content === '!vip') {
    	message.reply('V.I.P stojí 20 kč');
  	}
});

// THIS  MUST  BE  THIS  WAY
client.login(process.env.BOT_TOKEN);
