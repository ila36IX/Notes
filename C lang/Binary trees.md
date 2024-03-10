# Tree Data Structure

A tree is a nonlinear hierarchical data structure that consists of nodes connected by edges.
## Inorder traversal

1. First, visit all the nodes in the left subtree
2. Then the root node
3. Visit all the nodes in the right subtree

```
inorder(root->left)
display(root->data)
inorder(root->right)
```

---

## Preorder traversal

1. Visit root node
2. Visit all the nodes in the left subtree
3. Visit all the nodes in the right subtree

```c
display(root->data)
preorder(root->left)
preorder(root->right)
```

---

## Postorder traversal

1. Visit all the nodes in the left subtree
2. Visit all the nodes in the right subtree
3. Visit the root node

```c
postorder(root->left)
postorder(root->right)
display(root->data)
```