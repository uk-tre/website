# RSE TRE Community Quarterly Meeting (June 2023)

```{toctree}
:maxdepth: 1
:hidden: true

opensafely
project-maintenance
project-cost-recovery
project-federated-analytics
project-tre-fragmentation
breakout-tre-community
breakout-data-pipelines
breakout-tre-accreditation
breakout-federation-standards
```

**Date**: June 28th June 2023 13:30 - 17:00

## Useful links

- **JISC Mailing list**: https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?SUBED1=RSE-TRE-COMM&A=1
- **Slack channel**: https://ukrse.slack.com/archives/C045ETUPPD0
- **Report from last meeting**: https://uktre.readthedocs.io/en/latest/events/wg_workshops/2023-03-29-march-meeting/index.html
- **Newcastle Commitment**: https://uktre.readthedocs.io/en/latest/newcastle-commitment/index.html
- **Community GitHub**: https://github.com/uk-tre/website
- **Mentimeter**: https://www.menti.com/algf3akq4q6g
- **Read the docs**: https://uktre.readthedocs.io/en/latest/structure/index.html

## Schedule

| Time          | Agenda item                          | Presenters                                                                                     | Notes                                                                                                                  |
| ------------- | ------------------------------------ | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 13:30 - 13:40 | Introduction                         | Hari Sood (Turing)                                                                             | Introduction to day & community                                                                                        |
| 13:40 - 13:50 | Working group updates                | Hari Sood (Turing), Simon Li (Dundee), Fergus McDonald (DARE), Will Crocombe (RISG Consulting) | Updates from WGs on what they've done for the last 3 months, and what they're doing next                               |
| 13:50 - 14:00 | Community announcements              | All                                                                                            | A chance for anyone in the community to share announcements/updates with everybody else                                |
| 14:00 - 14:30 | OpenSAFELY                           | Seb Bacon (Bennett Institute)                                                                  | [Notes](opensafely)                                                                                                    |
| 14:30 - 14:55 | Project workshops 1                  | Breakout rooms                                                                                 | Room 1: [Maintenance burden and its impact on TRE development](project-maintenance) (Jim Madge)                        |
|               |                                      |                                                                                                | Room 2: [A rigorous and fair cost recovery process](project-cost-recovery) (David Sarmiento Perez)                     |
| 14:55 - 15:00 | Project workshops 1 shareout         | Hari Sood (Turing)                                                                             |                                                                                                                        |
| 15:00 - 15:25 | Project workshops 2                  | Breakout rooms                                                                                 | Room 1: [Problems with multiple technology solutions for federated analytics](project-federated-analytics) (Tom Giles) |
|               |                                      |                                                                                                | Room 2: [Unifying approaches to TRE fragmentation](project-tre-fragmentation) (Aida Sanchez)                           |
| 15:25 - 15:30 | Project workshops 2 shareout         | Hari Sood (Turing)                                                                             |                                                                                                                        |
| 15:30 - 15:40 | Break & vote on breakout discussions |                                                                                                |                                                                                                                        |
| 15:40 - 15:45 | Breakout discussion poll             | Hari Sood (Turing)                                                                             | Determining which topics to cover in the breakout discussions                                                          |
| 15:45 - 16:10 | Breakout discussions 1               | Breakout rooms                                                                                 | Room 1: [UK TRE community direction](breakout-tre-community)                                                           |
|               |                                      |                                                                                                | Room 2: [Data pipelines for ingress/analysis within a TRE](breakout-data-pipelines)                                    |
| 16:10 - 16:15 | Breakout discussions 1 shareout      | Hari Sood (Turing)                                                                             |                                                                                                                        |
| 16:15 - 16:40 | Breakout discussions 2               | Breakout rooms                                                                                 | Room 1: [TRE accreditation](breakout-tre-community)                                                                    |
|               |                                      |                                                                                                | Room 2: [Federation standards](breakout-federation-standards)                                                          |
| 16:40 - 16:45 | Breakout discussions 2 shareout      | Hari Sood (Turing)                                                                             |                                                                                                                        |
| 16:45 - 17:00 | Wrap up & Working Group breakouts    | Hari Sood (Turing)                                                                             |                                                                                                                        |

## Introduction

Hari Sood welcomed everyone to the third RSE TRE Community quaterly meeting, which has been renamed the 'UK TRE community' to encourage wider participation.
An announcement was made that the next meeting is to be the annual all-day **in person** event in Swansea on September 4th, as a satellite event to the RSE Conference 2023.
The morning will be hybrid, but the afternoon breakouts are in-person only.

## Working group updates and community announcements

The [Funding and Sustainability WG](https://uktre.readthedocs.io/en/latest/structure/funding-sustainability.html) announced that it is working on a position statement for more sustainable and long-term funding of digital research data infrastructure, and is also working on collecting use-cases for TREs.
There was a call to the community for anyone with knowledge of different cost-recovery models to get in touch with Fergus McDonald (fergus.mcdonald@dareuk.org.uk).

The [Information Governance WG](https://uktre.readthedocs.io/en/latest/structure/information-governance.html) met earlier in the month to discuss IG standards around risk tiering and data ingress and egress.

The DARE UK-funded SATRE project, which is looking to bring together a community-led standard for TRE architecture, also put out a call for members of the community to take part in their [collaboration cafes](https://hackmd.io/GI5EZQouTYuGhkYBSBYHmQ).

## Keynote presentation: OpenSafely

_Speaker: Seb Bacon, Bennett Institute_

Seb Bacon, CTO at the Bennett Institute, gave an excellent and succinct summary of OpenSAFELY, which contrary to some belief is NOT a database but rather open software built on top of databases to enable safe analysis of that data.

OpenSAFELY currently enables analysis of 58 million patients' GP data (over 70 billion records of primary care data) from health record system providers EMIS and TPP, as well as other important health datasets such as hospital data and ONS death registration data.

The OpenSAFELY model differs from many others in that it doesn't give researchers direct access to the data, but instead provides researchers with a randomly generated 'dummy' version of the data (with disclosure risk from the random data essentially zero), which they can use to write their code.
They then submit that code to be run against the real data, which is only accessible by a small number of approved OpenSAFELY staff.
All operations performed are open by design, however, with job request logs openly available, linked via a dashboard to the code that was run through GitHub, with any disclosure-controlled outputs also openly viewable.

The privacy-protecting safeguards of only providing arms-length access to the data to researchers, as well as the open and transparent principles built in by design, was emphasised as key to gaining the trust of the data providers.

A rich discussion followed the talk with lots of questions: please see the [notes](https://uktre.readthedocs.io/en/latest/events/wg_workshops/2023-06-28-june-meeting/opensafely.html)!

## Breakout discussions

### Maintenance burden and its impact on TRE development

_Chair: Jim Madge, Alan Turing institute_

#### Prompts

- Is your codebase difficult to maintain?
- Do you struggle to find or recruit people with the skills you need?
- Does the complexity of your codebase hinder or prevent you making improvements?

#### Discussion

The group discussed challenges with maintaining TRE codebases which are typically large (especially as extra configs are added to fix bugs or improve security), complex, and multi-lingual, and requiring a good knowledge of the technologies on which it is built.
Challenges were split into two categories: recruitment of skilled staff, and high maintenance overheads hindering development, with a lack of even internal comprehensive understanding of it risking trustworthiness.

##### Recruitment and retention of staff

Competitive salaries and cultivating a pleasant working environment where RSE's can work were seen as important draws in recruiting and retaining staff.
Turing offers permament contracts for RSEs (noted as unusual in academia), and Bennett institute fought hard to offer competitive salaries to their RSEs.
Fostering a rewarding working environment could involve ensuring autonomy, interesting work, regular meet-ups, and career development pathways focusing on tech rather than management.

Retention of skilled staff is important and valuable because engineers leaving gives a leak of knowledge which is difficult to recover, and onboarding new engineers onto a big codebase project is difficult.

##### Codebase maintainance

Big and complex codebases are resource intensive to maintain, and academic funding does not support maintainance.
Priorities are often (particularly in small teams) to focus on providing a service to the users leaving little time for development.

One important point of discussion was around trustworthiness: if you don't understand the codebase how can you trust it? And how can you convince the infomation governance authorities that it’s trustworthy? Good documentation is almost as resource intensive as writing the code itself, and questions were raised as to whether it was the best way of imparting knowledge.
One approach that was discussed was to delegate ownership of subsections of the codebase to different people, rather than expect a small number of people to understand it in its entirety.

#### Next steps

The [Funding and Sustainability WG](https://uktre.readthedocs.io/en/latest/structure/funding-sustainability.html) is planning to write a position paper on the 'short-term funding for long-term operation' headache. Do get involved!

### A rigorous and fair cost recovery process

_Chair: David Sarmiento-Perez, Alan Turing Institute_

#### Prompts

- How do you fund the operation of TREs at your institution?
- What activities and costs do you include in the budget?

#### Discussion

Different cost recovery models were discussed, with UCL longitudinal social studies having their costs covered centrally by the funder (so that use of their TRE was free at point of use by the researcher), while others such as the Alan Turing Institute needing to quickly stand-up a cost recovery model in the face of a lack of a dedicated service team for data access requests following their TRE codebase development.
There was some support for the notion that TREs should be centrally subsidised as a public service, where TREs apply for core funding to run their services.

#### Next steps

Nothing immediate was identified, but noting the [Funding and Sustainability WG](https://uktre.readthedocs.io/en/latest/structure/funding-sustainability.html) plans for a position paper on sustainable funding for TREs as above.

### Problems with multiple technology solutions for federated analytics

_Chair: Tom Giles, University of Nottingham_

#### Prompts

- What are the considerations and challenges involved when selecting which federated analytics toolkits TREs should run?
- What security and privacy considerations need to be addressed when managing federated analytics toolkits?

#### Discussion

Many federated analytics toolkits exist, and there is demand among different users for different toolkits.
However, installing and managing multiple federated analytics toolkits on Trusted Research Environments can present a significant burden, requiring careful coordination, technical expertise, and ongoing maintenance.
Bringing in each toolkit requires installation and configuration, compatability and integration with TRE infrastructure, compliance with privacy regulations, computational resource management, updates and maintainance, and the provision of training, challenges which become compounded as more and more toolkits are added especially in the absence of standardisation across different toolkits.

Discussion focussed on how TREs should decide on which toolkits to provide, and challenges in standardisation of these toolkits particularly around security and the Five Safes.
One suggestion was to move the burden of standardisation away from the federated toolkits and onto the TREs themselves.
There is some work, for example, looking at how to describe 5 safes requirements for data objects.
This could enable any federated toolkit to be applied on condition it conforms to the data objects ‘rules’, thus allowing standardisation of the audit trail.
Getting buy-in for this sort of standardisation from a majority of TREs, especially the larger 'high-impact' TREs, was seen as necessary but challenging.
Potential opportunities were also identified, however, especially for those built on similar technology stacks (such as the NHS-SDE Network).

### Unifying approaches to TRE fragmentation

_Chair: Aida Sanchez, UCL_

#### Prompts

- Can TREs have a unified technical approach for ingest to ease sharing of the same datasets across multiple TREs?
- How can information governance be unified or federated to streamline a project's access to datasets across multiple TREs?
- How can federated data discovery be enabled, and who could support this?

#### Discussion

The group discussed the pressures on local data management teams to share the same datasets across multiple TREs, and the resource burden and time it takes to do so when each TRE has their own specifications for ingested data/metadata format.
This has knock-on effects for researchers in timely access to data for their projects, within the context of a drive for data movement to enable increasingly multi-disciplinary research agendas.

Another discussion focussed on the need to support different tools for researchers working within TREs in the face of pressure to stop supporting the use of 'legacy' tools, with pushback from older researchers who tend to be invested in the use of tools like Stata and SPSS, in contrast to younger researchers more comfortable using statistical programming languages like R and Python.

### The future of the UK TRE community

_Chair: Hari Sood, Alan Turing Institute_

#### Prompts

- What is the purpose of this group?
- Should there be paid resource ensuring delivery/accountability around this purpose, and what form should that take?

#### Discussion

Hari started the discussion with a call to consider the group's overall purpose roughly a year since its conception, reflecting on progress and noting the importance of the 'ritual' of bringing like-minded people together, but also challenges in forming productive working groups when relying on people to work on them for free in the absence of dedicated resource to support them.

The group noted the value of the community for knowledge exchange and building awareness across the various TRE teams operating within the landscape.
The group was also seen as important as an advocacy group for Research Software Engineers to help ensure that data providers align to RSE prioirties and needs.

Different models for funding community group management and coordination was also discussed, either by organisations such as DARE UK directly providing secretariat support, or else resourcing that by buying out time from individuals for community management.
Even in the absence of such administrative support, support from funders for travel and subsistence to support community group events was seen as important.

### Data pipelines for ingress and egress

_Chair: Arron Lacey, Alan Turing Institute_

#### Prompts

- Challenges in building data pipelines
- Scope for automation

#### Discussion

Discussion focused on challenges in ingesting datasets lacking a common format or schema, and whether data harmonisation could be done before the data is ingested or else needs to occur within the TRE.
The need for common standards was also discussed, with the suggestion that TREs could only accept ingestion of data in a set number of formats.

### TRE accreditation

#### Prompts

- Who has experience gaining TRE accreditation?

### Discussion

The group discussed the various types of TRE accreditation out there, including the Digital Economy Act (DEA) accreditation and NHS Data Security and Protection Toolkit (DSPT), which are awarded at organisational level.
The group questioned whether accreditation could occur at the level of software and independent of the institution that operates the TRE.
This was seen as unlikely, although the software accreditation could potentially ease accreditation of the institutions that deploy them.
Value was seen for alignment across different organisations/data providers to accept the same accreditation standard, with potential roles for brokering discussions to support this identified for organisations like HDR UK.

### Federation standards

_Chair: Rob Baxter, DARE UK_

#### Prompts

- What levels of standardisation do we need before we’ve got enough to be trustworthy?
- What can we standardise?

#### Discussion

Discussion focused on the importance of standardisation across TREs to enable interconnectivity, noting the proliferation of different federated standards and emphasising the need to simplify the landscape: how do we enforce adoption of a single standard and which one stands the best chance of widespread adoption?
