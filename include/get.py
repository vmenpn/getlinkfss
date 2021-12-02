from get_fshare import FSAPI

URL = 'https://www.fshare.vn/file/5K6WSX12VY1UZ5G?token=1636681269'

bot = FSAPI(email="hoaa20092013@gmail.com", password="Sangphe410!@")
bot.login()
sillicon_valley_ss1 = bot.get_folder_urls(URL)

for episode in sillicon_valley_ss1:
    print(episode['name'], bot.download("https://www.fshare.vn/file/{}".format(episode['linkcode'])))