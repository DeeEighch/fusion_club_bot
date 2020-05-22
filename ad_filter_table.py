import re
AD_FILTER_FLAGS = re.IGNORECASE
AD_FILTERS = [
    r"(.+)?auto\.ria\.com(.+)?",
    r"(пр[оа]дам|пр[оа]даю|прода[её]тся|прада[её]тся)?(.+)?(\d+(\.\d+)?(.+)?(грн|usd|грв|\$|UAH|хрн|гривен|хривен))(.+)?"
]