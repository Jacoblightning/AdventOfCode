# Year is $1
# Day is $2

set -e

# Open webbrowser now so we don't have to wait later
python -c "import webbrowser;webbrowser.open('https://adventofcode.com/$1/day/$2')" 2>/dev/null

# User has control of request rate.
echo "As per automation rules, please don't repeatedly run this script"
wget -O "$1/day$2/input.txt" -U "https://github.com/jacoblightning/AdventOfCode/master/fetch.sh Jacob Freeman (jacoblightning3.aternos.me@gmail.com)" "https://adventofcode.com/$1/day/$2/input"
cat "$1/day$2/input.txt"
echo
echo "As per automation rules, please don't repeatedly run this script"
python