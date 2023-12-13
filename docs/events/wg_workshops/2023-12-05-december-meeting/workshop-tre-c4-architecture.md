# Data architecture of a TRE with C4 modelling language

**Lead:** Joe Leach (Tower Hamlets)

## Summary

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

## Preparation

Ideally participants would be familiar with [The Goldacre Review](https://www.goldacrereview.org/), though this is not critical!

## Target audience

Colleagues from data science, engineering, and governance.

## Summary

## Raw notes
