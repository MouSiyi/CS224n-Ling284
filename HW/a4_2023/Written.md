## 1.(i)
### (i)
- Advantage: fewer parameters, less computational complexity
- Disadavantage: assumed the same dimentions for values and query, less flexibility

### (ii)
- Advantage: More flexibility in dimension setting for values and queries; more information saved
- Disadvantage: more parameters than dot product; addition conveys less information of the semantic similarity of values and queries(???maybe)

## 2
### (a)
The convolutional layer can get some local features of the input

### (b)
#### 1 
- Error: Confusion between pural and single
- Possible reason: lack of background and context in the source sentence

#### 2
- Error: not fully translated and repeated translated the last few words
- Possible reason: model limitation, too much attention put on the last few words in the source
- Possible fixes: constructure adjustment

#### 3
- Error: important translation information skipped
- Possible reason: training set may not cover the words in the source
- Possible fix: larger corpus

#### 4
- Error: error in semantics
- Possible reason: training set may not cover the specific meaning of the word in the source
- Possible fix: larger corpus and higher dimention for embedding construction

### (c)
#### 1
c1:         
$$BP = exp(1 - \frac{11}{9})$$
$$p_1 = \frac49$$
$$p_2 = \frac38$$
$$BLEU = BP\times exp(0.5logp_1 + 0.5logp_2)=0.327$$
c2:     
$$BP = 1$$
$$p_1 = 1$$
$$p_2 = \frac35$$
$$BLEU = exp(0.5log(3/5)) = 0.775$$

$c_2$ is considered better by BLEU, but is not better translated actually

#### 2
c_1       
$$BP = exp(1 - \frac{9}{6})$$
$$p_1 = \frac49$$
$$p_2 = \frac38$$
$$BLEU = 0.248$$

c_2      
$$BP = 1$$
$$p_1 = \frac36$$
$$p_2 = \frac15$$
$$BLEU = 0.316$$
still $c_2$, not better

#### 3
Due to the flexibilty of translation, a word has many synonyms, a sentence can be expressed with multiple different structures and orders. When there's only a single reference translation, the length of the translation is limited to near the reference'length, and the words and sentence structure is also limited.

#### 4
- pros: fast and easy in computation; objective and standard in scoring
- cons: rigid, restricting creativity; lower precicion, may be false-leading

