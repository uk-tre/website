# Safety and security of Python and R package import into TREs

## Overview

### Summary

Currently TREs allow access to PyPI and CRAN for less-sensitive data but only specific packages for more sensitive data.
Yet there are a variety of current approaches (some TREs have CRAN access while others do not).
Even though there are controls if there was a malicious python/R package, you could still just write the same thing inside the environment.
It is challenging to establish the line between R & Python files and AI/ML models.

Regarding egress there are challenges around the labour intensiveness of it, for which there are some automated tools.

### Next Steps

- Collaborate on a shared allowlist/blocklist for packages

## Raw Notes

- Current TREs allow access to PyPI and CRAN for less-sensitive data but only specific packages for more sensitive data.
- Different people have different experiences. Some have no access to CRAN others do
  - Scottish safe haven - no CRAN access
  - Dundee & GM allow full CRAN acceess
- CRAN have a fairly strict pipeline for adding packages so can be trusted?
  - but perhaps just coding standards rather than pen testing, file system access etc.
- If can lockdown egress sufficiently does it matter?
  - also need to ensure things like file access, network access etc are prohibited
  - can this be done?
- Is there a difference between R & python files, and a large ai/ml model? Not sure there's a clear dividing line of things we allow, and things we don't
- R has a system command to allow executing arbitrary code
- If there was a malicious python/R package you could just write it inside the environment - so preventing access to libs makes it harder but not impossible to do bad things.

### Egress

- Disclosure control labour intensive
- Some talk of automated tools
- Can prevent accidental disclosure
- What about malicious attempts to extract data e.g. encrypted, embedded in image files, in binary models etc.
- File size potentially helps
  - E.g. plausible to extract small amounts of patient data in an encrypted way that passes disclosure control. But unlikely you could do that with 1000s of records

### Roadmap plan

- Is it possible to lock down a TRE sufficiently so it is possible to allow unlimited ingress? If so best solution as no friction for researchers. Also allows future ingress items such as LLMs / neural nets etc..
- If not, then can TREs collaborate to whitelist (and blacklist) packages to prevent each one needing to repeat work.
  - Central register / co-ordination
  - But what to do about versioning?
- Could have a dual model:
  1. Docker based containerised TREs that are completely locked down meaning that any ingress is allowed
  2. TREs with a list of packages that are allowed, and you need to just use those. Process to request new packages
