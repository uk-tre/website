# Package allow lists
**Lead:** Jim Madge (Alan Turing Institute)

## Summary

The [packages repository](https://github.com/uk-tre/packages) was created recently as a place for TRE operators to share their decisions on packages allowed in their TREs.

The lists are structured as JSON documents conforming to a schema, which sets out what information is required. 
In this way, the lists can easily be validated and parsed to be used by other tools.

In the workshop we'll discuss adding your allowlists to the repository, making improvements and building tooling to use the lists.

We hope that sharing our decisions like this will encourage us to be honest and confident about our security and to benefit from using the data.

## Preparation
Attendees are encouraged to look at [the repository](https://github.com/uk-tre/packages) beforehand and bring ideas to the workshop.

For example, you might want to add your own organisation, you might want to propose a change to the schema, you might want to add tooling to create, modify or analyse the lists.

A good output would be to open a pull request or issue suggesting improvements.

## Target audience
TRE builders and operators with an interest in managing packages in TREs.

The session will be quite technical - the repository currently uses JSONSchema and Python.