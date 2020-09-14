#!/usr/bin/env zsh

# Install command-line tools using Homebrew.

# a few cleanup and checkup runs ...
brew cleanup
brew doctor
brew update
brew upgrade
brew cleanup

# Store Homebrew's installed location.
BREW_PREFIX=$(brew --prefix)

# ------------------------------------ Install Favorite Utilities
# Install GNU core utilities (those that come with macOS are outdated).
# Don't forget to add `$(brew --prefix coreutils)/libexec/gnubin` to `$PATH`.
brew install coreutils

# temp path fix
PATH="${BREW_PREFIX}/coreutils/libexec/gnubin:${PATH}"

# add path to startup script
case ${SHELL##*/} in
		zsh) rcfile=~/.zshrc ;;
		bash) rcfile=~/.bashprofile ;;
		*) rcfile=~/.profile ;;
esac

echo PATH="${BREW_PREFIX}/coreutils/libexec/gnubin:${PATH}" >> $rcfile

# link for use now
ln -s "${BREW_PREFIX}/bin/gsha256sum" "${BREW_PREFIX}/bin/sha256sum" >/dev/null 2>&1

# Install some other useful utilities like `sponge`.
brew install moreutils
# Install GNU `find`, `locate`, `updatedb`, and `xargs`, `g`-prefixed.
brew install findutils
# Install GNU `sed`, overwriting the built-in `sed`.
brew install gnu-sed


# Install latest Bash and Zsh
brew install bash bash-completion@2 bash-git-prompt
brew install zsh zsh-autosuggestions zsh-completions zsh-syntax-highlighting

# Install `wget` with IRI support.
brew install wget # --with-iri # outdated option

# Install latest GnuPG to enable PGP-signing commits.
brew install gnupg

# Install more recent versions of some macOS tools.
brew install vim #--with-override-system-vi
brew install grep
brew install openssh
brew install screen
brew install php
brew install gmp

# Install font tools.
brew tap bramstein/webfonttools
brew install sfnt2woff
brew install sfnt2woff-zopfli
brew install woff2

# Install some CTF tools; see https://github.com/ctfs/write-ups.
brew install aircrack-ng
brew install bfg
brew install binutils
brew install binwalk
brew install cifer
brew install dex2jar
brew install dns2tcp
brew install fcrackzip
brew install foremost
brew install hashpump
brew install hydra
brew install john
brew install knock
brew install netpbm
brew install nmap
brew install pngcheck
brew install socat
brew install sqlmap
brew install tcpflow
brew install tcpreplay
brew install tcptrace
brew install ucspi-tcp # `tcpserver` etc.
brew install xpdf
brew install xz

# Install other useful binaries.
brew install ack
#brew install exiv2
brew install git
brew install git-lfs
brew install imagemagick --with-webp
brew install lua
brew install lynx
brew install p7zip
brew install pigz
brew install pv
brew install rename
brew install rlwrap
brew install ssh-copy-id
brew install tree
brew install vbindiff
brew install zopfli

# Remove outdated versions from the cellar.
brew cleanup
brew doctor

# Switch to using brew-installed zsh as default shell
if ! fgrep -q "$(brew --prefix zsh)" /etc/shells; then
  echo "$(brew --prefix zsh)" | /usr/bin/sudo tee -a /etc/shells;
  /usr/bin/sudo /usr/bin/chsh -s "$(brew --prefix zsh)";
fi;

# reload shell environment
exec ${SHELL} -l
