capitals = {"Russia":"Moscow","Belarus":"Minsk","Armenia":"Erevan","Turkey":"Istanbul","France":"Paris"}
capitals['Russia'],capitals["France"] = capitals["France"],capitals["Russia"]
capitals.pop("Belarus")
capitals["new_key"] = "new_value"
print(capitals)