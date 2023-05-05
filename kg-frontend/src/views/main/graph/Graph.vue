<template>
  <div class="graph">
    <div ref="chart" class="chart"></div>
    <div class="el-icon-refresh" @click="refresh"></div>
    <div class="field">
      <el-select v-model="value" placeholder="请选择">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
          :change="change()"
        >
        </el-option>
      </el-select>
    </div>
  </div>
</template>
<script>
import { getGraphData } from "api/graph";
import * as echarts from "echarts";

export default {
  name: "Graph",
  components: {},
  data() {
    return {
      graphData: {},
      options: [
        {
          value: "literature",
          label: "literature",
        },
        {
          value: "biology",
          label: "biology",
        },
        {
          value: "medicine",
          label: "medicine",
        },
      ],
      datas: {},
      value: "literature",
      chart: null
    };
  },
  methods: {
    refresh() {},
    initGraph(datas) {
      let arr = [];
      datas.Nodes.forEach(function (node) {
        arr.push(node.entity_type);
      });
      this.chart = echarts.init(this.$refs.chart);
      const categories = Array.from(new Set(arr));
      const colorList = ["#04f2a7", "#82dffe", "#fac858", "#ee6666", "#73c0de"];
      const option = {
        legend: [
          {
            data: categories.map(function (a) {
              return a;
            }),
            itemWidth: 14,
            itemHeight: 14,
            itemGap: 10,
            top: "top",
          },
        ],
        series: [
          {
            type: "graph",
            layout: "force",
            label: {
              show: true,
              formatter: "{b}",
            },
            animation: true,
            SymbolSize: 100,
            edgeSymbol: ["none", "arrow"],
            edgeLabel: {
              show: true,
              formatter: "{c}",
              fontSize: 15,
              color: "#222222",
            },
            roam: true,
            draggable: true,
            data: datas.Nodes.map((node) => {
              return {
                id: node.id,
                name: node.name,
                category: categories.indexOf(node.entity_type),
                symbolSize: 40,
              };
            }),
            links: datas.Edges,
            force: {
              repulsion: 100,
            },
            edges: datas.links,
            categories: categories.map((category) => {
              return {
                name: category,
                itemStyle: {
                  //根据节点类别设置颜色
                  borderColor: colorList[categories.indexOf(category)],
                  borderWidth: 2,
                  shadowBlur: 20,
                  shadowColor: colorList[categories.indexOf(category)],
                  color: "#001c43",
                },
              };
            }),
            force: {
              repulsion: 1000,
              edgeLength: 150,
            },
          },
        ],
      };
      this.chart.setOption(option);
    },
    async change() {
      this.graphData = (await getGraphData({ field: this.value })).data;
      this.initGraph(this.graphData);
    },
    async mounted() {
      const res = await getGraphData({ field: this.value });
      this.graphData = res.data;
      this.chart = echarts.init(this.$refs.chart);
      this.initGraph(this.graphData);
    },
  },
};
</script>
<style scoped>
.graph {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  /* margin-left: -50px; */
  position: relative;
}
.chart {
  width: 90%;
  height: 600px;
  border: 2px solid #5e85bf;
  margin-top: 20px;
  /* background: #1a4377; */
  border-radius: 30px;
}
.el-icon-refresh {
  position: absolute;
  font-size: 30px;
  cursor: pointer;
  top: 80px;
  right: 170px;
}
.el-icon-refresh:hover {
  color: #409eff;
}
.field {
  position: absolute;
  top: 80px;
  left: 65px;
}
.field .el-select {
  width: 15px;
}
.field :deep(.el-select) {
  width: 110px;
}
</style>
