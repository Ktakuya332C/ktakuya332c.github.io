# 広告オークション関連の論文まとめ

広告オークション関連の論文をつぎのソースから集めてきたのでまとめておく

- [Foundations of Sponsored Search](https://timroughgarden.org/f07/f07.html)
- [Google Research: Economics and Electronic Commerce](https://research.google/pubs/?area=economics-and-electronic-commerce)
- [Meta Research: Economics and Computation](https://research.facebook.com/publications/)
- [Microsoft Research: Economics](https://www.microsoft.com/en-us/research/publications/)
- [ACM Conference on Economics and Computation](https://ec21.sigecom.org/program/accepted-papers/)
- [The Conference on Web and Internet Economics](https://hpi.de/wine2021/accepted-papers/)

## 規範的な分析

広告オークションの最適な仕組みの理論的な研究

### GSPの分析

GSPの静的な均衡に関する論文

- [2006] [Truthful Auctions for Pricing Search Keywords](https://web.stanford.edu/~ashishg/papers/laddered_auction_extended.pdf)
- [2006] [Position auctions](https://people.ischool.berkeley.edu/~hal/Papers/2006/position.pdf)
- [2006] [An Analysis of Alternative Slot Auction Designs for Sponsored Search](https://courses.cs.duke.edu/spring07/cps296.3/fp185-lahaie.pdf)
- [2007] [Internet Advertising and the Generalized Second-Price Auction](https://www.benedelman.org/publications/gsp-060801.pdf)

GSPの動的な均衡に関する分析

- [2006] [Vindictive Bidding in Keyword Auctions](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.98.1213&rep=rep1&type=pdf)
- [2007] [Greedy Bidding Strategies for Keyword Auctions](https://homes.cs.washington.edu/~karlin/papers/ecc.pdf)
- [2007] [Dynamics of Bid Optimization in Online Advertisement Auctions](http://www2007.thewebconf.org/papers/paper089.pdf)

### 予算制約問題

広告掲載枠を広告主に割り当てるonlineアルゴリズムを求める問題(Adwords-problem)に関する論文

- [2007] [AdWords and Generalized On-line Matching](https://web.stanford.edu/~saberi/adwords.pdf)
- [2007] [Online Primal-Dual Algorithms for MaximizingAd-Auctions Revenue](http://www.columbia.edu/~cs2035/courses/ieor8100.F18/buchbinder.pdf)
- [2009] [Online Stochastic Matching: Beating 1-1/e](https://arxiv.org/abs/0905.4100)
- [2011] [Near Optimal Online Algorithms and Fast Approximation Algorithms for Resource Allocation Problems](https://www.cs.cmu.edu/~sandholm/cs15-892F15/near%20optimal%20online%20algs%20for%20resource%20allocation.ec11.pdf)
- [2012] [Asymptotically Optimal Algorithm for Stochastic Adwords](http://pages.cs.wisc.edu/~balu2901/papers/2012/adwords_optimal.pdf)
- [2012] [Online Matching and Ad Allocation](https://storage.googleapis.com/pub-tools-public-publication-data/pdf/9b9bacbb54799b5b7b38fb53aa81ccc3b55604db.pdf)
- [2014] [Biobjective Online Bipartite Matching](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.718.3997&rep=rep1&type=pdf)

Adwords-problemに対してさらに広告主のインセンティブを考慮した論文

- [2012] [Polyhedral Clinching Auctions and the Adwords Polytope](https://arxiv.org/pdf/1201.0404.pdf)
- [2012] [Clinching Auctions with Online Supply](https://arxiv.org/pdf/1210.1456.pdf)
- [2008] [Budget Constrained Bidding in Keyword Auctions and Online Knapsack Problems](https://www.microsoft.com/en-us/research/publication/budget-constrained-bidding-keyword-auctions-online-knapsack-problems/)

予算消化ペースの調整方法についての論文

- [2012] [Sequential Auctions of Identical Items with Budget-Constrained Bidders](https://www.microsoft.com/en-us/research/publication/sequential-auctions-identical-items-budget-constrained-bidders/)
- [2012] [Prior-free Auctions for Budgeted Agents](https://www.nikhildevanur.com/pubs/ec14-devanur.pdf)
- [2012] [Budget Smoothing for Internet Ad Auctions: A Game Theoretic Approach](https://www.microsoft.com/en-us/research/publication/budget-smoothing-internet-ad-auctions-game-theoretic-approach/)
- [2012] [Budget Optimization for Sponsored Search: Censored Learning in MDPs](https://www.microsoft.com/en-us/research/publication/budget-optimization-for-sponsored-searchcensored-learning-in-mdps/)
- [2014] [Efficient Regret Bounds for Online Bid Optimisation in Budget-Limited Sponsored Search Auctions](https://www.microsoft.com/en-us/research/publication/efficient-regret-bounds-for-online-bid-optimisation-in-budget-limited-sponsored-search-auctions/)
- [2017] [Multiplicative Pacing Equilibria in Auction Markets](https://arxiv.org/abs/1706.07151)
- [2018] [Pacing Equilibrium in First-Price Auction Markets](https://arxiv.org/abs/1811.07166)
- [2021] [The Complexity of Pacing for Second-Price Auctions](https://arxiv.org/abs/2103.13969)
- [2021] [Throttling Equilibria in Auction Markets](https://arxiv.org/abs/2107.10923)

### リッチ広告関連の論文

リッチ広告に対するオークション設計

- [2014] [Randomized Revenue Monotone Mechanisms for Online Advertising](https://research.google/pubs/pub43282/)
- [2018] [Fast Core Pricing for Rich Advertising Auctions](https://www.microsoft.com/en-us/research/publication/fast-core-pricing-for-rich-advertising-auctions/)
- [2019] [The Ad Types Problem](https://arxiv.org/abs/1907.04400)
- [2021] [Simple Mechanisms for Welfare Maximization in Rich Advertising Auctions](https://hpi.de/wine2021/accepted-posters/)

動画広告のオークション設計

- [2018] [Optimizing Ad Refresh In Mobile App Advertising](https://research.google/pubs/pub46847/)

### 繰り返しオークションの分析

繰り返しオークションにおける均衡分析

- [2009] [Convergence Analysis of No-Regret Bidding Algorithms in Repeated Auctions](https://arxiv.org/abs/2009.06136)
- [2021] [Learning to Bid in Contextual First Price Auctions](https://research.google/pubs/pub50822/)

繰り返しオークションのデザイン

- [2016] [Dynamic Auctions with Bank Accounts](https://research.google/pubs/pub45750/)
- [2018] [Dynamic Mechanism Design in the Field](https://research.google/pubs/pub47745/)
- [2019] [Prior-Free Dynamic Auctions with Low Regret Buyers](https://research.google/pubs/pub49331/)
- [2019] [Optimal Dynamic Auctions are Virtual Welfare Maximizers](https://research.google/pubs/pub47737/)
- [2019] [A Robust Non-Clairvoyant Dynamic Mechanism for Contextual Auctions](https://research.google/pubs/pub49424/)
- [2020] [Robust Pricing in Dynamic Mechanism Design](https://research.google/pubs/pub49903/)
- [2020] [Non-Clairvoyant Dynamic Mechanism Design](https://research.google/pubs/pub47744/)
- [2021] [Non-Excludable Dynamic Mechanism Design](https://research.google/pubs/pub49576/)
- [2021] [Revenue-Incentive Tradeoffs in Dynamic Reserve Pricing](https://research.google/pubs/pub50657/)

### 利得関数が異なる広告主

tCPA制約やtROAS制約を持つ広告主のモデル

- [2014] [Clinching auctions beyond hard budget constraints](https://arxiv.org/pdf/1404.5000.pdf)
- [2019] [Autobidding with Constraints](https://research.google/pubs/pub48721/)
- [2021] [The Landscape of Autobidding Auctions: Value versus Utility Maximization](https://research.google/pubs/pub50579/)
- [2021] [Robust Auction Design in the Auto-bidding World](https://openreview.net/pdf?id=01884FCwbNf)
- [2021] [Towards Efficient Auctions in an Auto-bidding World](https://research.google/pubs/pub50310/)
- [2021] [Prior-independent Dynamic Auctions for a Value-maximizing Buyer](https://openreview.net/pdf/be174d96434d7a3bad61654285fe0babf20aa194.pdf)

### オークションにおける機械学習

機械学習を用いてオークションの設計を行う

- [2019] [Automated mechanism design via neural networks](https://research.google/pubs/pub48310/)
- [2019] [Optimal Auctions through Deep Learning](https://research.google/pubs/pub48185/)
- [2020] [Optimizing Multiple Performance Metrics with Deep GSP Auctions for E-commerce Advertising](https://arxiv.org/abs/2012.02930)
- [2021] [Neural Auction: End-to-End Learning of Auction Mechanisms for E-Commerce Advertising](https://dl.acm.org/doi/10.1145/3447548.3467103)

オークション構造を考慮したCTR予測等の学習方法

- [2017] [Loss Functions for Predicted Click-Through Rates in Auctions for Online Advertising](https://research.google/pubs/pub46552/)
- [2018] [Incentive-Aware Learning for Large Markets](https://research.google/pubs/pub46913/)

機械学習の学習を行うための探索と活用のトレードオフ

- [2007] [Handling Advertisements of Unknown Quality in Search Advertising](http://www.cs.cmu.edu/~spandey/publications/ctrEstimation.pdf)
- [2010] [Maintaining Equilibria During Exploration in Sponsored Search Auctions](http://www.vorobeychik.com/2010/ssaexplore.pdf)

### 他の広告市場との比較

一位価格オークションへの移行に対する考察

- [2020] [Why Competitive Markets Converge to First Price Auctions](https://research.google/pubs/pub49912/)

広告主がCV情報やユーザー情報をどのような場合に開示するかに関する考察

- [2021] [Auctioning with Strategically Reticent Bidders](https://research.google/pubs/pub50821/)

Ad-Exchange関連の論文

- [2016] [Where to sell: Simulating auctions from learning algorithms](https://research.google/pubs/pub45455/)
- [2016] [Pricing a low-regret seller](https://research.google/pubs/pub45454/)
- [2016] [Reservation Exchange Markets for Internet Advertising](https://research.google/pubs/pub45875/)
- [2017] [Dynamic Revenue Sharing](https://research.google/pubs/pub47736/)

広告主に提示する予測メトリクスの調整方法について

- [2021] [Welfare-maximizing Guaranteed Dashboard Mechanisms](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3858104)

## 実証的な分析

すでに動いている広告オークションの実証的な研究

### オークションの隠れパラメータの推定

直接広告主価値を推定する

- [2011] [A Structural Model of Sponsored Search Advertising Auctions](http://economics.mit.edu/files/6975)
- [2011] [Stochastic Variability in Sponsored Search Auctions: Observations and Models](https://www.microsoft.com/en-us/research/publication/stochastic-variability-in-sponsored-search-auctions-observations-and-models/)
- [2013] [Counterfactual Reasoning and Learning Systems: The Example of Computational Advertising](https://www.microsoft.com/en-us/research/publication/counterfactual-reasoning-and-learning-systems-the-example-of-computational-advertising/)
- [2017] [A Quantal Regret Method for Structural Econometrics in Repeated Games](https://www.microsoft.com/en-us/research/publication/quantal-regret-method-structural-econometrics-repeated-games/)
- [2017] [Inference on Auctions with Weak Assumptions on Information](https://arxiv.org/abs/1710.03830)

インセンティブ両立性を推定する

- [2019] [Online Learning for Measuring Incentive Compatibility in Ad Auctions](https://arxiv.org/abs/1901.06808)
- [2019] [Testing Dynamic Incentive Compatibility in Display Ad Auctions](https://research.google/pubs/pub49340/)
- [2019] [Envy, Regret, and Social Welfare Loss](https://arxiv.org/abs/1907.07721)
- [2019] [Estimating Approximate Incentive Compatibility](https://par.nsf.gov/servlets/purl/10119656)
- [2020] [A Data-Driven Metric of Incentive Compatibility](https://research.google/pubs/pub49036/)

間接的に社会厚生等を推定する

- [2015] [Robust Data-Driven Guarantees in Auctions](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2601928)
- [2017] [Efficiency Guarantees from Data](https://www.microsoft.com/en-us/research/publication/efficiency-guarantees-data/)
- [2020] [Learning Utilities and Equilibria in Non-Truthful Auctions](https://arxiv.org/abs/2007.01722)

### オークションのA/Bテスト関連

オークションのKPIに関する論文

- [2013] [Ranking and Tradeoffs in Sponsored Search Auctions](https://arxiv.org/abs/1304.7642)
- [2014] [Optimising Trade-offs Among Stakeholders in Ad Auctions](https://www.microsoft.com/en-us/research/publication/optimising-trade-offs-among-stakeholders-in-ad-auctions/)
- [2014] [The Economic and Cognitive Costs of Annoying Display Advertisements](https://www.microsoft.com/en-us/research/publication/the-economic-and-cognitive-costs-of-annoying-display-advertisements/)
- [2015] [Focus on the Long-Term: It's better for Users and Business](https://research.google/pubs/pub43887/)

オークションの変更の影響の推定

- [2016] [A/B Testing of Auctions](https://arxiv.org/abs/1606.00908)
- [2017] [Mechanism Redesign](https://arxiv.org/abs/1708.04699)
- [2019] [Variance Reduction in Bipartite Experiments through Correlation Clustering](https://proceedings.neurips.cc/paper/2019/file/bc047286b224b7bfa73d4cb02de1238d-Paper.pdf)
- [2019] [Computing large market equilibria using abstractions](https://arxiv.org/abs/1901.06230)
- [2019] [Robust Multi-agent Counterfactual Prediction](https://arxiv.org/abs/1904.02235)
- [2019] [Sample Complexity for Non-Truthful Mechanisms](https://dl.acm.org/doi/pdf/10.1145/3328526.3329632)

## 他の参考文献

- [Tim Roughgarden's Online Courses](http://timroughgarden.org/videos.html)
- [Paper Collection of Real-Time Bidding](https://github.com/wnzhang/rtb-papers)
- [计算广告论文、学习资料、业界分享](https://github.com/wzhe06/Ad-papers)
