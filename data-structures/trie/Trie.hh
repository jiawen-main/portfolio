#ifndef JIAW_TRIE_HH
#define JIAW_TRIE_HH

#include <iostream>
#include "Node.hh"
#include <memory>

// Represent efficiently an array of strings
//
// The cost of all operations, except destructor,
// is linear, O(s.size())
class Trie
{
    private:

    // The root node of the trie
    std::unique_ptr< Node<char> > root;

    public:

    // ---------------- //
    // BASIC OPERATIONS //
    // ---------------- //

    // Constructor of the trie
    Trie();

    // Constructor of a copy of the trie (not allowed)
    Trie(const Trie& copy) = delete;

    // Assignation operator (not allowed)
    Trie& operator=(const Trie& copy) = delete;

    // Add a new string s to the trie
    void insert(const std::string& s);

    // Erase the string s from the trie
    void erase(const std::string& s);

    // Tell whether the string s exists in the trie
    bool contains(const std::string& s) const;

    // Clear the trie (call the destructor)
    void clear();

    // ------------------- //
    // ADVANCED OPERATIONS //
    // ------------------- //

    // Count the number of preffix s
    // from all the strings inserted
    int count_prefix(const std::string& s) const;
};

#endif