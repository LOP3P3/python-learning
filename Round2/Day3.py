
installed_apps = ["TikTok", "BrawlStars", "Telegram"]
number = 1   

installed_apps.remove("TikTok")
installed_apps.append("Discord")
installed_apps.sort()

for i in installed_apps:  
    print(f"{number}. {i}")
    number = number + 1    

number_of_apps = len(installed_apps)

print("Всего приложений:",number_of_apps)

if "Telegram" in installed_apps:
    print("Telegram установлен: да")
else:
    print("Telegram установлен: нет")