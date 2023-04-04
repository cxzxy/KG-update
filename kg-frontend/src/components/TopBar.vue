<template>
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
  background-color: #f9f9f9;
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
</style>
