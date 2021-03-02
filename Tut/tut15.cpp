int mul(Node root)
{
    if (root == null)
        return 1;
    int left = mul(root.left);
    if (left == 0)
        return 0;
    int right = mul(root.left);
    if (right == 0)
        return 0;
    return root.val ∗ left * right;
}