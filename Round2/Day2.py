def app_check_size(space_left):
    if space_left >= 40:
        return("Места достаточно")
    elif space_left >= 30: 
        return("Нормально")
    elif space_left >= 20:
        return("Маловато")
    else:
        return("ВПРИТЫК!")

apps = {"TicTok":2, "Brawl Stars":10, "PhotoAnapa2015":30 }

free_space_gb = 50
number = 1 

print("*" * 50)
print(" ")
print(f"На телефоне сейчас свободно: {free_space_gb} Gb")
print("Выберите что вы хотите скачать:")
print(" ")
for app_name, app_size in apps.items():
    space_left = free_space_gb - app_size
    print(f"{number}. {app_name} -> {app_size} Gb: Останется {space_left} / {app_check_size(space_left)}")
    number = number + 1
print(" ")
print("*" * 50)
print(" ")

chosen_app = input("Введите название: ")


try:
    app_size_gb = apps[chosen_app]
except KeyError:
    print("В списке нет такого приложения!")
else:
    free_space_after = free_space_gb - app_size_gb
    print(f"Вы Скачали {chosen_app}\nТеперь у вас столько памяти: {free_space_after}Gb")
    print(app_check_size(free_space_after))