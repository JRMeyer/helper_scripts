for dir in ./*/
do
    dir=${dir%*/}

    echo ""
    echo "################"
    echo ${dir##*/}
    cd ${dir##*/}
    git status
    echo "################"
    echo ""

    cd ..
done
