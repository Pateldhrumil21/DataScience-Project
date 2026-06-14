# import pandas as pd

# data = {
#     "name":["rahul","ram","pooja","amit","dhruv"],
#     "maths":[85,99,45,7,95],
#     "science":[90,100,70,8,98],
#     "english":[87,100,80,4,99]
# }
# df = pd.DataFrame(data)
# print(df)
# # print("\n")

# # Total marks
# print("\n Total marks")
# df["total"] = df["maths"] + df["science"] + df["english"]
# print(df)

# # Total average
# print("\n Total average")
# df["average"] = df["total"]/3                                 
# print(df)

# # Find topper highest
# print("\n Topper")                       
# print(df.loc[df["total"].idxmax()])

# # lowest marks 
# print("\n Lowest marks")                         
# print(df.loc[df["total"].idxmin()]) 

# # Fail Student
# print("\nFail student")
# fail = df[df["average"] < 40]                               
# print(fail)


# #subj wise average marks
# print("\n Subj wise average marks")
# print(df[["maths","science","english"]].mean())

# # 2 Method used  
# # print("\nMethod used")
# print("\n 2 Method used")          
# subj = df[["maths","science","english"]].mean()
# print(subj)

# # Grade student
# print("\nGrade student")       
# def grade(average):                                          
#     if average >=90:
#         return "A"                                            
#     elif average >=75:
#         return "B"
#     elif average>=65:
#         return "C"
#     else:
#         return "D"
# df["grade"] = df["average"].apply(grade)
# print(df) 


# # Rank Top student
# print("\n Rank top student ")
# df['rank'] = df["total"].rank(ascending=False)                   
# print(df)

# # Sort number
# print("\n Sort number")       
# print(df.sort_values(by="total",ascending=False)) 


# # Top 3 student topper
# print("\n Top 3 student ")
# top3 = df.nlargest(3,"total")                                        
# print(top3)

# # Subj wise max marks
# print("\n Subj wise max marks")
# print(df[["maths","science","english"]].max())
# res = df[["maths","science","english"]].max()
# print(res)
