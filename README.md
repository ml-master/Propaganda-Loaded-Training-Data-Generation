学号：2310274043 姓名：杨晓帆

复现论文名称：Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation

将课程提供的6个数据集按照7:3的比例将数据分为训练集和测试集，预处理后的数据集放在data/下。


运行以下代码，训练模型

    cd roberta/
    python train.py
    
运行以下代码，测试结果

    cd roberta/
    python test.py


# 实验结果
![image](https://github.com/ml-master/Propaganda-Loaded-Training-Data-Generation/assets/58066192/4d8655ec-587a-4588-ac94-5ecbb6768af6)

    
# Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation (ACL 2023)


[Kung-Hsiang (Steeve) Huang](https://khuangaf.github.io/), [Kathleen McKeown](https://www.cs.columbia.edu/~kathy), [Preslav Nakov](https://mbzuai.ac.ae/study/faculty/preslav-nakov), [Yejin Choi](https://homes.cs.washington.edu/~yejin/) and [Heng Ji](https://blender.cs.illinois.edu/hengji.html)


## Abstract

Despite recent advances in detecting fake news generated by neural models, their results are not readily applicable to effective detection of human-written disinformation. What limits the successful transfer between them is the sizable gap between machine-generated fake news and human-authored ones, including the notable differences in terms of style and underlying intent. With this in mind, we propose a novel framework for generating training examples that are informed by the known styles and strategies of human-authored propaganda.  
Specifically, we perform self-critical sequence training guided by natural language inference to ensure the validity of the generated articles, while also incorporating propaganda techniques, such as *appeal to authority* and *loaded language*.  In particular, we create a new training dataset, PropaNews, with 2,256 examples, which we release for future use. Our experimental results show that fake news detectors trained on PropaNews are better at detecting human-written disinformation by 3.62--7.69% F1 score on two public datasets.


## Data

The generated data and the test data used in our experiments are included in the `data` folder. `train.jsonl`, `dev.jsonl`, and `test.jsonl` are our generated data. `snopes_test.jsonl` and `politifact_test.jsonl` contain real and fake news from Snopes and PolitiFact.


## Citation

If you find this work useful, please consider citing:

```bibtex
@inproceedings{huang2023faking,
  title     = "Faking Fake News for Real Fake News Detection: Propaganda-loaded Training Data Generation",
  author    = "Huang, Kung-Hsiang, Kathleen McKeown, Preslav Nakov, Yejin Choi, and Heng Ji",
  year = "2023",
  month= july,
  booktitle = "Proceedings of the 61th Annual Meeting of the Association for Computational Linguistics",
  publisher = "Association for Computational Linguistics",
}
```

