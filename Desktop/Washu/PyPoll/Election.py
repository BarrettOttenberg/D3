import os
import csv

input_file = 'election_data.csv'
output_file = 'election_results.txt'

csv_input_path = os.path.join('raw_data', input_file)
txt_output_path = os.path.join('results_doc', output_file)

# Define measures

candidates, total_candidates, candidate_percentage, candidate_total, summaries = ([] for i in range(5))

with open(csv_input_path, mode='r', newline='') as election_data:
    reader - csv.reader(poll_data, delimiter=',')

    next(reader)

    num_rows = 0

    for row in reader:
        total_candidates.append(row[2])
        num_rows += 1

#results

print("\nElection Results")
print("-" * 40)
print("Vote Total:", num_rows)
print("-" * 40)

for j in range(len(candidates)):
    candidates_count = 0

    candidate_percentage.append(round(candidate_count / num_rows * 100, 1))
    candidate_total.append(candidate_count)

Responding_output = zip(candidates, candidate_percentage,candidate_total)

for row in Responding_output:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) +")")
    summary = (row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) +")")
    summaries.append(summary)



for j in range(len(candidate_percentage)):
    if candidate_total[j] > candidate_total[j - 1]:
        Overall_Winner = candidates[j]


print("-" * 40)
print("Winner:")
print("-" * 40)
print("\n\n")

with open(txt_output_path, mode='w', newline='') as posted_summaries:
    write = csv.writer(posted_summaries)

    writer.writerows([
        ["Election Results for: " + input_file],
        ["-" * 40],
        ["Total Votes: " + str(num_rows)],
        ["-" * 40]
    ])
    writer.writerows(summaries)
    writer.writerows([])
        ["-" *40],
        ["Winner: "],
        ["-" *40]
    ])
