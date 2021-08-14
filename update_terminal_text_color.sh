# CMD + Shift + .  ## to view the hidden files
# search for .zshrc
# update script with prompt

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/ram/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/ram/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/ram/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/ram/miniconda3/bin:$PATH"
        PROMPT='%B%F{blue}%3~%f %F{178}$%f %b' #%b to add text in bold & %f to add specific color
        ZSH_THEME="robbyrussell"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

