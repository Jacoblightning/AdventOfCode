# Year is $1
# Day is $2

set -e

wget -O "$1/day$2/input.txt" -U "https://github.com/jacoblightning/AdventOfCode/master/fetch.sh Jacob Freeman (jacoblightning3.aternos.me@gmail.com)" "https://adventofcode.com/$1/day/$2/input"
cat "$1/day$2/input.txt"
