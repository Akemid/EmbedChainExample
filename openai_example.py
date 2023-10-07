from embedchain import App
from embedchain.config.add_config import AddConfig, LoaderConfig

valtx_bot = App()

config = AddConfig()
config.loader = LoaderConfig(language="es")

youtube_videos = [
    "https://youtu.be/ssb3vYbdNuE",
    "https://youtu.be/CW1N9p1ExQg",
    "https://youtu.be/RrBaJYk_L6c",
]

webpages = [
    "https://www.infobae.com/peru/2023/10/06/corte-masivo-de-agua-en-la-mitad-de-lima-menos-en-estos-distritos-conoce-en-donde-no-se-suspendera-el-servicio/"
]
# Embed Online Resources
for webpage in webpages:
    valtx_bot.add(webpage)

for youtube_video in youtube_videos:
    valtx_bot.add(youtube_video, config=config)

chat = True
while chat:
    question = input("Chat:")
    if question == "salir":
        chat = False
    response = valtx_bot.chat(question)
    print(response)
