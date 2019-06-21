"""
Implementation in Python of the algorithm to calculate a risk score for cardiovascular disease
from http://riskscore.lshtm.ac.uk/calculator.html

@author Pietro Moretto
@version 0.1
"""


def check_range(name, value, min, max, units):
    """Check if a value is between a min and a max value"""
    if value > max or value < min:
        raise ValueError(
            f"The value for {name} is outside the allowed range ({min}-{max} {units})!"
        )
    else:
        return True


def risk_score(
    age,
    sex,
    smoker,
    sbp,
    chol,
    cholunits,
    diab,
    lvh,
    mi,
    st,
    creat=-1,
    creatunits="",
    hght=-1,
    hghtunits="",
):
    """
    Args:
        age: age of the subject (between 35 and 74)
        sex: male or female
        smoker: True or False if the subject is a smoker
        sbp: systolic blood pressure between 90 and 250 [mm Hg]
        chol: total cholesterol 
        cholunits: cholesterol units [mmol/l or mg/dl]
        diab: True or False if the subject has diabetes
        lvh: True or False if the subject has left ventricular hypertrophy
        mi: True or False if the subject already had a myocardial infaction
        st: True or False if the subject already had a stroke
        creat: creatine if known otherwise it is automatically detected based on sex
        creatunits: creatine units [umol/l or mg/dl]
        hght: height of the subject if know otherwise it is automatically detected based on sex
        hghtunits: height units [cms or inches]

    Returns:
        The risk score as float percentage

    Raises:
        ValueError: if some values are out of range
    """

    check_range("Age", age, 35, 74, "years")

    sex = sex.lower()
    if sex == "male" or sex == "m":
        sex = 1
    elif sex == "female" or sex == "f":
        sex = 0
    else:
        raise ValueError("You must specify Sex - either Male or Female")

    smoker = int(smoker)  # 0 or 1 whether non-smoker or smoker

    check_range("Systolic Blood pressure", sbp, 90, 250, "mm Hg")

    cholunits = cholunits.lower()
    if cholunits == "mmol/l":
        cholunits = 0
    elif cholunits == "mg/dl":
        cholunits = 1
    else:
        raise ValueError(
            "You must specify units for Total Cholestrol, either mmol/l or mg/dl"
        )

    if cholunits == 0:
        check_range("Cholesterol", chol, 3, 14, "mmol/l")
    else:
        check_range("Cholesterol", chol, 100, 550, "mg/dl")
        chol = chol / 38.7

    creat_val = -1
    if creat == -1:
        if sex == 0:
            creat_val = 83
        else:
            creat_val = 101
    else:
        creat_val = creat

    creatunits = creatunits.lower()
    if creatunits == "umol/l":
        creatunits = 0
    elif creatunits == "mg/dl":
        creatunits = 1
    else:
        if creat != -1:
            raise ValueError(
                "You must specify units for Creatinine, either umol/l or mg/dl"
            )

    if creat != -1:
        if creatunits == 0:
            check_range("Creatinine", creat, 30, 200, "umol/l")
        else:
            check_range("Creatinine", creat, 0.3, 2.3, "mg/dl")
            creat_val *= 88.5

    hght_val = -1
    if hght == -1:
        if sex == 0:
            hght_val = 160
        else:
            hght = 173
    else:
        hght_val = hght

    hghtunits = hghtunits.lower()
    if hghtunits == "cms":
        hghtunits = 0
    elif hghtunits == "inches":
        hghtunits = 1
    else:
        if hght != -1:
            raise ValueError("You must specify units for Height, either cms or inches")

    if hght != -1:
        if hghtunits == 0:
            check_range("Height", hght, 120, 210, "cms")
        else:
            check_range("Height", hght, 45, 85, "inches")
            hght_val *= 2.54

    diab = int(diab)
    lvh = int(lvh)
    mi = int(mi)
    st = int(st)

    score = 10 * (
        (0.0909179 * (age - 37.5))
        - (0.0190903 * sex * (age - 37.5))
        + (1.343643 * sex)
        + (1.302315 * smoker)
        - (0.4399128 * sex * smoker)
        - (0.0146243 * smoker * (age - 37.5))
        - (0.0147991 * (hght_val - 180))
        + (0.010771 * (sbp - 115))
        + (0.9108246 * diab)
        - (0.7664304 * sex * diab)
        + (0.8198657 * mi)
        + (0.8079117 * st)
        + (0.0482319 * (chol - 4.5))
        + (0.1321689 * sex * (chol - 4.5))
        + (0.3321234 * lvh)
        + (0.0059917 * (creat_val - 40))
    )

    score = round((score * 100) / 100, 2)

    return score


if __name__ == "__main__":
    # score = risk_score(
    #     39,
    #     "male",
    #     False,
    #     160,
    #     8,
    #     "mmol/l",
    #     False,
    #     False,
    #     False,
    #     False,
    #     100,
    #     "umol/l",
    #     170,
    #     "cms",
    # )
    score = risk_score(
        70,
        "female",
        True,
        120,
        200,
        "mg/dl",
        True,
        False,
        False,
        True,
        hght=160,
        hghtunits="cms",
    )
    print("Score", score)
