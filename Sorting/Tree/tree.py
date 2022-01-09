class TreeNode:
    def __init__(self,data, children=[]) -> None:
        self.data = data
        self.children = children

    def __str__(self, level=0) -> str:
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode('Drinks',[])
hot = TreeNode('Hot',[])
cold = TreeNode('Cold',[])
tree.addChild(hot)
tree.addChild(cold)
cold.addChild(TreeNode('Cola',[]))
cold.addChild(TreeNode('Fanta',[]))
hot.addChild(TreeNode('Tea',[]))
hot.addChild(TreeNode('Coffee',[]))
print(tree)

tree1 = TreeNode('Foods',[])
lunch = TreeNode('Rice',[])
dinner = TreeNode('Chapati',[])
tree1.addChild(lunch)
tree1.addChild(dinner)
dinner.addChild(TreeNode('Naan',[]))
dinner.addChild(TreeNode('Shirmaal',[]))
lunch.addChild(TreeNode('Pulao',[]))
lunch.addChild(TreeNode('Biryani',[]))
print(tree1)
tree2 = TreeNode('Menu',[tree1,tree])
print(tree2)