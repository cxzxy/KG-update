<template>
  <div>
    <div ref="chart" class="chart"></div>
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
    };
  },
  methods: {},
  async mounted() {
    const res = await getGraphData();
    this.graphData = res.data;
    const chart = echarts.init(this.$refs.chart);
    let arr = [];
    this.graphData.Nodes.forEach(function (node) {
      arr.push(node.entity_type);
    });
    const categories = Array.from(new Set(arr));
    const colorList = [ "#5470c6", "#91cc75", "#fac858","#ee6666","#73c0de"];
    const option = {
      title: {
        text: "知识图谱",
      },
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
          },
          draggable: true,
          data: this.graphData.Nodes.map(function (node) {
            return {
              id: node.id,
              name: node.name,
              category: categories.indexOf(node.entity_type),
              symbolSize: 40,
            };
          }),
          links: this.graphData.Edges,
          force: {
            repulsion: 100,
          },
          edges: this.graphData.links,
          categories: categories.map(function (category) {
            return {
              name: category,
              itemStyle: {
                //根据节点类别设置颜色
                color: colorList[categories.indexOf(category)],
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
    console.log(option);
    chart.setOption(option);
  },
};
</script>
<style scoped>
.chart {
  width: 90%;
  height: 600px;
  border: 1px solid #666666;
  margin-top: 20px;
}
</style>
