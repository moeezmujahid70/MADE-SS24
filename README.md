# Exercise Badges

![](https://byob.yarr.is/moeezmujahid70/MADE-SS24/score_ex1) ![](https://byob.yarr.is/moeezmujahid70/MADE-SS24/score_ex2) ![](https://byob.yarr.is/moeezmujahid70/MADE-SS24/score_ex3) ![](https://byob.yarr.is/moeezmujahid70/MADE-SS24/score_ex4) ![](https://byob.yarr.is/moeezmujahid70/MADE-SS24/score_ex5)


# Methods of Advanced Data Engineering 

![image](https://github.com/moeezmujahid70/MADE-SS24/assets/51213035/586f00da-5bcd-4995-b18e-45dc5033bf21)


Climate change is a critical global issue because of its effect on the environment, human health, and economies. Through statistical analysis, this project investigates the relationship between temperature changes and CO2 emissions. The results are expected to examine the impact of CO2 emissions on temperature change. They may be used as information for future policy decisions related to greenhouse gas emissions.
In this Project, analysis are performed on following topics:

- How Have Temperature Changes and CO2 Emission  Varied Over the Years?
- What is the Impact of CO2 Emissions on Temperature Change Globally?
- What is the Impact of CO2 Emissions on Temperature Change in Individual Countries? 


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
