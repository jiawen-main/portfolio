#include "Trie.hh"
using namespace std;

Trie::Trie()
{
    root = make_unique< Node<char> >();
}

void Trie::insert(const string& s)
{
    if (contains(s)) return;
    
    Node<char>* pnode = root.get();
    for (char c : s)
    {
        Node<char>* child = pnode->child(c);
        if (child == nullptr)
        {
            pnode->insertChild(c);
            child = pnode->child(c);
        }
        child->addCount(1);
        pnode = child;
    }

    pnode->mark(true);
}

void Trie::erase(const string& s)
{
    if (not contains(s)) return;

    Node<char>* pnode = root.get();
    for (char c : s)
    {
        Node<char>* child = pnode->child(c); 
        child->addCount(-1);
        if (child->count() == 0)
        {
            pnode->removeChild(c);
            return;
        }
        pnode = child;
    }
    pnode->mark(false);
}

bool Trie::contains(const string& s) const
{
    Node<char>* pnode = root.get();
    for (char c : s)
    {
        pnode = pnode->child(c);
        if (pnode == nullptr)
            return false;
    }
    return pnode->isMarked();
}

void Trie::clear()
{
    root.reset();
    root = make_unique< Node<char> >();
}

int Trie::count_prefix(const string& s) const
{
    Node<char>* pnode = root.get();
    for (char c : s)
    {
        pnode = pnode->child(c);
        if (pnode == nullptr) return 0;
    }
    return pnode->count();
}