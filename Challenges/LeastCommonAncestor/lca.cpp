/**
 * Lowest common ancestor problem from codeeval
 * https://www.codeeval.com/open_challenges/11/
 *
 * Copyright (c) 2014 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2014-05-20
 */

#include <iostream>
#include <string>
#include <sstream>

class BinaryTree {
    class Node {
        public:
        int data;
        Node *left;
        Node *right;
    };
    Node *root;

    void insert_at(Node *&, Node *&);
    // first value must be smaller
    int lca_internal(const Node *, const int &, const int &) const;

    public:
    BinaryTree();
    void insert(const int &);
    // values don't need to be in sequence
    int lca(int, int) const;
};

int main() {
    int values[] = { 30, 8, 3, 20, 10, 29, 52 };
    BinaryTree tree;
    for (int val : values) {
        tree.insert(val);
    }
    int a, b;
    std::string line;
    std::istringstream iss;

    while (std::getline(std::cin, line)) {
        iss.clear();
        iss.str(line);
        iss >> a;
        iss >> b;
        std::cout << tree.lca(a, b) << std::endl;
    }

    return 0;
}

BinaryTree::BinaryTree() {
    root = nullptr;
}

// newly inserted nodes are always leaves
void BinaryTree::insert(const int &data) {
    Node *data_node = new Node;
    data_node->data = data;
    data_node->left = nullptr;
    data_node->right = nullptr;
    insert_at(root, data_node);
}

void BinaryTree::insert_at(Node *&loc, Node *&data_node) {
    if (loc == nullptr) {
        loc = data_node;
        return;
    }
    if (data_node->data <= loc->data) {
        insert_at(loc->left, data_node);
        return;
    }
    insert_at(loc->right, data_node);
}

int BinaryTree::lca(int val1, int val2) const {
    int smaller = val1,
        larger = val1;
    if (val1 > val2) {
        smaller = val2;
    } else {
        larger = val2;
    }
    return lca_internal(root, smaller, larger);
}

int BinaryTree::lca_internal(const Node *nodeptr, const int &smaller, const int &larger) const {
    if (smaller == nodeptr->data) { return smaller; }
    if (larger == nodeptr->data) { return larger; }
    if (smaller < nodeptr->data) {
        if (larger > nodeptr->data) { return nodeptr->data; }
        return lca_internal(nodeptr->left, smaller, larger);
    }
    return lca_internal(nodeptr->right, smaller, larger);
}
