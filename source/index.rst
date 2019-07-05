.. toctree::
   :hidden:
   :maxdepth: 2

   self
   projects
   code-of-conduct

About the Working Group
=======================

Presently, the key projects associated with Python's critical HTTP libraries are scattered
across various projects and maintainers, with some projects lacking maintainers altogether.
Practically speaking, no one has a complete picture of how all of these components fit and
work together and there is no cohesive vision for the Python HTTP stack.

This leads to problems. As we look towards the future of Python with asyncio and innovations
within HTTP specifications we are risking grave fragmentation and confusion among users.
Without funding and contributors we risk many projects becoming unmaintained and existing
maintainers being burned out. Without a code of conduct and enforcement we risk toxic actors
creating an environment where all contributors are not welcome.

Key Milestones
--------------

The Python HTTP Working Group should endeavor to accomplish the following things:

1. **Provide well maintained, documented low-level libraries for building HTTP clients.**

    These libraries are foundational, `sans-I/O`_, libraries such as URL validation, certificate handling
    and HTTP parsers / encoders. These encourage the stability of high-level, critical libraries while
    providing a common base for experimental libraries.

2. **Clearly mark which libraries are stable and intended for long-term use.**

    With the proliferation of experimental libraries it's important that we communicate to users
    which libraries are ready for broad consumption and which will be supported for a long time.

3. **Create a strong community of shared maintainers across projects.**

    All member projects should have a straightforward path for maintainers of other member
    projects to be given commit access.

4. **Make key decisions on proposals made by member projects**

    This is especially important for emerging projects where broad use-cases and interoperability
    are important for their future.

5. **Seek sources of funding for member projects**

    This can come in the form of grant proposal writings towards the PSF and other grant making
    organizations as well as managing sponsorships from organizations such as Tidelift.

6. **Author PEPs related to the Python HTTP ecosystem**

    This includes helping people outside the Working Group author and review PEPs.

 .. _sans-I/O: https://sans-io.readthedocs.io/
