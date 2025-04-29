# AlienGame
Assignment 4 for Advanced Cognitive Modelling

In assignment 4 you are asked to implement a formalized model of categorization as applied to the alien game we played during the lectures. You can use the GCM (modifying the version presented during lectures), or whatever other model of categorization you would like to use.

# Overview

The output of the assignment should be a report briefly describing the task, briefly motivating and explaining your model, briefly showcasing the results of the simulation of the model on the task, briefly showcasing model fit on the simulated data, discussing model fit and estimates on the empirical data.

## More details

### Structure of the experiment:

the stimuli are conceptualized as 5 dimensional vectors of 0s and 1s (5 features, binary values)
there are 32 possible stimuli, all 32 stimuli are presented in randomized order, in three iterations (stimuli 1-32 in random order, stimuli 1-32 in a new random order, stimuli 1-32 in a new random order).
the stimuli are categorized along two dimensions: danger (0-1) and nutrition (0-1). Feel free to simplify your life and only consider one dimension (but kudos for considering both).
Responses are 1-4, where 3 and 4 indicate danger, 1 and 2 not danger; 2 and 4 indicate nutritious, 1 and 3 not nutricious
the association between feature and category varies over session. 
In the first session: danger depends on the alien having spots AND eyes on stalks (feature 1 AND feature 2 both being 1); nutrition depends on arms being up (feature 4 being 1).
In the second session: danger depends on arms being up (feature 4 being 1); nutrition depends on at least two amongst eyes on stalks, slim legs, and spots (at least 2 out of feature 1, 2 and 3 being 1)
In the third session: danger depends on arms up and green color (feature 4 and 5 being both 1); nutrition depends on at least two amongst eyes on stalks, slim legs, spots, or green color (at least 2 amongst feature 1, 2, 3, 5 being 1)
The experiment also contrasted dyads (condition 1) with individuals (condition 2), but that's less relevant for the simulation.
You'll have to implement the structure of the experiment and simulate your model's behavior on it. Then plot how the model does (e.g. performance over trial), and comment on how well it does (bonus points if you compare it to the empirical data).

You should then fit the Stan model to the simulated data. Bonus points for full parameter recovery, but for the purpose of the exercise, a simpler model quality check is sufficient.

Empirical data: https://www.dropbox.com/s/vbckcxggw9ppewb/AlienData.txt?dl=0

You should then visually explore the empirical data and fit the Stan model to them. Bonus points for multilevel implementations and checking all 3 sessions, but fitting the model by participant and sticking to 1 session is sufficient to pass. Do model quality checks, and comment on the results (including visualizations).
