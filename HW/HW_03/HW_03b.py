# Файл data/visits.txt: каждая строка - название сайта.
# Нужно:
# 1) посчитать частоты (dict)
# 2) посчитать total = сумма всех посещений
# 3) вывести и сохранить отчет в формате: site: count (percent%)
# 4) найти top site и добавить строку TOP SITE: ...
# Требование к формату одной строки: google: 3 (37.5%)


visits = {}
total_visits = 0

with open("data/visits.txt", "r", encoding="utf-8") as s:
    for line in s:
        site = line.strip()

        if site == "":
            continue

        total_visits += 1

        if site not in visits:
            visits[site] = 0
        visits[site] += 1


most_popular = None
visits_number = -1

for site, v in visits.items():
    if v > visits_number:
        visits_number = v
        most_popular = site


with open("data/visits_report.txt", "w", encoding="utf-8") as f:
    f.write("===REPORT===\n")

    if total_visits == 0:
        f.write("No visits yet\n")
    else:
        for site, c in visits.items():
            percent = (c / total_visits) * 100
            f.write(f"{site}: {c} ({percent:.1f}%)\n")

        top_percent = (visits_number / total_visits) * 100
        f.write(f"\nTOP SITE: {most_popular}: {visits_number} ({top_percent:.1f}%)")
