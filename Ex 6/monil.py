import pandas as pd

movie= pd.read_table("movies.dat", header = None, sep = "::", names = ["MovieID", "Title", "Genres"], engine='python')
rating= pd.read_table("ratings.dat", header = None, sep = "::", names = ["UserID", "MovieID", "Rating", "Timestamp"], engine='python')
user= pd.read_table("users.dat", header = None, sep = "::", names = ["UserID", "Gender", "Age", "Occupation", "Zip-Code"], engine='python')

print("\nFirst 3 rows in movies DataFrame:")
print(movie.head(3))
print("\nFirst 3 rows in ratings DataFrame:")
print(rating.head(3))
print("\nFirst 3 rows in users DataFrame:")
print(user.head(3))

movierating = movie.merge(rating, how = "inner")
data = movierating.merge(user, how = "inner")

print("\nFollowing are the number of records in each data frame:")
print("Movies:", movie["MovieID"].count())
print("Ratings:", rating["UserID"].count())
print("Users:", user["UserID"].count())
print("Data:", data["UserID"].count())

data.Occupation.replace(range(0,21,1),["Other/not specified", "academic/educator", "artist", "clerical/admin", "college/grad student", "customer service", "doctor/health care", "executive/managerical", "farmer", "homemaker", "K-12 student", "lawyer", "programmer", "retired", "sales/marketing", "scientist", "self-employed", "technician/engineer", "tradesman/craftsman", "unemployed", "writer"], inplace = True)

print("\nLast 3 rows of the DataFrame DATA are:")
print(data.tail(3))
