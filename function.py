from datacenter.models import *
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
import random

def get_compliment():
    compliments = [
        "Молодец!",
        "Отлично!",
        "Хорошо!",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!",
        "Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
        "Ты, как всегда, точен!",
        "Очень хороший ответ!",
        "Талантливо!",
        "Ты сегодня прыгнул выше головы!","Я поражен!",
        "Уже существенно лучше!",
        "Потрясающе!",
        "Замечательно!",
        "Прекрасное начало!",
        "Так держать!",
        "Ты на верном пути!",
        "Здорово!",
        "Это как раз то, что нужно!",
        "Я тобой горжусь!",
        "С каждым разом у тебя получается всё лучше!",
        "Мы с тобой не зря поработали!",
        "Я вижу, как ты стараешься!",
        "Ты растешь над собой!",
        "Ты многое сделал, я это вижу!",
        "Теперь у тебя точно все получится!"
    ]
    return random.choice(compliments)

def fix_marks(name):
    try:
        Mark.objects.filter(schoolkid=Schoolkid.objects.get(full_name__contains=name), points__in=[2,3]).update(points=5)   
    except ObjectDoesNotExist:    
        print("Имя отсутствует в списке.")
    except  MultipleObjectsReturned:
        print("Найдено более одного имени.")

def remove_chastisements(name):
    try:
        Chastisement.objects.filter(schoolkid=Schoolkid.objects.get(full_name__contains=name)).delete()
    except ObjectDoesNotExist:    
        print("Имя отсутствует в списке.")
    except  MultipleObjectsReturned:
        print("Найдено более одного имени.")

def create_commendation(name, lesson):
    try:
        schoolkid=Schoolkid.objects.get(full_name__contains=name)
        random_lesson=Lesson.objects.filter(year_of_study=schoolkid.year_of_study, 
                                    group_letter=schoolkid.group_letter,
                                    subject__title = lesson).order_by('?').first() 
        Commendation.objects.create(text=get_compliment(),created=random_lesson.date,schoolkid=schoolkid,subject=random_lesson.subject,teacher=random_lesson.teacher)
    except ObjectDoesNotExist:    
        print("Имя отсутствует в списке.")
    except  MultipleObjectsReturned:
        print("Найдено более одного имени.")

    







