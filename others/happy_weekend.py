# 欢乐的周末
# 小华和小为是很要好的朋友，他们约定周末一起吃饭。
#
# 通过手机交流，他们在地图上选择了多个聚餐地点（由于自然地形等原因，部分聚餐地点不可达），求小华和小为都能到达的聚餐地点有多少个？

# 输入描述
# 第一行输入m和n，m代表地图的长度，n代表地图的宽度。
# 第二行开始具体输入地图信息，地图信息包含：
# 0 为通畅的道路
# 1 为障碍物（且仅1为障碍物）
# 2 为小华或者小为，地图中必定有且仅有2个 （非障碍物）
# 3 为被选中的聚餐地点（非障碍物）


# 可以被两方都到达的聚餐地点数量，行末无空格。
# 示例1  输入输出示例仅供调试，后台判题数据一般不包含示例
# 输入
# 4 4
# 2 1 0 3
# 0 1 2 1
# 0 3 0 0
# 0 0 0 0
# 输出
# 2
# 说明
# 第一行输入地图的长宽为3和4。
# 第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个）；0代表可以通行的位置；1代表不可以通行的位置。
# 此时两者能都能到达的聚餐位置有2处。
# 示例2  输入输出示例仅供调试，后台判题数据一般不包含示例
# 输入
# 4 4
# 2 1 2 3
# 0 1 0 0
# 0 1 0 0
# 0 1 0 0
# 输出
# 0
# 说明
# 第一行输入地图的长宽为4和4。
# 第二行开始为具体的地图，其中：3代表小华和小明选择的聚餐地点；2代表小华或者小明（确保有2个）；0代表可以通行的位置；1代表不可以通行的位置。
# 由于图中小华和小为之间有个阻隔，此时，没有两人都能到达的聚餐地址，故而返回0。
# 备注:
# 地图的长宽为m和n，其中：
# 4 <= m <= 100
# 4 <= n <= 100
# 聚餐的地点数量为 k，则
# 1< k <= 100

# # 为了方便，就不再处理输入，直接用变量表示
# n, m = map(int, input().split())
# map_ = [input().split() for i in range(m)]
m,n = 4,4
map_ = [
    [2,1,0,3],
    [0,1,2,1],
    [0,3,0,0],
    [0,0,0,0],
]

start_point = []

end_point = []

for i in range(m):
    for j in range(n):
        if map_[i][j] == 2:
            start_point.append((i,j))
        elif map_[i][j] == 3:
            end_point.append((i,j))

count = 0

for end_ in end_point:

    def dfs(si,sj,cache):
        if (si,sj) in cache:
            return False
        cache.append((si,sj))
        if not (0<=si<m and 0<=sj<n):
            return False
        if map_[si][sj] == 1:
            return False
        if (si,sj) == tuple(end_):
            return True
        return dfs(si+1,sj,cache) or dfs(si-1,sj,cache) or dfs(si,sj+1,cache) or dfs(si,sj-1,cache)


    cache_a = []
    cache_b = []
    if dfs(start_point[0][0],start_point[0][1],cache_a) and dfs(start_point[1][0],start_point[1][1],cache_b):
        count += 1

print(count)