Clone the repository or create a new project.
Install the required dependencies as mentioned in the prerequisites.
Replace the existing code in the target file with the provided code.
Ensure you have a valid Discord bot token. If not, create a new bot application on the Discord Developer Portal.
Replace the 'BOT_TOKEN' placeholder in the code with your actual Discord bot token.
Start your bot application using a Node.js runtime.
Once the bot is up and running, you can use the /nike command followed by the SKU of the Nike product to retrieve information about it.


/nike --sku ABC123
The bot will respond with an embedded message containing details about the Nike product, including its title, status, price, release date, stock levels, and relevant links. In case the SKU is not found, an error message will be displayed.
