from decision_tree import*

tenis_df = pd.read_csv('tennis.csv')
example = tenis_df.iloc[6]
attributes = [row for row in tenis_df]

decision_tree = decision_tree_learning(tenis_df,attributes,None,None,None)
decision_tree.print_tree()