# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.

from utils import evaluate_places

eval_corpus_path = "../birth_dev.tsv"
eval_text = open(eval_corpus_path, encoding='utf-8').readlines()
len_eval = len(eval_text)
baseline = ["London"] * len_eval
total, correct = evaluate_places(eval_corpus_path, baseline)
if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
else:
    print('No targets provided')
