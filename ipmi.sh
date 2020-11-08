if [ "$#" -ne 1 ]; then
  echo "ERROR: Must give time duration argument in seconds"
  exit 1
fi

mkdir -p outputs

(( COUNT = 0 ))
BEGIN=$SECONDS
(( END = BEGIN + $1 ))
while [ $SECONDS -lt $END ]; do
	(( COUNT += 1  ))
	sudo ipmitool dcmi power reading > outputs/out_$COUNT.txt
done
