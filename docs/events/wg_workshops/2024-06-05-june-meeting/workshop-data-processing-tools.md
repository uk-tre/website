# Workshop: Data processing tools

**Leads**: James Friel (University of Dundee), Aida Sanchez (UCL)

Discussion around data processing, de-identification, and cohort building.

## Required preparation

A general understanding of data anonymisation.
The ICO anonymisation guidance & the ADF (anonymisation decision making framework) may be of interest as a grounding in this.

## Target audience

People who work in data de-identification and data providers for TREs

## Prompts

- Risk appetite to deposit data in a TRE - What level of de-identification is comfortable for use within a TRE? e.g truncation, pseudo-anonymization
- What do current data processing pipelines look like? And are their pain points in the process?
- What de-identification tools are being used? What has worked? What hasn't?

## Notes

CPRD Clinical Practice Research Datalink

- https://www.cprd.com/cprd-tre-features-guide-users

Canon: have non-opensource tools (DICOM, FHIR, CSV, Free Text, 'omics, Pathology)

- Only available via agreement with https://research.eu.medical.canon/

NetCDF, ArcGIS Enterprise, 100+TB data, SPARK to process data

- Provide data to federated TREs

Plans for using OpenShift. Possible batch schedulers:

- https://www.coreweave.com/blog/sunk-slurm-on-kubernetes-implementations
- https://kueue.sigs.k8s.io/

## Summary

General discussion of approaches and tools used
