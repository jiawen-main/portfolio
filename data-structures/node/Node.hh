#ifndef JIAW_GENERIC_NODE_HH
#define JIAW_GENERIC_NODE_HH
#include <vector>

/**
 * Represent a non-assignable, generic node that
 * cannot have auto-referenced or repeated childs
*/
template <typename T> class Node
{
    private:

    // The value of the node
    T _value;

    // The number of _value count
    int _count;

    // Tells whether this node is marked
    bool _reg;

    // All the subsequent childs of the node
    std::vector<Node*> _next;

    public:

    // Constructor of the node
    Node() :
        _value(T{}),
        _count(0),
        _reg(false),
        _next() 
    {}

    // Constructor of the node
    explicit Node(T value) :
        _value(value),
        _count(0),
        _reg(false),
        _next()
    {}

    // Constructor of a copy of the node
    Node(const Node& copy) :
        _value(copy._value),
        _count(copy._count),
        _reg(copy._reg),
        _next()
    {
        for (Node* child : copy._next)
            this->_next.push_back(new Node(*child));
    }

    // Destructor of the node
    ~Node()
    {
        for (Node* child : _next)
            delete child;
    }

    // Assignation operator (not allowed)
    Node& operator=(const Node& node) = delete;

    // Increment the count of the node by the value of the parameter
    void addCount(int value)
    {
        _count += value;
    }
    // Return the value of the node
    T value() const
    {
        return _value;
    }

     // Return the number of count
    bool count() const
    {
        return _count;
    }

    // Insert a new child node with the value of parameter
    void insertChild(T value)
    {
        for (Node* child : _next)
            if (child->value() == value)
                return;
        _next.push_back(new Node(value));
    }

    // Remove the child node with the value of parameter
    // Nothing is done if it does not exist
    void removeChild(T value)
    {
        auto it = _next.begin();
        while(it != _next.end())
        {
            if ((*it)->value() == value)
            {
                delete *it;
                _next.erase(it);
                break;
            }
            else 
                ++it;
        }
    }

    // It marks the node with the value of reg
    void mark(bool reg)
    {
        _reg = reg;
    }

    // Tells whether the node is marked
    bool isMarked() const
    {
        return _reg;
    }

    // Returns the pointer to the child node with the value of parameter
    // If it does not exist then return nullptr
    Node* child(T value) const
    {
        for (Node* child : _next)
            if (child->value() == value)
                return child;
        return nullptr;
    }

    // Returns the number of childs it contains
    int numChild() const
    {
        return _next.size();
    }
};

#endif