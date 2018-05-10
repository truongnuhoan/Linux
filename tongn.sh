echo "Nhap n"
read -p "n =" n
let "i = 0"
let "tong = 0"
let "n = $n +1"
while [ $i -lt $n ];
do
	let "tong = $tong + $i"
	let "i = $i +1"
done
let "n = $n -1"
echo "Tong tu 1 den $n:"
echo $tong
