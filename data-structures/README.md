# Data structures implementation

This directory shows technical implementation of fundamental data structures, with a modular design.

### Node
[implementation][link-1]

An implementation of a non-assignable generic node.

Features:

- Generic type support by using template.
- Memory management using **raw pointers**.
- Using std::vector (contiguous memory allocation) to store multiples childs.
- No self-referenced or duplicated childs

### Trie
[header][link-2] | [implementation][link-3]

An efficient implementation of an array of string in C++

Features:

- Optimal efficiency on insertion, elimination and search (lineal cost respect the size of the string)
- Optimal efficiency on calculating the number of prefixes (lineal cost respect the size of the prefix).
- The cost of the destructor is O(1), by using smart pointer which manages automatically the memory.
- The memory is used more efficiently because of sharing prefixes 

| Operation    | Trie complexity | Map complexity |
|--------------|-----------------|----------------|
| Insertion    | O(**m**)        | O(**m** log N) |
| Deletion     | O(**m**)        | O(**m** log N) |
| Search       | O(**m**)        | O(**m** log N) |
| Prefix count | O(**m**)        | O(**m** log N) |

Note: **m** is the size of the string/prefix, N is the size of the map

[link-1] https://github.com/jiawen-main/portfolio/tree/main/data-structures/node/Node.hh
[link-2] https://github.com/jiawen-main/portfolio/tree/main/data-structures/trie/Trie.hh
[link-3] https://github.com/jiawen-main/portfolio/tree/main/data-structures/trie/Trie.cc