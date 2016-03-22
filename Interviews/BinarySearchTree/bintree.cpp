/**
 * Binary search tree
 *
 * Copyright (c) 2016 Marshall Farrier
 * license http://opensource.org/licenses/gpl-license.php GNU Public License
 *
 * @author Marshall Farrier
 * @since 2016-03-21
 */

#include <iostream>

class BinaryTree {
    private:
        class Node {
            public:
                Node *left;
                Node *right;
                int data;
                Node(const int &data);
                ~Node();
        };
        Node *root;
        void insert(const int &data, Node *&node);
        bool search(const int &val, const Node *node);
    public:
        BinaryTree();
        ~BinaryTree();
        void insert(const int &data);
        bool search(const int &val);
};

int main() {
    BinaryTree tree;
    tree.insert(3);
    tree.insert(2);
    tree.insert(4);
    int val = 5;
    if (tree.search(val)) {
        std::cout << val << " found" << std::endl;
    }
    else {
        std::cout << val << " NOT found" << std::endl;
    }
    val = 4;
    if (tree.search(val)) {
        std::cout << val << " found" << std::endl;
    }
    else {
        std::cout << val << " NOT found" << std::endl;
    }
    return 0;
}

BinaryTree::BinaryTree() {
    root = NULL;
}

BinaryTree::~BinaryTree() {
    if (root) { delete root; }
}

BinaryTree::Node::Node(const int &data) {
    left = NULL;
    right = NULL;
    this->data = data;
}

BinaryTree::Node::~Node() {
    delete left;
    delete right;
    std::cout << "deleting node with value " << data << std::endl;
}

void BinaryTree::insert(const int &data, Node *&node) {
    if (!node) {
        node = new Node(data);
    }
    else if (data <= node->data) {
        insert(data, node->left);
    }
    else {
        insert(data, node->right);
    }
}

void BinaryTree::insert(const int &data) {
    insert(data, root);
}

bool BinaryTree::search(const int &val, const Node *node) {
    if (!node) {
        return false;
    }
    if (val == node->data) {
        return true;
    }
    if (val < node->data) {
        return search(val, node->left);
    }
    return search(val, node->right);
}

bool BinaryTree::search(const int &val) {
    return search(val, root);
}
