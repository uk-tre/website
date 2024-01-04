# Data architecture of a TRE with C4 modelling language

**Lead:** Joe Leach (Tower Hamlets)

## Proposal

### Summary

This workshop will run some research questions through a draft TRE design for a HDRC (Health Determinants Research Collaborative).
This design exposes the interfaces between architecture and trust for regulatory control of research data management.
We will demonstrate how to:

1. Run a catalogue of fresh metadata describing a network of data controllers (council and health services)
   - Enrich metadata (e.g. by describing data quality dimensions)
2. Support reproducible analytical pipelines that run inside a TRE to:
   - Receive de-identified data from different sources, each of which has applied the same encryption key to identifiers.
     - The encryption key is maintained by a third-party trust (e.g. another HDRC)
   - Link de-identified records (e.g. education/housing/health)
   - Run analyses in-place
   - Perform statistical disclosure control
3. Output trusted analyses

You’d be forgiven for thinking this TRE sounds like a sandbox, but the special ingredient here is the implementation of governance protocols, checking and balancing data uses at key turning points.

To help communicate this approach to TRE design, we have experimented with analogies such as central reference libraries and air traffic control, and will workshop some examples to round off this thought experiment.

### Preparation

Ideally participants would be familiar with [The Goldacre Review](https://www.goldacrereview.org/), though this is not critical!

### Target audience

Colleagues from data science, engineering, and governance.

## Session

### Summary

This workshop introduced the idea of TREs within local council work, making specific reference to the London NHS SNSDE, and how Structurizr can be used for rendering C4 diagrams of data architecture.

Next steps include publishing the design that was workshopped and discussed.

### Raw notes

- Brief introduction of London Borough of Tower Hamlets and Health Determinants Research Collaboration( HDRC)
- Brief Introduction - subnational NHS SDE
- The importance of metadata architecture as a foundation to TRE
- Introduction to C4 model: https://c4model.com/
- X
- TRE design in HDRC/ local authority:
  - To comply with the data governance, the linked dataset (administrative and NHS data) needs to be stored in data haven that are accrediated.
  - Such challenge in data storage and handling make it difficult to facilitate a collaborative research environment under the current data system.
  - AS such, TRE provides a possible solution to offer a playground/ sandbox to allow researchers from council, community, academia and etc. to access and analyse the dataset.
  - Still, the team still faces other issues, IG of NHS data, pipeline to get linked dataset out of the data haven to the TRE, etc.
- Regional London SDE applies to governance on health data, especially for linking
- Subnational SDEs not quite ready for this type of research!
- Usefulness of Structurizr for rendering C4 diagrams of data architecture - as a text based modelling language, you can do your version control with git! - you can incorporate data models (Entity Relations) as images at the lowest "Code" level perspective of diagramming
  11

#### Next steps

- publish the design discussed?
