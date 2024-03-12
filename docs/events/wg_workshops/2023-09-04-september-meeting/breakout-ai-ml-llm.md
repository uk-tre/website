# Current state of the art re data linkage/federation/AI&ML&LLM across infrastructures: federation, governance, safe output methods

## Overview

### Summary

Issues about federation of datasets were discussed, including identifying different datasets across multiple systems, how to collect identifiable information robustly, and how we can link up different approaches across the 4 nations effectively.

There was further discussion on how to effectively check ML models within TREs.

In the case of governance, it was suggested that a project working across multiple TREs should have one singular governance process.

### Next steps

- Create a 'panel' focused on specific type of data/research (e.g. health, crime, financial) who can oversee specific research projects within these fields

## Raw notes

### Data Linkage

#### How do you go about the NHS Number?

- Uses NHS Standard NF5, after 3 they went to manual to track through the system.
- Issues with health and non-health data

#### Names such as Dave / David can cause problems.

- Linksmart is a solution for this.
- Collecting Crime Data

#### Scotland's Approach

- a national ID number

### Federation between datasets

- Identifying with confidence across TREs is important
- Problem: Linking health with something else is problematic to match up and link it with addresses and names
- Separation functions
- Person has all the identifying information, but they do not have the data
- TREs communications between each other need specific criteria, Scotland has 5 TREs
- Having more than two, and introducing a central one is a possibility
- Issues with identifying A-B data sets across multiple systems
- Seeding Death Data -- David and Debra Smith: D. Smith & D. Smith causes gender incompatibility issues
- National Drug Treatment Data -- At source they only collected initials 'D.S.', Gender and MM/YYYY of DOB. Deidentifying can cause linking problems. Education to non-education where they don't have their common 'number' -- how confident can we be that Participant A is the same participant in another TRE? If you're not sharing names & addresses
- Bringing in NHS data and also pseudo anonymise it -- how can you work with it without a key?
- Once you got a data linkage -- bringing the different data types into a data set (TRE). E.g. Linking mental health data and shopping data, if you anonymise that and have their own key -- they can do it anonymously for external sources
- Education data between England, Scotland and Wales might use different notations
- Residential Data can be used as a key
- 'E-child' trying to link the NHS with the Department of Education

### AI & ML

- People misunderstand the terms AI & ML with 'Statistical Modeling'
- Based on risk factors you can determine 70% precision pre-diabetic chance
- Accessing 'clinical like data' with similar terminology to mimic clinic systems
- AI -- Offline AI: you can have an offline machine learning model -- yes
- Would multiple AIs learn the same thing on same data sets? -- no
- You can make it work with a shared API though (Stroke Predicition)
- APRs -- 8-9 expensive centre
- Different type of interpretation of ML, ML data on health 'takes your job', ML data on other scenarios might be socially acceptable
- Pattern finding models are popular and precise, this is lacking in statistical modeling
- At the end of the day, medical data ML is not understood why it gives that result
- Checking models are problematic and difficult, unsure results and unsure contents of the model begs the question of the model's authenticity

### Governance

- Process is repeated a lot, no committee talks to each other and are a separate entity
- Cannot start work unless approved
- Doing a project between TREs, each TRE will have an approval process, ideally a multi TRE Project requires a single approval process, this decision should be approved across the other one

#### What would a solution to this problem look like?

- Current state of the art is the overarching question -- needs a TRE panel to decide what is state of the art
- Single 'panel' on a specialty (e.g. health, crime) who deal with specific projects, additionally members of the national TRE supervision
