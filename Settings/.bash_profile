export PATH=/usr/local/bin:/Users/marshallfarrier/.gem/ruby/1.8/bin:/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/X11/bin:/usr/local/git/bin:/usr/local/ncbi/blast/bin
export PATH=$PATH:/Users/marshallfarrier/node_modules/.bin:/usr/texbin

# Set architecture flags
export ARCHFLAGS="-arch x86_64"

# Load .bashrc if it exists
test -f ~/.bashrc && source ~/.bashrc

# Command prompt
export PS1='\n`date`\n[\u] \w$ '
# Color coding for command line
export CLICOLOR=1
export LSCOLORS=GxFxCxDxBxegedabagaced
# show line numbers in less
export LESS="-N"

# for bash-completion. Cf.: http://hackercodex.com/guide/mac-osx-mavericks-10.9-configuration/
if [ -f $(brew --prefix)/etc/bash_completion ]; then
    source $(brew --prefix)/etc/bash_completion
fi
# shortcuts
alias inv='cd ~/Workspace/investor-bot'
export ESCAPED_SD_ROOT="/Volumes/SANDISK64"
alias cdf='cd '$ESCAPED_SD_ROOT' && cd '
alias ws='cd '$ESCAPED_SD_ROOT'/Workspace'
alias coursera='cd '$ESCAPED_SD_ROOT'/Workspace/Solutions/ClassesTaken/Coursera/2014'
alias lfd='cd '$ESCAPED_SD_ROOT'/Workspace/Solutions/ClassesTaken/edX/2014/LearnFromData'
alias sol='cd '$ESCAPED_SD_ROOT'/Workspace/Solutions'
alias cm='cd '$ESCAPED_SD_ROOT'/Workspace/codemelon/2014'
alias kag='cd '$ESCAPED_SD_ROOT'/Workspace/Shared/kaggle'
alias lang='cd '$ESCAPED_SD_ROOT'/Documents/Education/Languages'
alias statm='cd '$ESCAPED_SD_ROOT'/Workspace/Solutions/Books/StatisticalModels'
[ -s $HOME/.nvm/nvm.sh ] && . $HOME/.nvm/nvm.sh # This loads NVM

[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm" # Load RVM into a shell session *as a function*
