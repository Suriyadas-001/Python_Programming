#prakash maiti
# #12. Given a text file data.txt containing:
  #  name,score
   # Alice,85
   #Bob,90
   #Charlie,78
#Write a program to read the file and create a dictionary like {'Alice':85, 'Bob':90, 'Charlie':78}.
# create empty dictionary
data_dict = {}

# open and read file
with open("data.txt", "r") as file:
    lines = file.readlines()

# skip header and process data
for line in lines[1:]:
    name, score = line.strip().split(",")
    data_dict[name] = int(score)

# print result
print(data_dict)