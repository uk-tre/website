# Researcher Passports

**Leads:** Loki Sinclair (HDR UK) & Fergus McDonald (DARE UK)

## Proposal

### Summary

The purpose of the session is to get a sense from the TRE Community – primarily those running and operating SDEs/TREs – that if a nationwide service were available to verify the “Safe People” criteria would that be beneficial to SDE/TRE operators? If so, what are the requirements for such a service? We would also like to understand the appetite for supporting single sign on across TREs/SDEs.

### Preparation

We’d encourage community members to reflect on the following questions:

- Are you aware of any other groups developing a “researcher passport” that you think we should know about or be collaborating with?
- As someone who maintains a secure data and/or a trusted research environment, what factors do you consider most when approving researchers “safe people” (from 5 safes model). E.g.
  - What training courses they have been on?
  - Depth of experience of working with sensitive data?
  - Previous breaches of your terms of access or other policies?
  - Location i.e. Are they physically present in the UK?
  - Nature of relationship between the researcher and their organisation?
    - i.e. Are they an employee, secondee, under an honorary contract etc?
  - Organisation a researcher works for?
    - If there is an agreement in place with the organisation
  - Identity validation such as a copy of driving license?
  - ORCID?
  - Ethical approvals?
  - Data governance access approvals?
  - Projects they have done research on?
  - Any conflicts of interest/commercial interests e.g. works for a university but also is the director of an SME working in the same field?
- Similarly, what factors do you consider when approving institutes and/or organisations?
- What evidence must a researcher provide to prove compliance with your requirements/the factors above in the eyes of your organisation, prior to being granted access to your environment?
- What evidence must the host organisation of a researcher provide to be considered a “safe setting” organisation to work with?
- If a system could collate all the information you need to consider a bona fide researcher into a single place for review, would this be helpful for you? Are you likely to use such a system?
- In an ideal scenario, what method of singular authentication and researcher approval would you envision streamlining your entire process?
  - Feel free to brainstorm and outline an optimal software solution that not only caters for user authentication (I.e. SSO), but also verification and data access being granted.
- When dealing with inappropriate data use, what processes do you follow?
- If a system could offer a complete history of a researcher’s data access approvals from other institutes and potential red flagging, would this be considered helpful or harmful?
- If there was a UK wide solution supporting single sign on for researchers accessing sensitive data, how likely are you to support such an access model within your existing methods for researcher account authorisation?
- Federated analysis projects are likely to require a single sign of for researchers across TREs. To support such projects do you have any preferences on what single sign on/authorisation standard is adopted across the TRE community? Any thoughts on what would help support these types of projects?
- What is the most important aspect when considering feature development and implementation of external interoperable systems within your institute? For example:
  - Do you consider ease of implementation over feature-set or does feature-set on offer ultimately determine solution adoption?
    And finally...
- Would you be interested in working with us to provide requirements and test a researcher passport solution?

#### Reading:

- Brophy, R., Bellavia, E., Bluemink, M. G., Evans, K., Hashimi, M., Macaulay, Y., McNamara, E., Noble, A., Quattroni, P., Rudczenko, A., Morris, A. D., Smith, C. and Boyd, A. (2023) “Towards a standardised cross-sectoral data access agreement template for research: a core set of principles for data access within trusted research environments”, International Journal of Population Data Science, 8(4). doi: 10.23889/ijpds.v8i4.2169.
  - [Publication](https://ijpds.org/article/view/2169)
  - [Template agreement](https://zenodo.org/records/8256235)

##### Extracts from the [DARE UK Phase 1 Recommendations](https://zenodo.org/records/7022440):

###### Federated identity and user authentication standards

There is a need to identify – in collaboration with stakeholders from across the landscape – and drive forward the adoption of a common user authentication protocol by infrastructure providers.
Conceivably, this would need to be coordinated and overseen by UKRI itself, as it has the appropriate remit to act as such an authority.
A transparent, cross-domain, national approach could remove the responsibility from individual groups and therefore improve consistency and increase efficiency across the sensitive data research ecosystem.

Stakeholders engaged with during DARE UK Phase 1 have highlighted that this is a prerequisite for all forms of federation to occur and will aide in the creation of a ‘research passport’ that is cross-linked to multiple regulatory bodies for verification and validation by data custodians.
Stakeholders also highlighted existing federations, for example the UK Access Management Federation for Education and Research, which will need to either be expanded or linked to other federations being created, such as NHS Care Identity Service 2 (CIS2) or GovRoam.
The existence of modern industry and community standards of user authentication (for example, SAML, OIDC, OAUTH2 and Global Alliance for Genomics and Health (GA4GH) Passports) were also highlighted.
These existing standards should be leveraged as the basis for user authentication to allow for maximum interoperability at a national and international level.
As user authentication is a crucial component of a national TRE standard, stakeholders also highlighted the need to support different forms of identity verification and have logging and auditing embedded across the system.

###### Researcher accreditation

A key requirement highlighted by stakeholders has been the need for a streamlined approach to researcher accreditation.
While there are a number of existing training modules for sensitive data handling (for example, those provided by ONS), many of these trainings are duplicative without allowing for equivalence or mutual recognition between modules.
Those engaged with during Phase 1 highlighted the need to develop a shared standard with service users and providers towards a federated approach to training content.
Modularisation was also highlighted as important to allow for flexibility to cater for specific data modalities or sensitivities, for example through ‘core’ modules as a standard foundation for all accreditation courses with the possibility of ‘extended’ modules in specific cases or contexts as needed.
Stakeholders affirmed that work to standardise and streamline the researcher accreditation process was sorely needed, along with reciprocal or mutual recognition of accreditation by different TRE providers.
Providers should aim to offer a consistent researcher experience across data access points, and ideally make the process feel as though the researcher were accessing data on their own machine when this is not the case.
Training could be made portable across TREs through standard accreditation for researchers acting as a TRE ‘passport’.
The Digital Economy Act, 2017 (DEA) already works as a passport in some respects, with shared accreditation existing across certain TREs.

###### Private sector and international researcher accreditation

Currently, private sector researchers can apply to become accredited researchers under the DEA, and therefore apply for access to data held within DEA-accredited research environments once accredited, via the same process as academic researchers.
In the context of UKRI-funded research, private sector researchers can also participate in sensitive data research in the public good as part of consortia led by a UKRI-approved research organisation.
However, there was widespread feedback from stakeholders engaged with during DARE UK Phase 1 that improving the ability for private sector researchers to collaborate on sensitive data research is important.
Participants of the DARE UK public dialogue wanted sensitive data to be made securely accessible to private sector organisations and did not see a need for data access requirements to differ for these organisations, as long as the research is motivated by public benefit over financial profit and there is transparency throughout the research lifecycle (see Chapter 3: Demonstrating trustworthiness).

### Target audience

TRE operators and/or information governance professionals (as related to the requirements for approving researcher access).

## Session

### Summary

It was highlighted how resource intensive the current manual researcher approval process at UK biobank is, and how an autonated system would help with this.

Achieving the perfect system may take a long time, but an MVP-style system that verifies researchers' identity and project history could be a good starting point.

There was a question of whether an independent body needs to exist to accredit these passports, or whether providing appropriate researcher details would be sufficient on a TRE-by-TRE basis.

Further discussions centred around processes to interrogate validity of researcher records, how to record 'untrustworthy' researchers, and how to accommodate different levels of permission for different researchers, depending on how sensitive the project they are working on is.

### Raw notes

- UK Biobank working with additional biobanks in pipeline (international perspective additionally challenging)
- 6 FTE managing the overall workload of researcher approval
- Do not make a quality assessment of a researcher
- Main process currently followed:
  - Applicant must supply CV
  - Applicant supplies any relevant papers/publications
  - Email / Telephone number provided
  - Institute contacted to check alignment
- Since inception, ~30,000 applicants. Very manual, painful process. Process takes between ~10-60mins per application.
- Would other TRE/SDEs be willing to use the collected researcher verifications already accepted from UK Biobank DB?
- An automated system that provided a full history of researchers would free up time from our point of view. We don't vet their skills or what coding languages they're familiar with. Just that they are who they say they are.
- The perfect system could take "15 years" to cover all eventualities. Start with the basics to build an MVP style verification. A global "fits all" will likely end up in nothing being delivered.
- Bona fide researcher
  - Approved researcher training (e.g. ONS/UKSA approved researcher training)
  - Is a system like this needed? Yes, but adoption becomes key. Our numbers are smaller than those of very established TREs.
  - 5 safe's already sets the path for people verification
  - Process:
    - Due diligence against bona fide "employee and employer" - treated as a single entity by LLC.
    - Conflicts. Look at CV, training and track record. How people who have multiple employers may have conflicts in application.
  - Question:
    - Who is going to do the accrediting of these passports?
    - TREs are a step removed from this and it should be external to us and better by an independent adjudicator
      - Does anyone _need_ to accredit a passport, with full history of researcher activity being sent - would that be enough to make a decision at TRE level?
      - It's about how trustworthy the details are? Due diligence can't be based on "trust" alone.
- There is a marginal benefit to a system that could provide this information in a passport "stamping" fashion.
- Only UK accessible (at least for now). Requires ONS researcher training. Contact institution for validation. Ethics project level review process, where it confirms UKSA template, and if a project meets criteria then a panel review for "public good".
  - One of the key issues is about timeliness of accessing data. Current records that ONS and/or UKSA have don't reflect changes.
  - How do you "block" someone off if they have damaged another TRE? More from the operational aspect
  - How can we trust the information - implication being that we can interrogate and get answers, but can we trust the data being entered?
  - Who can accredit?
  - What secure methods can be designed to prevent tampering?
  - Part of the process would mainly be removing the tedious processes behind the vetting. To some extent it doesn't need to _say_ anything about the history, just provide key indicators.
  - Discussions surrounding structure about "what do we mean", "who do we trust". Implementing a system as an ORCID++ to later build on trust info to interrogate would be a good starting point. Separate issue about trustworthy facts being available and current / "live" can come later.
- How do we capture the 'experience' of the user?
  - H-Index like system tied to an ORCID?
- After a series of projects, open subscription account as reward. Self-triaged system for FO, in a more trusted env than machine. Demonstrating a trusted user.
- OpenSafely have differing tiers. Defining different levels of "permissions" depending on status of trust for user.
- History of TRE access would lead to federation of mapping users with access to multiple environments.
- Building 'credit' feature to define level of trust and access tier.
