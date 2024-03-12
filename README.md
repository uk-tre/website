# UK Trusted Research Environment Working Group (UK-TRE)

[![Build](https://github.com/uk-tre/website/actions/workflows/build.yml/badge.svg)](https://github.com/uk-tre/website/actions/workflows/build.yml)
[![Documentation Status](https://readthedocs.org/projects/uktre/badge/?version=latest)](https://uktre.readthedocs.io/en/latest/?badge=latest)

https://uktre.readthedocs.io/

# :wave: Welcome to the UK-TRE website repo!

# Join the Community

The UK-TRE community is open to anyone with an interest in Trusted Research Environments, including researchers, operators, information governors and managers and more, from all sectors and disciplines.

UK-TRE aims to encourage open collaborations and sharing of innovative ideas to support the delivery of groundbreaking research with sensitive data across the UK and beyond.

This repository is for the UK-TRE community website hosted on Read the Docs https://uktre.readthedocs.io/

## How to join

Anyone can join our mailing list and attend our meetings, you do not need to provide any information other than your email address.

:Mailing list: https://www.jiscmail.ac.uk/cgi-bin/wa-jisc.exe?SUBED1=UK-TRE-COMM&A=1
:Slack channel: https://ukrse.slack.com/archives/C045ETUPPD0

# :family: Community and Support

- Visit [our readthedocs site](https://uktre.readthedocs.io/en/latest/index.html) to see latest developments with the community
- Look through our [issues on GitHub](https://github.com/uktre/website/issues) to see what we're working on, and create a new issue if you have something to add!

# :handshake: Contributing

We welcome contributions from anyone who is interested in this community.
There are lots of ways to contribute, not just writing docs!

See our [Code of Conduct](CODE_OF_CONDUCT.md) and our [Contributor Guide](CONTRIBUTING.md) to learn more about how we work together as a community and how you can contribute.

## :computer: Building the docs

This repository is published using [Read the Docs](https://uktre.readthedocs.io/).
The documentation is built with Sphinx, and written in [Markdown with the MyST Parser](https://myst-parser.readthedocs.io/).

To build this repository locally, create a Python environment and install the requirements:

```sh
cd docs
pip install -r requirements.txt
```

Then build the documentation:

```sh
make html
```

[pre-commit](https://pre-commit.com/) is used to check the documentation for common issues, and to auto-format all content.

To run pre-commit locally:

```sh
pre-commit run --all-files
```

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-13-orange.svg?style=flat-square)](#contributors)

<!-- ALL-CONTRIBUTORS-BADGE:END -->
