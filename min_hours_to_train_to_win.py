initialEnergy = 1
initialExperience = 1
energy = [1, 1, 1, 1]
experience = [1, 1, 1, 50]

total_hour_in_energy = sum(energy) - initialEnergy + 1

total_hour_in_experience = 0

# now how to find how manyhours should i spend training my experience?
for exp in experience:
    print(f"Needed experience = {exp}")
    print(f"Experinece i have is {initialExperience}")

    if exp < initialExperience:
        print(f"Hurray i won, no now i have energy = {exp + initialExperience}")
        print(f"To win against this opponent, i didn't need to train my experience")

    else:
        hours_needed = exp - initialExperience + 1
        print(
            f"Oops i lost, i needed {hours_needed} more hours in experience tranining"
        )
        total_hour_in_experience += hours_needed
        initialExperience += 1

    initialExperience = exp + initialExperience

print(f"Total hours needed to train my energy = {total_hour_in_energy}")
print(f"Total hours needed to train my experience = {total_hour_in_experience}")
