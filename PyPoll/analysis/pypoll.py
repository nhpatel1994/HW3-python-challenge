import os
import csv

candidates = {}

total_votes = 0

winner_count = 0
winner = ""

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        candidate_name = row[2]

        total_votes = total_votes + 1

        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        else:
            candidates[candidate_name] = 1


    print("--------Election Results--------")
    print("--------------------------------")
    print("Total Votes: ", total_votes)
    print("--------------------------------")

    with open("pybank.txt", "w") as txt_file:

        output = "--------Election Results--------"
        txt_file.write(output + '\n')
        output = "--------------------------------"
        txt_file.write(output + '\n')
        output = "Total Votes: " + str(total_votes)
        txt_file.write(output + '\n')
        output = "--------------------------------"
        txt_file.write(output + '\n')

        for key, value in candidates.items():
            
            if value > winner_count:
                winner = key
                winner_count = value
                percent_votes = (winner_count / total_votes) * 100

            
            output = key + ": " + str("{:.3f}".format(percent_votes)) + "% (" + str(value) + ")"
            print(output)
            txt_file.write(output + '\n')

        output = "--------------------------------"
        txt_file.write(output + '\n')
        print(output)
        output = "Winner: " + str(winner)
        txt_file.write(output + '\n')
        print(output)



