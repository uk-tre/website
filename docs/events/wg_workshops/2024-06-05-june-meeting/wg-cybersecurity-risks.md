# Working Group: Cybersecurity Risks

Chair: Donald Scobbie EPCC

## Notes

- Review of group focus
- Use of containers for code import
  - Canon SHAIP (Safe Haven AI Platform) uses containers for ingress. Harbor private registry. Also Win11/RStudio desktop with approval process for import
  - GitLab/Docker
  - Container assessment processes & tools
    - Want to build sample breakout containers to verify environment is safe for containers
    - Can we engage with Purple Teams?
    - Focus on TRE safety over container safety. We run routine standard tests + external pen tests
    - IG teams still expect confidence in imported software, even if outputs give false confidence or highlight CVEs that can't be fixed whilst maintaining reproducibility
    - Looking at Trivy in both Harbor and in CI
    - Static analysis / code reviews outside TRE before import
- WG practices
  - Want to build documentation & knowledge base
  - Platform tooling? Read the docs / GitHub wikis
- CyberSec Feedback Capture
  - Want to solicit (high-level) feedback from groups
  - GitHub issues. Possibly anonymously so as not to discourage contributions. Also via direct email as a proxy
  - WG chairs to email TRE mailing list to request feedback & report back
  - Who can submit Pull Requests? No objections to be publicly open
- Initial tasks
  - EPCC setting up example Trivy CI, configuration
  - Can we create a GitHub project as a TRE project template?
  - GitHub processes
    - Socket (https://socket.dev/) paid-for service for code analysis
    - Built-in GitHub tooling (Links in Slack channel)
  - How to structure outputs from analysis tools for consumption by IG staff?
- Challenge: How to scale scanning of large containers?
  - Starts to look similar to importing VM images
  - Increases workload on IG team
  - SBOM provision is not a panacea
  - Detailed package and dependency analysis is not an SBOM output:

To finish the sentence before we warped out, the general consensus was that no-one could provide SBOMs. Not Oracle. Not anyone. So self-declared researchers declaring dependencies is not going to work IMHO.

## Summary

Example tooling is welcome.

Shortcoming of code assessment tools, scope and quality is a challenge.

Communication of any technical assessment process outputs to non-technical IG teams will be difficult.
