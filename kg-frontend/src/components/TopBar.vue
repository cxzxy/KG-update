<template>
  <div class="top-container">
    <img src="https://github.githubassets.com/favicons/favicon.svg" class="avatar"/>
    <div class="username">
      <span>{{ this.$store.getters.getUser }} ({{ identity }})</span>
    </div>
    <el-button @click="layout" class="layout">退出</el-button>
  </div>
</template>
  <script>
export default {
  name: "TopBar",
  components: {},
  data() {
    return {
      search: "",
      avatarUrl: "",
      show: false,
    };
  },
  computed: {
    identity() {
      return this.$store.getters.getIdentity ? "管理员" : "普通用户";
    },
  },
  methods: {
    layout() {
      this.$store.commit("clearUser");
      this.$message.success("退出成功");
      this.$router.replace("/login");
    },
  },
};
</script>
  <style scoped>
.top-container {
  width: 100%;
  height: 60px;
  background-color: rgb(94, 133, 191);
}
.avatar {
    position: absolute;
    top: 10px;
    left: 30px;
}
.username {
  float: left;
  margin: 15px 0 0 80px;
  color: white;
}
.layout {
  float: right;
  margin: 13px 20px 0 0;
  cursor: pointer;
  color: #5e85bf;
  border-radius: 20px;
  width: 80px;
  text-align: center;
  font-size: 14px;
}
</style>
  
<!-- <template>
  <div class="top-container">
    <span class="username">用户名：{{this.$store.getters.getUser}} ({{ identity }})</span>
    <span @click="layout" class="layout">退出登录</span>
  </div>
</template>
<script>
export default {
  name: "TopBar",
  components: {},
  data() {
    return {
      search: "",
      avatarUrl: "",
      show: false,
    };
  },
  computed: {
    identity() {
      return this.$store.getters.getIdentity ? "管理员" : "普通用户";
    },
  },
  methods: {
    layout() {
      this.$store.commit("clearUser");
      this.$message.success("退出成功");
      this.$router.replace("/login");
    },
  },
};
</script>
<style scoped>
.top-container {
  width: 100%;
  height: 80px;
  /* background-color: rgb(94,133,191); */
  background-color: rgb(36, 41, 47);
  color: #fff;
}
.username {
    float: left;
    margin: 20px 0 0 20px;
}
.layout {
    float: right;
    margin: 20px 20px 0 0;
    cursor: pointer;
}
</style> -->
