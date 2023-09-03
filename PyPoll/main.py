#imports
import os
import csv

#file attachment and output
file_to_load = os.path.join(".", "Resources", "election_data.csv")
file_to_output = os.path.join(".", "election_analysis.txt")

total_votes = 0

candidate_votes = {}
candidate_options = []

winning_candidate = ""
winning_count = 0

with open (file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    header = next(reader)
    #print(header)

    for row in reader:
        #print(row) -> checking to make sure the loop worked correctly 
        total_votes = total_votes + 1
        
        #getting name from each row
        candidate_name = row[2]

        #adding unqiue names to the list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1    

    #print(candidate_options)
    #print(candidate_votes)




with open(file_to_output, "w") as txt_file:
    election_results = (
        f"Elecetion Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------\n"
    )

print(election_results)
txt_file.write(election_results)

for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    vote_percentage = float(votes) / float(total_votes) *100
    if(votes > winning_count):
        winning_count = votes
        winning_candidate = candidate
    voter_output = f"{candidate}: {vote_percentage:.3f}%({votes})\n"
    
    #print(votes)
    #print(vote_percentage)
    print(voter_output)
    txt_file.write(voter_output)

winning_candidate_summary = (
    f"----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"----------------------\n"
)

print(winning_candidate_summary)    
txt_file.write(winning_candidate_summary)
