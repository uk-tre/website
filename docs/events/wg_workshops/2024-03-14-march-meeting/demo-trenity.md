# Trenity demo - an in house tool for managing users, projects and file transfers in TREs

The demoed tool is a commercial solution

**Lead**: Michael Dania (Aenon)

## Proposal

### Summary

This Session will be centred around Trenity – a self-hosted 'Five Safes' compliant platform designed to support the management of data, projects, users and file transfer in Trusted Research Environments.

What Will Be Covered?

- Presentation
  - Introduction to Trenity: Overview and the philosophy behind its design.
  - Key Features and Benefits: Deep dive into Trenity's features, including user, data and project management as well as its unique approach to data egress and ingress.
  - Live Demonstration: See Trenity in action, showcasing real-world applications, its user-friendly interface, and how it handles day-to-day TRE activities.
  - Project Management in a TRE: Navigate through managing various projects with ease.
  - Building Your Data Catalog: Organize and provide access to data within your TRE.
  - User Management - User Onboarding, Support and Knowledge Base
  - Understanding the Egress Process: Explore secure data transfer mechanisms.
  - Remote Desktop Access in Action: Access remote Desktop from Trenity without additional tools
- Trenity Roadmap
- Q&A Session: Your chance to ask questions and discuss how Trenity can be tailored to your specific requirements.

### Required preparation

To make the most of this session, we encourage you to visit https://trenity.co.uk beforehand.

### Target audience

This session is open to anyone managing or looking to manage a TRE or TRE Project

## Session

###  Summary

Trenity aims to standardize the construction, deployment, and management of Trusted Research Environments (TREs), driven by principles like SATRE (achieving 70% SATRE compliance from the outset) and the Five Safes framework. The product suite includes Trenity Secure and Trenity Edge among others, all managed through a unified dashboard facilitating Information Governance (IG) actions such as data ingress and egress, customizable descriptive data models, and comprehensive views of assets (datasets) and projects. Project dashboards provide members with various tools including task management, discussions, and literature review, with a distinct results tab that integrates the approval process for data release through a multi-role approval process (PI -> reviewer -> final release by TRE) for data egress. Trenity plans to adopt a service-based business model, offering the "base" software for free with a service-based business model on top.

### Raw notes

- [Trenity](https://trenity.co.uk/) demo
- Aim is to harmonise the building, deployment & management of TREs
- Big drivers for Trenity include
    - SATRE, Five Safes
- Aim is a 1-tool solution for deploying & managing a TRE
    - 70% SATRE compliance on day 1
- Four products
    - Trenity Secure
    - 2
    - 3
    - Trenity Edge
- Single management dashboard for IG actions like ingress/egress
    - What's the descriptive data model behind the scenes?
        - Can define and customise your own
    - Views of assets (datasets), projects, etc.
- Project dashboard visible to project members
    - tabs for task views, discussions, literature, more
    - results tab allows PI approval for release, then creating "outbound request"
        - this hands off to an approval process
    - Three roles involved: PI (to release from project); reviewer (IG review); release authority (final release from TRE)
        - "release" pushes approved files to Internet-facing part of the TRE
        - still requires log-in to access
- Plan is to release "base" Trenity software for free, with service-based business model on top
- Currently Azure-based
    - auto-deployment of TRE would be a premium/freemium feature
    - pretty cloud-agnostic underneath
