#!/bin/bash
filename="./twitgone.txt"
while read -r line
do
    uri="$line"
    echo "Name read from file - $uri"
    name=$(echo -n $uri | md5sum | cut -d" " -f1)
    name+=".html"
    echo $uri "," $name >> ./html/html.key
    curl $uri > ./html/$name  
done < "$filename"
