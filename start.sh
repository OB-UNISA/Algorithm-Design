cd ./exercises

echo Select the block of exercises
read block
echo "You selected block $block"

echo "Enter the number of exercise in the block"
read number
echo "You selected exercise $number"

python exercises${block}_${number}.py
