# Keynote: # Crick's TRE: history and approach

<iframe width="560" height="315" src="https://www.youtube.com/embed/1FqVEP0OVlY?si=9OoPOnnTe90sAvv6" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Q&A

- How cloud agnostic is it?
  - Azure, AWS and Azure not beyond that (limited to what Snowflake supports)
- How much of what we saw is in operation? Everything, working for a year and a half
  - focus of the process on legal and agreement aspects via forms
- Can you explain the metadata side of the platform, EG what software is being used?
  - Snowflake offers standard data model for all objects in all accounts
  - Projects are created in Snowflake sub-accounts
  - Data brought out of Snowflake, collated, and replicated as one outside of Snowflake
- You have a lot of integration across providers, IBM, microsoft and AWS. How have you overcome interoperability challenges?
  - lot's of these integrations are at a data level, which is easier than a functionality level for those tools
- Do you ever act as data processors on behalf of data providers or is this effectively a data hosting service (where the data comes processed by the data providers/controllers)?
  - Both, if you are a data processor on your own right you could bring your own "bedroom" and retain control of it
- Any idea of cost
  - https://www.snowflake.com/en/data-cloud/pricing-options/
- How are you managing audit and compliance across the three cloud platforms?
  - Snowflake does it! Objects are created by snowflake on the three clouds, ensuring compliance
- Am I right in thinking you only host consented data?
- How do users see what they are spending in the platform, or how many of their credits they have used?
  - Automatic threshold detector for every processing compute, message sent depending on threshold (e.g 75%)
- Who are the Roles (Loader, Processor, etc.) assigned to: study team members, central services, IG specialists?
  - They are assigned by the accountable owners (by authorising emails or actions on servicenow) of each collaborating partner or the board for the collaboration account. So a human can have many roles if approved by their organisation or the project.
- Can you provide a quick overview of Snowflake and the core features it provides
  - Their website is well documented: I would try these links....
  - https://docs.snowflake.com/en/user-guide/organizations
  - https://docs.snowflake.com/en/user-guide/admin-account-identifier
  - https://docs.snowflake.com/en/guides-overview-sharing#label-about-direct-share
  - https://other-docs.snowflake.com/en/collaboration/provider-listings-auto-fulfillment
  - https://other-docs.snowflake.com/en/collaboration/collaboration-listings-about
  - https://docs.snowflake.com/en/sql-reference/commands-user-role
