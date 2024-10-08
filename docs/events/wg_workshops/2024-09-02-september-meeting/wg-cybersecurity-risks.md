# Working Group: CyberSecurity Risk

Chair: Donald Scobbie (EPCC)

## Notes

- Presentation (Donald): How to assess import of researcher analysis code to a TRE
- Investigation of container vulnerability scanning
  - 16 examples for researchers
  - 25 with 1bn+ downloads, recently built, "official" or "sponsored"
  - Scan with Trivy and assess vulnerabilities
- Results (1bn+ club)
  - Top ~20 resuls all based on Debian
  - Many more unpatched vulnerabilities than would ever be allowed as part of infrastructure or research VM. Not unexpected!
  - Alpine comes out quite well...
- Container "best practices" may need to be reviewed for TRE use-cases
- Results (Research examples)
  - Large number of outstanding defects e.g. pytorch has ~1k defects
  - More Ubuntu base images, no Alpine
  - Security clearly not a concern
- Immediate thoughts
  - Major distros appear to be poorly rated
  - Best practices undermined
    - Build on existing "good" images
    - Difficult to retrofit "security" on existing containers
  - Imperative to share global code base
  - Why does Alpine score so well?
- CVE review
  - Debian apparently has poor CVE history, but is quite heavily scrutinised vs others
  - Alpine has basically 0 CVEs reported. Appears that no one is looking at it closely! May not be as easy as "switch to Alpine"
- Coverage blind spots in scanning tools
- What's the point?
  - Remote exploits rare compared to breaches due to human error
  - TREs need to conform to compliance / audit requests
  - Being compliant may not adequately address the actual risks
- Still to investigate
  - Is over-reporting an issue?
  - Does patching make a difference
  - Other scanners beyond Trivy?
  - Hardening reports using Lynis
- Working Group Next steps
  - Publish initial findings paper
  - Begin monthly WG meetings
  - Community survey
- Group Discussion
  - UCL TRE group very interested! Contradiction of vulnerable containers vs researchers having choice of software. Can risks such as data egress be mitigated by the environment? Even when users have super-user privileges
  - How to "sell" this to IG groups? (all software is buggy)
  - Can rootless containers be a potential solution?
  - Win7 example. Core infrastructure had to be wrapped. NCSC advice was this is not sustainable. TRE containers are ephemeral though, so is this the same?
  - Will these mitigations cause deployment and infrastructure issues when analyses are scaled-out?
  - What are implications of vulnerabilities in e.g. Quarto? Don't know! EPCC will baseline container and monitor additional software to show vulnerabilities are no worse
  - Some benefits are unclear beyond ensuring compliance, and come with great effort
