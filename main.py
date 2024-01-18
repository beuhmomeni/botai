import discord
from discord.ext import commands
from model import get_class


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file disimpan atas nama {file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] == 'cabe\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah cabe")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'cengkeh\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah cengkeh.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'jahe\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah jahe.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'kunyit\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah kunyit.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'bawang putih\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah bawang putih.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'bawang merah\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah bawang merah.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'bawang bombay\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah bawang bombay.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'pala\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah pala.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            elif hasil[0] == 'merica\n' and hasil[1] >= 0.6:
                await ctx.send("Ini adalah merica.")
                await ctx.send("harga pasarnya dapat Anda lihat disini https://hargapangan.slemankab.go.id/")

            else:
                await ctx.send("Tidak dapat mendeteksi gambar")
            

    else:
        await ctx.send('mohon maaf, tetapi anda tidak mengirim apapun')
        
bot.run("MTEzNjI2ODA2NTc4NTUyODM5MQ.GHbadg.nDgwIdDqQ2MF1g0RvPxI6KSk9wtmQd-2flysfc")