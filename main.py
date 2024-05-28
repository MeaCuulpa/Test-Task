from db_main import create_tables, insert_url, get_url, insert_segm_url
from yadi import get_link, get_from_link, upload_to_disk, clear_results
from yolov8 import model

create_tables() #создаем таблицу (если существует, то заново)

insert_url(get_link('photo.jpg')) #получаем ссылку на скачивания фото с яндекс диска и вставляем в таблицу

get_from_link(get_url(1)) #скачиваем фото с яндекс диска

model.predict('photo.jpg', save = True) #сегментируем фото

upload_to_disk('runs/segment/predict/photo.jpg') #загружаем результат на яндекс диск

insert_segm_url(get_link('photo-segmented.jpg'), 1) #вставляем в таблицу ссылку на скачивание

#clear_results() #удаляет фото с яндекс диска, для отладки
