import yadisk
# Получаем токен для яндекс диска, скачиваем фото
def get_link(name):
    y = yadisk.YaDisk(token = "y0_AgAAAABff34NAAvNqwAAAAEFIlSlAADCv0vl33hIO5RIl6Z52klhvDBrPg")
    return y.get_download_link(f'cv test task/{name}')

def get_from_link(link):
    y = yadisk.YaDisk(token = "y0_AgAAAABff34NAAvNqwAAAAEFIlSlAADCv0vl33hIO5RIl6Z52klhvDBrPg")
    y.download_by_link(link, 'photo.jpg')
    
def upload_to_disk(name):
    y = yadisk.YaDisk(token = "y0_AgAAAABff34NAAvNqwAAAAEFIlSlAADCv0vl33hIO5RIl6Z52klhvDBrPg")
    y.upload(name, f'cv test task/{name.split("/")[-1][:-4]}-segmented.jpg')

def clear_results():
    y = yadisk.YaDisk(token = "y0_AgAAAABff34NAAvNqwAAAAEFIlSlAADCv0vl33hIO5RIl6Z52klhvDBrPg")
    y.remove('cv test task/photo-segmented.jpg')