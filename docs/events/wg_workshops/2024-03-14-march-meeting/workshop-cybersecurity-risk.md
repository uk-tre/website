# Handling cybersecurity risk in TREs, through technology and IG

**Leads**: Jim Madge (Turing), Ruairidh Macleod (EPCC), Martin O'Reilly (Turing), Donald Scobbie (EPCC)

## Proposal

### Summary

Risk is unavoidable.
However, we are particularly concerned about, and averse to, risk when working with sensitive data.
Seeking reassurance, IG teams may offload manging risk onto technical team, particularly when it comes to software, container images, VM images available in a TRE.
To some, it may seem reasonable to ask for reassurance that all software is secure.
However, as technical experts we know that the full cascade of dependencies is so large that we cannot reasonably assess it.
Furthermore, we know that software cannot simply be labelled secure or insecure.
 
It is also not fair to assess risks inside TREs in the same way as in other computing systems.
The extra security controls in TREs, such as locked down networking mean that certain types of attacks are not possible.
Even privilege escalation may be contained within a TRE to prevent severe exploitation.
 
We would like to address,
 
- How to appropriately describe risk in TREs
- How to explain why risk assessment is different in TREs to IG experts
- What can we reasonably do to assess and control software risk (vulnerability scanning, CVEs, allow/trust lists)

### Required preparation
None required, but it would be helpful for people to have any documentation on their approach or resources they use ready to share.

### Target audience
Anyone with an interest in security, TRE usability, information governance.