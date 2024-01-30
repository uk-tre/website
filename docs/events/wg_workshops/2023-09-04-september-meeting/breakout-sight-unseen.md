# Sight unseen: how far can we go with keeping data hidden from users?

## Overview

### Summary

This is the model of [OpenSAFELY](https://www.opensafely.org/).
Questions explored were how to ensure that the provided metadata is sufficient, how to extend the approach to more complex data (highly relational/linked databases) and the implied need of code review before running on actual data.

In summary this can be done but there are limitations.

## Raw notes

- What are the advantages and disadvantages of hiding data from users?
- How do we minimise barriers and frustration when working with unseen data?
- Pros and cons of hiding data. Is it even worth it?
- Challenge with interpretting the question - is this about restricting just identifiable information?
- In what scenario would it be beneficial to keep data hidden?

- Federated analytics - [OpenSAFELY](https://www.opensafely.org) model. Allows you to see data that is structured the same as the original but filled with random (synthesised?) data.
  - Can we provide sufficient metadata to allow for unclean or missing data?
  - Additional challenge with more complex data (highly relational/linked databases)
  - There is a need for code review before running on the original data
- Who's resposibility is it to create the metadata and do the cleaning? The data provider? The TRE (probably not)?
- On the question of how far we can take this:
  - It can be possible, but there are limitations. Including reducing the chance of the results.
- Pros of hiding data:
  - increase trust in research
  - potential for higher quality research (no p-hacking, more hypothesis testing, less data mining, etc)
- There are some doubts about the value/need for this. Aren't TREs with anonymised data enough?

### Roadmap plan

#### Questions

- What would a solution to this problem look like?
- What resources would be needed (people, time, funds, infrastructure etc.)?
- How can this community support you in getting them?
- What working groups/orgs are already working on this, if any? How can we collaborate with them effectively?

#### Notes

- Something along the lines of the OpenSAFELY model could work
- Requires trust in the data providers and researchers
- Limitations of types of data and types of analyses
- Resources required: people to do the code review step
