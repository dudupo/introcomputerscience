#!/bin/sh

for ((i=1;i<=3;i++));
do
   python ./ex11_sudoku.py ./sudoku_tables/sudoku_table$i.txt
done
python ./ex11_map_coloring.py ./adjacency_files/adj_usa_ex11.txt
python ./ex11_improve_backtrack.py ./adjacency_files/adj_example1.txt
python ./ex11_improve_backtrack.py ./adjacency_files/adj_usa_ex11.txt
