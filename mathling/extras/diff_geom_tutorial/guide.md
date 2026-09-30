學習目標概覽

從幾何直覺出發，系統學習微分幾何的核心概念，最終能夠閱讀並理解 LLM representation geometry 相關研究文獻中的幾何語言。

學習者背景

具備微積分（單變量與多變量）與線性代數（向量空間、線性映射）基礎

無正式微分幾何或拓撲學背景，這是第一次系統學習

正在研究 LLM 內部機制，特別關注 embeddings 向量空間的幾何結構與流形假說（manifold hypothesis）

希望能看懂「embedding 空間是低維流形」這類論述背後的數學意義

學習偏好

先建立幾何直覺，再引入嚴格定義

大量具體例子，理論輔助

每個概念盡量連結回 LLM / embeddings 的應用場景

先建立全局視野，再深入細節

課程規劃

曲面幾何入門（進行中）—— 從古典幾何與曲面出發，建立流形、曲率、測地線與 Riemannian metric 的直覺與基本語言

可能的後續方向：微分流形的正式理論（切向量、微分形式）、黎曼幾何深化、或直接銜接 representation geometry 研究文獻——依學習進展決定。



---

本課程以 Wilson 的《Curved Spaces》為主軸，系統性地帶領學習者從熟悉的歐幾里得幾何出發，逐步掌握球面幾何、雙曲幾何、黎曼度量、曲率、測地線，最終抵達抽象流形的語言。整個學習旅程先建立幾何直覺與具體例子，再引入嚴格數學定義，並以 Bloch 和 Lovett 的教材補充拓撲基礎與抽象流形理論。每個核心概念都會連結回 LLM embedding 空間與流形假說的實際應用場景，讓學習者能夠以幾何眼光理解高維向量空間的結構。


Preferences
偏好較為寬鬆、留白較多的排版結構。

段落應簡短，多使用換行與清單來增加視覺上的舒適度。

偏好更直覺、簡單的描述方式，多使用生活化比喻。

強調視覺化，希望在解釋數學概念時多配合圖示（diagrams）輔助理解。

Expected outcome
完成本課程後，學習者能夠理解流形的精確數學定義、在曲面上運用黎曼度量計算距離與曲率、掌握測地線的幾何意義，並能夠閱讀 representation geometry 相關研究文獻中涉及流形假說、geodesic distance 與內積幾何的數學論述。

Topic 0: 課程介紹
建立本課程的全局視野：微分幾何研究什麼？它與 LLM embedding 空間有什麼關聯？這一講介紹整個學習路線圖，幫助學習者看清每個主題的位置與意義，讓後續的數學學習始終有實際的問題意識作為錨點。

0.1
課程路線圖導覽
從歐幾里得平面到抽象流形——每個主題學什麼、為何重要、如何連結 LLM embedding 空間
Topic 1: 幾何學的大地圖
在深入任何具體計算之前，先從高空俯瞰微分幾何的研究版圖：它研究什麼樣的問題？與代數、分析、拓撲的關係是什麼？這一講也建立「embedding 空間作為流形」的直覺動機，讓學習者帶著問題意識進入後續主題。

1.1
微分幾何研究什麼
曲線、曲面、流形——幾何學如何從平面擴展到任意彎曲的空間
1.2
為何 embedding 空間是流形
流形假說（manifold hypothesis）的直覺：高維數據為何集中在低維曲面附近
1.3
幾何語言與 AI 研究的交匯
representation geometry 文獻中出現的幾何術語：geodesic distance、curvature、Riemannian metric 各指什麼
Preface（整體目標與課程哲學）
Chapter 3: Differentiable Manifolds（動機與引言）
Topic 2: 歐幾里得幾何回顧
這是本課程的起點與量測語言的建立。距離函數、等距映射（isometry）、曲線長度是後續所有幾何概念的基礎。透過熟悉的歐幾里得空間，學習者先掌握「度量空間」的語言，為球面幾何和黎曼度量做好準備。

2.1
距離函數與度量空間
三角不等式、Cauchy-Schwarz 不等式——距離函數需要滿足哪些條件？
2.2
等距映射（Isometry）
保持距離的變換——旋轉、反射、平移的共同本質，以及 O(3,ℝ) 群的介紹
2.3
曲線長度的積分定義
如何用積分計算空間中任意曲線的長度——這是測地線概念的前身
2.4
完備性（Completeness）與緊緻性
Cauchy 列收斂、有界閉集——空間「沒有洞」意味著什麼
2.5
歐幾里得多邊形與角度和定理
平面三角形的角度和等於 π——這個熟悉結論在球面上將會失效
Chapter 1: Euclidean Geometry（pp. 13-35）
Topic 3: 球面幾何
球面是本課程的核心具體例子，也是第一個「非平坦」的幾何空間。在球面上，直線換成了大圓、三角形的角度和大於 π、平行線不存在——這些奇異現象都源自正曲率。球面幾何為後續的曲率概念提供最直接的幾何直覺。

3.1
球面距離與大圓
球面度量的定義：兩點距離等於它們張開的圓心角——為何大圓是球面上的「直線」
3.2
球面三角形與球面餘弦定理
球面版本的餘弦定理與正弦定理——與歐幾里得版本的比較
3.3
球面三角形的角度和
球面三角形三個內角之和大於 π——多出來的量叫做「球面超量（spherical excess）」，這正是正曲率的信號
3.4
球面上的 Gauss-Bonnet 定理初探
球面多邊形的角度和公式——幾何與拓撲的第一次相遇
3.5
球面等距群與 SO(3)
球面的對稱性：哪些變換保持球面距離？有限等距群的分類
3.6
球面幾何與 embedding 空間的類比
球面是正曲率流形的原型——embedding 空間中的類似結構意味著什麼
Chapter 2: Spherical Geometry（pp. 37-61）
Topic 4: 拓撲基礎
微分幾何的嚴格語言需要拓撲作為地基。這一主題介紹開集、閉集、連續映射、同胚（homeomorphism）等核心概念，幫助學習者理解「空間的形狀」與「局部如何貼合成整體」。這些概念是定義流形的必要準備，也是理解「embedding 空間的拓撲結構」的語言工具。

4.1
開集與閉集
以度量空間為出發點定義開球、開集、閉集——拓撲學的基本語言
4.2
連續映射的拓撲定義
開集的原像是開集——用拓撲重新理解「連續性」的本質
4.3
同胚（Homeomorphism）
「拓撲等價」的精確定義：雙向連續的雙射——咖啡杯與甜甜圈為何等價
4.4
連通性（Connectedness）
路徑連通與連通的區別——空間「不能被一刀切開」意味著什麼
4.5
緊緻性（Compactness）
有限覆蓋的開覆蓋——為何緊緻的曲面比非緊緻的更容易分析
4.6
拓撲曲面的概念
每個點都有鄰域同胚於 ℝ² 的空間——這正是二維拓撲流形的定義
Chapter I: Topology of Subsets of Euclidean Space（pp. 17-61）
Chapter II: Topological Surfaces（pp. 63-124）
Topic 5: 三角剖分與拓撲不變量
這一主題建立幾何與拓撲之間的橋樑：曲面的「形狀」（如有幾個洞）可以用 Euler 示性數這個整數來刻畫。透過三角剖分與環面的分析，學習者初步體驗「整體幾何性質」如何反映拓撲，為後來的 Gauss-Bonnet 定理做理論準備。

5.1
環面的幾何結構
把正方形的對邊黏起來——環面如何從平面構造出來，以及它的拓撲意義
5.2
三角剖分（Triangulation）
把曲面切成三角形——任何緊緻曲面都可以三角剖分嗎？
5.3
Euler 示性數（Euler Characteristic）
V - E + F = χ——這個數為何與剖分方式無關，只與曲面的拓撲類型有關
5.4
g 孔環面的分類
緊緻連通可定向曲面的完整分類——χ = 2 - 2g，從球面到高虧格曲面
5.5
拓撲與幾何的早期交匯
簡單版的 Gauss-Bonnet：球面三角剖分的角度和公式初探
Chapter 3: Triangulations and Euler Numbers（pp. 63-86）
Chapter III: Simplicial Surfaces（pp. 126-181）
Topic 6: 黎曼度量
黎曼度量（Riemannian metric）是本課程最核心的概念之一：它讓我們在每個點上定義內積，從而可以在任意曲面上量測距離、角度與面積。這一主題從微分形式與 Chain Rule 出發，建立 Edu² + 2Fdu dv + Gdv² 的具體表示，直接對應 embedding 空間中的內積幾何結構。

6.1
多變量微分回顧：導數與 Chain Rule
從 Jacobian 矩陣到微分形式 df——這是理解黎曼度量的微積分語言
6.2
微分形式（Differentials）的嚴格定義
dx、dy 不只是符號——它們是切空間上的線性形式，構成對偶基底
6.3
開集上的黎曼度量定義
Edu² + 2Fdudv + Gdv²——在 ℝ² 的開子集上定義平滑變化的內積族
6.4
用黎曼度量計算曲線長度
長度積分公式的具體計算——速度的「大小」由當前點的內積決定
6.5
黎曼等距（Isometry）
保持度量的映射——兩個不同形狀的曲面可以是等距的嗎？
6.6
黎曼度量與 embedding 內積的連結
token embedding 的內積結構——cosine similarity 背後的幾何意義，以及為何它等價於某種黎曼度量
Chapter 4: Riemannian Metrics（pp. 87-100）
Topic 7: 雙曲幾何
雙曲平面是負曲率空間的典型例子，與球面的正曲率形成對照。透過 Poincaré 上半平面模型和圓盤模型，學習者在具體座標中掌握黎曼度量的計算，並深入理解「不同的度量可以賦予同一個拓撲空間截然不同的幾何性質」這一核心觀念。

7.1
雙曲平面的 Poincaré 模型
上半平面 H 與圓盤模型 D——兩種座標系統下的黎曼度量 (dx²+dy²)/y²
7.2
雙曲直線與雙曲距離
在 H 模型中，測地線是哪些曲線？如何計算兩點之間的雙曲距離
7.3
雙曲三角形與角度和
雙曲三角形的內角和小於 π——負曲率的直接幾何表現
7.4
雙曲平行線與超平行線
Euclid 第五公設在雙曲幾何中失效——透過一點可以畫無限多條平行線
7.5
雙曲幾何的等距群
Möbius 變換保持雙曲度量——雙曲空間的對稱性比歐幾里得空間更豐富
7.6
負曲率空間在 embedding 中的意義
雙曲空間能比歐幾里得空間更高效地嵌入樹狀結構——為何 Poincaré embedding 受到 NLP 研究者關注
Chapter 5: Hyperbolic Geometry（pp. 101-125）
Topic 8: 光滑嵌入曲面
從抽象的度量概念回到具體的幾何對象：嵌入在 ℝ³ 中的光滑曲面。透過參數化、切空間、法向量的概念，學習者掌握「局部座標系統」的思想，這正是流形定義的具體版本。第一基本形式（First Fundamental Form）在此登場，為後續的曲率計算奠定基礎。

8.1
光滑曲面的參數化定義
σ: V → U ⊂ ℝ³ 滿足哪些條件才算是「光滑嵌入曲面」的局部座標圖
8.2
切空間（Tangent Space）
曲面在一點的切平面——由偏導數 σᵤ、σᵥ 張成的子空間
8.3
法向量（Normal Vector）
垂直於切平面的單位向量 N——它的變化率將揭示曲面如何彎曲
8.4
第一基本形式作為黎曼度量
Edu² + 2Fdudv + Gdv²——ℝ³ 的標準內積誘導到切空間上的內積
8.5
曲面長度與面積的計算
用第一基本形式積分計算曲線長度與曲面面積的具體例子（球面、環面、旋轉面）
8.6
參數變換的相容性：座標無關性
不同參數化給出同一個切空間——為何幾何量不依賴座標選取
Chapter 6: Smooth Embedded Surfaces（pp. 127-143）
Chapter V: Smooth Surfaces（pp. 218-285）
Topic 9: 曲率
曲率是微分幾何的核心量，它度量空間「彎曲的程度」。這一主題從法向量的變化出發，引入第二基本形式（Weingarten map）、主曲率與高斯曲率，並解釋為何高斯曲率是一個「內蘊」量——它只依賴第一基本形式，與嵌入方式無關。這一洞察（Theorema Egregium）直接聯繫到 embedding 空間的幾何分析。

9.1
法向量的變化：Weingarten 映射
N 沿切方向的微分 dN——從法向量的轉動率定義曲面的「彎曲算子」
9.2
第二基本形式（Second Fundamental Form）
L du² + 2M dudv + N dv²——刻畫法曲率、描述曲面如何遠離切平面
9.3
主曲率（Principal Curvatures）
κ₁ 與 κ₂：曲面在特定方向上的最大與最小彎曲率——馬鞍面的直覺例子
9.4
高斯曲率（Gaussian Curvature）
K = κ₁κ₂——球面 K=1、平面 K=0、馬鞍面 K<0 的幾何直覺
9.5
旋轉面的曲率計算
K = -f''/f——用旋轉面具體練習高斯曲率的計算
9.6
Gauss 的 Theorema Egregium（卓越定理）
高斯曲率只依賴第一基本形式——曲率是內蘊幾何量，與嵌入方式無關
9.7
曲率在高維 embedding 空間中的意義
embedding 流形的曲率如何影響模型的表徵能力——representation geometry 研究中的曲率指標
Chapter 6: Gaussian Curvature（第 6.4 節，pp. 135-143）
Chapter VI: Curvature of Smooth Surfaces（pp. 286-322）
Topic 10: 測地線
測地線是曲面上「最短路徑」的幾何化版本，也是本課程與 LLM embedding 空間連結最直接的概念之一。這一主題從變分法出發推導測地線方程，並研究測地線的存在性、唯一性與長度最小化性質。Geodesic distance 直接對應 embedding 空間中「沿流形走的最短距離」，與 cosine distance 等指標有本質的幾何差異。

10.1
曲線的能量泛函
能量 = ∫||γ'||² dt——為何最小化能量比最小化長度在計算上更方便
10.2
變分法與 Euler-Lagrange 方程
對能量泛函做「小擾動」——一條曲線是測地線當且僅當它滿足 Euler-Lagrange 方程
10.3
嵌入曲面上的測地線方程
具體推導球面、環面、旋轉面上的測地線——它們滿足怎樣的二階 ODE？
10.4
長度最小化與測地線的關係
局部最短路徑一定是測地線，但測地線未必是整體最短路徑——反例：球面的大圓
10.5
測地線的存在性與法坐標
每個點都有「法坐標鄰域」——測地極坐標 (ρ, θ) 的構造與 Gauss 引理
10.6
Geodesic Distance 與 Embedding 空間
流形上的測地距離 vs. 歐幾里得距離——為何在 token embedding 分析中，測地距離更能捕捉語義結構
Chapter 7: Geodesics（pp. 145-163）
Chapter VII: Geodesics（pp. 325-342）
Topic 11: Gauss-Bonnet 定理
Gauss-Bonnet 定理是本課程的頂點之一：它精確地揭示幾何（曲率的積分）與拓撲（Euler 示性數）之間的深刻聯繫。這一定理告訴我們，曲面的「整體彎曲程度」完全由其拓撲類型決定，與具體形狀無關——這是幾何與拓撲相互制約的最美麗範例。

11.1
Gauss-Bonnet 定理（測地三角形版本）
∫∫K dA + 邊界貢獻 = 2π——曲率積分與角度超量的精確關係
11.2
指數映射（Exponential Map）
以測地極座標為工具，理解曲面在一點附近的「展開」結構
11.3
Gauss-Bonnet 定理（緊緻曲面版本）
∫∫K dA = 2πχ(S)——高斯曲率對全曲面的積分等於 2π 乘以 Euler 示性數
11.4
三個幾何的統一驗證
在球面（K=1，χ=2）、環面（K=0，χ=0）和雙曲曲面（K=-1，χ<0）各自驗證定理
11.5
非歐幾何的統一視野
Gauss-Bonnet 如何統一解釋三種古典幾何——正、零、負曲率空間的本質差異
11.6
Gauss-Bonnet 的 LLM 意涵
若 embedding 流形有特定拓撲結構，其整體曲率分佈受到哪些限制——representation 的幾何約束
Chapter 8: Abstract Surfaces and Gauss-Bonnet（pp. 165-188）
Chapter VIII: The Gauss-Bonnet Theorem（pp. 344-394）
Topic 12: 抽象流形初步
前面所有內容都在研究嵌入在 ℝ³ 中的曲面。現在我們脫離嵌入的束縛，建立「不依賴外部空間的流形」的抽象定義：座標圖（chart）、圖集（atlas）、光滑結構、切空間。這個語言正是高維 embedding 空間（如 GPT 的 512 維向量空間）的正確數學框架，讓「embedding 空間是流形」這類論述獲得精確含義。

12.1
抽象光滑曲面的定義
脫離 ℝ³ 嵌入：用座標圖與圖集（atlas）定義二維流形——過渡函數需要是微分同胚
12.2
抽象流形上的黎曼度量
在圖集的每個座標圖上定義相容的黎曼度量——局部度量如何黏合成整體度量
12.3
n 維可微流形的定義
Lovett 的嚴格定義：Hausdorff 拓撲空間 + 第二可數 + 光滑圖集——從二維到任意維度
12.4
切空間的抽象定義
不依賴嵌入的切向量：方向導數算子的等價類——從具體向量到抽象切叢
12.5
流形上的光滑映射與微分
流形之間的光滑映射、微分（pushforward）——高維 embedding 的「投影」與「轉換」的幾何語言
12.6
Riemannian 流形的定義
光滑流形 + 黎曼度量 = Riemannian 流形——這是 embedding 空間幾何研究的正式語言
12.7
連接（Connection）與平行移動的概念初覽
Levi-Civita 連接——在流形上如何「搬運」切向量，以及它與曲率的聯繫
Chapter 8: Abstract Smooth Surfaces（第 8.2 節，pp. 167-188）
Chapter 3: Differentiable Manifolds（pp. 80-132）
Chapter 6: Introduction to Riemannian Geometry（pp. 266-321）
Topic 13: 多線性代數補充
理解現代微分幾何的文獻需要掌握張量（tensor）的語言。這一主題補充雙線性形式、對偶空間與張量積的基本概念，讓學習者能夠讀懂研究論文中出現的 covariant/contravariant 張量、metric tensor 等符號，並理解它們與之前學過的第一基本形式的關係。

13.1
對偶空間（Dual Space）
線性形式的集合——dx 作為對偶基底，與切向量的配對關係
13.2
雙線性形式與度量張量
gᵢⱼ = g(∂ᵢ, ∂ⱼ)——黎曼度量用矩陣表示後就是「度量張量」
13.3
共變與逆變指標（Einstein 求和約定）
上下標的幾何意義——為何微分幾何習慣用 xⁱ 而不是 xᵢ
13.4
張量積（Tensor Product）
如何從向量空間建立張量——(0,2) 型張量就是雙線性形式，這正是黎曼度量的本質
13.5
流形上的張量場
在每個切空間上光滑指定一個張量——度量張量場 g 是最重要的例子
Chapter 4: Multilinear Algebra（pp. 134-192）
Topic 14: Riemannian 幾何核心概念
這一主題是通向現代幾何研究文獻的最後一道門。在抽象流形的框架下，我們重新審視連接、曲率張量、測地線，並介紹 Ricci 曲率與曲率張量的完整版本。完成這一主題後，學習者將具備閱讀 representation geometry 研究論文所需的幾何語言。

14.1
Levi-Civita 連接（Connection）
流形上的「協變微分」——如何對切向量場求導，以及為何 Levi-Civita 是最自然的選擇
14.2
Christoffel 符號
Γᵢⱼᵏ——連接在座標下的具體表示，從度量的偏微分計算
14.3
測地線的抽象版本
∇_γ'γ' = 0——用協變微分重新表述「平行移動的切向量」即為測地線
14.4
平行移動（Parallel Transport）
沿曲線平行移動向量——為何平行移動的結果與路徑有關，且這正是曲率的幾何本質
14.5
曲率張量（Riemann Curvature Tensor）
R(X,Y)Z = ∇ₓ∇ᵧZ - ∇ᵧ∇ₓZ - ∇_{[X,Y]}Z——曲率衡量協變微分「不可交換」的程度
14.6
截面曲率（Sectional Curvature）與高斯曲率的推廣
截面曲率是高斯曲率在高維的推廣——為何球面、歐幾里得空間、雙曲空間是截面曲率為常數的標準模型
14.7
Ricci 曲率與純量曲率初探
曲率張量的收縮——Ricci 曲率在廣義相對論和幾何分析中的角色，以及在高維 embedding 分析中的潛在意義
Chapter 6: Introduction to Riemannian Geometry（pp. 266-321）
Topic 15: 綜合應用：Embedding 空間的幾何分析
這是本課程的總結主題，將所有學過的幾何工具連結回最初的學習動機：LLM embedding 空間的幾何結構。學習者將動手分析一個低維流形模型，理解 manifold hypothesis 的數學涵義，並練習閱讀一篇 representation geometry 研究論文，建立從數學到 AI 研究的完整路徑。

15.1
流形假說（Manifold Hypothesis）的精確表述
「高維數據集中在低維流形附近」——這句話的嚴格數學意義是什麼？需要什麼條件才成立
15.2
Embedding 空間中的內蘊幾何
把 token embedding 空間視為黎曼流形——度量如何誘導、測地距離如何計算
15.3
Geodesic Distance vs. Cosine Similarity
兩種「相似度」的幾何對比——什麼情況下它們等價？什麼情況下測地距離更有意義
15.4
表徵的曲率分析
幾個代表性研究中如何估計 embedding 流形的曲率——正曲率、負曲率各代表什麼語義結構
15.5
閱讀 Representation Geometry 論文實戰
導讀一篇具體的幾何分析論文——識別其中的流形語言、黎曼度量假設、測地線論述
15.6
課程總結與後續學習路徑
從本課程出發：Riemannian Geometry、Differential Topology、Geometric Deep Learning 的下一步指引
Postscript（後記：後續學習方向）
Further Study（後續閱讀指引）
Chapter 7: Applications of Manifolds to Physics（pp. 322-376）


---

Lesson plan

這堂課從最高視角俯瞰整個學習旅程：微分幾何研究什麼、它與 LLM embedding 空間有什麼關係，以及你將在後續課程中逐一掌握的幾何語言。

Part 1: 課程路線圖

帶你鳥瞰整門課的學習旅程，建立每個主題之間的連結，讓你知道我們要去哪裡、為什麼這樣走。

這門課從歐幾里得平面出發，一路走到抽象流形

每個主題如何層層堆疊，最終抵達 representation geometry 的語言

為什麼從「具體曲面」開始，而不是直接學抽象定義

你在學完這門課後能讀懂什麼樣的研究文獻

Source: Preface（課程哲學與目標）, Preface: What is Differential Geometry?

Related Topics: Topic 0.1

Part 2: 微分幾何是什麼

解釋微分幾何研究的問題：從曲線到曲面到流形，幾何學如何藉助微積分工具拓展到任意彎曲的空間。

古典幾何 vs. 微分幾何：加入「微積分」之後幾何能回答什麼新問題

曲線 → 曲面 → 流形：三個層次的幾何對象

三大核心主題：能做微積分的空間（流形）、如何量測（黎曼度量）、如何彎曲（曲率）

一個貫穿全書的例子：球面作為最直觀的非平坦空間

Source: Preface: What is Differential Geometry?（pp. 8-9）, Preface（課程整體定位）

Related Topics: Topic 1.1

Part 3: Embedding 空間是流形

從 LLM 的 token embedding 出發，解釋「流形假說」的直覺意義：為什麼高維數據不是隨機散布在整個空間，而是集中在低維結構上。

LLM 的 embedding 向量是什麼？它們住在哪種空間裡？

流形假說（manifold hypothesis）：高維資料集中在低維流形附近

為什麼「語義相近的詞語在幾何上也相近」這件事需要流形語言來描述

幾個視覺化直覺：從 1D 曲線嵌入 2D 平面，到 2D 曲面嵌入 3D 空間，再到高維的類比

Source: Chapter 3: Differentiable Manifolds（動機段落）

Related Topics: Topic 1.2

Part 4: 幾何語言初覽

帶你認識在 representation geometry 論文中頻繁出現的幾何術語，讓你建立第一印象，知道這些詞語在後續課程中各自扮演什麼角色。

Riemannian metric（黎曼度量）：如何在彎曲空間裡量距離

Geodesic（測地線）：曲面上的「最短路徑」，與 cosine similarity 的幾何對比

Curvature（曲率）：空間「彎曲程度」的數量化描述

Tangent space（切空間）：在一個點上的「局部平面近似」

這些詞語在論文裡怎麼出現——一個真實句子的示範閱讀

Source: Preface: Organization of Topics（pp. 9-10）, Preface（整體課程架構）

Related Topics: Topic 1.3

Review

透過主動回想問題鞏固這堂課的核心概念。

Next Lesson

下一堂課我們將進入主題 2「歐幾里得幾何回顧」，從距離函數與度量空間的定義出發，建立整門課的量測語言：距離需要滿足哪些條件、等距映射是什麼

---

