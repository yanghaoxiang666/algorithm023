学习笔记
递归：循环。通过函数体实现的循环。
1.递归终结条件 2.处理当前逻辑  3.下探到下一层  4.清理当前层
思维要点：1.不要人肉进行递归 2.找到最近的最简方法，将其拆解成可重复解决的问题（重复子问题）3.数学归纳法思维 。
回溯：，又称为试探法，是一种选优搜索法，按选优条件向前搜索，以达到目标。回溯法采用试错的思想，它尝试分步的去解决一个问题。在分步解决问题的过程中，当它通过尝试发现现有的分步答案不能得到有效的正确的解答的时候，它将取消上一步甚至是上几步的计算，再通过其它的可能的分步解答再次尝试寻找问题的答案。
在最坏的情况下，回溯法会导致一次复杂度为指数时间的计算。
分治法：可以通俗的解释为：把一片领土分解，分解为若干块小部分，然后一块块地占领征服，被分解的可以是不同的政治派别或是其他什么，然后让他们彼此异化。
分治法的精髓：
分--将问题分解为规模更小的子问题；治--将这些规模更小的子问题逐个击破；合--将已解决的子问题合并，最终得出“母”问题的解。
分治法在每一层递归上都有三个步骤：
分解：将原问题分解为若干个规模较小，相互独立，与原问题形式相同的子问题；
解决：若子问题规模较小而容易被解决则直接解，否则递归地解各个子问题；
合并：将各个子问题的解合并为原问题的解。