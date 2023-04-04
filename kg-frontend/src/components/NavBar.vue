<template>
  <div class="nav-bar">
    <nav-bar-item class="navname" path="/main/upload">
      <div slot="nav">
        <span class="el-icon-service iconfont"></span
        ><span class="text">文献上传</span>
      </div>
    </nav-bar-item>

    <nav-bar-item class="navname" path="/main/answer">
      <div slot="nav">
        <span class="el-icon-user iconfont"></span
        ><span class="text">智能问答</span>
      </div>
    </nav-bar-item>
    <nav-bar-item class="navname" path="/main/graph">
      <div slot="nav">
        <span class="el-icon-s-fold iconfont"></span
        ><span class="text">知识图谱</span>
      </div>
    </nav-bar-item>
    <nav-bar-item class="navname" path="/main/management">
      <div slot="nav">
        <span class="el-icon-user iconfont"></span
        ><span class="text">后台管理</span>
      </div>
    </nav-bar-item>
  </div>
</template>
<script>
import NavBarItem from "components/NavBarItem.vue";

export default {
  name: "NavBar",
  components: {
    NavBarItem,
  },
  data() {
    return {};
  },
  methods: {},
};
</script>
<style scoped>
.nav-bar {
  position: fixed;
  top: 60px;
  height: 100%;
  width: 200px;
  background-color: #f1f3f4;
}
.navname {
  height: 70px;
  line-height: 70px;
  font-size: 18px;
  cursor: pointer;
}
.iconfont {
  margin-right: 15px;
  margin-left: 30px;
}
</style>
