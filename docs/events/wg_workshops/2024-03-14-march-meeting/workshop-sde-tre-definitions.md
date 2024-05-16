# SDE/TRE Definitions

**Lead**: Madalyn Hardaker (KCL)

## Proposal

### Summary

The UK TRE Working Group on SDE/ TRE Definitions has recently developed a draft scope and output report framework [available here](https://github.com/FrancisCrickInstitute/UK_TRE/tree/main/SDE%20TRE%20Definitions%20Working%20Group).

Initial discussions have generally agreed SDEs and TREs are different, but views on how and the extent to which they differ are varied. The working group released a survey in February [available here](https://forms.office.com/pages/responsepage.aspx?id=B3jtTq3rWkGnqZFwlH9OrugHht_C0ZhBkdNS6wqs4JxUMkRWNldaMTFFUVIwTUEyMVBaRzhBT0UzNC4u) to gather more information about the community’s views and would like to provide an interim update at this meeting.

### Required preparation

It would be very useful if everyone completed the survey in question - [available here](https://forms.office.com/pages/responsepage.aspx?id=B3jtTq3rWkGnqZFwlH9OrugHht_C0ZhBkdNS6wqs4JxUMkRWNldaMTFFUVIwTUEyMVBaRzhBT0UzNC4u)

### Target audience

All are welcome

## Session

### Summary

Discussion focused on the thorny topic of distinctions between what is meant by the terms 'Safe Data Environments (SDEs)' (adpoted by the NHS SDE network) and 'Trusted Research Environments (TREs)' (the more widespread and historical term). The lively discussions already held on this topic on the UK TRE email list, as well as survey responses to a working group forming around this, were mentioned (with links)

There was debate over explicitly labeling environments as "trusted" or "secure," drawing parallels to assurances like "poison-free" water, suggesting that trust is earned and should not need to be asserted.

Survey feedback and other previous discussions hinted at a distinction between handling identifiable versus de-identified data, with some suggesting that SDEs might focus more on operational analysis and data preparation (including the use of non-deidentified data), whereas TREs could be more research-focused, handling de-identified data for scientific research under less stringent governance regulations like the DEA. However, it was acknoweldged that there isn't consensus on this view, and whether those falling either side of this proposed boundary would accept it. The debate is clearly far from over!

### Raw notes

- Initial zoom discussions in January, with 25 people. Draft scope and output report framework was developed see notes in this folder https://github.com/FrancisCrickInstitute/UK_TRE/tree/main/SDE%20TRE%20Definitions%20Working%20Group
  - In this Jan discussion there was consensus that SDEs and TREs are different but different views on how they differ and to what extent.
  - Conversation on the UK TRE Community email list with a diversity of views - https://forms.office.com/e/sCTnuJZgbP
- Survey open for people to respond to to stimulate discussion
  - SDE/DSH
  - TRE Platform (hosting project TREs)
  - Project TREs
- Challenge is there as many different things that are wanted as there are people. Trying to come up with one label for what is in practice likely to be quite a few different things, prioritising different functionality.
  Are these definitions for verbs or nouns? A single "thing" (noun: system + people) could provide multiple functionality (verb)
  Have concerns about explicitly labelling "trust" and "secure". Comapre with "poison-free" water. If you have to say it
- Pedigree matters. Trust is earned. Rather than choose one term, agree on a couple of bullets for these terms and then reference how these are used.
- "A TRE is a secure area of (typically) cloud infrastructure containing a number of isolated workspaces. Workspaces are used to process data securely, either to prepare data, or to do research on this data. The research workspaces are sometimes called research TRE’s and used for a specific project.SDE is synonymous with TRE but the former is better understood by the public and preferred by the NHS."
- Meaningful distinction between handling / preparation of identifiable data (SDE?) vs only ahndling de-identified data (TRE - overall research platform, not just project space). TRE for the research space.
- Agreed Will - specifically for Scientific Research (which is defined and specially treated in GDPR/DPA) it is a requirement that these two stages of i) preparation and then ii) further use, are separated. Preparation is done by Data Controllers, and further use is of effectively anonymised data. The DPDI 2 Bill makes this even more explicit.
- In NI used TRE as that was the common terminology when we started. Mainland NHS has opted for SDE as a later iteration.
  Not a fan of the work "Trusted". Can't **tell** someone somethign is trusted. People have to choose to give trust, but changing names can be challenging and people can feel resistance for this.
- Re: what raises hackles, feels like TRE is a research / academic focussed term with a clear purpose / focus. There are other purposes. There may be lots of similarities but think there are meaningful differences, especially in purpose / driver. For SDEs the research is not the **primary** motivation. improving patient care etc are important drivers.
  - So what about NI which doesn't have an SDE but has a TRE in the HSC (our NHS)?
- See SDE and TRE as largely meaning the same thing. Even within TREs there are many differences. Feels the SATRE work is important for this.
- It feels like there are meaningful differences being talked about between (1) dealing with identifiable vs deidentified data; (2) operational analysis vs data preparation / linking / curation vs research use cases.
- Don't see the categorical differences. Feels like a sliding / tiered risk model
- Are SDEs more default "no we won't do that" vs TREs default "what wil it take to support this research in a safe enough way"?
  - Access to the research bucket should be on a needs asis, by pukka people, to data which is the least they need to do the job that's been approved.
    We should do what we need to do to make stuff happen (legally).
- Real risk is missed use not mis-use.
  What's the use of spearate SDE/TRE terms - e.g. SAIL has a great brand and calling themselves an SDE likely won't provide much value to them.
- I think perhaps part of what people who feel strongly about having a distinction between SDEs and TREs is to have that shortcut of what you can assume about a platform. e.g. "You know SAIL the NHS SDE - they're an SDE and so are we" (or vice versa for non-health/government contexts like e.g. finance). I think in the world where there isn't a distinction between SDE and TRE this shortcut couldbe achived by e.g. sensitivity tiers (e.g. a TRE that supports Tier 4 data + use cases provides the same assurances about wht you can expect as saying something is an SDE)
- Whatever we decide, I think we should get to a place where everyine agrees that there are differenced between platforms falling either side of the proposed SDE/TRE boundary (even if they disagree about whether there should be a boundary or where it should fall). Also, if we do decide the difference is identifable vs deidentified data (or non-research use cases va research use cases), would those who strongly feel they are SDEs accept that, if and when they support work with deidentified data / research work, they are operating as TREs (coming back to Paul's comment about noun vs verb) and, if they happen to apply their stronger SDE controls to working with less sensitive TRE qualifying data, will they recognise that those are above and beyind what is required and that TREs that only support deidentified research use cases are not "lesser" for this work?
