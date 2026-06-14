import pandas as pd

df = pd.DataFrame({
    "student":["amit","ram","pooja"],
    "present":[18,20,13],
    "absent":[2,0,5]
})
# print(df)

# Total attendance
print("\n Total attendance")
df["Total"] = df["present"] + df["absent"]
print(df)

# Present 
print("\n present")
df["present %"] = df["present"] / df["Total"] * 100
print(df)

#  absent
print("\n absent")
df["absent %"] = df["absent"] / df["Total"] * 100
print(df)

# New student add
# print("\n New student add")
# # Multiple student added
# new = pd.DataFrame({
#     "student":["raju","rajesh"],
#     "present":[15,17],
#     "absent":[4,3]
# })

# df = pd.concat([df,new],ignore_index=True)
# print(df)

# name = input("enter your name:")
# present = int(input("present days:"))
# absent = int(input(" absent days:"))
# df.loc[len(df)] = [name,present,absent,"Total","present %","absent %"]
# print(df)

# Student delete
print("\n student delete")
# name = input("enter student name to delete:")
# df = df[df["student"] != name]
# print(df)

# low attendance
print("\n low attendance")
low_att = df[df["present"] < 15]
print(low_att)

# monthly att
print("\n monthly att")
print(df["present %"].mean())

# highest attendance
print("\n higest attendance")
print(df.loc[df["present"].idxmax()])