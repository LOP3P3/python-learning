# size_mb = 1750

# if size_mb > 3000:
#     print("Большое приложение")
# elif size_mb > 1000:
#     print("Средние приложение")
# else:
#     print("Маленькое приложение")


apps = {"TicTok":2, "Brawl Stars":10, "PhotoAnapa2015":30 }

free_space_gb = 50


print("*" * 30)
print(" ")
print(f"На телефоне сейчас свободно: {free_space_gb} Gb")
print("Выберите что вы хотите скачать:")
print(" ")
print(apps)
print(" ")
print("*" * 30)
print(" ")

chosen_app = input("Введите название: ")

try:
    app_size_gb = apps[chosen_app]
except KeyError:
    print("В списке нет такого приложения!")
else:
    free_space_after = free_space_gb - app_size_gb
    print(f"Вы Скачали {chosen_app}\nТеперь у вас столько памяти: {free_space_after}Gb")
    if free_space_after >= 40:
        print("Места достаточно")
    elif free_space_after >= 30:
        print("Нормально")
    elif free_space_after >= 20:
        print("Маловато")
    else:
        print("ВПРИТЫК!")
