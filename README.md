# Portfolio

Hello World!

Thanks for taking the time to look at my portfolio.

For scientific work, have a look at my [CV](https://sweeney-th.github.io/cv/). For programming and data science projects, see below.

### COVID19 antibody diagnostics app

Our [lab](https://www.omics.kitchen/) has been working with a number of collaborators on a study of lateral flow assays for the detection of SARS-CoV-2 antibodies. We've designed and implemented an interactive [app](https://covid.omics.kitchen/) to complement the [study](https://www.medrxiv.org/content/10.1101/2021.01.02.20248998v1). Interested parties getting an antibody test are advised to speak with their healthcare provider about interpreting their results with that app, which uses local COVID19 prevelance data from [usafacts.org](https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/) (also used by the CDC) and measurments from the study to estimate the probability they do or do not have SARS-CoV-2 antibodies given their result.

### A case study of silent data corruption in an RNA-Seq experiment: Don't get buRned by factors

A misleading error message and some weird factor behavior is all it takes to spoof the results of a differential expression analysis. You have been [warned!](https://github.com/sweeney-th/type-issue-case-study)

### An Investigation into a drop in gun deaths in February

[This](http://pythoninthewyld.com/wp-content/uploads/2019/08/Main.nb_.html) is based on an observation I made while exploring CDC gun deaths for machine learning practice.

### StRuen

An R Shiny app that permits interactive visualization of the Wisconsin breast cancer dataset. There is also an extra, fictitious (randomly generated) "cohort" variable to permit demonstration of some additional features (tracking members of the same cohort across multiple graphs). Check it out the [video](https://www.youtube.com/watch?v=qcZ4sB-RUk4).

### ASH

ASH (Antigen Selection Heuristic) is a working prototype bioinformatics tool that finds chemically distinct regions in proteins. When designing an antibody to target a protein, it is often beneficial to know which regions are the most distinct. This helps manage the odds of cross-reactivity. For example, if you want to study XYZprotein1 but not XYZprotein2, selecting a region that composed of the same amino acid sequence in both of them will make it likely that your assays are sensitive to both targets.

ASH uses a scale based on hyrdophilicity to compare residues. It used this scale to generate a "mismatch" score to quantify how unlike one another regions are based on their chemical traits, not just a match/no-match system. There is a Jupyter notebook in the ASH directory detailing the algorithm and showcasing prototype Python code. There is also a subdirectory called "ASH++" that shows how the algorithm could be re-written in C++ for greater performance. There is a walkthrough of the [basic idea](https://github.com/sweeney-th/Portfolio/blob/master/Bioinformatics/ASH/documentation/ASH_demo.pdf), and the full implementation with documentation and unit tests is [here](https://github.com/sweeney-th/Portfolio/tree/master/Bioinformatics/ASH).

### Trump v Clinton numeric Twitter metadata classifier

Because analyzing text presents numerous challenges in the form of word-stemming, context, and tone, I wrote a tweet [classifier](https://nbviewer.jupyter.org/github/sweeney-th/Portfolio/blob/master/DataScience/TwitterClassifier/signatureProject.pdf) that uses only numeric metadata to predict determine if a given message came from the handle of Hillary Clinton or Donald Trump. It uses a Kaggle dataset that I heavily re-engineered using Python scripts to more than double its wide. The classifier() works with ~97% accuracy.

### PythonInTheWyld.com

I am building a [teach-yourself-python website](http://pythoninthewyld.com/). I am not a heavy social media user, but do keep up a light presence for the site, so feel free to [get in touch](http://pythoninthewyld.com/home/contact/).

### Examples by language

[Here](https://github.com/sweeney-th/Portfolio/tree/master/Misc/ExamplesByLanguage) you will find smaller programs where practice a variety of languages: Python, Perl, C, and Java. For R code, see the above classifier as I generally use it for Data Science tasks only.

### Monte Hall Monte Carlo Simulation

Sometimes you need to have a little stochastic fun and write a [Monte Carlo Simulation](https://github.com/sweeney-th/Portfolio/blob/master/Misc/MonteHall.py) of the Monte Hall Paradox.

Thanks again for reading, and feel free to reach out with any questions through the contact link above.

Regards:
----Thadryan
