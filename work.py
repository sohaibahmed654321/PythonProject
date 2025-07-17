import pandas as pa
Rista_profile = {
    "name" : ["Moheeb","Faraz","Muneeb","Asad","Uzair"],
    "Gender" :["m","m","m","m","m"],
    "Preferred_Caste" :["Syed", "Bihari", "Rajput", "Mughal", "Pathan"],
    "Preferred_Area" :["Lahore", "Karachi", "Islamabad", "Rawalpindi", "Multan"],
    "Profession" : ["Engineer", "Doctor", "Software Developer", "Teacher", "Businessman"],
    "No_of_Siblings" :[4,3,5,2,6]
}
df_Rista = pa.DataFrame(Rista_profile)
df_Rista["Age"] = [20,22,23,40,30]
df_Rista["Matital_Status"] = ["Single","Widow","Divoce","Divoce","Single"]
del df_Rista["Profession"]
df_Rista["NAtionality"] = ["PAkistan","PAkistan","PAkistan","PAkistan","PAkistan"]

print(df_Rista[df_Rista["Preferred_Caste"] == "Pathan"])
print(df_Rista[df_Rista["No_of_Siblings"] >2])
print(df_Rista[df_Rista["Preferred_Area"] == "DHA" ])
print(df_Rista[(df_Rista["Preferred_Area"] == "NAzaimabad") & (df_Rista["Gender"] == "f")])



print(df_Rista)