import ROOT


def merge_trees(trees, new_tree_name, debug=False):
    ''' trees = [[tree1name, file1path], [tree2name, file2path], ...] '''
    tree_dict = {}
    tree_list = ROOT.TList()
    for i, itree in enumerate(trees):
        tree_dict["tree_%i"%i] = ROOT.TChain(itree[0])
        tree_dict["tree_%i"%i].Add(itree[1])
        tree_list.Add(tree_dict["tree_%i"%i])
        if debug:
            print "Added tree # %i: %s in %s with %i entries"%(i, itree[0], itree[1], tree_dict["tree_%i"%i].GetEntries())
    tree = ROOT.TTree.MergeTrees(tree_list)
    tree.SetName(new_tree_name)
    return tree