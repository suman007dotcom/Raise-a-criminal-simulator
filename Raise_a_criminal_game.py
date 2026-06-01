from question import QUESTIONS
import joblib

knn = joblib.load("knn_model.pkl")
scaler = joblib.load("scaler.pkl")

player = {
    "abuse":0,
    "parental_neglect":0,
    "school_neglect":0,
    "substance_exposure": 0,
    "household_instablity":0,
    "peer_delinquency":0,
    "impuslvity_score":0,
    "mental_health_score":0}

flags = {
    "in_school": True,
    "family_stable": True,
    "high_risk_peers": False,
    "mental_health_support": True
}

for q in QUESTIONS:
    if q["flag"] is not None:

        if flags[q["flag"]] != q["flag_value"]:
            continue
    print("\n" + "-" * 50)
    print("AGE: ", q['age'])

    print(q["question"])
    print("-" * 50)
    for letter in ["A", "B", "C"]:
        print(letter,":", q['choices'][letter]['text'])

    choice = input("\nChoice: ").upper()

    while choice not in ["A","B","C"]:
        choice = input("Choose A, B or C: ").upper()

    selected = q["choices"][choice]

    for stat, value in selected["effects"].items():

        player[stat] += value

        if player[stat] < 0:
            player[stat] = 0
    for flag, value in selected["flags"].items():
        flags[flag] = value

features = [[
    player["abuse"],
    player["parental_neglect"],
    player["school_neglect"],
    player["substance_exposure"],
    player["household_instability"],
    player["peer_delinquency"],
    player["impulsivity_score"],
    player["mental_health_score"]
]]

features = scaler.transform(features)
prediction = knn.predict(features)
prob = knn.predict_proba(features)
risk = prob[0][1] * 100

print("\n" + "-" * 50)
print("RESULT")
print("-" * 50)
print(f"Risk Score: {risk:.1f}%")

sorted_stats = sorted(player.items(), key=lambda x: x[1], reverse=True)

print("\nBiggest Risk Factors:")

for stat, value in sorted_stats[:3]:
    print(f"- {stat}: {value}")