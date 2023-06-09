# SimRent
Rent Crisis Simulator

I'm just starting to learn python.  And I started trying to make a rent crisis simulator game, but I couldn't get the 
drivers to work for pygame at first.  So this version is just a simple database with a little tkinter window.

It assigns weighted random populations for five income cohorts, then gives them weighted random incomes.  They each have
some incidence of homelessness, there's a homeless census too.  If they have rent, this version initially sets it at 30% as a
placeholder.  

Each turn is one month.  There is a built in variable rent increase for everyone every year.  They can be fired for 1-6 turns.
They get rehired at a random salary.  There's an option to subsidize rent, but it's not totally finished.

They all have a wellbeing score of 1-10, randomly assigned but with a couple of modifiers.  I'm building in a really 
simple "hospital" function and a really simple "healthcare subsidy" function, something like "2 wellbeing for $1000".

It should have graphics of some kind in Version 5 probably.
