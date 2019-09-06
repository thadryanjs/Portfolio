# Portfolio

Hello World!

Thanks for taking the time to look at my portfolio.

It is made up of a collection of projects in a variety of formats and languages.

Here are the highlights:

[note: My code on here is pretty heavily commented, enough that some might say "overcommented". This is to demonstrate that I understand the concepts fully and not always indicative of how I would comment a project I was working on as part of a team.]

### ASH

ASH (Antigen Selection Heuristic) is a working prototype bioinformatics tool that finds chemically distinct regions in proteins. When designing an antibody to target a protein, it is often beneficial to know which regions are the most distinct. This helps manage the odds of cross-reactivity. For example, if you want to study XYZprotein1 but not XYZprotein2, selecting a region that composed of the same amino acid sequence in both of them will make it likely that your assays are sensitive to both targets.

ASH uses a scale based on hyrdophilicity to compare residues. It used this scale to generate a "mismatch" score to quantify how unlike one another regions are based on their chemical traits, not just a match/no-match system. There is a Jupyter notebook in the ASH directory detailing the algorithm and showcasing prototype Python code. There is also a subdirectory called "ASH++" that shows how the algorithm could be re-written in C++ for greater performance. A walkthrough of the basic idea can be found [here](), and the main repo with documentation and unit tests [here]().


### StRuen

An R Shiny app that permits interactive visualization of the Wisconsin breast cancer dataset. There is also an extra, fictitious (randomly generated) "cohort" variable to permit demonstration of some additional features (tracking members of the same cohort across multiple graphs). check it out [here](https://www.youtube.com/watch?v=qcZ4sB-RUk4).


### An Investigation into a Drop in Gun Deaths in February

This is based on an observation I made while exploring CDC gun deaths for machine learning practice.

### Trump v Clinton Numeric Twitter Metadata Classifier

This is located under the DataScience folder. Because analyzing text presents numerous challenges in the form of word-stemming, context, and tone, I wrote a tweet classifier that uses only numeric metadata to predict determine if a given message came from the handle of Hillary Clinton or Donald Trump. It uses a Kaggle dataset that I heavily re-engineered using Python scripts to more than double its wide. The classifier works with ~97% accuracy.

### Examples By Language

Here you will find smaller programs where practice a variety of languages: Python, Perl, C, C++, and Java. For R code, see the above classifier as I generally use it for Data Science tasks only.

Lately, I have been practicing a lot of Scala and Java, and am always using Python.

### PythonInTheWyld.com

I am building a teach-yourself-python website that can be found at http://pythoninthewyld.com/.
I am not a heavy social media user, but do keep up a light presence for the site, and you can get in touch here:
http://pythoninthewyld.com/home/contact/

Thanks again for reading, and feel free to reach out with any questions through the contact link above.

Regards,

Thadryan
