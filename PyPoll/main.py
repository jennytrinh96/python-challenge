# PyPoll

# Total number of vote casts
# List of candidates who received votes
# % of votes per candidate (# of votes per candidate / total votes)
# Total number of votes per candidate
# Winner of election


# Import Modules
import os
import csv

# Create file paths
electiondata_path = os.path.join("Resources", "election_data.csv")

# Create output path for analysis
election_analysis_path = os.path.join("Analysis", "poll_analysis.txt")


# Variables to use:

# Accumulator for total number of votes
total_votes = 0

# Create list that holds candidates
candidates = []

# Create dictionary to hold votes per candidates
candidate_votes= {}

# Holds winning count
winner_count = 0

# Holds Winner name
winner_candidate = ''


# Open csv file
with open(electiondata_path) as election_file:

    # Create Reader object
    csv_reader = csv.reader(election_file)

    # Skip Header
    csv_header = next(csv_reader)

    # Rows will be list
        # user id = index 0
        # user's choice = index 2

    # Create loop to calculate the followings
    for row in csv_reader:

        # Increment the total_votes
        total_votes += 1

        # Validate with candidates are in list of candidates
        if row[2] not in candidates: 

            # If not in list, add into list
            candidates.append(row[2])

            # Add value to dictionary as well
            # Dict = {"key": "value"}, 
            # Start count at 1 for votes
            candidate_votes[row[2]] = 1

        else:
            # If candidate already exits in lists, add vote to count
            candidate_votes[row[2]] += 1


vote_output = ''

for cv in candidate_votes:
    # Get vote count and % of votes
    votes = candidate_votes.get(cv)
    vote_perc = (float(votes) / float(total_votes)) * 100.00 
    #print(votes) 

    vote_output += f"{cv}: {vote_perc:.2f}% with {votes} votes.\n"
    #print(vote_output)
    
    # Compare the votes to winner_count
    if votes > winner_count:

        # Update replace winning vote each time theres a higher value
        winner_count = votes

        # Update winning candidate
        winner_candidate = cv

winner_output = f"Winner: {winner_candidate}"


# Generate output
output = (
f"\n\tElection Poll Results!\n"
f"-------------------------------------"
f"\nTotal Votes = {total_votes}\n"
f"-------------------------------------"
f"\nNominations: \n"
f"\n{vote_output}\n"
f"-------------------------------------"
f"\n{winner_output}"
)

# Print Output
print(output)

# Export output to .txt file to Analysis Folder
with open(election_analysis_path, 'w') as text_file:
    text_file.write(output)