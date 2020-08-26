#!/usr/bin/env python3

import os
import subprocess
import sys

from subprocess import run

from typing import Dict, Iterable, List, Tuple, Union


try:
    import regex as re
except ImportError:
    import re


def shell(
    command: Union[str, List[str]],
    stdout: int = subprocess.PIPE,
    stderr: int = subprocess.STDOUT,
) -> subprocess.Popen:
    cmd_list: List[str]
    if isinstance(command, str):
        cmd_list: List[str] = command.split(" ")
    elif isinstance(command, (list, tuple, set)):
        cmd_list = list(command)
    return subprocess.Popen(cmd_list, stdout=stdout, stderr=stderr)


def get_ls(
    filenames: str = ".", params: str = "-lAgG", ignore_errors: bool = False
) -> str:
    cmd_list: List[str] = ["ls"]
    if not filenames:
        filenames = "."
    cmd_list.extend(filenames.split(" "))
    cmd_list.extend(params.split(" "))
    out: Popen = shell(cmd_list)
    stdout, stderr = out.communicate()
    if stderr and not ignore_errors:
        raise OSError(stderr)
    return stdout.decode()


class File:
    mode: str


def ls(filenames: str = ".", params: str = "-lAgG", ignore_errors: bool = False):
    data = get_ls(filenames=filenames, params=params, ignore_errors=ignore_errors)

    for line in data:
        if line[0] == "d":
            pass
    print(data)


ls()

# get_os_result=os.
VERSION = shell("poetry version | cut -d ' ' -f 2")

RE_SEMVER = "^(?P<major>0|[1-9]\d*)\.(?P<minor>0|[1-9]\d*)\.(?P<patch>0|[1-9]\d*)(?:-(?P<prerelease>(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?(?:\+(?P<buildmetadata>[0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"


# echo $VERSION

# The new version should ideally be a valid semver string or a valid bump rule:
#   patch, minor, major, prepatch, preminor, premajor, prerelease.

# Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.

# Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MUST be incremented if any public API functionality is marked as deprecated. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.

# Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY also include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.


# semver rules
# Semantic Versioning Specification (SemVer)
# The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in RFC 2119.

# Software using Semantic Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it SHOULD be precise and comprehensive.

# A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -> 1.10.0 -> 1.11.0.

# Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.

# Major version zero (0.y.z) is for initial development. Anything MAY change at any time. The public API SHOULD NOT be considered stable.

# Version 1.0.0 defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes.

# Patch version Z (x.y.Z | x > 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.

# Minor version Y (x.Y.z | x > 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MUST be incremented if any public API functionality is marked as deprecated. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.

# Major version X (X.y.z | X > 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY also include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.

# A pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92, 1.0.0-x-y-z.–.

# Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-]. Identifiers MUST NOT be empty. Build metadata MUST be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence. Examples: 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85, 1.0.0+21AF26D3—-117B344092BD.

# Precedence refers to how versions are compared to each other when ordered.

# Precedence MUST be calculated by separating the version into major, minor, patch and pre-release identifiers in that order (Build metadata does not figure into precedence).

# Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: Major, minor, and patch versions are always compared numerically.

# Example: 1.0.0 < 2.0.0 < 2.1.0 < 2.1.1.

# When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version:

# Example: 1.0.0-alpha < 1.0.0.

# Precedence for two pre-release versions with the same major, minor, and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows:

# Identifiers consisting of only digits are compared numerically.

# Identifiers with letters or hyphens are compared lexically in ASCII sort order.

# Numeric identifiers always have lower precedence than non-numeric identifiers.

# A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal.

# Example: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0.
