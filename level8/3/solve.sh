grep -iE "(flag|code)" out.txt | cut -d ":" -f 2 | cut -d " " -f 2
