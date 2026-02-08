# meh. Dark Blood Rewind, a new beginning.
git_prompt_info() {
  git rev-parse --is-inside-work-tree &>/dev/null || return

  local branch
  local staged unstaged
  local ahead behind
  local status

  branch=$(git symbolic-ref --short HEAD 2>/dev/null || git rev-parse --short HEAD)

  # Cambios staged
  staged=$(git diff --cached --name-only 2>/dev/null | wc -l | tr -d ' ')
  [[ $staged -gt 0 ]] && staged="${staged}" || staged="0"

  # Cambios unstaged
  unstaged=$(git diff --name-only 2>/dev/null | wc -l | tr -d ' ')
  [[ $unstaged -gt 0 ]] && unstaged="${unstaged}" || unstaged="0"

  # Commits ahead / behind
  local upstream
  upstream=$(git rev-parse --abbrev-ref --symbolic-full-name @{u} 2>/dev/null)

  if [[ -n $upstream ]]; then
    ahead=$(git rev-list --count HEAD..$upstream 2>/dev/null)
    behind=$(git rev-list --count $upstream..HEAD 2>/dev/null)

    [[ $behind -gt 0 ]] && behind="%F{blue}↑${behind}%f" || behind="0"
    [[ $ahead -gt 0 ]] && ahead="%F{yellow}↓${ahead}%f" || ahead="0"
  fi

  echo "[%F{cyan}${branch}%f, ${staged} st. ch., ${unstaged} unst. ch., ${behind} comm. and ${ahead} comm.%{$fg[blue]%}]"
}
PROMPT=$'%{$fg[blue]%}┌[%{$fg_bold[white]%}User %n%{$reset_color%}%{$fg[blue]%}] %{$(git_prompt_info)%}%(?,,%{$fg[blue]%}[%{$fg_bold[white]%}%?%{$reset_color%}%{$fg[blue]%}])
%{$fg[blue]%}└[%{$fg_bold[white]%}In directory: %~%{$reset_color%}%{$fg[blue]%}]>%{$reset_color%} '
PS2=$' %{$fg[red]%}|>%{$reset_color%} '

ZSH_THEME_GIT_PROMPT_PREFIX="%{$fg[blue]%}[%{$fg_bold[white]%}"
ZSH_THEME_GIT_PROMPT_SUFFIX="%{$reset_color%}%{$fg[blue]%}] "
ZSH_THEME_GIT_PROMPT_DIRTY=" %{$fg[blue]%}REPO MODIFIED%{$reset_color%}"
