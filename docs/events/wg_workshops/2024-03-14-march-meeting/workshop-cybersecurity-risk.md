# Handling cybersecurity risk in TREs, through technology and IG

**Leads**: Jim Madge (Turing), Ruairidh Macleod (EPCC), Martin O'Reilly (Turing), Donald Scobbie (EPCC)

## Proposal

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

## Session

### Summary

The discussion centered on assessing and managing security risks within TREs, particularly concerning the introduction and handling of code, software, and containers. Participants explored various aspects of security, including the possibility of assessing the security of different components within TREs, how to communicate security assessments, and strategies for managing "insecure" code through technical or information governance (IG) controls. There was a consensus on the importance of understanding how to assess risks and interact with IG teams to effectively manage these risks. 

The conversation also touched on the concept of "risk credit" and how the inherent security measures within a TRE might allow for a reduction in the need for additional risk mitigation efforts. For example, it was noted that in the TRE context, data ingress security failure is somewhat protected through other 5 safes protection within the environment. This is not the case with data egress, which can present a much higher security risk. The dipscussion included considerations on whether to allow arbitrary code, the implications of containerization from a risk perspective, and the challenges of inspecting and sandboxing code effectively.

Participants covered practical experiences and approaches from various institutions, emphasizing the balance between enabling research and ensuring data security. The discussion highlighted the complexity of differentiating between code, scripts, software, and containers, and the practical challenges of thoroughly inspecting code due to dependencies and the vast amount of code that could be involved. 

The overarching theme was the need for a nuanced understanding of risk within TREs, advocating for technical (e.g.  network isolation), system resilience (e.g. secure even at privilege escalation) and IG controls (e.g. Safe People) to mitigate risks associated with software and data management. 

#### Next steps 

- Form a working group around this topic to produce outputs such as:
    - a risk mitigation framework
    - establish categories of bad incidents
    - white paper
    - explanatory documents tailored to different personas (e.g.technical, researcher, IG) to better communicate and manage risks involved in TRE operations

### Raw notes

- Conversation about security in TREs.
  - Is it possible to assess the security of environments, containers, software?
  - If so, how do we communicate that?
  - For example, do we refuse to allow in "insecure" code, do we mitigate with technical or IG controls?
  - Would like to understand how we all assess risk and interact with IG teams to explain/manage risk.
  - How much does the "risk credit" / reduced risk in a TRE help us reduce what we need to do to address risk concerns - things are less risky because of the Safe Setting / Safe Data for egress etc.
  - Do some of the proposed enhancements to Safes help (e.g. more automated disclosure control risk analysis)
  - Should we support arbitrary code? Is a container different from a risk perspective to custom code written by aresearcher?
  - Constraints around what points are inspectable. What can be effectively sandboxed? Inspection can provide some confidence.
- I understand that Genomics England allow BYO code with pull down of code from GitHub but have prevented pushing changes back to GitHub  through TRE environment config
- We have "risk credits", TREs provide a lot of protections which allow us to spread risk. The risk inside a TRE is lower due to controls, how do we manage that?
- Don't see a big difference between allowing someone bring code in versus letting them write the code inside. There are controls so we can be more confident
  - Similar problem here with software packages (Python, R, _etc._)
-  Enabling workflows involving containers means being confident about containerisation _and_ the contents of the contain (code). Perhaps easier with open source. Can we create a framework for assessing containers, what should it include?
- I understand that Genomics England allow BYO code with pull down of code from GitHub but have prevented pushing changes back to GitHub  through TRE environment config
-  From an IG perspective the difference between "code", "software", "scripts", "containers" with regards to risk is confusing. What are these?
  - An artifical distinction. Code, scripts, software are really the same. Even containers are software.
    Previously some TREs did try and distinguish between scripting and programming.
    The real challenge is inspecting all of the code. Software imports dependencies making a full assessment unrealistic and unreliable.
    In any case, TREs could be robust against malicious code (_e.g._ privillege escalation)
    - In a previous life I was involed in supporting this - https://www.ga4gh.org/work_stream/cloud/ which provided interfaces around remote container execution. A lot of the secureity concerns would be reduced with the container being executed into a secure sandbox such as an SDE workspace. Also more recently this - https://dareuk.org.uk/driver-project-tre-fx/
  - Agreeing largely with what’s been said in the room, but I would suggest complexity is the main implication. One or two files of python or R that only depend on packages that have been localised, maybe that’s just code or scripts. But if it’s a whole application, depends on many packages etc… are you going to inspect all of that? That’s probably software.Then if you put it in a container, you’re no longer constrained by the host environment. If your environment supports python, R and “containers”, then actually in the containers you’re allowing any runtime, any packages etc. (unless you have a mechanism to use only vetted container images). Thereby comes the question of whether to vet containers, or to provide an environment for them that’s so secure you don’t care what’s in them?
  - The distinction is quite artificial.
    What is more important is looking at the where the code has come from, do you trust it?
    Containers can be very large (one example ~8GB). Can you really inspect all of that at the level of lines of code?
    There are tools to scan for known problems.
    One example, log4j, had a serious vulnerability, which might sound bad, however it may not be a risk in a TRE because it will not be able to be exploited to break the security of a TRE.
  - Compared to data sharing, there are now many extra things we are worrying about. I like that there is a system-level means to mitigate risk rather than putting problems on individuals
    That would yield the benefits we want.
  - I have experience from central government IT projects which are also very concerned with data security.
    Maybe techniques/knowledge can be shared.
    Standard benchmarks for hardening container images
    Scanning for malicious items within container images
    Actively monitoring data movement, "does this look like normal database access". Pattern recognition for known malware. Learning tools which look for deviation from baseline behaviour. Looking at "behaviour" rather than "state".
  - My main concern around TRE InfoSec is no so much a failure of Confidentiality or Integrity (TREs are so concerned with these there is already the onion-model in place), but availibility. Would there be something which in the code could cause a serious denial of service.
  - New to TREs at King's, very similar experiences and questions.
    We have strong isolation between projects, each can be configured to suit the projects risk.
    In case of a problem, we can close a particular project, not affect the whole system.    https://docs.er.kcl.ac.uk/CREATE/TRE/tre_architecture/
    _E.g._ some projects can get pull access to GitHub, R repositories through a proxy
      - Also at the Turing, strong isolation of projects with some shared resources.
      - Also at SAIL, read only access to any git repository by creating a mirror
- In general, much more concerned with data egress than ingress.
  Have been asked to improve auditability, restrict data access _etc._
  We prefer to be robust and promote effective research, avoiding uneccessarily restrictive rules
- One of the concerns around ingress here is that more data/information is brought in that could affect identifiability - which is probably easier with a container?
- Data exfiltration or system level intrusion are perhaps not the main risk. Importing malware is a bigger issue, with the risk that project data might be ransomed or destroyed, and the project suffer from a denial of service attack. This risk remains even if the TRE has been locked down effectively.
    - I guess the way out of this is to incinerate the workspace and restore code and data from back-up. Or have i over simplified?! 
    - That is interesting. At the Turing I think we feel the opposite. The important data is read only, working data is backed up, and the environments are ephemeral and may be redeployed.
      Not the case for everyone, I would guess particularly TREs which host large datasets permanently
    - At the Turing we've generally considered confidentiality our primary driver, with integrity our second due to the risk of invalidation of research insights, leaving availability as our lowest priority area. Ransomware is definitely a risk we're not fully robust to but our business continuity plan is basically what Simon L-M suggested. We can trash a project environment and redeploy in a day or two, connecting to the unaffected read-only input data and restoring any project created data since the last back up cycle (though not robust to ransomware / stealthy corruption of project created data). While we don't put ourselves in the "long term curator / provider of datasets", this read-only approach to source sata means we do strongly isolate the source data we bring into our TRE/DSH from the projects that use it in terms of risk of corruption / losing availability. How does this compare to the mechanisms employed by those who do hold long term research data sets as a primary source to pretect their primary source data?
- Data ingress and egress are different. With ingress failure we still have other five safes protections. With egress failure the data is in the public, without those controls.
  We feel comfortable saying ingress failure is less severe than egress failure. To help have conversations with IG colleagues, have others looked into something like Open Digital Rights Language (ODRL) to consistently capture rights/policy at the ingress/egress stages?
- One of the concerns around ingress here is that more data/information is brought in that could affect identifiability - are there checks that could be done for that without requiring line by line code review?
- This debate has been scoped for software because I think that was the problem in front of us. But the scope could easily include RO-Crates in which case additional data and identification risk is an issue.
  - I know we’re running short on time now, but would like to see this elaborated on and discuss. Is Ro-crate here a shorthand for workflow use, or that the format is poorly understood, or that it could package a larger volume of files for egress (similar to the software problem where size/complexity is an issue for confidence), or something else? Definitely would be suitable to follow up with me/someone on HDR Fed A around this concern.
- How does IG navigate these issues? A good understanding of risk: threat and vulnerability is important. Not every threat can be exploited. Not every vulnerability will be exploited.
  The structure of TREs mean that the "normal" considerations don't necessarily apply. We need to keep an eye on the threat and vulnerability _within_ the systems of a TRE to have a proper assessment.
   - I, and parts of Oxford, are quite new to the TRE space.
     Risk assessment process are established (though not the standard asset register with risks).
     Risk register has been useful to explain how risk is different in the TRE, what the potential impact could be.
     Good for explaining to senior decision makers who might not be convinced by technical details.
     Articulating risk in a way that makes sense to these people, and their broader concerns about risk, outputs
 - maybe some things depend on the levels we assess risk at: system, project, dataset etc. And risks of what: identifiability within datasets, inappropriate data egress to the public domain, public perceptions, the whole TRE exploding...etc etc. Examples of worst case scenarios could help. Simple language helps IG
- There is a difference between
  This is completely unacceptable
  If this happened we could explain everything we did to prevent it and be comfortable.
  It would be good to identify these as a group.

#### Next steps
- Concensus that risk _is different_ in TREs
  It is reasonable to mitigate "software risk" like malicious code with technical controls (_e.g._ network isolation), system resilience (_e.g._ secure even at privilege escalation) and IG controls (_e.g._ Safe people)
  We should explain this for different audiences (technical, researcher, IG) to engender trust.
- Outputs could be:
  - Whitepaper
  - Risk mitigation framework
  - Explanatory documents for different roles (IG, public, ...)
- Give a better understanding of how risk should be perceived
- Establish the categories of bad incidents
    1. This must never happen
    2. If this happened, we would be confident explaining everything we did to prevent it
    Acknolwedge that risk is unavoidable and the strictest security would prevent good research occuring.
- Form a working group to work on (one of) these goals