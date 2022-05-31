# GraphAnalyzer
Library dedicated to analyzing Graph data structures. Able to identify if they are Eulerean and/or Hamiltonian. Also performs Depth and Breadth searches.
- Currently receives csv and txt files as input.
- Early Support for Directed Graphs
- More features and functions to come

## input examples
Select csv or txt folder and add corresponding file.

### CSV Files Format
- Csv files must be organized in adjacency matrixes, each row represents a vertex in the graph, the row must have *n* slots within it. *n* being the total amount of vertexes.
- The slot corresponding to an adjacent vector must contain the character **'1'** to represent the edge and the weight of said edge. <mark>The values must be separated by '|'</mark>. EX. **1|4** (edge exists with a weight of 4)

#### CSV Example
,'1|2','1|4'<br>
'1|2',, <br>
'1|4,, <br>
- In this Graph our first vertex (row 1) is connected to vertex 2 (row 2) and vertex 3 (row 3). Meanwhile vertex 2 and vertex 3 are connected only to vertex 1.
- The edge connecting vertex 1 and 2 has a weight of 2 and the edge between vertex 1 and 3 has a weight of 4.
- Spaces where there is no edge are left blank.

##### Directed Graph
- In a directed graph, the matrix will only hold the **'1'** value and the weight within the line tjhat represents th vertex from which the edge originates. 

,'1|2','1|4'<br>
,, <br>
,, <br>

- This example represents the same graph as the former but both edges are directed away from the first vertex. Hence they are only shown in the line where they originate from and not in the lines representing their destinations (in this case being the other two vertices).



### TXT Files Format
- Txt files begin with *n*, *n* being the number of vertexes in the graph. This is followed by lines composed of three values, the start vertex, the end vertex and the weight of the edge. EX. **1 2 4** (edge begins in vertex 1, ends in 2 and posseses a weight of 4)
- The amount of lines is determined by the number of edges in the graph.

#### TXT Example
3<br>
1 2 2<br>
1 3 4<br>

- This is the txt representation of the graph found in the CSV Example section.
