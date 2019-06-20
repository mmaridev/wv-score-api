# Copyright (c) 2019 Marco Marinello

import requests
from bs4 import BeautifulSoup


def query(age, sex, cholesterol, max_press, smokes, origin_country="Italy"):
    """
    age -> integer
    sex -> "M" or "F"
    cholesterol -> integer (mmol/l)
    maximum pressure -> integer (mmHg)
    smokes -> boolean
    origin_country -> country in english (string)

    Returns the percentage as a float
    """
    if type(age) is not int:
        raise ValueError("Age is not an integer")
    if sex not in ["M", "F"]:
        raise ValueError("Sex is not male or female")
    if type(cholesterol) is not int:
        raise ValueError("Cholesterol is not an integer")
    if type(max_press) is not int:
        raise ValueError("Maximum pressure is not an integer")
    if type(smokes) is not bool:
        raise ValueError("Smokes is not a boolean")
    if type(origin_country) is not str:
        raise ValueError("Origin country is not a string")

    data = {
        "age": age,
        "gender": sex == "M" and "male" or "female",
        "country": origin_country,
        "cholesterol": cholesterol,
        "sbp": max_press,
        "smoker": smokes and "1" or "0",
        "cholesterol_unit": "mmol/l",
    }

    r = requests.post("https://www.centrostudigised.it/calcola_il_tuo_rischio_cardiovascolare.php", data=data)
    soup = BeautifulSoup(r.content, features="lxml")
    txt = soup.select("div[id='cardio'] > p")[1].text
    val = txt.split(" ")[0][:-1].replace(",", ".")
    return float(val)



if __name__ == "__main__":
    print(query(50, "M", 8, 150, True))
