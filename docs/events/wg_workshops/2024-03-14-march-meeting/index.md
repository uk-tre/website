# UK TRE Community meeting - March 2024

:Date: [Thursday 14th March 2024](https://arewemeetingyet.com/London/2024-03-14/09:30/UK%20TRE%20Community%20meeting)
:Time: 09:30 - 13:00
:Registration: https://lu.ma/n7yybonh
:Location: Online

```{toctree}
:maxdepth: 1
:hidden: true

demo-kings-tre
demo-scotland-ras
demo-trenity
discussion-researcher-verification
workshop-community-governance
workshop-cybersecurity-risk
workshop-glossary
workshop-sde-tre-definitions
```

## Background

​​The UK TRE Community is a community of over 200 people that has grown organically over the last year for anyone interested in TREs, including researchers, operators, information governors, managers and more, from all sectors and disciplines.

​​The core aims of fostering collaboration and sharing of innovative ideas to support the delivery of groundbreaking research with sensitive data have resonated across the UK and beyond.

​​The community has a website, an active mailing list and Slack channel, and working groups tackling shared problems.
We also run quarterly events like this for the community to come together, discuss ideas and problems within the TRE space and work collaboratively together on possible solutions and ways forward!

## Agenda

| Time          | Agenda Item                                  |
| ------------- | -------------------------------------------- |
| 09:30 - 09:45 | Welcome and intro                            |
| 09:45 - 10:30 | [Keynote + discussion](#keynote)             |
| 10:30 - 10:45 | [Community updates](#community-updates)      |
| 10:45 - 10:55 | Break                                        |
| 10:55 - 11:00 | Intro to breakout session 1                  |
| 11:00 - 11:45 | Breakout session 1 [(see below)](#session-1) |
| 11:45 - 11:55 | Break                                        |
| 11:55 - 12:00 | Intro to breakout session 2                  |
| 12:00 - 12:45 | Breakout session 2 [(see below)](#session-2) |
| 12:45 - 13:00 | Wrap up                                      |

### Keynote

Dr Chris Russell, Head of NHS Research SDE Network: Data for R&D

### Community updates

#### Launch of the Researcher Access Service at Research Data Scotland in Spring 2024

_Katie Oldfield_

The service is a streamlined pathway for data professionals.
It digitises the process for the first time, making it simpler to apply to access Scottish Public Sector data for research.

Initially launching with 9 datasets https://www.researchdata.scot/our-work/current-projects/researcher-access-service/

#### Scottish Safe Haven Charter Refresh

_Katie Oldfield_

Scottish Safe Haves are refreshing the charter to reflect advances in Scotland and across the UK https://www.researchdata.scot/our-work/current-projects/scottish-safe-havens-steering-group/

#### Public Engagement Fund Completed

_Katie Oldfield_

We funded eight projects across Scotland to carry out public engagement activities around data.
Their findings, summaries and contact details are available online for more info https://www.researchdata.scot/our-work/shaping-our-services/public-engagement/

#### DARE federated architecture blueprint v. 2.0 out soon

_Rob Baxter_

#### Working Groups

##### Citizen Agency Working group

_Pete Barnsley_

The UK TRE Working Group on Citizen Agency has recently developed a draft scope and output report framework [available here](https://github.com/FrancisCrickInstitute/UK_TRE/tree/main/Citizen%20Agency%20Working%20Group).

It was recognised that citizens could have much more involvement in research and this would be a good thing.
How it relates to Information Governance and data release processes is a key area.

It would be very useful if everyone read the initial reports from January.  
Input to the proposed Discussion Document is particularly welcome - ideas on services that both citizen and researcher may want and views on the Information Governance implications and impacts on federation approaches.

##### Extending control Working Group

_Pete Barnsley_

The UK TRE Working Group on Extending Control has recently developed a draft scope and output report framework [available here](https://github.com/FrancisCrickInstitute/UK_TRE/tree/main/Extending%20Control%20Working%20Group).

It was generally recognised this is a key area, how Information Governance can be extended by technology, but views on how and the extent to which they differ are varied.

It would be very useful if everyone read the initial reports from January, and shared views on issuing a “Request for Input”.

This process would collect solutions, or components to one, and ideas on how extending control can be implemented.  
Also it would be helpful to have thought about the constituencies that should be approached and how to do that.

##### SATRE Working group

_Chris Cole_

We had a successful meeting on 27th Feb where several topics around implementation, evaluation and accreditation were discussed which we’re in the process of bringing together and reporting on.

### Breakout sessions

#### Session 1

- [](./workshop-cybersecurity-risk.md)
- [](./workshop-glossary.md)
- [](./demo-scotland-ras.md)
- [](./workshop-community-governance.md)

#### Session 2

- [](./workshop-sde-tre-definitions.md)
- [](./discussion-researcher-verification.md)
- [](./demo-kings-tre.md)
- [](./demo-trenity.md)
- [](./workshop-community-governance.md)

# UK TRE meeting 14th March 2024 - Breakout room summary discussion write-up

## Breakout session 1, Room 1: Handling cybersecurity risk in TREs, through technology and IG

**Summary**
The discussion revolved around assessing and managing security risks within TREs, particularly concerning the introduction and handling of code, software, and containers. Participants explored various facets of security, including the possibility of assessing the security of different components within TREs, how to communicate security assessments, and strategies for managing "insecure" code through technical or information governance (IG) controls. There was a consensus on the importance of understanding how to assess risks and interact with IG teams to effectively manage these risks. 

The conversation also touched on the concept of "risk credit" and how the inherent security measures within a TRE might allow for a reduction in additional risk mitigation efforts. For example, it was noted that in the TRE context, data ingress security failure is somewhat protected through other 5 safes protection within the environment, which is not the case with data egress, making data egress much The debate included considerations on whether to allow arbitrary code, the implications of containerization from a risk perspective, and the challenges of inspecting and sandboxing code effectively.

Participants covered practical experiences and approaches from various institutions, emphasizing the balance between enabling research and ensuring data security. The discussion highlighted the complexity of differentiating between code, scripts, software, and containers, and the practical challenges of thoroughly inspecting code due to dependencies and the vast amount of code that could be involved. 

The overarching theme was the need for a nuanced understanding of risk within TREs, advocating for technical (e.g.  network isolation), system resilience(e.g. secure even at privilege escalation) and IG controls (e.g. Safe People) to mitigate risks associated with software and data management. 

**Next steps**
- Form a working group around this topic to produce outputs such as:
    - a risk mitigation framework
    - establish categories of bad incidents
    - White paper
    - explanatory documents tailored to different personas (e.g.technical, researcher, IG) to better communicate and manage risks involved in TRE operations


## Breakout Session 1, Room 2: Glossary working group scoping

**Summary**
The discussion revolved around the creation of a unified glossary for the Trusted Research Environment (TRE) community to ensure a common understanding of terms across various projects and entities. Given the existence of multiple glossaries (with surprisingly little overlap - only 2 entrie - including the term 'TRE') there is a proposal to consolidate these resources, merging and reconciling terms where necessary and hosting the unified glossary on a dedicated platform like GitHub. 

Why do this? It was agreed that a shared lexicon is crucial for achieving interoperability and federation among TREs (technical/operational alignment), as well as for ensuring a shared understanding of terminology that can support provenance and compliance efforts/governance and security requirements set by data controllers. 

Challenges discussed include how to manage changes to the glossary over time, resolve conflicts between differing terminologies, and ensure the glossary remains aligned with related (and sometimes changing) legal and regulatory frameworks. The importance of considering public understanding and perception of these terms was also emphasized, suggesting that the glossary should be accessible and comprehensible to a wider audience beyond just the immediate TRE community. There is a need for a balance between formal definitions to support service federation and interoperability, and a more casual vocabulary that remains transparent and understandable to the public. The consensus leans towards initiating this project by putting forward a preliminary version of the glossary for community feedback, with an understanding that the glossary's development and refinement will be an ongoing process.

**Next steps**
- Set something up in UK TRE GitHub
- Focus as a goal on "formal" definitions for federation of services/interoperability



## Breakout Session 1, Room 3: Recognising, and implementing, the GDPR and Data Protection Act provisions for scientific research in Scotland’s Research Access Service

**Summary**
Scotland is advancing its data systems to facilitate research while navigating GDPR regulations. The approach includes dividing the challenge into two segments: data controllers preparing and anonymizing data to create 'research-ready' datasets in compliance with GDPR, and once researchers access this anonymized data within a Trusted Research Environment (TRE), it's considered outside GDPR's purview because of anonymisation. This strategy aims to move away from the inefficient create-and-destroy method, reducing the oversight burden on privacy boards. The discussion also focused on the importance of maintaining public trust, with plans to engage the public in dialogues about the definition of public good and the mechanisms of data access and use by researchers, alongside a review of private sector access to NHS data.

Discussions highlighted the necessity of explaining to the public the low likelihood of reidentification from anonymized datasets and the non-applicability of GDPR to such data in research contexts. The conversation acknowledged ongoing challenges, such as bottlenecks caused by the requirement to keep data separate across different organizations and concerns over private sector access to NHS data

**Next steps**
- info sharing between RDS and Smart Data Foundry on public engagement plans, and on Rowntree foundation on fine grain data into TREs for answering policies - Launch of Income Volatility Dashboard with JRF (smartdatafoundry.com)


## Breakout Session 1, Room 4: UK TRE Community Governance and progress

**Summary**
Short discussion:
- suggestion that an overview diagram showing the different organisations in the UK TRE network would be useful 
- some discussion on incentives for official endorsement, with exposure and buy-in from the growing community seen as potentially very valuable

Complete notes taken during the session: Room 4[UK TRE Community Governance and progress](https://hackmd.io/Vvdzld4NTO6-4Dt5m_poLQ) - Discussion

## Breakout Session 1, Room 5: SATRE

**Summary**
The discussion revolved around the experiences of the Safe Haven AI Platform (SHAIP) and AzureTRE of evaluating their TREs using the SATRE specification, and feedback on it. 

One idea put forward was for some segmentation of the SATRE specification for capabilities by domain (e.g., technology providers vs. operational roles) to tailor evaluations more precisely. This approach could enable TREs to self-assess against the parts of SATRE that are most relevant. Initial impressions of using SATRE highlighted its comprehensive nature but suggested a need for a more condensed version to improve usability. It was also noted that requirements for federated research environments are missing.



## Breakout Session 2, Room 1: SDE/TRE Definitions

**Summary**
Discussion focused on the thorny topic of distinctions between what is meant by the terms 'Safe Data Environments (SDEs)' (adpoted by the NHS SDE network) and 'Trusted Research Environments (TREs)' (the more widespread and historical term). The lively discussions already held on this topic on the UK TRE email list, as well as survey responses to a working group forming around this, were mentioned (with links)

There was debate over explicitly labeling environments as "trusted" or "secure," drawing parallels to assurances like "poison-free" water, suggesting that trust is earned and should not need to be asserted.

Survey feedback and other previous discussions hinted at a distinction between handling identifiable versus de-identified data, with some suggesting that SDEs might focus more on operational analysis and data preparation (including the use of non-deidentified data), whereas TREs could be more research-focused,  handling de-identified data for scientific research under less stringent governance regulations like the DEA. However, it was acknoweldged that there isn't consensus on this view, and whether those falling either side of this proposed boundary would accept it. The debate is clearly far from over!

**Next steps**


## Breakout Session 2, Room 2: Researcher verification in line with Safe People principle

**Summary**
The discussion revolved around work being led out of HDR UK on a Researcher Registry/"passport" system aimed at facilitating access to Safe Data Environments (SDEs) and Trusted Research Environments (TREs) by verifying researchers. Key points touched upon the registry's validity period, the importance of a digital identifier aligned with existing digital identity frameworks (like DSIT's digital identities work), and the registry serving as a "living ledger" of a researcher's identity, credentials, experience, and affiliations. The potential use of blockchain technology was discussed for maintaining a balance between immutable and mutable information to provide a comprehensive view of researchers' accreditations.

Challenges and considerations included aligning accreditation meanings across different organizations, integrating information from external systems like ORCHID and IRAS for ethics verification, and the responsibility of TREs to make final access decisions based on registry data. The registry aims to streamline the vetting process by compiling information from various systems into a common model, thereby assisting TREs in making informed decisions regarding data access. The conversation also highlighted the necessity of including project ethics and permissions in the vetting criteria and discussed the logistics of maintaining the registry's accuracy and currency, emphasizing the collaborative role of researchers and organizations in keeping their information up to date.

**Next steps**

- Slides and break out notes to be circulated following the meeting. 
- Interested in working with us to provide requirements and/or test a researcher passport solution? Please contact rachel.tesfaye@hdruk.ac.uk


## Breakout Session 2, Room 3: TRE at King’s: Deployment & Egress Simulation

**Summary**
Michal presented a demo and overview of King's College London's new Trusted Research Environment (TRE), currently hosting of 16 live projects, including notable ones like the MIREDA maternity study and Kings/GSK digital biological twin studies. The on-prem TRE has an automated deployment process with a software stack that is 99% open-source, using tools like Terraform/OpenTofu for environment deployment and Chocolatey for software package deployment, including Microsoft Office, R, and Stata. Each project within the TRE is limited to a maximum of two users. The importance of data egress over ingress was mentioned (note Breakout Session 1, Room 1 discussion on Cybersecurity that discussed a similar point). During a demo, Michal showcased how researchers access the TRE, including a view of the deployed software packages and the Data Egress Portal, which features tasks functionality exclusive to Egress Supervisors. Researchers also have access to data backups for up to 20 days in case they delete something accidently. Future considerations for the TRE include a potential move from on-prem to Azure and exploring automation for the egress process, though challenges remain due to the variety of output formats and resource limitations (one person only) for implementing new features.

**Next steps**
- DARE UK AI Risk Evaluation Workgroup publishing report end of March/Early April which will detail additional steps & consideration needed as part of egress process for AI models from TRE's https://dareuk.org.uk/dare-uk-community-working-groups/dare-uk-community-working-group-ai-risk-evaluation-working-group/#:~:text=AI%20Risk%20Evaluation%20Group&text=The%20AI%20Evaluation%20Working%20Group,of%20individuals%20within%20the%20data.


## Breakout Session 2, Room 4: Trenity demo - an in house tool for managing users, projects and file transfers in TREs

**Summary**
Trenity aims to standardize the construction, deployment, and management of Trusted Research Environments (TREs), driven by principles like SATRE (achieving 70% SATRE compliance from the outset) and the Five Safes framework. The product suite includes Trenity Secure and Trenity Edge among others, all managed through a unified dashboard facilitating Information Governance (IG) actions such as data ingress and egress, customizable descriptive data models, and comprehensive views of assets (datasets) and projects. Project dashboards provide members with various tools including task management, discussions, and literature review, with a distinct results tab that integrates the approval process for data release through a multi-role approval process (PI -> reviewer -> final release by TRE) for data egress. Trenity plans to adopt a service-based business model, offering the "base" software for free with a service-based business model on top.

**Next steps**


## Breakout Session 2, Room 5: UK TRE Community Governance and progress

**Summary**
The DARE UK grant for the Community Management group (concluding end March 2024) included development of a more user-friendly resource hub to replace the existing ReadTheDocs website, using Hugo for cost-effective, low-maintenance web development. This hub will feature sections for governance documents, resources, working groups (with a requirement for at least one open meeting), a comprehensive events calendar, and opportunities for community involvement. Additionally, the governance documentation of the community is now developed and open for review and input through an open project board on GitHub. Concerns have been raised about ensuring broader community engagement beyond GitHub for (final) community group output endorsement, highlighting the need for transparent objection handling and decision-making, as well as logging conflicts of interest during any community voting processes.

**Next steps**
- Generate 1-pager, with instructions on how to submit an event, instructions on how to submit a community resoruce etc. Could be useful to share with comms teams from different orgs (comms people don't generally come to UK TRE meetings but will be better across events/resources that might be of interest)
- Add submission link (Google form) to https://www.uktre.org/en/latest/events/index.html

