#
# ~/.bash_profile
#

[[ -f ~/.bashrc ]] && . ~/.bashrc
if uwsm check may-start; then
	clear
	setfont ter-132n
	echo -e "Welcome,\e[36m $USER\e[0m. \e[32mHyprland\e[0m will start in a moment."
	sleep 1.5
	echo -e "Starting \e[32mHyprland\e[0m"
	sleep 1
	exec uwsm start hyprland.desktop >/dev/null 2>&1
fi
