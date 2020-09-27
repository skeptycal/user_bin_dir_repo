# shell script automation

## _Requirements_:

- `zsh 5.8 (x86_64-apple-darwin19.3.0)`
- `Python 3.8.5 (default, Jul 30 2020, 08:33:23)`
- `[Clang 12.0.0 (clang-1200.0.22.19)]`

- `dDarwin Kernel Version 20.1.0: Sat Sep 12 20:06:09 PDT 2020; root:xnu-7195.40.84.171.4~1/RELEASE_X86_64 x86_64 i386 MacBookPro11,4 Darwin`

---

## _Goals_:

- modules - locate files with various .... features

- link to bash 'find' command?

- write a go utility?

- locate files

  - find files with '#!/usr/bin/env.\*sh' or ...???
  - find all py, etc ...

- parse files

  - parse / edit INI files
  - parse / edit TOML
  - parse / edit CSV
  - parse / edit ZSH
  - search for leading spaces
  - replace with leading tabs

- regex

  - needle replacements
  - needle counts
  - info searches
  - translate to database formats

- header maintenance

  - last successful test info
  - change copyright / license block to consistent value
  - correct shebang
  - locate 'python' and change to 'python3'
  - locate 'bash' and change to 'zsh'
  - add/remove shebang
  - zsh example shebang block:

    ```py
    #!/usr/bin/env zsh
    -_- coding: utf-8 -_-
        shellcheck shell=bash
        shellcheck source=/dev/null
        shellcheck disable=2178,2155
    ...
    ```
