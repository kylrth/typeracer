import datetime
import sys

from bs4 import BeautifulSoup
import requests

months = {
    "Jan.": 1,
    "Feb.": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "Aug.": 8,
    "Sept.": 9,
    "Oct.": 10,
    "Nov.": 11,
    "Dec.": 12,
}


def parse_date(s: str) -> datetime.date:
    if s == "today":
        return datetime.date.today()

    spl = s.split()
    if len(spl) != 3:
        raise ValueError("unrecognized date string", s)

    return datetime.date(int(spl[2]), months[spl[0]], int(spl[1][:-1]))


def get_results(user: str):
    url = "https://data.typeracer.com/pit/race_history?user=" + user + "&n=100&startDate="
    results = {}

    while True:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, "html.parser")

        rows = soup.select("div[class=Scores__Table__Row]")

        for row in rows:
            race_number = int(
                row.select("div[class=profileTableHeaderUniverse]")[0].find("a").string.strip()
            )
            wpm = int(row.select("div[class=profileTableHeaderRaces]")[0].string.strip().split()[0])
            acc = (
                float(row.select("div[class=profileTableHeaderRaces]")[1].string.strip()[:-1]) / 100
            )
            date = row.select("div[class=profileTableHeaderDate]")[0].string.strip()
            date = parse_date(date)

            results[race_number] = {
                "wpm": wpm,
                "acc": acc,
                "date": date,
            }

        new_url = soup.find("a", href=True, string=lambda s: "load older results" in str(s))
        if new_url is None:
            return results
        url = url.split("?")[0] + new_url["href"]


if __name__ == "__main__":
    results = get_results(sys.argv[1])

    print("race number,date,wpm,acc")
    for race_number in sorted(results.keys()):
        r = results[race_number]
        print(f"{race_number},{r['date'].strftime('%Y-%m-%d')},{r['wpm']},{r['acc']}")
