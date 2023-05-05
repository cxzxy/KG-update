
<template>
  <div class="nav-bar">
    <nav-bar-item class="navname" path="/main/upload">
      <div slot="nav" class="nav_content">
        <i class="el-icon-upload iconfont"></i
        ><span class="text">文献管理</span>
      </div>
    </nav-bar-item>

    <nav-bar-item class="navname" path="/main/answer">
      <div slot="nav">
        <i class="el-icon-user iconfont"></i><span class="text">问答管理</span>
      </div>
    </nav-bar-item>

    <nav-bar-item class="navname" path="/main/graph">
      <div slot="nav" class="nav_content">
        <i class="el-icon-s-fold iconfont"></i
        ><span class="text">知识图谱</span>
      </div>
    </nav-bar-item>

    <nav-bar-item
      class="navname"
      path="/main/management"
      v-show="this.$store.getters.getIdentity"
    >
      <div slot="nav" class="nav_content">
        <i class="el-icon-user iconfont"></i><span class="text">权限管理</span>
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
    // return {};
    return {};
  },
  methods: {},
};
</script>
   <style scoped>
* {
  padding: 0;
  margin: 0;
  text-decoration: none;
}

body {
  justify-content: space-evenly;
  align-items: center;
}

.nav-content {
  display: flex;
  overflow: hidden;
}
.nav-bar {
  display: flex;
  flex-direction: column;
  transition: 0.3s;
  overflow: hidden;
  position: fixed;
  top: 50px;
  height: 100%;
  width: 200px;
  background-color: white;
  padding-top: 50px;
}
.navname {
  font-family: bold;
  display: block;
  height: 70px;
  position: relative;
  transition: 0.3s;
  line-height: 70px;
  font-size: 18px;
  cursor: pointer;
}

.navname span {
  position: relative;
  left: 60px;
  opacity: 1;
  transition: 0.1s;
}

.iconfont {
  position: absolute;
  margin: 27px 10px 0 13px;
}

.nav-bar:hover {
  width: 200px;
}

.nav-bar:hover span {
  opacity: 1;
}
</style>
   
<!-- <template>
  <div class="nav-bar">
    <nav-bar-item class="navname" path="/main/upload">
      <div slot="nav">
        <span class="el-icon-upload iconfont"></span
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
    <nav-bar-item class="navname" path="/main/management" v-show="this.$store.getters.getIdentity">
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
  top: 80px;
  height: 100%;
  width: 200px;
  /* background-color: rgb(94,133,191); */
  background-color: rgb(94,133,191);
  color: #fff;
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
</style> -->
