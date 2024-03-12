# Multi-TRE analysis: challenges, governance requirements, federation

## Overview

### Summary

For multi-TRE analysis to work, there needs to be trust between TREs.
This first relies on a shared understanding of what exactly a TRE is and needs to do, and will thrive when SOPs, accreditations and governance methodologies are shared. This would also benefit from shared understandings and laguage around architecture, sensitivity tiering and more.

The more different TREs there are, the more risk of variability and bad practice, which can affect an entire system of federation.
Public trust is a large concern, and concerted effort will need to be made to ensure the public buys into any federated system of TREs.

### Next steps

Next steps focused on the short, medium and long term:

- **Short term**: Define what a TRE is with a PEST framework, a TRE Maturity Model, common language for sensitivity Tiers
- **Medium term**: Review archiectures for working between TREs, identify key roles and responsibilties in a federated landscape
- **Long term**: Focus on PPIE and public perception, how data is held and managed

## Raw notes

Take home message: Its not about the Technology. In fact the more TREs technically enabled the more risk that the TREs are not fit for purpose for true operation and not trusted for federation. Process and Responsibility => Trust

### Roadmap and Next Steps

**Short term**: understanding what we have

- Define what is a TRE, wrt to **multiple** TREs within a PEST framework that highlights issues that are not just technical, for example includes the diversity of TRE models, the business models of TREs, where risk, responsibility and accountability lay, and includes certifiable PROCESS as a core pillar (shared SOPs). Multi-TREs require new Processes.
- Define a TRE Maturity Model that builds on above to develop a more objective model of TRUST, RISK and RESPONSIBILITY for inter-TRE data exchange. Could be used to assess, compare, and facilitate trust between TREs.
- A common language scale for the ‘tiers’ of TREs suitable for different levels of inter-TRE sensitivity.
- Identify and clarify PEST bottlenecks with examples

**Medium Term**: shifting to newer ways

- Review different architectures and processes for working between TREs
- What would be just enough with what we already have (e.g. 5SROCrate as m-TRE middleware using current processes)
- What m-TRE processes would we need to introduce
- The role of trusted intermediaries (brokers, federated analytics services) to take on risk and responsibility and reposition the Data Sharing Agreements. e.g global identity services linking identities and records, who takes responsibility?

**Long Term**: radical shift

- PPIE education outside the PPIE self selecting bubble to counter mistrust of government and conspiracy theory
- Expectation that data is owned by the NHS?
- Rethink of data holdings and services from Data Warehouses to Data Fabrics.

### Notes

- What is a TRE ?
  - Are they always repositories for single datasets, popup TRE?
  - Not always - many of the environments have multiple users and projects on top of the core dataset, through project-based access through VMs/virtual desktops.
  - There is also a requirement for high performance computing for some datatypes (GPU for AI/imaging, workflows etc)
- Do we need federation? Can we avoid multiple TREs?
  - Governance requirements vary between data classes - you may need TREs to meet each governance requirements.
  - But each TRE is expensive to run, especially assurance, governance, data egress control.
- How do TREs know they can trust each other?
  - When workflows have to be shared between environments, it is easier to share between those with similar accreditations - e.g ISO27001.
  - Federating TREs requires interoperability at the process level, shared SOPs etc.
  - There will be many TREs built from the technological parts - but if there are poorly run ones, they will damage the whole 'brand' and impact on all TRE operators. More TREs, more risk.
  - A 'maturity model' could be used to assess, compare, and facilitate trust between TREs.
  - Legal obligations on indvidual TRE providers act as a strong constraint on data sharing; but a common list of questions might help.
- Can we develop a new brokered distributed/federated anaytics model?
  - We need a new model to allow this.
  - TRE-FX type solutions need to be driven by TREs.
  - Need a common language scale for the 'tiers' of TREs suitable for different levels of sensitivity.
  - People need to query across datasets - there are few cases where you can answer the research question without linking identities and records.
  - But a global identity connecting service would be a huge responsibility.
- How do we carry the public with us?
  - Estonia have an opt-out system for health records, opt-in for genomics data; but when public confidence drops, opt-outs increase.
  - Public perception of risk is a problem.
  - In COVID, people were happy to share data.
  - Even trust in NHS is not universal now...
  - Education outside the TRE 'bubble' to counteract conspiracy theories etc.
- Do trusted data fabrics offer a different view?
  - Networks of secure data services based on Enterprise data models.
