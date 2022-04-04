cd ./exercises

echo Select the block of exercises
read block
echo "You selected block $block"

echo "Enter the number of exercise in the block"
read number
echo "You selected exercise $number"

answer=y
while [ $answer = y ]
do
	python exercises${block}_${number}.py
	echo "Do you want to rerun the test? (y/n)"
	read answer
done
