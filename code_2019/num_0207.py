class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(index,visited):
            if visited[index]==1:
                return True
            if visited[index]==-1:
                return False
            visited[index] = -1
            for x in project[index]:
                if not dfs(x,visited):
                    return False
            visited[index] = 1
            return True
        project ={k:[] for k in range(numCourses)}
        visited = {k:False for k in range(numCourses)}
        for pair in prerequisites:
            project[pair[0]].append(pair[1])
        for pair in prerequisites:
            if visited[pair[0]]==1:
                continue
            if not dfs(pair[0],visited):
                return False
        return True


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        ordered = []  # 存结果

        graph = collections.defaultdict(list)  # 表示图
        for out, into in prerequisites:
            graph[into].append(out)

        zero_in_degree = [i for i in range(numCourses) if i not in graph]  # 存入度为0的顶点集合

        for item in zero_in_degree:
            for key, val in graph.items():
                if item in val:  # 图中含有该节点准备删除
                    val.remove(item)  # 移除该顶点
                    if len(val) == 0:  # 该顶点入度为0，则将该节点插入到0 degree 集合 下次继续遍历
                        zero_in_degree.append(key)
            ordered.append(item)
        return len(ordered) == numCourses