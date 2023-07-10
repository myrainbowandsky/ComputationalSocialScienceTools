#!/bin/sh
for i in {3..27} 
do
  echo $i'.jsonl'
  nohup twarc2 csv /mnt/data/Project7/fakenews/$i'.jsonl' /mnt/data/Project7/fakenews/$i'.csv' &
done