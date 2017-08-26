# You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 620100
# -------------------------
# Rogers: 36.0% (223236)
# Gomez: 54.0% (334854)
# Brentwood: 4.0% (24804)
# Higgins: 6.0% (37206)
# -------------------------
# Winner: Gomez
# -------------------------
# Your final script must be able to handle any such similarly-structured dataset in the future (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Dependencies
# --------------------------------------
import csv

# Files to Load / Output

file_to_load = "Resources/election_data_1.csv"
file_to_output = "analysis/election_analysis_1.txt"

# Variables to Track

candidate_options = []
candidate_votes = {}
vote_percentages = []

winning_candidate = ""
winning_count = 0

total_votes = 0

greatest_vote_candidate = ""
greatest_vote_percentage = 0

# Reading the file
with open(file_to_load) as election_data:
  reader = csv.DictReader(election_data)

  # For Each row...
  for row in reader:

    # Total Votes
    total_votes = total_votes + 1

    # Build our Array of Unique Candidates 
    if row["Candidate"] not in candidate_options:

      # Add the candidate as an option
      candidate_options.append(row["Candidate"])

      # Set that candidate's initial vote count to 0
      candidate_votes[row["Candidate"]] = 0

    # If the candidate is NOT unique
    candidate_votes[row["Candidate"]] =  candidate_votes[row["Candidate"]] + 1

  for candidate in candidate_votes:

    votes = candidate_votes[candidate]
  print("Total Votes: ", total_votes)

  # Iterate through the candidate_votes
  for candidate in candidate_votes:

    votes = candidate_votes[candidate]
    vote_percentage = round(((votes / total_votes)  * 100),1)
    vote_percentages.append(vote_percentage)
    
    print(candidate,":",votes,"(",vote_percentage,"%)")

    if(vote_percentage > greatest_vote_percentage):

      greatest_vote_candidate = candidate
      greatest_vote_percentage = vote_percentage

  # Printing The Winner
  print(" ")
  print("The winning candidate is " + greatest_vote_candidate)
  print("The greatest vote percentage is: " + str(greatest_vote_percentage) + "%")

  # Output Files (Txt File) - *Failing*
with open(file_to_output, "w") as txt_file:

   txt_file.write("Total Votes: " + str(total_votes))
   txt_file.write("\n")
   txt_file.write(candidate_options[0] + ":" + str(candidate_votes[candidate_options[0]]) + " (" + str(vote_percentages[0]) + "%)")
   txt_file.write("\n")
   txt_file.write(candidate_options[1] + ":" + str(candidate_votes[candidate_options[1]]) + " (" + str(vote_percentages[1]) + "%)")
   txt_file.write("\n")
   txt_file.write(candidate_options[2] + ":" + str(candidate_votes[candidate_options[2]]) + " (" + str(vote_percentages[2]) + "%)")
   txt_file.write("\n")
   txt_file.write(candidate_options[3] + ":" + str(candidate_votes[candidate_options[3]]) + " (" + str(vote_percentages[3]) + "%)")
   txt_file.write("\n")
   txt_file.write("\n")
   txt_file.write("The winning candidate is " + greatest_vote_candidate)
   txt_file.write("\n")
   txt_file.write("The greatest vote percentage is: " + str(greatest_vote_percentage) + "%")
    
    