let "sum=0"
for so in {1..10}; do
let "sum=$sum+$so"
done
echo $sum
