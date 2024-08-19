#!/usr/bin/env bash

curl -s "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops" >laptops.html

awk '/<div[^>]* class="product-wrapper card-body">.*<\/div>/' laptops.html |
    while IFS= read -r laptop; do

        echo "$laptop"

        name=$(echo "$laptop" | awk -F '<a[^>*]+ class="title" title="[^"]+">' '{print $2}' | awk -F '</a>' '{print $1}')

        echo "Nom du laptop: $name"
    done
