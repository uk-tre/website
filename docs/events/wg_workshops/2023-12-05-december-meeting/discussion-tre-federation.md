# TRE Federation: appetite for a standards working group(s)?

**Chair**: Rob Baxter (DARE UK)

## Prompts

Federating TREs to enable linked-data research is a big topic, with lots of current activity.
DARE UK have tried, in the spirit of George Box[^1], to draw the current threads together into a common architecture.
But what next? Forming a community working group to develop the architecture and technical standards seems like a good thing to do.

- How much enthusiasm is there to form a WG? Assuming there is some…
- What should its scope be? Infrastructure standards? Query standards? Data? Governance?
- What starting points make sense? DARE UK architecture (v 2.0 coming soon)? Current tech ideas?
- What outputs would we aim for, on what timescales?
- How best would we organise and collaborate? Docs on GH webpages, with issues, boards etc? Something else?

[^1]: _All models are wrong, but some are useful_

## Summary

Conversation started by asking what work is already being done in this space.
This included exploring pre-existing standards, whether there is already a shared definition of federation, and where the use cases for federation already exist.

The need to map the ecosystem was highlighted, to show where the influence lies and how key decisions are made - especially in spaces where the data is not allowed to move out of internal systems.

The need to factor in data and information governance, in tandem with any technical solution, was highlighted.

Next steps include setting up a high-level federation working group, and use this to explore critical topics within the idea of federation.

## Raw notes

- Important to note that there are organisations that are already working in this space - their meetings will be set.
- Question: what other working groups exist and why do we need a new one? What aren't they covering?
- Question: Are there any existing standards?
  - Small scale projects have succeeded - some funded by DARE UK - but not broad demonstration... yet?
    - Teleport:
      - https://dareuk.org.uk/driver-project-teleport
      - https://dareuk.org.uk/preserving-public-trust-in-the-evolution-of-trusted-research-environments-teleport-federated-data-access
    - TRE-FX:
      - https://dareuk.org.uk/driver-project-tre-fx/
      - Final report from the TRE-FX DARE UK project: https://zenodo.org/records/10055354
- Question: Do we have a shared definition of federation?
  - How is that different to data pooling?
  - Should we be aiming for a meta-learning? distributed learning?
  - Potential definition: federation is a group of TREs that trust each other
    - Doesn't have to involve moving data... but can...
- Examples of federation in the genomics space
  - Question: what does it mean that the federation is specific to genomics?
    - No limit on the fedearation architecture but front end standardisation would need to assess the data for egress.
- Question: Do we have a list of use-cases that describe the need for federation to exist.
  - Yes for small ones but not coherently collected in one place.
  - One idea: run a workshop to build up "grand challenge" style definitions
- From the zoom chat:
  - The 'trustworthy' and 'governance' bits depend entirely on what information flows over this inter-SDE network.
  - https://dash.ohdsi.org/research
  - https://www.datashield.org/about/about-datashield-collated
  - the above are examples of existing use-cases
- Note that the individual TREs publish many more research outputs than OHDSI - interested to know why that is - what are the needs that OHDSI aren't meeting?
- Improved analyses / insights / inference with very large data sets
  - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6451771/
  - Note though that without a common data model it is very hard to combine data for such large scale analyses.
    - Common data standards are very expensive to implement.
      - Not total agreement in the room.
      - But note that the mapping to a data standard - eg OMOP - is very variable.
- Note that many goverment departments / organisations are focusing on "data not moving" - so where is the space for federation?
  - "lift and shift" stops being able to scale very well....
- Need to map the ecosystem of working groups
  - Need to understand who has the power and influence...
  - "A federated protocol for the working groups!"
- Note that the design of a TRE is conceptualised to bring researchers in and to NOT let data out...
  - So do we need a concept beyond a TRE? Do we need a new phrase / name?
  - TREs that are designed from the outset to federate?
- DataSHIELD has been around for 10 years - not complete but huge open source community of researchers.
  `- And there is this -> https://www.hpe.com/us/en/solutions/ai-artificial-intelligence.html
- Data always move - even Genomics which are years ahead, the raw data does not move but the findings from the genomics do - that's data
- NHS SDE - adopting OMOP I believe - seeking to share maps across SDEs rather than each doing own
- I think the big challenge is around people understanding this space and removing the IG blockers.
- The NW SDE is 'federated' by design.
- How does anyone validate federated analyses if data doesn't move! You can't see the outputs...
- Addressing the techie part of federation without factoring in the data & governance pieces is only a fraction of answer.
  - These things do run at different speeds

### Next steps

- Propose a high-level federation WG (IG?) as an umbrella/place to start, using the UK TRE/DARE UK/RDA model
  - Prob host on GitHub somewhere
  - Use DARE UK Federated Architecture Blueprint v2.0 to seed (coming soon!)
- Within that, tease out the best approaches to key topics:
  - Federation terminology (cf. Pete/Madalyn's idea, and the [DARE UK Driver common vocab](https://docs.google.com/document/d/1SJ6CJG8yHzsvtU7MyzdNOF_S0fZVJb_i/edit) )
  - What is a TRE? Is it an individual "cluster of boxes", or can it be a formal federation of a number of "clusters of boxes"? (a super-cluster?)
    - What does TRE accreditation for a piece of public cloud mean, for instance?
    - Is the NHS SDE Network a TRE in itself?
    - What is the sound of one hand clapping?
  - Governance around this broader idea of a TRE as a "federation of smaller sub-TREs"
    - Is "thinking federal" from the get-go useful? Possible?
  - Data & queries: how can we ever harmonise data enough for a federated query to return comparable answers?
