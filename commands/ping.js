const { SlashCommandBuilder } = require('@discordjs/builders');
const axios = require('axios');
const { MessageEmbed } = require('discord.js');

module.exports = {
  data: new SlashCommandBuilder()
    .setName('nike')
    .setDescription('Get information about a Nike product.')
    .addStringOption(option => option.setName('sku').setDescription('The SKU of the Nike product.').setRequired(true)),
  async execute(interaction) {
    const sku = interaction.options.getString('sku');
    const url = `https://api.nike.com/product_feed/threads/v2?filter=language(en-GB)&filter=marketplace(IL)&filter=channelId(d9a5bc42-4b9c-4976-858a-f159cf99c647)&filter=productInfo.merchProduct.id(d1660725-3b4b-5c8d-a321-2df5def6b112,33d44ce0-cd51-5b52-bd14-28571bbdc9a5,ea391c6a-045a-5e43-8a77-bc1ab6c21301,05bf5964-0924-59f5-960c-f7556e7b1649,7d143ce9-3726-5267-9dc4-5943093a012d,5804beec-b2de-5f5d-b202-cbfac43b782f,11c4fba3-263c-5fd2-9950-9c1e63edbf62,2b1fceb1-93f3-5853-8173-6bdd8735b3c6,84b0e00d-6e65-590e-8f31-824fe54d5e6c,a6778fca-a04e-5ef8-a021-92fceaf376bc)`;

    try {
      const response = await axios.get(url);
      const product = response.data.objects[0].productInfo[0];

      const title = product.productContent.title;
      const status = product.merchProduct.status;
      const price = product.merchPrice.currentPrice;
      const releaseDate = `<t:${Math.floor(Date.parse(product.merchProduct.commercePublishDate)/1000)}:D>`;
      const isExclusiveAccess = product.merchProduct.isExclusiveAccess;
      const thumbnail = product.imageUrls.productImageUrl;
      const skuCode = product.merchProduct.styleColor;
      const lastUpdated = `<t:${Math.floor(Date.parse(product.merchProduct.modificationDate)/1000)}:F>`;
      const site = product.merchProduct.channelId === 'd9a5bc42-4b9c-4976-858a-f159cf99c647' ? 'SNKRS' : 'Nike';
      const snkrsLink = `https://invite.weziye.cn/snkrs/${skuCode}`;
      const nikeLink = `https://invite.weziye.cn/nike/${skuCode}`;
      const stockxLink = `https://stockx.com/search?s=${skuCode}`;
      const goatLink = `https://www.goat.com/search?query=${skuCode}`;
      const links = `[SNKRS](${snkrsLink}) | [Nike](${nikeLink}) | [StockX](${stockxLink})`;

      const embed = new MessageEmbed()
        .setColor('#0099ff')
        .setTitle(title)
        .setURL(`https://www.nike.com/us/launch/t/${sku}`)
        .setThumbnail(thumbnail)
        .setDescription(`SKU: ${skuCode}`)
        .addFields(
          { name: 'Status', value: status, inline: true },
          { name: 'Price', value: `$${price.toFixed(2)}`, inline: true },
          { name: 'Release Date', value: releaseDate, inline: true },
          { name: 'Exclusive Access', value: isExclusiveAccess ? 'Yes' : 'No', inline: true },
          { name: 'Last Updated', value: lastUpdated, inline: true }
        )
        .addField('Stock Levels', product.skus.map((sku, i) => `${sku.nikeSize} - ${product.availableSkus[i].level}`).join('\n'))
        .addField('Links', links)
        .setFooter('Developed by @13maxh');

      await interaction.reply({ embeds: [embed] });
    } catch (error) {
      console.error(error);
      await interaction.reply(`${sku} is not loaded on Nike.`);
    }
  },
};
