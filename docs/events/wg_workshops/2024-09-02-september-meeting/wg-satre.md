# Working Group: SATRE

Chair: Chris Cole

## Prompts

- Community updates/priorities
- DARE phase 2
- Working Group activities
- Specification Version 2.0

## Notes

### In Person Group

- SATRE: a baseline specification for what a TRE is
- Feedback from Vicky Glynn - SATRE was useful for defining what good looks like. Haven't yet assessed ourselves
- In the near future, a question we should answer is how to sustain SATRE? Fee for accreditation? - Important to identify how to fund maintenance. This was part of the original proposal but remains to be done - CE has a tiered model, self accreditation and _formal_ accreditation
- The industrial/IT world has moved on faster than the research world, what is acceptable looks different. SATRE should be ambitious and push for improvement - There is also an accessibility argument. If rules are too strict/specific they could unreasonably exclude existing TREs - Also, if rules are too fuzzy or vague, the spec could be toothless and ineffective
- SATRE 1 achievements
  - Using what exists and fitting what the community is doing, rather than dictating
  - Engaging public
  - Started as a purely technical spec, became a truly community driven project
- SATRE could be a tool to help federation. When talking to the public about data sharing/federation, SATRE could be used as a common understanding of what a TRE is, why they are trustworthy
- The next DARE phase could be reference implementations of SATRE elements. We should get feedback on what components the community would value the most.
  - We imagine modular components would be useful
  - Many existing TREs are fairly monolithic
  - Modularity/reusability also benefits from system agnostic designs. E.g. targetting Kubernetes rather than a particular cloud provider
- There are a couple of in-depth questions being raised. The SATRE standard is pretty high level. What does good look like at a process/technical implementation or policy level, e.g. Infrastructure-as-code environment on Kubernetes or machine readable information risk assessment
- Nuanced approach where things are aware of the tier of data being processed.
- We did some work in SACRO to look at the risk and tiering model.

### Online group

NHS SDE research network in England have taken the published SATRE model and enhanced it for their own needs, such as adding maturity levels.

- 11 subnational SDEs in addition to NHS England SDE which is using the core data returned by all the providers.
- Split of 12 SDEs
- For SDE read TRE

Key part of what was needed was federation piece.

- Starting to tackle the federation aspect.
- Pulling out the federation aspects (prefixed SNSDE things they have added).
- Federation and interoperability pulled out to focus on needs of SDE colleagues.

Focus on capabilities that weren't well defined in initial SATRE draft.

- Use SATRE model to self assess capabilities - for a number of them taken some of these capabilities and started to think about the different ways they can implement that capability.
- Initially started off thinking this would be a maturity model, but for a number of them there are a number of different ways to do it none of which are any better than the others.

End user computing taken as an example

- different aspects of the SATRE model - egress (Code, ML model, data)
- may need all of them.

What's our minimum maturity level across our SDEs?

Support for adding federation

- Talk to MONAI FL working group?

SATRE - more a specification right now - move to becoming more of a standard. Certifying SDEs against that standard.

Be careful that SATRE is not just for SDEs, SATRE is moving towards accreditation.

- Wider process - UK Stats authority - using this architecture and the stats behind it.
- Self assessment wider than the existing spreadsheet that already exists.

Can some of SNSDE be brought back into SATRE?

- Federation and interoperability: either a separate pillar or incorporate into existing pillars. A piece of work providing we have capacity to do it.
- Can we see what can't be brought into SATRE, and see if the remainder can be tweaked so it's applicable?

"Data de-identification" suggested rather then pseudonymisation.

What do you mean by federation?

- In NHS England it is data access without the data moving. The least mature is to copy it all into one place.

NVidia's NVFlare and federated learning

SATRE v1 compared to SHAIP v3

- Numbers broke out as 80 enablers, 10-12 on supporters, requires/NA another 60 or so,
- For each of the 160
- If it becomes a standard wouldn't want to be trapped by the ones a solution can't do.

Aridhia: similar numbers / findings to SHAIP.

- Quite high level descriptions, not detailed.
- Like it as a standard, found it stronger on security/supporting services than on specific software requirements.
- Performed own SATRE assessment in early 2024: https://www.aridhia.com/assessing-the-aridhia-dre-against-the-satre-specification/

Would like to see v2 of a standard to tackle federation.
