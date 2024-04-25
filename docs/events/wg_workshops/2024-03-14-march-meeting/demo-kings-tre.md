# TRE at King’s: Deployment & Egress Simulation

**Lead**: Michal Rosiek (KCL)

## Proposal

### Summary

The session will be a brief PowerPoint presentation followed by an egress simulation.

The PowerPoint presentation will encompass:

- Blueprint of our TRE design
- Automated deployment process
- Ensuring secure ingress & egress
- Access control mechanisms
- Development timeline overview
- Current metrics update

In the egress simulation, we will cover:

- Demonstrating secure login procedures to TRE project resources
- Highlighting distinctions among resources
- Explaining directory structures
- Simulating secure ingress with approval from egress authority groups

This session is intended to benefit both TRE owners/developers and researchers by providing insights into how we tailor our TRE to meet project needs and expectations.

### Required preparation

I suggest that anyone interested familiarize themselves with our TRE webpage, which contains comprehensive information, including diagrams of the architecture and a video showcasing the user experience.

https://docs.er.kcl.ac.uk/CREATE/TRE/tre/

### Target audience

This session is open to anyone interested in both using and deploying TRE.

## Session

### Summary

Michal presented a demo and overview of King's College London's new Trusted Research Environment (TRE), currently hosting of 16 live projects, including notable ones like the MIREDA maternity study and Kings/GSK digital biological twin studies. The on-prem TRE has an automated deployment process with a software stack that is 99% open-source, using tools like Terraform/OpenTofu for environment deployment and Chocolatey for software package deployment, including Microsoft Office, R, and Stata. Each project within the TRE is limited to a maximum of two users. The importance of data egress over ingress was mentioned (note Breakout Session 1, Room 1 discussion on Cybersecurity that discussed a similar point). During a demo, Michal showcased how researchers access the TRE, including a view of the deployed software packages and the Data Egress Portal, which features tasks functionality exclusive to Egress Supervisors. Researchers also have access to data backups for up to 20 days in case they delete something accidently. Future considerations for the TRE include a potential move from on-prem to Azure and exploring automation for the egress process, though challenges remain due to the variety of output formats and resource limitations (one person only) for implementing new features.

#### Next steps

- DARE UK AI Risk Evaluation Workgroup publishing [report](https://dareuk.org.uk/dare-uk-community-working-groups/dare-uk-community-working-group-ai-risk-evaluation-working-group/#:~:text=AI%20Risk%20Evaluation%20Group&text=The%20AI%20Evaluation%20Working%20Group,of%20individuals%20within%20the%20data) end of March/Early April which will detail additional steps & consideration needed as part of egress process for AI models from TRE's 

### Raw notes

- Michal provided an overview of the timeline of implementation of the Kings TRE - slides to be attached to these notes
- Current Metrics for the TRE were presented. 98.63% uptime, 16 Live projects
- Projects include MIREDA maternity study and Kings/GSK digital biological twin studies
- Automated Deployment Process - 99% of software stack used is open source. Use Terraform/OpenTofu to deploy environment. Uses Chocolatey to deploy software packages such as Microsoft Office, R, Stata.
- Maximum two users per project
- Egress more important than ingress
- Non-sensitive egress process described.
- Michal provided a demo of the TRE access, and connected to a VM as a researcher, showing the deployed software packages as requested by the researcher.
- The Data Egress Portal was demoed. 'Tasks' functionality is only available to Egress Supervisors.
- Researchers can access backups of their data for up to 20 days, in case they delete something accidentally.
- Is the environment in the cloud, or on-prem?
    - It's currently on-prem, but assessing a move to Azure in the future.
- Any thoughts on using automation for the Egress process?
    - Too many output formats to be able to cover with current automation tools. Responsibility of the PI to decide what files to send into the Egress process.
- Have you thought about for support for API submitted egress requests (e.g. from a workflow)?
    = have looked at the feature but not high enough on the roadmap given the limited resource available to implement changes to the TRE environment (just Michal!!!)
- TRE [intranet page](https://docs.er.kcl.ac.uk/CREATE/TRE/tre/_) in King's 
- My contact email michal.rosiek@kcl.ac.uk
- [Link to the presentation](https://emckclac-my.sharepoint.com/:p:/g/personal/k2256745_kcl_ac_uk/ER_QyW2DfztKgDIP-_PUY80BJ_VtwgLs5uZghva1Z0IGPA?e=4X7I3H)

#### Next steps

- Dare UK AI Risk Evaluation Workgroup publishing [report](https://dareuk.org.uk/dare-uk-community-working-groups/dare-uk-community-working-group-ai-risk-evaluation-working-group/#:~:text=AI%20Risk%20Evaluation%20Group&text=The%20AI%20Evaluation%20Working%20Group,of%20individuals%20within%20the%20data) end of March/Early April which will detail additional steps & consideration needed as part of egress process for AI models from TRE's 