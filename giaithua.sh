echo "Nhap n:"
read -p "n =" n
let "i = 1"
let "gt = 1"
while [ $i -lt $n ]
do
	let "i = $i + 1 "
	let "gt = $gt * $i"
done 
echo "giai thua cua $n:"
echo "$gt"

