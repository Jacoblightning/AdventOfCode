# Year is $1
# Day is $2

set -e

wget -O "$1/day$2/input.txt" "https://adventofcode.com/$1/day/$2/input"
cat "$1/day$2/input.txt"
