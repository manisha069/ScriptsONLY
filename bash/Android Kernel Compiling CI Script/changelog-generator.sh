#!/bin/bash
changelog() {
	# Generates changelog day by day
	NEXT="$(date +%F)"
	SINCE="last month"
	UNTIL="$NEXT"
	echo "CHANGELOG"
	echo ----------------------
	git log --no-merges --since="$SINCE" --until="$UNTIL" --format="%cd" --date=short | sort -u -r | while read -r DATE; do
		echo
		echo ["$DATE"]
		git log --no-merges --format=" * %s" --since="$DATE 00:00:00" --until="$DATE 24:00:00"
	done
}
